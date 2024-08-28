from abc import ABC, abstractmethod

class DroneController:
    def takeoff(self):
        print('Дрон взлетает')

    def move_forward(self, distance: float):
       print(f"Летим вперед на {distance} меторов")

class ICommand(ABC):
    @abstractmethod
    def execute(self):
        pass
    #def undo(self):
     #   pass

class Takeoff(ICommand):
    def __init__(self, drone: DroneController):
        self.__drone = drone
    def execute(self):
        self.__drone.takeoff()

class MoveForward(ICommand):
    def __init__(self, drone: DroneController,
                 distance: float
                 ):
        self.__drone = drone
        self.distance = distance
    def execute(self):
        self.__drone.move_forward(self.distance)

class IFlightStrategy(ABC):
    @abstractmethod
    def execute(self, commands: list):
        pass

#Стратегия разведывательной миссии
class ReconMissionStrategy(IFlightStrategy):
    def execute(self, commands: list):
        print(f"Начало выполнения разведывательной миссии")
        for command in commands:
            command.execute()
        print(f"Конец миссии")
