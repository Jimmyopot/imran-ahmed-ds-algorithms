# example 1 (Imran Ahmed)
def linearSearch(list, item):
    index = 0
    found = False 
    
    while index < len(list) and found is False:
        if list[index] == item:
            found = True 
        else:
            index = index + 1
            
    return found

list = [12, 33, 11, 99, 22, 55, 67] 
print(linearSearch(list, 22))

# Big O = 0(n)
