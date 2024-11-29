from elevator.elevator_process import ElevatorProcess
import time

class Elevator(ElevatorProcess):
    def __init__(self):
        self.current_floor = 1

    def move_floors_of_elevator(self, total_floors: int):
        result = []
        for floor in range(total_floors, 0, -1):
            result.append(floor)
        return result

    def up_move_of_elevator(self, floor_count: list, user_floor: int, target_floor: int, users: str):
        self.move_elevator(floor_count, 
                           user_floor, 
                           target_floor, 
                           users, 
                           direction="up")

    def down_move_of_elevator(self, floor_count: list, user_floor: int, target_floor: int, users: str):
        self.move_elevator(floor_count, 
                           user_floor,
                           target_floor, 
                           users, 
                           direction="down")

