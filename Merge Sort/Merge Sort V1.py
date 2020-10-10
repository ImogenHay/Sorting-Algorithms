## Merge Sort V1 ##

alist = [42,31,12,3,37,18,29,47]
split = []
for i in range (0,len(alist)):
    number = []
    number.append(alist[i])
    split.append(number)
    number = []
print(split) 
for i in range (0,int(len(split) / 2)):
    if split[0] > split[1]:
        number = split[1] + split[0]
    else:
        number = split[0] + split[1]
    split.remove(split[0])
    split.remove(split[0])
    split.append(number)
print(split)


merge = []
for i in range (0,2):
    number = []
    for i in range (0,4):     
        if len(split[0]) == 0:
            number.append(split[1][0])
            split[1].remove(number[i])
        elif len(split[1]) == 0:
            number.append(split[0][0])
            split[0].remove(number[i])
        else:
            if split[0][0] > split[1][0]:
                number.append(split[1][0])
                split[1].remove(number[i])
            else:
                number.append(split[0][0])
                split[0].remove(number[i])
    merge.append(number)
    split = split[2:4]
split = split + merge

print(split)


merge = []
for i in range (0,1):
    number = []
    for i in range (0,8):     
        if len(split[0]) == 0:
            number.append(split[1][0])
            split[1].remove(number[i])
        elif len(split[1]) == 0:
            number.append(split[0][0])
            split[0].remove(number[i])
        else:
            if split[0][0] > split[1][0]:
                number.append(split[1][0])
                split[1].remove(number[i])
            else:
                number.append(split[0][0])
                split[0].remove(number[i])
    merge.append(number)
    split = split[0]
split = split + merge
   


    
