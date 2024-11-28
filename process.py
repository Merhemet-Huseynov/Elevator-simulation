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
    elevator_current_floor = elevator.current_floor
    floors = elevator.move_floors_of_elevator(floors_count)
    
    # About the user
    user_current_floor = user.current_floor(floors_count)
    user_target_floor = user.target_floor(floors_count)
    user_count = user.generate_user_count()

    # Elevator movement logic
    if user_current_floor > elevator_current_floor:
        if user_target_floor > user_current_floor:
            return elevator.up_move_of_elevator(floors, 
                                                user_current_floor, 
                                                user_target_floor, 
                                                user_count
                                                )
    elif user_current_floor < elevator_current_floor:
        if user_target_floor < user_current_floor:
            return elevator.down_move_of_elevator(floors, 
                                                  user_current_floor, 
                                                  user_target_floor, 
                                                  user_count)
                                                  
    
    return "User current floor is same as target floor"

# Run the simulation
result = simulation()
print(result)
