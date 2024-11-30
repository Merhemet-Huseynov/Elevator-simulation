import os

class Clear:  
    def clear_terminal(self):
        os.system("cls" if os.name == "nt" else "clear")