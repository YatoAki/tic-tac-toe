class Player:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark

    def get_move(self):
        user_in = input("Use your keypad to place a mark : ")
        return user_in
        

