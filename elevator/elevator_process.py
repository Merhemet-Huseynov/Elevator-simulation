from clear import Clear
import time

class ElevatorProcess(Clear):
    def move_elevator(self, floor_count: list, user_floor: int, target_floor: int, users: str, direction: str):
        target = []
        user_arrived = False

        if direction == "up":
            start, end, step = self.current_floor, len(floor_count) + 1, 1
        else:
            start, end, step = self.current_floor, 0, -1

        for floor in range(start, end, step):
            self.clear_terminal()
           
            if not user_arrived:
                result = ""
                print(f"elevator {start} {users} Current floor - {user_floor}  Target floor - {target_floor}")

            for user in range(len(floor_count), 0, -1):
                if user == floor:
                    if not user_arrived:
                        result += f"{user} - {target} \n"
                    if user == user_floor:
                        target.append(users)
                    if user == target_floor:
                        user_arrived = True
                        target = [] 
                        print("The user has reached the target floor..")
                        self.current_floor = target_floor
                else:
                    result += f"{user} - \n"

            print(result)
            time.sleep(1)
            if user_arrived:
                break
