from game_parser import read_lines
from grid import grid_to_string
from game_parser import parse
from player import Player
from game_parser import string_to_grid
from cells import Fire


class Game:
    def __init__(self, filename):
        self.map=string_to_grid(filename)
        self.lose=False   #lose switch
        self.win = False  #win switch
        self.get_water_bucket= False   #get water bucket switch
        self.throw_water_bucket= False #throw water bucket switch
        self.move_illegal= False   #illegal move switch
        self.wait = False  #wait(e) switch
        self.tp = False   #teleport switch
        self.quit_game =False  #quit game(q) switch



    def legal_move(self,row,col):
        """setter method: determine the move is legal or not

        :param:
            row -- receive the row of player in the current point
            col -- receive the col of player in the current point

            """
        if row < 0 or col < 0 or row >= len(self.map) or col >= len(self.map[0]) or self.map[row][col].display == '*':
            self.move_illegal = True

        else:
            self.move_illegal =False



    def game_move(self, move,player):
        '''setter method: set the new col and row for the player

        :param:
            move -- receive command from run.py 'w,a,s,d,e,q'
            player -- receive an object of player

        '''
        row=player.row
        col=player.col

        if move == 'w':
            self.legal_move(row-1, col)
            if self.move_illegal == False:
                player.row -=1
        elif move == 'a':
            self.legal_move(row, col-1)
            if self.move_illegal == False:
                player.col -= 1
        elif move == 's':
            self.legal_move(row+1, col)
            if self.move_illegal == False:
                player.row += 1
        elif move == 'd':
            self.legal_move(row, col+1)
            if self.move_illegal == False:
                player.col += 1
        elif move == 'e':
            self.wait = True
        elif move == 'q':
            self.quit_game = True




    def starting(self,player):
        '''getter method: let the player in the starting point X

        :param:
            player -- receive an object of player

        :return
            a map with the player at starting point X

        '''
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.map[row][col].display == 'X':
                    player.row = row
                    player.col = col

        map=grid_to_string(self.map,player)

        return map



    def teleport(self,row,col,player):
        '''setter method: make player from one tp pad to the other, and renew tp status

        :param:
            player -- receive an object of player
            row -- receive the row of player in the current point
            col -- receive the col of player in the current point

                '''
        that_gate = self.map[row][col].display
        that_gate_point = (row, col)
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                if self.map[x][y].display == that_gate:
                    if (x, y) != that_gate_point:
                        player.row = x
                        player.col = y
                        self.tp = True



    def water_wall(self,row,col,player):
        '''setter method: renew the water bucket status and number of water buckets of player

        :param
        player -- receive an object of player
        row -- receive the row of player in the current point
        col -- receive the col of player in the current point

        '''
        player.num_water_buckets += 1
        self.get_water_bucket = True
        self.map[row][col].display = ' '



    def fire_wall(self,row,col,player):
        '''setter method: renew the throw water bucket status and determine lose or not

        :param
            player -- receive an object of player
            row -- receive the row of player in the current point
            col -- receive the col of player in the current point

        '''
        if player.num_water_buckets > 0:
            player.num_water_buckets -= 1
            self.throw_water_bucket = True
            self.map[row][col].display = ' '

        else:
            self.lose = True



    def normal(self,player):
        '''getter method: normal map

        :param:
            player -- receive an object of player

        :return:
            normal map

        '''
        self.throw_water_bucket = False
        self.get_water_bucket = False
        self.tp = False

        row=player.row
        col=player.col
        tp_gate=['1', '2', '3', '4', '5', '6', '7', '8', '9']


        if self.move_illegal == False:
            if self.map[row][col].display == 'W':
                self.water_wall(row,col,player)

            if self.map[row][col].display == 'F':
                self.fire_wall(row,col,player)

            if self.map[row][col].display in tp_gate:
                if self.wait == False:
                    self.teleport(row,col,player)
                elif self.wait == True:
                    self.teleport(row,col,player)

            if self.map[row][col].display == 'Y':
                self.win = True

        map = grid_to_string(self.map, player)

        return map





