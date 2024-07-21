# Реализация фабричного паттерна
class Sensor:
    def get_data(self):
        pass

class Camera(Sensor):
    def get_data(self):
        return "Данные с камеры"
class Lidar(Sensor):
    def get_data(self):
        return "Данные с лидара"
class SensorFactory:
    def create_sensor(self):
        pass
class CameraFactory(SensorFactory):
    def create_sensor(self):
        return Camera()

class LidarFactory(SensorFactory):
    def create_sensor(self):
        return Lidar()

if __name__ == "__main__":
    sensor_factory = CameraFactory()
    sensor = sensor_factory.create_sensor()
    data = sensor.get_data()
    print(data)
