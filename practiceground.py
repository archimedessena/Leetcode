# checking if a particular number in an array is greater than the immediate number 
def checking(arr):
    first, second = 1, len(arr) - 1
    while first < second:
        midd = (first + second) // 2
        if arr[midd + 1] < arr[midd]:
            second = midd
        else:
            second = midd + 1

    return first



arrive = [24,69,100,99,79,78,67,36,26,19]
neat = checking(arrive)
print(neat)  

