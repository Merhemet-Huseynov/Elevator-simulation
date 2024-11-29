import random

class User:
    def generate_user_count(self):
        user_count = random.randint(1, 3)
        return " ".join(["user"] * user_count)

    def current_floor(self, number_of_floors: int):
        return 9

    def target_floor(self, number_of_floors: int):
        return 4
