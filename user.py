import random

class User:
    def generate_user_count(self):
        return random.randint(1, 3)

    def current_floor(self, number_of_floors):
        return random.randint(1, number_of_floors)

    def destination_floor(self, number_of_floors):
        return random.randint(1, number_of_floors)
