from elevator_system import User, Building
from elevator import Elevator
from time import sleep

def move_elevator_to_user(elevator, floors, elevator_current_floor, user_current_floor, user_count):

    """Moves the elevator to the user's current floor."""
    if user_current_floor > elevator_current_floor:
        elevator.up_move_of_elevator(floors, 
                                     elevator_current_floor, 
                                     user_current_floor, 
                                     user_count
                                     )
    elif user_current_floor < elevator_current_floor:
        elevator.down_move_of_elevator(floors, 
                                       elevator_current_floor, 
                                       user_current_floor,
                                       user_count
                                       )

def move_elevator_to_target(elevator, floors, user_current_floor, user_target_floor, user_count):
    """Moves the elevator to the user's target floor."""
    if user_target_floor > user_current_floor:
        elevator.up_move_of_elevator(floors, 
                                     user_current_floor, 
                                     user_target_floor, 
                                     user_count
                                     )
    elif user_target_floor < user_current_floor:
        elevator.down_move_of_elevator(floors, 
                                       user_current_floor,
                                       user_target_floor, 
                                       user_count
                                       )

def simulation():
    # Creation of objects  
    building = Building()
    elevator = Elevator()  
    user = User()      

    # Building details
    floors_count = building.number_of_floors
    
    # Elevator details
    elevator_current_floor = elevator.current_floor
    floors = elevator.move_floors_of_elevator(floors_count)
    
    # User details
    user_current_floor = user.current_floor(floors_count)
    user_target_floor = user.target_floor(floors_count)
    user_count = user.generate_user_count()

    # Elevator movement logic
    if user_current_floor != elevator_current_floor:
        move_elevator_to_user(elevator, 
                              floors, 
                              elevator_current_floor, 
                              user_current_floor, 
                              user_count)
        sleep(1)

    if user_target_floor != user_current_floor:
        move_elevator_to_target(elevator, 
                                floors, 
                                user_current_floor, 
                                user_target_floor, 
                                user_count)
        sleep(1)
    else:
        return "User current floor is same as target floor"




