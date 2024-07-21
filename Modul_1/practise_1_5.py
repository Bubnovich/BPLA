import random
class GPS:
    def __init__(self, init_coordinates=(0.0, 0.0)):
        self.coordinates = init_coordinates

    def update_coordinates(self):
        """
        Симулирует обновление координат GPS
        :return:
        """
        #lat = round(random.uniform(1, 50), 4) # Широта
        #lon = round(random.uniform(1, 50), 4)  # долгота

        lat_variation = round(random.uniform(-0.0001, 0.0001), 4) # изменение широты
        lon_variation = round(random.uniform(-0.0001, 0.0001), 4)  # изменение широты
        lat = round(self.coordinates[0] + lat_variation, 4)
        lon = round(self.coordinates[1] + lon_variation, 4)
        self.coordinates = (lat, lon)
        #print(f"Обновление координаты: {self.coordinates}")
        return self.coordinates

class DistanceSensor:
    def __init__(self, max_dist=10000.0):
        self.max_dist = max_dist
        self.cur_dist = self.update_dist()
    def update_dist(self):
        """
        Симулируем измерение растояния
        :return:
        """
        return random.uniform(0, self.max_dist)

    def get_dist(self):
        print(self.cur_dist)
        return self.cur_dist


if __name__ == '__main__':
    print(gps_module.coordinates)
    for i in range(100):
        gps_module.update_coordinates()