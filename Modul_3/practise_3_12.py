import time
from abc import ABC, abstractmethod

class IDroneAPI(ABC):
    def __init__(self, connect_uri=None):
        self.client = None
        self.connect_uri = connect_uri
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_image(self, max_attempts=10, delay=1):
        pass


import airsim
import numpy as np
import cv2

class AirSimAPI(IDroneAPI):
    def connect(self):
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()
        print(f"Подключение через Air Sim")

    def get_image(self, max_attempts=10, delay=1):
        responses = self.client.simGetImages([airsim.ImageRequest("0", airsim.ImageType.Scene, False, False)])
        if responses:
            response = responses[0]

            img_1D = np.frombuffer(response.image_data_uint8, dtype=np.uint8)
            img_rgb = img_1D.reshape(response.height, response.width, 3)

            cv2.imwrite('test.jpg', img_rgb)
            print("Image saved")
        else:
            print("No images found")

from pymavlink import mavutil
import time
class MavLinkAPI(IDroneAPI):
    def connect(self):
        self.client = mavutil.mavlink_connection(self.connect_uri)
        self.client.wait_heartbeat()
        print("Соединение с дроном установлено")

    def get_image(self, max_attempts=10, delay=1):
        self.client.mav.command_long_send(
            self.client.target_system,
            self.client.target_component,
            mavutil.mavlink.MAV_CMD_IMAGE_START_CAPTURE,
            0,
            0,
            0,
            1,
            0,
            0, 0, 0
        )
        print("Армирование дрона завершено")

        for _ in range(max_attempts):
            response = self.client.recv_match(type='CAMERA_IMAGE_CAPTURE', blocking=True, timeout=5)
            if response:
                print(f"Путь до фото {response.file_path}")
                break
            else:
                print(f"Ожидание камеры...")
            time.sleep(delay)

class DroneAPIFactory:
    @staticmethod
    def gets_drone_api(type_api, connect_uri):
        if type_api == "AirSim":
            return AirSimAPI(connect_uri)
        elif type_api == "MavLink":
            return MavLinkAPI(connect_uri)
        else:
            raise ValueError("Такое API не реализовано")


if __name__ == "__main__":
    type_api = "AirSim"
    connect_uri = "tcp://127.0.0.1:5555"
    drone = DroneAPIFactory.gets_drone_api(type_api, connect_uri)
    drone.connect()
    drone.get_image()
