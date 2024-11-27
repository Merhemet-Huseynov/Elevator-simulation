from building import Building
from elevator import Elevator
from user import User

def simulation():
    building = Building() 
    elevator = Elevator()  
    user = User()       

    # About the building
    floors_count = building.number_of_floors
    
    # About the elevator
    floors = elevator.move_floors_of_elevator(floors_count)
    down_move = elevator.down_move_of_elevator(floors)
    up_move = elevator.up_move_of_elevator(floors)

    # About the user
    user_current_floor = user.current_floor(floors_count)
    user_target_floor = user.target_floor(floors_count)
    user_count = user.generate_user_count()

    os.system("cls")
    return

result = simulation()
print(result)



