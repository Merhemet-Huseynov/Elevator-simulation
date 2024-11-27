import time

class Elevator:
    def __init__(self):
        self.current_floor = 1

    def move_floors_of_elevator(self, total_floors: int):
        result = []
        for floor in range(total_floors, 0, -1):
            result.append(f"{floor}")
        return result

    def down_move_of_elevator(self, floor_count: list):
        result = ""
        for x in range(len(floor_count)-1, -1, -1):
            result = ""
            for y in range(len(floor_count), 0, -1):
                if y == x + 1:
                    result += f"{y} - []\n"
                else:
                    result += f"{y} - \n"
            print(result)
            time.sleep(1)
        return result

    def up_move_of_elevator(self, floor_count: list):
        result = ""
        for x in range(len(floor_count)):
            result = ""
            for y in range(len(floor_count), 0, -1):
                if y == x + 1:
                    result += f"{y} - []\n"  
                else:
                    result += f"{y} - \n"
            print(result)
            time.sleep(1) 
        return result