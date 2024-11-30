import random

class User:
    user_current_floor = None

    def generate_user_count(self):
        user_count = random.randint(1, 5)
        return " ".join(["user"] * user_count)

    def current_floor(self, number_of_floors: int):
        User.user_current_floor = random.randint(1, number_of_floors)
        return User.user_current_floor

    def target_floor(self, number_of_floors: int):
        return random.randint(1, number_of_floors)