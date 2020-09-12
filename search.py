# A typical binary search
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)
        guess = arr[mid]
        if guess == item:
            guess = mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


lo = [4, 3, 2, 1]
l = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
print(binary_search(lo, 4))