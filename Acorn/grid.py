def grid_to_string(grid,player):
    """Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """
    player_row = player.row
    player_column = player.col
    water_buckets = player.num_water_buckets
    colum_ls = []
    row_ls = []

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if row==player_row and col==player_column:
                colum_ls.append(player.display)
            else:
                colum_ls.append(grid[row][col].display)
        #player display and turn objects into string
        row_ls.append(colum_ls)
        row_ls.append('\n')
        colum_ls = []

    d = ''
    for b in row_ls:
        for c in b:
            d += c

    if water_buckets == 1:
        msg = '\nYou have {} water bucket.'.format(water_buckets)
    else:
        msg = '\nYou have {} water buckets.'.format(water_buckets)

    return d + msg



