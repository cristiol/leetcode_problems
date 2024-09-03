

def quick_sort(arr, left, right):
    if left < right:
        partition_pos = partition_(arr, left, right)
        quick_sort(arr, left, partition_pos - 1)
        quick_sort(arr, partition_pos + 1, right)


def partition_(arr, left, right):

    i = left
    j = right
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if left < right:
        arr[i], arr[right] = arr[right], arr[i]
    return i

arr_test = [2,1,8,6,5,7,3,4]
quick_sort(arr_test, 0, len(arr_test)-1)
print(arr_test)

