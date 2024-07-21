import unittest
from Modul_1.practise_1_15 import Drone

class TestDrone(unittest.TestCase):
    def setUp(self):
        self.drone = Drone("ABC", battery_capcity=100)

    def test_takeoff(self):
        # высокий уровень заряда
        self.drone.battery_capacity = 50
        result = self.drone.takeoff()
        self.assertTrue(self.drone.is_fly)
        self.assertEqual(result, "Дрон взлетел")

        # низкий уровень заряда
        self.drone.battery_capacity = 10
        result = self.drone.takeoff()
        self.assertTrue(self.drone.is_fly)
        self.assertEqual(result, "низкий заряд батареии")

    def test_land_not_fly(self):
        self.drone.is_fly = False
        result = self.drone.land()
        self.assertFalse(self.drone.is_fly)
        self.assertEqual(result, "Дрон на земле")

    def test_land_fly(self):
        self.drone.is_fly = True
        result = self.drone.land()
        self.assertFalse(self.drone.is_fly)
        self.assertEqual(result, "Дрон приземлился")


if __name__ == "__main__":
    unittest.main()