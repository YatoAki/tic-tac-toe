class Board:
     decoder = { '7': [0,0], '8': [0,1] , '9': [0,2],
                 '4': [1,0], '5': [1,1] , '6': [1,2],
                 '1': [2,0], '2': [2,1] , '3': [2,2]}

     def __init__(self):
          self.grid = [[None,None,None],[None,None,None],[None,None,None]]

     def display_board(self):
          for indexR,row in enumerate(self.grid):
               for indexC,column in enumerate(row):
                    if column == None:
                         print('   ',end = '')
                    else:
                         print(' '+column+' ',end = '')
                    if indexC != 2:
                         print('|', end= '')
               if indexR != 2:
                    print()
                    print(' - + - + - ')
          print()

     def win_row(self,mark):
          for row in self.grid:
               if row.count(mark) == 3:
                    return True
          return False

     def win_col(self,mark):
          for i in range(3):
               l = [self.grid[0][i],self.grid[1][i],self.grid[2][i]]
               if l.count(mark) == 3:
                    return True
          return False

     def win_diag(self,mark):
          if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == mark or self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == mark:
               return True
          else:
               return False

     def win(self,mark):
          if self.win_row(mark) or self.win_col(mark) or self.win_diag(mark):
               return True
          else:
               return False

     def winner(self):
        if self.win('X'):
            return "p1"
        elif self.win('Y'):
            return "p2"

     def full(self):
          for row in self.grid:
               if None in row:
                    return False
          return True

     def game_over(self):
          if self.winner() or self.full():
               return True
          else:
               return False

     def set(self,key,mark):
          x,y = Board.decoder[key][0],Board.decoder[key][1]
          self.grid[x][y] = mark

     def empty(self,key):
          x,y = Board.decoder[key][0],Board.decoder[key][1]
          if self.grid[x][y] != None:
               return False
          return True
