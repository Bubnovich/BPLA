from practise_3_13 import *

drone_controller = DroneController()

takeoff = Takeoff(drone_controller)
move_forward = MoveForward(drone_controller, 100)

#takeoff.execute()
#move_forward.execute()

commands = [
    Takeoff(drone_controller),
    MoveForward(drone_controller, 100),
MoveForward(drone_controller, -100)
]

strategy = ReconMissionStrategy()
strategy.execute(commands=commands)