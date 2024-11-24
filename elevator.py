class Elevator:
    def __init__(self):
        self.current_floor = 1

    def move_up(self, target_floor):
        return (f"The lift is on the {self.current_floor}th floor:\n"
                f"Moving up to the {target_floor}th floor."
               )

    def move_down(self, target_floor):
        return (f"The lift is on the {self.current_floor}th floor:\n"
                f"Moving down to the {target_floor}th floor."
               )


    def operate(self, current_floor, user_floor, target_floor):
        if current_floor < user_floor:
            action = self.move_up(user_floor)
            self.current_floor = user_floor
        elif current_floor > user_floor:
            action = self.move_down(user_floor)
            self.current_floor = user_floor
        else:
            action = "The lift is already on the floor where the user is."

        if self.current_floor < target_floor:
            action += f" {self.move_up(target_floor)}"
            self.current_floor = target_floor
        elif self.current_floor > target_floor:
            action += f" {self.move_down(target_floor)}"
            self.current_floor = target_floor
        else:
            action += "The user is already on the desired floor."

        return action
