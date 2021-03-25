from game_parser import parse
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)


def test_parse1():
    #postive testcase
    grid = ['**X**\n', '*W1**\n', '* F1*\n', '**Y**']
    actual = parse(grid)
    excepted = [[isinstance(actual[0][0],Wall), isinstance(actual[0][1],Wall),isinstance(actual[0][2],Start), isinstance(actual[0][3],Wall), isinstance(actual[0][4],Wall)],
                [isinstance(actual[1][0], Wall), isinstance(actual[1][1], Water), isinstance(actual[1][2],Teleport),isinstance(actual[1][3], Wall), isinstance(actual[1][4], Wall)],
                [isinstance(actual[2][0], Wall), isinstance(actual[2][1], Air), isinstance(actual[2][2], Fire),isinstance(actual[2][3], Teleport), isinstance(actual[2][4], Wall)],
                [isinstance(actual[3][0], Wall), isinstance(actual[3][1], Wall), isinstance(actual[3][2], End),isinstance(actual[3][3], Wall), isinstance(actual[3][4], Wall)]]
    for item in excepted:
        for a in item:
            assert a == True, 'testcase test_parse1 failed.'



def test_parse2():
    #negative testcase with no starting
    grid = ['*****\n', '*W1**\n', '* F1*\n', '**Y**']
    try:
        actual = parse(grid)
    except Exception as e:
        assert type(e) == ValueError, 'testcase test_parse2 failed.'
        assert str(e) == 'Expected 1 starting position, got 0.', 'testcase test_parse2 failed.'


def test_parse3():
    #negative testcase with 2 endings
    grid = ['**X**\n', '*W1**\n', '* F1*\n', '*Y*Y*']
    try:
        actual = parse(grid)
    except Exception as e:
        assert type(e) == ValueError, 'testcase test_parse3 failed.'
        assert str(e) == 'Expected 1 ending position, got 2.', 'testcase test_parse3 failed.'


def test_parse4():
    #negative testcase with unmatching pad
    grid = ['**X2*\n', '*W1**\n', '* F1*\n', '**Y**']
    try:
        actual = parse(grid)
    except Exception as e:
        assert type(e) == ValueError, 'testcase test_parse4 failed.'
        assert str(e) == 'Teleport pad 2 does not have an exclusively matching pad.', 'testcase test_parse4 failed.'


def test_parse5():
    #negative testcase with bad letter
    grid = ['**X**\n', '*W1**\n', '* F1*\n', '!*Y**']
    try:
        actual = parse(grid)
    except Exception as e:
        assert type(e) == ValueError, 'testcase test_parse5 failed.'
        assert str(e) == 'Bad letter in configuration file: !.', 'testcase test_parse5 failed.'


def test_parse6():
    #edge case with 4 teleport gates
    grid = ['**X**\n', '*W77*\n', '* F77\n', '**Y**']
    actual = parse(grid)
    excepted = [[isinstance(actual[0][0], Wall), isinstance(actual[0][1], Wall), isinstance(actual[0][2], Start), isinstance(actual[0][3], Wall), isinstance(actual[0][4], Wall)],
                [isinstance(actual[1][0], Wall), isinstance(actual[1][1], Water), isinstance(actual[1][2], Teleport),isinstance(actual[1][3], Teleport), isinstance(actual[1][4], Wall)],
                [isinstance(actual[2][0], Wall), isinstance(actual[2][1], Air), isinstance(actual[2][2], Fire),isinstance(actual[2][3], Teleport), isinstance(actual[2][4], Teleport)],
                [isinstance(actual[3][0], Wall), isinstance(actual[3][1], Wall), isinstance(actual[3][2], End),isinstance(actual[3][3], Wall), isinstance(actual[3][4], Wall)]]
    for item in excepted:
        for a in item:
            assert a == True,  'testcase test_parse6 failed.'

def test_parse7():
    #edge case with 5 teleport gates
    grid = ['**X2*\n', '*W8**\n', '* F8*\n', '2*Y*8']
    try:
        actual = parse(grid)
    except Exception as e:
        assert type(e) == ValueError, 'testcase test_parse7 failed.'
        assert str(e) == 'Teleport pad 8 does not have an exclusively matching pad.', 'testcase test_parse7 failed.'


def run_tests():
    test_parse1()
    test_parse2()
    test_parse3()
    test_parse4()
    test_parse5()
    test_parse6()
    test_parse7()






