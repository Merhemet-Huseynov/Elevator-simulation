from user import User
from clear import Clear
import time

class ElevatorProcess(Clear, User):

    def get_floor_status(self, level: int, 
                         user_floor: int, 
                         target_floor: int, 
                         user_level: int, 
                         target: list) -> str:

        """Determines whether the elevator is full or not, its status."""

        result = ""
        if user_floor >= target_floor:
            if user_floor >= target_floor:
                result += f"{level} - {target} \n"
            else:
                result += f"{level} - [] \n"
        else:
            if level >= user_level:
                result += f"{level} - {target} \n"
            else:
                result += f"{level} - [] \n"
        return result


    def get_direction_params(self, direction: str, floor_count: list) -> tuple:

        """Determines whether the elevator will travel in an upward or downward direction."""

        if direction == "up":
            start, end, step = self.current_floor, len(floor_count) + 1, 1 
        else:
            start, end, step = self.current_floor, 0, -1 
        return start, end, step


    def check_floor_status(self, level: int, 
                           user_floor: int, 
                           target_floor: int, 
                           users: str, 
                           user_arrived: bool, 
                           target: list) -> tuple:

        """Checks whether the elevator has reached the user's floor or the 
             target floor and updates the elevator's current floor."""

        if level == user_floor:
            target.append(users) 
        if level == target_floor:
            user_arrived = True  
            target = []  
            print("The user has reached the target floor..")
            self.current_floor = target_floor  
        return user_arrived, target


    def print_elevator_message(self, user_level: int,
                               user_floor: int, 
                               target_floor: int,
                               floor: int,
                               users: str) -> None:

        """This prints messages about the elevator's movement and the 
              user's current floor and reaching the target floor."""

        if user_floor >= target_floor:
            if user_floor >= target_floor:
                print(f"Elevator movement {floor}\n{users}"
                      f"\nUser\'s current floor  - {user_level}"
                      f"\nUser\'s target floor - {target_floor}")
            else:
                print(f"The elevator was called from the {user_level}th floor.")
        else:
            if floor >= user_level:
                print(f"Elevator movement {floor}\n{users}"
                      f"\nUser\'s current floor  - {user_level}"
                      f"\nUser\'s target floor - {target_floor}")
            else:
                print(f"The elevator was called from the {user_level}th floor.")


    def move_elevator(self, floor_count: list, 
                      user_floor: int, 
                      target_floor: int, 
                      users: str, 
                      direction: str) -> None:

        """Simulates the movement of the elevator, 
             updating the floor status and 
        tracking the user's journey to the target floor."""
        
        # User's current floor
        user_level = User.user_current_floor

        result = ""
        target = []
        user_arrived = False

        # Direction check
        start, end, step = self.get_direction_params(direction, 
                                                     floor_count)

        for floor in range(start, end, step):
            self.clear_terminal()
            result = ""
            
            if not user_arrived:
                # Print elevator movement and user information
                self.print_elevator_message(user_level, 
                                            user_floor, 
                                            target_floor,
                                            floor, users)
                
            for level in range(len(floor_count), 0, -1):
                if level == floor:
                    if not user_arrived:

                        # Call get_floor_status to check the floor status
                        result += self.get_floor_status(level, 
                                                        user_floor, 
                                                        target_floor, 
                                                        user_level, 
                                                        target)

                    # Check floor and whether user has reached the target
                    user_arrived, target = self.check_floor_status(level, 
                                                                   user_floor, 
                                                                   target_floor, 
                                                                   users, 
                                                                   user_arrived, 
                                                                   target)

                else:
                    result += f"{level} - \n"

            print(result)
            time.sleep(1)
            if user_arrived:
                break
                
