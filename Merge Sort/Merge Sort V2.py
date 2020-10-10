## Merge Sort V2 ##

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

x = 4
y = 2
while len(split) != 1:
    merge = []
    x = x / 2
    y = y * 2
    for i in range (0,int(x)):
        number = []
        for i in range (0,int(y)):     
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



    
