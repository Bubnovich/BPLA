# Реализация фабричного паттерна
from abc import ABC, abstractmethod

class Mission(ABC):
    @abstractmethod
    def execute(self):
        pass

class BackMission(Mission):
    def execute(self):
        return "Выполнение миссии возврат на базу"

class MappingMission(Mission):
    def execute(self):
        return "Выполнение картографирования"

class PatrolMission(Mission):
    def execute(self):
        return "Выполнение патрулирования"

class FireFightMission(Mission):
    def execute(self):
        return "Выполнение тушения пожара"

class EvacuationMission(Mission):
    def execute(self):
        return "Выполнение эвакуации"

class FollowingMission(Mission):
    def execute(self):
        return "Выполнение следования за объектом"

class MissionFactory(ABC):
    @abstractmethod
    def create_mission(self):
        pass


class BackMissionFactory(MissionFactory):
    def create_mission(self):
        return BackMission()


class MappingMissionFactory(MissionFactory):
    def create_mission(self):
        return MappingMission()


class PatrolMissionFactory(MissionFactory):
    def create_mission(self):
        return PatrolMission()


class FireFightMissionFactory(MissionFactory):
    def create_mission(self):
        return FireFightMission()


class EvacuationFactory(MissionFactory):
    def create_mission(self):
        return EvacuationMission()


class FollowingMissionFactory(MissionFactory):
    def create_mission(self):
        return FollowingMission()

def mission_planner(factory: MissionFactory):
    mission = factory.create_mission()
    return mission.execute()

if __name__ == "__main__":
    test = BackMission()
    patrol_factory = PatrolMissionFactory()
    print(mission_planner(patrol_factory))

    mapping_factory = MappingMissionFactory()
    print(mission_planner(mapping_factory))