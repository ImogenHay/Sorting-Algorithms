## Merge Sort V3 ##

alist = [42,31,12,3,37,18,29,47]
split = []
for i in range (0,len(alist)):
    number = []
    number.append(alist[i])
    split.append(number)
    number = []
print(split)

while len(split) != 1:
    merge = []
    for i in range (0,int(len(split) / 2)):
        number = []
        for i in range (0,int(len(split[0])* 2)):     
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
        split.remove(split[0])
        split.remove(split[0])
    split = split + merge

    print(split)


    
