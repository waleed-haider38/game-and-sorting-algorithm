def insertion_sort(arr):
    size = len(arr)
    for i in range(1 , size):
        key = arr[i]
        j = i -1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    
    return arr

unsorted_list = [64, 19, 45, 39, 11]

print(F"The Unsorted List is: {unsorted_list}")

sorted_list = insertion_sort(unsorted_list)

print(f"The Sorted List is: {sorted_list}")
