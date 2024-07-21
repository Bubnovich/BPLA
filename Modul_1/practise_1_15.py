# Класс drone
# конструктор с атрибутами литим мы или нет и уровень заряда батареи
# взлет с проверкой батареи
# если больше 20% то разрешаем взлет

class Drone:
    def __init__(self, id, is_fly=False, battery_capcity=100):
        self.id = id
        self.is_fly = is_fly
        self.battery_capacity = battery_capcity

    def takeoff(self):
        if self.battery_capacity > 20:
            self.is_fly = True
            print(f"{id} уровень заряда батареи: {self.battery_capacity} - взлет разрешен")
            return "Дрон взлетел"
        else:
            print(f"{id} уровень заряда батареи: {self.battery_capacity} - взлет запрещен")
            return "низкий заряд батареии"

    def land(self):
        if self.is_fly:
            self.is_fly = False
            return "Дрон приземлился"
        else:
            return "Дрон на земле"
def main():
    my_drone = Drone("ABC", battery_capcity=100)
    print(my_drone.takeoff())
    print(my_drone.land())

if __name__ == "__main__":
    main()