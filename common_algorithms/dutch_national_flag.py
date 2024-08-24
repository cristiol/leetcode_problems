
def dutch_flag_partition(pivot, arr):

    l = 0
    r = len(arr)-1

    while l < r:
        if arr[l] <= pivot:
            l += 1
        elif arr[l] > pivot:
            arr[l], arr[r] = arr[r], arr[l]
            r -= 1
    return arr

print(dutch_flag_partition(1, [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))

