
# example 1 (Imran Ahmed)
def insertionSort(list):
    for i in range(1, len(list)):
        j = i-1
        element_next = list[i]
        
        while(list[j] > element_next and (j >= 0)):
            list[j+1] = list[j]
            j = j-1
        list[j+1] = element_next
        
    return list 

l = insertionSort([12, 4, 17, 54, 2, 61])
print(l)


# example 2 (mine)
def insertion_sort(array):
    for i in range(1, len(array)):  # 1st index of array
        position = i
        temp_value = array[i]  # temporary_value
        
        while position > 0 and array[position -1] > temp_value:
            array[position] = array[position -1]
            position = position -1
            
        array[position] = temp_value
        
    return array

lst = insertionSort([3,1,7,2,9,10])
print(lst)