# example 1 (Imran Ahmed)

def shellSort(list):
    distance = len(list) // 2
    
    while distance > 0:
        for i in range(distance, len(list)):
            temp = list[i]
            j = i 
            # sort sublist for this distance
            while j >= distance and list[j - distance] > temp:
                list[j] = list[j - distance]
                j = j - distance
            list[j] = temp 
        # reduce distance for the next element
        distance = distance // 2
    return list 

lst = shellSort([56, 78, 12, 10, 45, 83, 23, 7, 109])
print(lst)