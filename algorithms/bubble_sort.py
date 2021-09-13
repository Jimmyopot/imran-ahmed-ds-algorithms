'''
- Bubble sort is the simplest and slowest algorithm used for sorting.
- worst-case performance is O(N2).
- used for smaller datasets.
'''

# example 1 (Imran Ahmed)
def BubbleSort(list):
    # Exchange the elements to arrange in order
    lastElementIndex = len(list) -1
    
    for passNo in range(lastElementIndex, 0, -1):
        for idx in range(passNo):
            if list[idx] > list[idx+1]:
                list[idx], list[idx+1] = list[idx+1], list[idx]  # swap
                
    return list 

l = BubbleSort([3,1,6,0,4,1,5])
print(l)


# example 2 (mine)
def bubble_sort(my_list):
    full_length = len(my_list)
    
    for i in range(full_length):
        for j in range(full_length -1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
                
    return my_list

lst = bubble_sort([12, 2, 45, 23, 5, 89, 6, 0.4, 100])
print(lst)