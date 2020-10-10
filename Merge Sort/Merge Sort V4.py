## Merge Sort V4 ##

alist = [42,31,12,3,37,18,29,47,5,8,20,32]
split = []
for i in range (0,len(alist)):
    number = []
    number.append(alist[i])
    split.append(number)
    number = []
print(split)

while len(split) != 1:
    merge = []
    x = (len(split) / 2)
    y = int(len(split[0])* 2)
    if (len(split)) % 2 != 0:
        x = x + 0.5
        y = int(len(split[0]))
        
    print(x)
    print(int(x))
    for i in range (0,int(x)):
        number = []
        for i in range (0,y):
            if len(split) == 1:
                number.append(split[0])
            else:
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
        print(split)
        split.remove(split[0])
        split.remove(split[0]) #only one element left so cant do
    split = split + merge

    print(split)


    
