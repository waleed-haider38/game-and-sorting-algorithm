# Optimized bubble sort code
def bubble_sort(lst):
    size = len(lst)
    for i in range(size):
        swapped = False
        for j in range(size-1-i):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
                swapped = True
        
        if not swapped:
            break

    return lst

unsorted_list = [10 , 11 , 19 , 18 , 9 ,24]
print(f"The Unsorted list is: {unsorted_list}")

sorted_list = bubble_sort(unsorted_list)

print(f"The Sorted list is: {sorted_list}")