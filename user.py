import random

class User:
    def generate_user_count(self):
        return random.randint(1, 3)  

    def current_floor(self, number_of_floors: int):
        return random.randint(1, number_of_floors)

    def target_floor(self, number_of_floors: int):
        return random.randint(1, number_of_floors)
