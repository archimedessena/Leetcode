def countNegatives(b):
    return sum(n < 0 for q in b for n in q)
    



list_one  = [[4, -3, 2, 1], [3, 2, -1, -1], [1, 1, -1, -2], [-1, -1, -2, -3], [1, -2, -3, 10, -11, -34, 56, 78]]
neat = countNegatives(list_one)
print(neat)
