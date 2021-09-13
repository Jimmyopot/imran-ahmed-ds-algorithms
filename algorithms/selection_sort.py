# example 1 (Imran Ahmed)

def selectionSort(list):
    for fill_slot in range(len(list) - 1, 0, -1):
        max_index = 0
        
        for location in range(1, fill_slot + 1):
            if list[location] > list[max_index]:
                max_index = location
        list[fill_slot], list[max_index] = list[max_index], list[fill_slot]
        
    return list 

lst = selectionSort([23, 45, 12, 11, 45, 81, 35, 25])
print(lst)


# example 2 (mine)

def selection_sort(listA):
    n = len(listA) - 1
    
    for i in range(0, n):
        # Find the minimum element in remaining unsorted array
        low_value = i  # assume 1st element is the lowest
        
        for j in range(i+1, n):
            if listA[j] < listA[low_value]:
                low_value = j 
                
            if low_value != i:
                # Swap the found minimum element with the first element
                listA[i], listA[low_value] = listA[low_value], listA[i]
                
    return listA

lst = selection_sort([10, 12, 3, 34, 1, 2, 14, 23, 62])
print(lst)

# Time complexity: O(n^2)
# Space complexity: O(1)