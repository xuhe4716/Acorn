from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)


def read_lines(filename):
    """Read in a file, process them using parse(),
    and return the contents as a list of list of cells."""
    try:

        f = open(filename, 'r')
        ls_of_cell_instring = []
        while True:
            line = f.readline()
            if line == '':
                break
            ls_of_cell_instring.append(line)
        f.close()

        #try open file and appending the line to ls_of_cell_instring


    except FileNotFoundError:
        print("{} does not exist!".format(filename))
        quit()

        #rasie error if the file does not exit

    return ls_of_cell_instring






def parse(lines):
    """Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
        list -- contains list of lists of Cells
    """
    ls_of_line = []  #a  list of lists of cell
    ls_of_cells_inobject = []  #a list of cells' object
    x_occurrence = 0  #occurence of starting cell
    y_occurrence = 0  #occurence of ending cell
    teleport_checker = []  #a list to help check the teleport gates are valid or not
    cell_charater = ['X', 'Y', '*', ' ', 'W', 'F', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\n']  #valid cell character
    pad = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] #valid teleport pad
    for a in lines:
        for cell in a:
            if cell in cell_charater:
                if cell == 'X':
                    ls_of_cells_inobject.append(Start())  #storage the object of X
                    x_occurrence += 1

                elif cell == 'Y':
                    ls_of_cells_inobject.append(End())  #storage the object of Y
                    y_occurrence += 1

                elif cell == '*':
                    ls_of_cells_inobject.append(Wall())  #storage the object of *

                elif cell == ' ':
                    ls_of_cells_inobject.append(Air())  #storage the object of ' '

                elif cell == 'W':
                    ls_of_cells_inobject.append(Water())  #storage the object of W

                elif cell == 'F':
                    ls_of_cells_inobject.append(Fire())  #storage the object of F

                elif cell in pad:
                    teleport_checker.append(cell)
                    ls_of_cells_inobject.append(Teleport(cell))   #storage the object of teleport  pad
            else:
                raise ValueError('Bad letter in configuration file: {}.'.format(cell))
                #raise error if there is a bad letter

        ls_of_line.append(ls_of_cells_inobject)
        ls_of_cells_inobject = []  #renew the list for storaging object

    if x_occurrence > 1 or x_occurrence == 0:
        raise ValueError('Expected 1 starting position, got {}.'.format(x_occurrence))
        #check the occurrence of starting cell

    if y_occurrence > 1 or y_occurrence == 0:
        raise ValueError('Expected 1 ending position, got {}.'.format(y_occurrence))
        #check the occurrence of ending cell

    teleport_checker_set = set(teleport_checker)
    for each_pad_set in teleport_checker_set:
        count = 0
        for each_pad in teleport_checker:
            if each_pad_set == each_pad:
                count += 1
        if not count % 2 == 0:
            raise ValueError('Teleport pad {} does not have an exclusively matching pad.'.format(each_pad_set))
            #check the teleport pads exit in pair or not

    return ls_of_line




def string_to_grid(filename):
    readfile = read_lines(filename)
    ls_of_line = parse(readfile)
    return ls_of_line








