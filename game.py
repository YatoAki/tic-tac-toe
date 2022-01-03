import os
import time

from player import Player
from board import Board

class Game:
    def __init__(self,player_one,player_two,board):
        self.board = board
        self.p1 = player_one
        self.p2 = player_two
        self.current_player = self.p1

    def play_turn(self):
        os.system('clear')
        self.board.display_board()
        move = None
        while move == None:
            print("It is "+self.current_player.name+"'s turn!")
            move = self.current_player.get_move()
            if self.board.empty(move):
                self.board.set(move,self.current_player.mark)
                self.change_current_player()
            else:
                print("Tile is already taken")
                time.sleep(1)
                os.system('clear')
                self.board.display_board()
                move = None
        os.system('clear')

    def change_current_player(self):
        if self.current_player == self.p1:
            self.current_player = self.p2
        else:
            self.current_player = self.p1

    def play(self):
        while not self.board.game_over():
            self.play_turn()
        self.board.display_board()
        winner = self.board.winner()
        if winner:
            if winner == "p1":
                print("Congratulation! "+ self.p1.name + " win the match.")
            else:
                print("Congratulation! "+ self.p2.name + " win the match.")
        else:
            print("Oops! Nobody win this match.")




if __name__ == "__main__":
    n1 = input("Enter the name of player one for X : ")
    n2 = input("Enter the name of player two for Y : ")
    os.system('clear')
    p1 = Player(n1,'X')
    p2 = Player(n2,'Y')
    while(True):
        b = Board()
        g = Game(p1,p2,b)
        g.play()
        restart = input("Do you want to start another match?(y/n)")
        if restart == 'n' or restart == 'N':
            print("THANKS FOR PLAYING")
            break;
