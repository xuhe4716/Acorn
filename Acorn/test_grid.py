from grid import grid_to_string
from player import Player
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

def test_grid1():
    #postive testcase with 2 waterbucket at the other position
    grid = [[Wall(), Wall(), Start(), Wall(), Wall()],
            [Wall(), Water(), Teleport('1'), Wall(), Wall()],
            [Wall(), Air(), Fire(), Teleport('1'), Wall()],
            [Wall(), Wall(), End(), Wall(), Wall()]]
    player = Player()
    player.row = 1
    player.col = 1
    player.num_water_buckets = 2
    actual = grid_to_string(grid, player)
    excepted = '**X**\n*A1**\n* F1*\n**Y**\n\nYou have 2 water buckets.'
    assert actual == excepted, 'testcase test_grid1 failed.'


def test_grid2():
    #edge case with 0 waterbucket at the initial postion
    grid = [[Wall(),Wall(),Start(),Wall(),Wall()],
            [Wall(),Water(),Teleport('1'),Wall(),Wall()],
            [Wall(),Air(),Fire(),Teleport('1'),Wall()],
            [Wall(),Wall(),End(),Wall(),Wall()]]
    player = Player()
    actual = grid_to_string(grid,player)
    excepted = 'A*X**\n*W1**\n* F1*\n**Y**\n\nYou have 0 water buckets.'
    assert actual == excepted, 'testcase test_grid2 failed.'


def test_grid3():
    #edge case with 1 waterbucket at the other position
    grid = [[Wall(), Wall(), Start(), Wall(), Wall()],
            [Wall(), Water(), Teleport('1'), Wall(), Wall()],
            [Wall(), Air(), Fire(), Teleport('1'), Wall()],
            [Wall(), Wall(), End(), Wall(), Wall()]]
    player = Player()
    player.row = 2
    player.col = 1
    player.num_water_buckets = 1
    actual = grid_to_string(grid, player)
    excepted = '**X**\n*W1**\n*AF1*\n**Y**\n\nYou have 1 water bucket.'
    assert actual == excepted, 'tesecase test_grid3 failed.'



def run_tests():
    test_grid1()
    test_grid2()
    test_grid3()


