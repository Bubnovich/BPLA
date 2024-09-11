import random

from pyinstrument import Profiler
from flask import Flask, request, g, make_response
from numba import jit
import numpy as np
import unittest

app = Flask(__name__)

class Altimeter:
    def __init__(self, altitude=0):
        self.__altitude = altitude
        self.__rate = 0.0

    def update(self, motor_trust):
        self.__rate = motor_trust * 0.1
        self.__altitude += self.__rate + random.gauss(0, 0.1)

    def get_altitude(self):
        return self.__altitude

class Gyroscope:
    def __init__(self, orientation={'roll': 0.0, 'pitch': 0.0, 'yaw':0.0}):
        self.__orientation = orientation.copy()

    def update(self, roll_rate, pitch_rate, yaw_rate):
        self.__orientation['roll'] += roll_rate + random.gauss(0, 0.1)
        self.__orientation['pitch'] += roll_rate + random.gauss(0, 0.1)
        self.__orientation['yaw'] += roll_rate + random.gauss(0, 0.1)

    def get_orientation(self):
        return self.__orientation['roll'], self.__orientation['pitch'], self.__orientation['yaw']
class Drone:
    def __init__(self):
        self.__altimeter = Altimeter()
        self.__gyroscope = Gyroscope()
        self.__motors = [0.0, 0.0, 0.0, 0.0]
        self.__orientation = {'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0}
        self.__pid_roll = PIDRegulator(1, 0.001, 10)
        self.__pid_pitch = None
        self.__pid_yaw = None
        self.__pid_altitude = None

    def get_altitude(self):
        # получим с датчиков высоту
        return self.__altimeter.get_altitude()

    def update_altitude(self):
        self.__altitude = self.get_altitude()
        self.__orientation['roll'], self.__orientation['pitch'], self.__orientation['yaw'] = self.get_gyroscope()

    def get_gyroscope(self):
        #получим с датчиков
        self.__gyroscope.update(self.__orientation['roll'], self.__orientation['pitch'], self.__orientation['yaw'])
        self.__orientation = self.__gyroscope.get_orientation()
        return self.__orientation['roll'], self.__orientation['pitch'], self.__orientation['yaw']

    def motor_trust(self, trusts):
        self.__motors = trusts
        average_trust = sum(trusts) / len(trusts)
        self.__altimeter.update(average_trust)
        yaw_rate = (self.__motors[0] - self.__motors[1] - self.__motors[2] + self.__motors[3]) / 4
        pitch_rate = (self.__motors[0] + self.__motors[1] - self.__motors[2] - self.__motors[3]) / 4
        roll_rate = (self.__motors[0] - self.__motors[1] + self.__motors[2] - self.__motors[3]) / 4

        self.__gyroscope.update(roll_rate, pitch_rate, yaw_rate)
        print(f'Тяга: {trusts}, Альтиметр: {self.__altimeter.get_altitude()}, Гироскоп: {self.__gyroscope.get_orientation()}')

    def control(self, target_altitude, target_orientation):
        self.update_altitude()
        self.get_gyroscope()

        altitude_output, _, _ = self.__pid_altitude.update(target_altitude, self.__altitude)

        roll_output, _, _ = self.__pid_altitude.update(target_orientation['roll'], self.__orientation['roll'])
        pitch_output, _, _ = self.__pid_altitude.update(target_orientation['pitch'], self.__orientation['pitch'])
        yaw_output, _, _ = self.__pid_altitude.update(target_orientation['yaw'], self.__orientation['yaw'])
        trust = [
            altitude_output + roll_output + pitch_output + yaw_output,
            altitude_output - roll_output + pitch_output - yaw_output,
            altitude_output + roll_output - pitch_output - yaw_output,
            altitude_output - roll_output - pitch_output + yaw_output,
        ]
        self.motor_trust(trust)

        pass

    class PIDRegulator:
        def __init__(self, kp, ki, kd):
            self.__kp = kp
            self.__ki = ki
            self.__kd = kd
            self.old_error = 0.0
            self.integral_error = 0.0

        def update(self, setpoint, pv):
            error = setpoint - pv
            self.integral_error += error
            derivative_error = error - self.old_error
            self.old_error = error
            u = (self.__kd * error) + (self.__ki * self.integral_error) + (self.__kd * derivative_error)
            return u, error, self.integral_error

#def pid_regulator():


@app.route('/')
def index():
    return 'Управление дроном'

@app.before_request
def before_request():
    #if "profile" in request.args:
    g.is_profiling = "profile" in request.args
    if g.is_profiling:
        g.profile = Profiler()
        g.profile.start()

@app.after_request
def after_request(response):
    if g.is_profiling:
        g.profile.stop()
        output_html = g.profile.output_html()
        return make_response(output_html)
    return response

if __name__ == "__main__":
    app.run(debug=True)
