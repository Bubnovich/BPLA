from abc import ABC, abstractmethod

class DroneController:
    def takeoff(self):
        print('Дрон взлетает')


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
    def execute(self):
        self.__drone.move_forward()