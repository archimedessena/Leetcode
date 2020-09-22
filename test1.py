def countNegatives(grid):
    count = 0
    for i in range(len(grid)-1, -1,-1):
        for j in range(len(grid[0])-1,-1, -1):
            if grid[i][j] < 0:
                count +=1
    return(count)


    

list_one  = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3], [-1, -2, -3, -10, 11, 34, 56, 78]]
neat = countNegatives(list_one)
print(neat)

