## Bubble Sort ##

#Create list of numbers
alist = [9,5,4,15,3,8,11,2,3]
#Ensures process repeated for each item in list
for i in range (0,len(alist)):
#Makes sure process is repeated for each item in list that hasn't been sorted yet
    for j in range (0, len(alist) - i - 1):
#Makes sure item is only moved if it is still in the wrong position (bigger than the item above it)
        if alist[j] > alist[j + 1]:
#Swaps items in list to correct order 
            temp = alist[j]
            alist[j] = alist[j + 1]
            alist[j + 1] = temp
#Prints sorted list
    print(alist)


    
