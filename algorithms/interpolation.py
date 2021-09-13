'''
- Based on the logic that it focuses on the middle section of the data.
- E.g, assume we want to search for a word in an English dictionary, such as the word river.
    # We will use this information to interpolate and start searching for words starting with r
'''

# example 1 (Imran Ahmed)
def intPolSearch(list, x):
    idx0 = 0
    idxn = len(list) - 1 
    found = False
    
    while idx0 <= idxn and x >= list[idx0] and x <= list[idxn]:
        # find midpoint
        mid = idx0 + int((float(idxn - idx0) / (list[idxn] - list[idx0])) * (x - list[idx0]))
        # compare value at midpoint with search value
        if list[mid] == x:
            found = True 
            return found
        
    if list[mid] < x:
        idx0 = mid + 1
        
    return found

print(intPolSearch([12, 33, 11, 99, 12, 43, 26], 19)) 