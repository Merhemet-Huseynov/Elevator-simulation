from constant import Building
from elevator import Elevator
from user import User

def run_simulation():
    building = Building()
    elevator = Elevator()
    user = User()

    total_floors = building.number_of_floors

    elevator_start_floor = elevator.current_floor
    user_start_floor = user.current_floor(total_floors)
    user_target_floor = user.destination_floor(total_floors)

    print(f"The user is on the {user_start_floor}th floor\n",
          f"wants to go to the {user_target_floor}th floor."
         )

    result = elevator.operate(elevator_start_floor, user_start_floor, user_target_floor)
    return result

if __name__ == "__main__":
    result = run_simulation()
    print(result)
