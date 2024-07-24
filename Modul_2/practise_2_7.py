# паттерн Команда
from abc import ABC, abstractmethod
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def undo(self):
        pass

class Drone:
    def take_off(self):
        print(f"БПЛА взлетает")

    def change_course(self, new_course):
        print(f"БПЛА изменяет курс полета {new_course}")

    def land(self):
        print(f"БПЛА приземляется")

class TackeOFF(Command):
    def __init__(self, drone: Drone):
        self._drone = drone

    def execute(self):
        self._drone.take_off()

    def undo(self):
        self._drone.land()

class Land(Command):
    def __init__(self, drone: Drone):
        self._drone = drone

    def execute(self):
        self._drone.land()

    def undo(self):
        print(f"Отмена посадки невозможна")

class ChangeCourse(Command):
    def __init__(self, drone: Drone, course):
        self._drone = drone
        self._course = course
        self._previous_course = None

    def execute(self):
        self._previous_course = f"предыдущий курс"
        self._drone.change_course(self._course)

    def undo(self):
        if self._previous_course:
            self._drone.change_course(self._previous_course)

class RemoteControl:
    def __init__(self):
        self._commands = []
        self._history = []

    def add_command(self, command: Command):
        self._commands.append(command)

    def execute_command(self):
        for command in self._commands:
            command.execute()
            self._history.append(command)
        self._commands.clear()
    def undo_command(self):
        if self._history:
            command = self._history.pop()
            command.undo()

if __name__ == "__main__":
    drone = Drone()
    land = Land(drone)
    take_off = TackeOFF(drone)
    change_course = ChangeCourse(drone, "Новый курс")

    remote_control = RemoteControl()
    remote_control.add_command(take_off)
    remote_control.add_command(change_course)
    remote_control.add_command(land)
    remote_control.execute_command()

    remote_control.undo_command()

