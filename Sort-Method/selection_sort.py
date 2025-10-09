def selection_sort(lst):
    size = len(lst)
    for i in range(size):
        min_index = i
        for j in range(i+1 , size):
            if lst[j] < lst[min_index]:
                min_index = j

        if min_index != i:
            lst[i] , lst[min_index] = lst[min_index] ,lst[i]

    return lst

select = [64,19,45,39,11]

print(f"The unsorted list is: {select}")

sorted_list = selection_sort(select)

print(f"The sorted list is: {sorted_list}")