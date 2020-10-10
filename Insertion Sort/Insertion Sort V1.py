## Insertion Sort ##
    
slist = []
alist = [9,5,4,15,3,8,11,2,20]
slist.append(alist[0])
alist.remove(alist[0])

while len(alist) != 0:
    slist.append(alist[0])
    print(slist)
    y = 0
    while y + 1 < len(slist):
        index = slist.index(alist[0])
        if slist[index] < slist[index - 1]:
            number = slist.pop(index)
            slist.insert(index - 1, number)
        elif  len(slist) - 1 != index:
            if slist[index] > slist[index + 1]:
                number = slist.pop(index)
                slist.insert(index + 1, number) 
        print(slist)
        y = y + 1
    alist.remove(alist[0])       
alist = slist
