from practise_1_5 import GPS, DistanceSensor
class Drone:
    brand = 'БПЛА РФ'
    n_rotors = 4

    def __init__(self, model, weight, payload, id):
        self.id = id
        self.model = model
        self.weight = weight
        self.altitude = 0
        self.speed = 0
        self.payload = payload # Грузоподъемность в граммах
        self.pitch = 0 # Тангаж в градусах (Поворот вокруг поперчной оси (наклон вперед или назад)
        self.roll = 0 # Крен в градусах (Поворот вокруг продольной оси (наклон влево или вправо)
        self.yaw = 0 # Рысканье в градусах (Поворот вокруг вертикальной оси
        self.battery_capacity = 100 # Емкость батареи в процентах
        self.propellers_speed = [0, 0, 0, 0] # Скороть вращения пропеллеров в об/мин
        self.propellers_direction = ["CCW", "CW", "CW", "CCW"] # Направление вращения пропеллеров

        self.direction = 0 # Направление
        self.is_flying = False # Летит ли БПЛА
        self.is_connected = False # Подключен ли БПЛА
        self.is_armed = False # Арминг двигателя
        self.speed_k = 1000 # 1 м/с - 1000 об/мин

        self.cur_coordinates = (30.2344, 42.5332) # Начальные координаты
        self.coordinates = (50.1231, 30.5231) # Начальные координаты
        self.target_coord = (30.2344, 42.5332) # Координаты цели

        self.way_coords = [] # где был дро, его координаты пути
        self.gps = GPS(self.coordinates)
        self.dist_sensor = DistanceSensor()

    def get_dist(self):
        self.dist_sensor.get_dist()


    def get_coords(self):
        self.cur_coordinates = self.gps.update_coordinates()
        print(f'id: {self.id}, текущие координаты: {self.cur_coordinates}')

    def __del__(self):
        print("Экземпляр класса Drone уничтожен")

    def fly(self):
        pass
    def get_info(self):
        info = f"""
                -------Квадрокоптер-------
                Бренд: {self.brand}, Модель: {self.model}
                Количество роторов: {self.n_rotors}
                Высота: {self.altitude} м, Скорость: {self.speed} м/сек.
                Вес БПЛА: {self.weight} кг, Грузоподъемность: {self.speed} гр.
                Тангаж: {self.pitch}, Крен: {self.roll} Рысканье: {self.yaw}
                Скорость вращения пропеллеров: {self.propellers_speed}
                ({self.propellers_speed[0]})       ({self.propellers_speed[1]})
                 CCW      CW
                  \\        /
                   \\      /
                    ------
                   /      \\
                  /        \\
                 CW       CCW
                ({self.propellers_speed[2]})       ({self.propellers_speed[3]})
                """
        print(info)

if __name__ == "__main__":
    drone = Drone(model='Модель 1', weight=6, payload=1.5, id=4)
    drone.get_info()
    drone.get_coords()
    drone.cur_coordinates = (12.1234, 32.4321)
    drone.get_coords()

    drone2 = Drone(model='Модель 2', weight=3, payload=1.5, id=5)
    drone2.get_info()
    drone2.get_coords()