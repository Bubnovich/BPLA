#Бубнович Антон Владимирович
#No БПЛА_256-1
import requests
import threading

# Модель данных
class UAVModel:
    """
    Класс UAVModel отвечает за управление данными состояния беспилотного летательного аппарата (БЛА).
    """

    def __init__(self):
        """
        Инициализация данных о состоянии БЛА.
        """
        self.height = 0  # Высота полета
        self.velocity = 0  # Скорость движения
        self.coordinates = (0, 0)  # Текущие координаты
        self.battery = 100  # Заряд батареи в процентах

    def update_coordinates(self, new_coordinates):
        """
        Обновление координат БЛА.
        :param new_coordinates: Новые координаты (x, y)
        """
        self.coordinates = new_coordinates

    def update_height(self, new_height):
        """
        Обновление высоты БЛА.
        :param new_height: Новая высота
        """
        self.height = new_height

    def update_velocity(self, new_velocity):
        """
        Обновление скорости БЛА.
        :param new_velocity: Новая скорость
        """
        self.velocity = new_velocity

    def consume_battery(self, consumption):
        """
        Обновление заряда батареи.
        :param consumption: Потребление заряда в процентах
        """
        self.battery -= consumption

# Представление
class UAVView:
    """
    Класс UAVView отвечает за визуализацию данных о состоянии БЛА.
    """

    def show_status(self, model):
        """
        Выводит текущий статус БЛА на экран.
        :param model: Экземпляр UAVModel с данными о состоянии
        """
        print(f"Height: {model.height} meters, Velocity: {model.velocity} m/s, "
              f"Coordinates: {model.coordinates}, Battery: {model.battery}%")

    def warning(self, message):
        """
        Выводит предупреждающее сообщение.
        :param message: Текст предупреждения
        """
        print(f"WARNING: {message}")

# Контроллер
class UAVController:
    """
    Класс UAVController управляет логикой работы БЛА.
    """

    def __init__(self, model, view):
        """
        Инициализация контроллера.
        :param model: Экземпляр UAVModel
        :param view: Экземпляр UAVView
        """
        self.model = model
        self.view = view

    def adjust_position(self, new_coordinates):
        """
        Изменяет координаты БЛА.
        :param new_coordinates: Новые координаты (x, y)
        """
        self.model.update_coordinates(new_coordinates)
        self.view.show_status(self.model)

    def adjust_height(self, new_height):
        """
        Изменяет высоту полета БЛА.
        :param new_height: Новая высота
        """
        self.model.update_height(new_height)
        self.view.show_status(self.model)

    def adjust_velocity(self, new_velocity):
        """
        Изменяет скорость БЛА.
        :param new_velocity: Новая скорость
        """
        self.model.update_velocity(new_velocity)
        self.view.show_status(self.model)

    def check_battery(self):
        """
        Проверяет уровень заряда батареи и выполняет возвращение на базу при низком заряде.
        """
        if self.model.battery < 20:
            self.view.warning("Battery low! Initiating return to base.")
            self.return_to_base()

    def return_to_base(self):
        """
        Возвращает БЛА на базу.
        """
        self.model.update_coordinates((0, 0))
        self.model.update_height(0)
        self.model.update_velocity(0)
        self.view.show_status(self.model)
        self.view.warning("UAV has returned to base.")

# Наблюдатель и сенсор препятствий
class SensorListener:
    """
    Базовый класс наблюдателя за сенсорными данными.
    """

    def update(self, data):
        """
        Метод обновления сенсорных данных. Должен быть реализован в подклассах.
        """
        raise NotImplementedError("Метод update должен быть реализован")

class CollisionSensor(SensorListener):
    """
    Класс CollisionSensor отвечает за обработку данных о препятствиях и управляет БЛА.
    """

    def __init__(self, controller):
        """
        Инициализация сенсора препятствий.
        :param controller: Экземпляр UAVController для управления БЛА
        """
        self.controller = controller

    def update(self, data):
        """
        Обрабатывает данные сенсора о препятствиях и изменяет курс или останавливает БЛА.
        :param data: Данные сенсора (например, расстояние до препятствия)
        """
        if data['distance'] < 15:
            print("Obstacle detected! Altering course...")
            # Простейшая логика изменения курса: смещение на 15 единиц по оси y
            new_coordinates = (self.controller.model.coordinates[0], self.controller.model.coordinates[1] + 15)
            self.controller.adjust_position(new_coordinates)
        elif data['distance'] < 5:
            print("Critical proximity! Stopping UAV.")
            self.controller.adjust_velocity(0)  # Остановка

# Состояния полета
class UAVState:
    """
    Базовый класс для различных состояний полета БЛА.
    """

    def handle(self, uav):
        """
        Метод обработки состояния. Должен быть реализован в подклассах.
        """
        raise NotImplementedError("Метод handle должен быть реализован")

class AscentState(UAVState):
    """
    Класс AscentState отвечает за состояние набора высоты БЛА.
    """

    def handle(self, uav):
        """
        Реализует логику набора высоты БЛА.
        :param uav: Экземпляр StatefulUAV
        """
        print("Ascending...")
        uav.model.update_height(20)

class DescentState(UAVState):
    """
    Класс DescentState отвечает за состояние снижения высоты БЛА.
    """

    def handle(self, uav):
        """
        Реализует логику снижения высоты БЛА.
        :param uav: Экземпляр StatefulUAV
        """
        print("Descending...")
        uav.model.update_height(0)
        uav.model.update_velocity(0)

# БЛА с поддержкой состояний
class StatefulUAV:
    """
    Класс StatefulUAV управляет состояниями и действиями БЛА.
    """

    def __init__(self, state, model, view):
        """
        Инициализация БЛА с состояниями.
        :param state: Начальное состояние полета
        :param model: Экземпляр UAVModel
        :param view: Экземпляр UAVView
        """
        self.state = state
        self.model = model
        self.view = view

    def change_state(self, state):
        """
        Изменяет текущее состояние БЛА.
        :param state: Новое состояние полета
        """
        self.state = state

    def execute_action(self):
        """
        Выполняет действие в соответствии с текущим состоянием БЛА.
        """
        self.state.handle(self)
        self.view.show_status(self.model)

# Интеграция с внешним API
class WeatherService:
    """
    Класс WeatherService отвечает за взаимодействие с API для получения погодных данных.
    """

    def __init__(self, api_key):
        """
        Инициализация API с ключом доступа.
        :param api_key: Ключ доступа к API
        """
        self.api_key = api_key

    def fetch_weather(self, location):
        """
        Получает данные о погоде для указанного местоположения.
        :param location: Название местоположения (город, страна)
        :return: Погодные условия и скорость ветра
        """
        url = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={location}"
        response = requests.get(url)
        data = response.json()
        return data['current']['condition']['text'], data['current']['wind_mph']

# Пример использования WeatherService
# weather_service = WeatherService(api_key='your_api_key_here')
# current_weather, wind_speed = weather_service.fetch_weather('Los Angeles')
# print(f"Weather now: {current_weather}, Wind speed: {wind_speed} mph")

# Параллельная обработка данных с сенсоров
def handle_sensor_data(data):
    """
    Обрабатывает данные с сенсоров в параллельном потоке.
    :param data: Данные сенсора
    :return: Обработанные данные
    """
    processed_data = data * 3  # Пример обработки
    return processed_data

if __name__ == '__main__':
    sensor_data_samples = [2, 4, 6, 8, 10]
    threads = []
    results = []

    for data in sensor_data_samples:
        thread = threading.Thread(target=lambda q, arg1: q.append(handle_sensor_data(arg1)), args=(results, data))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Processed sensor data: {results}")

# Юнит-тесты
import unittest

class TestUAVNavigation(unittest.TestCase):
    """
    Класс TestUAVNavigation тестирует основные функции управления БЛА.
    """

    def test_adjust_position(self):
        """
        Тестирует обновление координат БЛА.
        """
        uav_model = UAVModel()
        controller = UAVController(uav_model, UAVView())
        controller.adjust_position((15, 30))
        self.assertEqual(uav_model.coordinates, (15, 30))

    def test_battery_check(self):
        """
        Тестирует проверку уровня заряда батареи и возвращение на базу.
        """
        uav_model = UAVModel()
        uav_model.consume_battery(85)  # Снижаем заряд батареи
        controller = UAVController(uav_model, UAVView())
        controller.check_battery()
        self.assertEqual(uav_model.coordinates, (0, 0))  # БЛА должен вернуться на базу

if __name__ == '__main__':
    unittest.main()
