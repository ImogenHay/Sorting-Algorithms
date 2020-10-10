## Binary Search V1 ##

alist = list(range(1,101))
number = int(input("Pick a number between 1 and 100: "))
found = False
while found == False:
    print("Numbers Left: " , alist)
    index = int(len(alist) / 2) - 1     
    if len(alist) % 2 != 0:
        index = index + 1
    middle = alist[index]
    print("Guess: " , int(middle))
    if middle == number:
        found = True
        print("Guess is correct! ")
    else:
        if number > middle:
            del alist[0:(index+1)]
        else:
            del alist[index:len(alist)]
        
