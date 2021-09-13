"""
Sort a list in ascending order
Return a new sorted list

- 3 steps:
   # Divide: Find midpoint of the list and divide into sublists
   # Conquer: Recursively sort the sublists created in previous step
   # Combine: Merge the sorted sublists created in previous step
   
   Takes O(n log n) time
"""

# example 1 (Imran Ahmed)
def mergeSort(list):
    if len(list) > 1:
        mid = len(list) // 2  # splits list into half
        left = list[:mid]
        right = list[mid:]
        
        # recursively reprats until length of each list is 1
        mergeSort(left)
        mergeSort(right)
        
        a = 0
        b = 0
        c = 0
        
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list[c] = left[a]
                a = a + 1
            else:
                list[c] = right[b]
                b = b + 1
            c = c + 1
            
        while a < len(left):
            list[c] = left[a]
            a = a + 1
            c = c + 1
            
        while b < len(right):
            list[c] = right[b]
            b = b + 1
            c = c + 1
            
    return list 

lst = mergeSort([45, 21, 89, 35, 12, 90, 123, 345, 25])
print(lst)