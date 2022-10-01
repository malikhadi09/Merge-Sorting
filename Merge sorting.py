def mergeSort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2
        Left_side = arr[:mid]
        Right_side = arr[mid:]

        mergeSort(Left_side)
        mergeSort(Right_side)
        i = j = k = 0
        while i < len(Left_side) and j < len(Right_side):
            if Left_side[i] < Right_side[j]:
                arr[k] = Left_side[i]
                i += 1
            else:
                arr[k] = Right_side[j]
                j += 1
            k += 1
        while i < len(Left_side):
            arr[k] = Left_side[i]
            i += 1
            k += 1
        while j < len(Right_side):
            arr[k] = Right_side[j]
            j += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


arr = [12, 11, 13, 5, 6, 7]
print("Given array is", arr)
mergeSort(arr)
print("Sorted array is: ", arr)
