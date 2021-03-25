from game import Game
from player import Player
from grid import grid_to_string
import os
import sys



def move_counter(move_ls):
    '''count movement times
    :param
        move_ls -- a list contains the valid command
    :return:
        message and times of movement
    '''
    move_msg = ''
    move_msg += ", ".join(str(i) for i in move_ls)
    move_time = len(move_ls)
    if move_time == 1:
        msg = '\nYou made {} move.\nYour move: {}'.format(move_time, move_msg)
    else:
        msg = '\nYou made {} moves.\nYour moves: {}'.format(move_time, move_msg)
    return msg


def game_over():
    # message of gameover
    msg = '\n=====================\n===== GAME OVER =====\n====================='
    return msg


def step_into_fire():
    # message of step into fire
    msg = '\n\nYou step into the fires and watch your dreams disappear \
:(.\n\nThe Fire Nation triumphs! The Honourable Furious Forest is reduced \
to a pile of ash and is scattered to the winds by the next storm... You have been roasted.'
    return msg


def conquer_maze():
    # message of win1
    msg = '\n\nYou conquer the treacherous maze set up by the Fire Nation \
and reclaim the Honourable Furious Forest Throne, restoring your hometown \
back to its former glory of rainbow and sunshine! Peace reigns over the lands.'
    return msg


def win():
    # message of win2
    msg = '\n=====================\n====== YOU WIN! =====\n====================='
    return msg


filename = sys.argv[1]  # filename

current_player = Player()  # set up a player
current_map = Game(filename)  # set up a game

starting_graph = (current_map.starting(current_player))
print(starting_graph)  # print starting map

valid_command = ['w', 'a', 's', 'd', 'e', 'q']
move_ls = []
move_time = 0

while True:
    command = input('\nInput a move: ').lower()  # get the command from input
    if command in valid_command:

        current_map.game_move(command, current_player)  # game move method receive valid command
        if current_map.move_illegal == False:  # determine the move is legal or not
            move_ls.append(command)

        if current_map.quit_game == True:  # if q is pressed
            print('\nBye!')
            break

        new_map = current_map.normal(current_player)# update the current map
        #os.system("clear")
        print(new_map)

        if current_map.move_illegal == True:  # if the move is illegal
            print('\nYou walked into a wall. Oof!')

        if current_map.get_water_bucket == True:  # if players walk into a water cell and get the bucket
            print("\nThank the Honourable Furious Forest, you've found a bucket of water!")

        if current_map.throw_water_bucket == True:  # if players walk into a fire cell and throw the bucket
            print("\nWith your strong acorn arms, you throw a \
water bucket at the fire. You acorn roll your way through the extinguished flames!")

        if current_map.tp == True:  # if player walks in to a tp gate
            print('\nWhoosh! The magical gates break Physics as \
we know it and opens a wormhole through space and time.')

        if current_map.win == True:  # if win
            print(conquer_maze())
            print(move_counter(move_ls))
            print(win())
            break


        elif current_map.lose == True:  # if lose
            print(step_into_fire())
            print(move_counter(move_ls))
            print(game_over())
            break


    else:
        new_map = current_map.normal(current_player)  # if invalid commands are pressed
        print(new_map)
        print('\nPlease enter a valid move (w, a, s, d, e, q).')
