def bubbleSort(arr):

    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped is False:
            break
    return arr


print(bubbleSort([64, 34, 25, 12, 22, 11, 90]))

