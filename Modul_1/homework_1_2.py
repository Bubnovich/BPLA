'''
Шаг 1. Создать классы
Drone (беспилотник),
Camera (камера),
GPS (система GPS) и
FlightController (контроллер полета).
'''
class Camera:
    def __init__(self, resolution='Full HD', zoom=1, frequency=5):
        self.resolution = resolution
        self.zoom = zoom
        self.frequency = frequency

    def capture_image(self): #Захват изображения
        print("произошел захват изображения")

    def take_photo(self): # Сделать фотографию
        print("Сделан снимок местности")

    def broadcast(self): # Трансляция
        print("Произошла передача изображения")

    def night_shooting(self): #Ночная съемка
        print("Проведена ночная съемка")

class GPS:
    def __init__(self, coordinates=(0.0, 0.0)):
        self.coordinates = coordinates

class FlightController:
    def __init__(self):
        self.coordinates = GPS()
        self.height = 0
        self.map_flight = []
        self.is_flying = False

    def start(self):
        print(f"Двигатели запущены")

    def takeoff(self):
        print(f"Начинаем взлет")

    def left(self):
        print(f"Поворачиваем налево")

    def right(self):
        print(f"Поворачивам направо")

    def adove(self):
        print(f"Поднимаемся выше")

    def below(self):
        print(f"Снижаемся")

class Drone(FlightController, GPS, Camera):
    def __init__(self, id="ABC", model="copter"):
        self.id = id
        self.model = model
        self.camera = Camera()
        self.gps = GPS(coordinates=(0.0, 0.0))
        self.fight_controller = FlightController()

if __name__ == "__main__":
    drone_1 = Drone()
    print(drone_1.camera.resolution)
    print(drone_1.fight_controller.start())