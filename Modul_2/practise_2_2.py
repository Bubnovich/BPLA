# Single Repondibility Principle (Принцип единственной ответственности)

class NovigationSystem:
    def calc_route(self, start, end):
        print(f"Расчет маршрута от {start} до {end}")
        # логика
        pass

class CommunicationSystem:
    def send_data(self, data):
        print(f"Отправка данных: {data}")
        # логика
        pass

# Open/Closed Principle (Принцип открытости/закрытости)

from abc import ABC, abstractmethod
class FlightMode(ABC):
    @abstractmethod
    def execute(self):
        pass
class ManualMode(FlightMode):
    def execute(self):
        print(f"Ручной режим управления")
        # логика
        pass

class AutoMode(FlightMode):
    def execute(self):
        print(f"Режим управления автопилотом")
        # логика
        pass

class EmergencyMode(FlightMode):
    def execute(self):
        print(f"Аваоийный режим")
        # логика
        pass

class DestructionMode(FlightMode):
    def execute(self):
        print(f"САМОЛИКВИДАЦИЯ")
        # логика
        pass

class Drone:
    def __init__(self, mode: FlightMode):
        self.__mode = mode
    def fly(self):
        self.__mode.execute()

    def change_mode(self, mode: FlightMode):
        self.__mode = mode

if __name__ == "__main__":
    manual_mode = ManualMode()
    destrution_mode = DestructionMode()
    drone = Drone(manual_mode)
    drone.fly()
    drone.change_mode(destrution_mode)
    drone.fly()
    print(f"\n============================\n")

# Liskov Substitution Principle (Принцип подстановки Лисков)
class Sensor(ABC):
    @abstractmethod
    def get_data(self):
        pass

class Camera(Sensor):
    def get_data(self):
        print(f"Получение видео с камеры")
        return "Данные с камеры"

class Lidar(Sensor):
    def get_data(self):
        print(f"Чтение данных с лидара")
        return "Данные с лидара"

class Battary(Sensor):
    def get_data(self):
        print(f"Чтение уровня заряда")
        return "Данные с батареи"

class Drone2:
    def __init__(self, sensor: Sensor):
        self.__sensor = sensor

    def gather_data(self):
        data = self.__sensor.get_data()
        print(f"Собранные данные {data}")

if __name__ == "__main__":
    battary = Battary()
    drone2 = Drone2(battary)
    drone2.gather_data()
