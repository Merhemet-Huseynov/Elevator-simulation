import time

class Elevator:
    def __init__(self):
        self.current_floor = 1

    def move_floors_of_elevator(self, total_floors: int):
        result = []
        for floor in range(total_floors, 0, -1):
            result.append(floor)
        return result

    def move_elevator(self, floor_count: list, user_floor: int, target_floor: int, users: str, direction: str):
        result = ""
        target = []
        user_arrived = False

        if direction == "up":
            start, end, step = 0, len(floor_count), 1
        else:
            start, end, step = len(floor_count) - 1, -1, -1


        for floor in range(start, end, step):
            result = ""
            if not user_arrived:
                print(f"{users} Current floor - {user_floor}  Target floor - {target_floor}")
            for user in range(len(floor_count), 0, -1):
                if user == floor + 1:
                    if not user_arrived:
                        result += f"{user} - {target} \n"
                    if user == user_floor:
                        target.append(users)
                    if user == target_floor:
                        user_arrived = True
                        target = [] 
                        print("The user has reached the target floor..")
                        break
                else:
                    result += f"{user} - \n"
            print(result)
            time.sleep(1)
            if user_arrived:
                break  
        self.current_floor = target_floor


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

