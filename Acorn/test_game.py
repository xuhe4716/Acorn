from game import Game
from player import Player



#testings of legal_move method testing
def legal_move1():
    #edge casewhen row is less than 0
    game = Game('board_test.txt')
    actual = game.legal_move(3,-1)
    assert game.move_illegal == True, 'testcase legal_move1 failed.'

def legal_move2():
    #edge case when col is less than 0
    game = Game('board_test.txt')
    game.legal_move(-2, 4)
    assert game.move_illegal == True, 'testcase legal_move2 failed.'

def legal_move3():
    #edge case when col is equal to zero
    game = Game('board_test.txt')
    game.legal_move(5, 0)
    assert game.move_illegal == False,'testcase legal_move3 failed.'

def legal_move4():
    #edge testcase when row is larger than the length of row
    game = Game('board_test.txt')
    game.legal_move(16, 1)
    assert game.move_illegal == True, 'testcase legal_move4 failed.'

def legal_move5():
    #edge case when col equals to the length of colum
    game = Game('board_test.txt')
    game.legal_move(6, 15)
    assert game.move_illegal == True, 'testcase legal_move5 failed.'

def legal_move6():
    #edge case when the map[row][col] equals to "*"
    game = Game('board_test.txt')
    game.legal_move(1, 3)
    assert game.move_illegal == True, 'testcase legal_move6 failed.'

def legal_move7():
    #postive testcase when row and col are all correct
    game = Game('board_test.txt')
    game.legal_move(1, 2)
    assert game.move_illegal == False, 'testcase legal_move7 failed'

def legal_move_tests():
    legal_move1()
    legal_move2()
    legal_move3()
    legal_move4()
    legal_move5()
    legal_move6()
    legal_move7()




#testings of game move
def game_move_w():
    #positive testcase for input w
    game = Game('board_test.txt')
    player = Player()
    player.row = 2
    player.col = 1
    game.game_move('w',player)
    assert game.move_illegal == False, 'testcase game_move_w failed.'
    assert game.wait == False,'testcase game_move_w failed.'
    assert game.quit_game == False,'testcase game_move_w failed.'
    assert player.row == 1
    assert player.col == 1

def game_move_a():
    # positive testcase for input a
    game = Game('board_test.txt')
    player = Player()
    player.row = 1
    player.col = 2
    game.game_move('a',player)
    assert game.move_illegal == False, 'testcase game_move_a failed.'
    assert game.wait == False, 'testcase game_move_a failed.'
    assert game.quit_game == False, 'testcase game_move_a failed.'
    assert player.row == 1
    assert player.col == 1

def game_move_s():
    # positive testcase for input s
    game = Game('board_test.txt')
    player = Player()
    player.row = 1
    player.col = 1
    game.game_move('s',player)
    assert game.move_illegal == False, 'testcase game_move_s failed.'
    assert game.wait == False, 'testcase game_move_s failed.'
    assert game.quit_game == False, 'testcase game_move_s failed.'
    assert player.row == 2
    assert player.col == 1

def game_move_d():
    # positive testcase for input d
    game = Game('board_test.txt')
    player = Player()
    player.row = 1
    player.col = 1
    game.game_move('d', player)
    assert game.move_illegal == False, 'testcase game_move_d failed.'
    assert game.wait == False,  'testcase game_move_d failed.'
    assert game.quit_game == False,  'testcase game_move_d failed.'
    assert player.row == 1
    assert player.col == 2

def move_illegal():
    #edge case for illegal move
    game = Game('board_test.txt')
    player = Player()
    player.row = 4
    player.col = 5
    game.game_move('d', player)
    assert game.move_illegal == True, 'testcase move_illegal failed.'
    assert game.wait == False, 'testcase move_illegal failed.'
    assert game.quit_game == False, 'testcase move_illegal failed.'
    assert player.row == 4
    assert player.col == 5

def game_move_e():
    # edge case for input e
    game = Game('board_test.txt')
    player = Player()
    player.row = 1
    player.col = 1
    game.game_move('e', player)
    assert game.move_illegal == False, 'testcase game_move_e failed.'
    assert game.wait == True, 'testcase game_move_e failed.'
    assert player.row == 1
    assert player.col == 1

def game_move_q():
    # edge case for input q
    game = Game('board_test.txt')
    player = Player()
    player.row = 1
    player.col = 1
    game.game_move('q', player)
    assert game.move_illegal == False, 'testcase game_move_q failed.'
    assert game.wait == False, 'testcase game_move_q failed.'
    assert game.quit_game == True, 'testcase game_move_q failed.'
    assert player.row == 1
    assert player.col == 1

def game_move_tests():
    game_move_a()
    game_move_d()
    game_move_s()
    game_move_w()
    move_illegal()
    game_move_e()
    game_move_q()




#testing of starting
def starting_test():
    #postive testcase for starting method
    game = Game('board_test.txt')
    player = Player()
    actual = game.starting(player)
    excepted = '*****A*********\n*  * 2    1   *\n* *W* \
*********\n* *  W*   3 F *\n* ********** **\n   1 *   ** F**\n* ** *2*  \
F   *\n* 3***W******F*\n*************Y*\n\nYou have 0 water buckets.'
    assert actual == excepted, 'testcase starting_test failed.'




#testing of teleport
def teleport_test():
    #postive test case when player in the tp gate
    game = Game('board_test.txt')
    player = Player()
    player.row = 1
    player.col = 5
    game.teleport(player.row,player.col,player)
    assert player.row == 6, 'testcase teleport_test failed.'
    assert player.col == 6, 'testcase teleport_test failed.'
    assert game.tp == True, 'testcase teleport_test failed.'




#testing of water_wall
def water_wall_test():
    game = Game('board_test.txt')
    player = Player()
    player.row = 2
    player.col = 3
    game.water_wall(player.row,player.col,player)
    assert player.num_water_buckets == 1, 'testcase water_wall_test failed.'
    assert game.get_water_bucket == True, 'testcase water_wall_test failed.'
    assert game.map[2][3].display == ' ', 'testcase water_wall_test failed.'




#testings of fire wall
def fire_wall_test1():
    #postive testcase when water buckets are larger than 0
    game = Game('board_test.txt')
    player = Player()
    player.row = 3
    player.col = 12
    player.num_water_buckets = 2
    game.fire_wall(player.row,player.col,player)
    assert player.num_water_buckets == 1, 'testcase fire_wall_test1 failed.'
    assert game.throw_water_bucket == True, 'testcase fire_wall_test1 failed.'
    assert game.map[3][12].display == ' ', 'testcase fire_wall_test1 failed.'

def fire_wall_test2():
    #edge test when water bucket is 0
    game = Game('board_test.txt')
    player = Player()
    player.row = 3
    player.col = 12
    player.num_water_buckets = 0
    game.fire_wall(player.row, player.col, player)
    assert player.num_water_buckets == 0, 'testcase fire_wall_test2 failed.'
    assert game.throw_water_bucket == False, 'testcase fire_wall_test2 failed.'
    assert game.lose == True, 'testcase fire_wall_test2 failed.'

def fire_wall_tests():
    fire_wall_test1()
    fire_wall_test2()




def normal1():
    #postive testcase: player in the air wall
    game = Game('board_test.txt')
    player = Player()
    player.row = 1
    player.col = 1
    actual = game.normal(player)
    excepted = '*****X*********\n*A * 2    1   *\n* *W* \
*********\n* *  W*   3 F *\n* ********** **\n   1 *   \
** F**\n* ** *2*  F   *\n* 3***W******F*\n*************Y*\n\nYou have 0 water buckets.'
    assert actual == excepted, 'testcase normal1 failed.'

def normal2():
    #postive testcase: player in the water cell
    game = Game('board_test.txt')
    player = Player()
    player.row = 3
    player.col = 5
    actual = game.normal(player)
    excepted = '*****X*********\n*  * 2    1   *\n* *W* \
*********\n* *  A*   3 F *\n* ********** **\n   1 *   ** \
F**\n* ** *2*  F   *\n* 3***W******F*\n*************Y*\n\nYou have 1 water bucket.'
    assert actual == excepted, 'testcase normal2 failed.'

def normal3():
    #postive testcase: player in the fire cell
    game = Game('board_test.txt')
    player = Player()
    player.row = 6
    player.col = 10
    actual = game.normal(player)
    excepted = '*****X*********\n*  * 2    1   *\n* *W* ****\
*****\n* *  W*   3 F *\n* ********** **\n   1 *   ** F**\n* **\
 *2*  A   *\n* 3***W******F*\n*************Y*\n\nYou have 0 water buckets.'
    assert actual == excepted, 'testcase normal3 failed.'

def normal4():
    #postive testcase: player in tp gate
    game = Game('board_test.txt')
    player = Player()
    player.row = 5
    player.col = 3
    game.wait = False
    actual = game.normal(player)
    excepted = '*****X*********\n*  * 2    A   *\n* *W* ********\
*\n* *  W*   3 F *\n* ********** **\n   1 *   ** F**\n* ** *2*  F\
   *\n* 3***W******F*\n*************Y*\n\nYou have 0 water buckets.'
    assert actual == excepted, 'testcase normal4 failed.'

def normal5():
    #edge case: player in tp gate but e is pressed
    game = Game('board_test.txt')
    player = Player()
    player.row = 1
    player.col = 10
    game.wait = True
    actual = game.normal(player)
    excepted = '*****X*********\n*  * 2    1   *\n* *W* *********\n* \
*  W*   3 F *\n* ********** **\n   A *   ** F**\n* ** *2*  F   *\n* 3*\
**W******F*\n*************Y*\n\nYou have 0 water buckets.'
    assert actual == excepted, 'testcase normal5 failed.'

def normal6():
    #postive testcase: player win
    game = Game('board_test.txt')
    player = Player()
    player.row = 8
    player.col = 13
    actual = game.normal(player)
    excepted = '*****X*********\n*  * 2    1   *\n* *W* ******\
***\n* *  W*   3 F *\n* ********** **\n   1 *   ** F**\n* ** *2*\
  F   *\n* 3***W******F*\n*************A*\n\nYou have 0 water buckets.'
    assert actual == excepted, 'testcase normal6 failed.'

def normal7():
    #edge case: move is illegal
    game = Game('board_test.txt')
    player = Player()
    player.row = 1
    player.col = 2
    game.move_illegal = True
    actual = game.normal(player)
    excepted = '*****X*********\n* A* 2    1   *\n* *W* ********\
*\n* *  W*   3 F *\n* ********** **\n   1 *   ** F**\n* ** *2*  F\
   *\n* 3***W******F*\n*************Y*\n\nYou have 0 water buckets.'
    assert actual == excepted, 'testcase normal7 failed.'

def normal_tests():
    normal1()
    normal2()
    normal3()
    normal4()
    normal5()
    normal6()
    normal7()






def run_tests():
    legal_move_tests()
    game_move_tests()
    starting_test()
    teleport_test()
    water_wall_test()
    fire_wall_tests()
    normal_tests()
    




