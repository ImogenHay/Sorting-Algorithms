## Bubble Sort ##

alist = [9,5,4,15,3,8,11,2,3,5,4,15,3,8,11,2,3]

for i in range (0,len(alist)):
    for j in range (0, len(alist) - i - 1):
        if alist[j] > alist[j + 1]:
            temp = alist[j]
            alist[j] = alist[j + 1]
            alist[j + 1] = temp
    print(alist)


    
