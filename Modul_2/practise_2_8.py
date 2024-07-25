# паттерн Легковес
class DroneFlyweight:
    def __init__(self, model, manufacture, sensors):
        self._model = model
        self._manufacture = manufacture
        self._sensors = sensors

    def operation(self, unique_state):
        print(f"""
        ============================
        Дрон:
            Модель: {self._model}
            Производитель: {self._manufacture}
            Датчики: {self._sensors}
            
        Текущие параменты
            Координаты: {unique_state["coordinates"]}
            Скорость: {unique_state["speed"]}
            Миссия: {unique_state["mission"]}
            Высота: {unique_state["altitude"]}
            Заряд батареи: {unique_state["battary"]}
        """)
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def manufacture(self):
        return self._manufacture

    @manufacture.setter
    def manufacture(self, value):
        self._manufacture = value

    @property
    def sensors(self):
        return self._sensors

    @sensors.setter
    def sensors(self, value):
        self._sensors = value

class DroneFactory:
    def __init__(self):
        self._drones = {}

    def get_drone(self, model, manufacturer, sensors):
        key = (model, manufacturer, sensors)
        if key not in self._drones:
            self._drones[key] = DroneFlyweight(model, manufacturer, sensors)
        return self._drones[key]
    def list_drones(self):
        print(f"Всего легковесных дронов: {len(self._drones)}")
        for value in self._drones.keys():
            model, manufacturer, sensors = value
            print(f"Ключ: модель {model}, производитель: {manufacturer}, сенсоры {sensors}")

def client_code():
    factory = DroneFactory()
    drone_1 = factory.get_drone("ModelY", "SkyTech", "camera, GPS, lidar")
    drone_1.operation({
        "coordinates": "10, 20",
        "speed": "50",
        "mission": "surveillance",
        "altitude": "100",
        "battary": "80"
    })

    drone_2 = factory.get_drone("ModelX", "DroneCorp", "camera, GPS")
    drone_2.operation({
        "coordinates": "110, 120",
        "speed": "50",
        "mission": "surveillance",
        "altitude": "130",
        "battary": "82"
    })

    drone_3 = factory.get_drone("ModelX", "DroneCorp", "camera, GPS")
    drone_3.operation({
        "coordinates": "101, 201",
        "speed": "70",
        "mission": "surveillance",
        "altitude": "100",
        "battary": "81"
    })

    factory.list_drones()

if __name__ == "__main__":
    client_code()