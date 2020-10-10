## Binary Search V2 ##

number = 0
#Creates list
alist = list(range(1,101))
#Ensures number chosen is within list
while number < 1 or number > 100:
    number = int(input("Pick a number between 1 and 100: "))
found = False
while found == False:
    print("Numbers Left: " , alist)
#Works out index of middle item in list, -1 because lists index starts at 0
    index = int(len(alist) / 2) - 1
#Makes sure correct index found if legth of list is odd because not divisable by 2 
    if len(alist) % 2 != 0:
        index = index + 1
#Finds and prints middle item in list as a guess
    middle = alist[index]
    print("Guess: " , int(middle))
#If guess is correct loop ends
    if middle == number:
        found = True
        print("Guess is correct! ")
    else:
#Removes guess and numbers before it from list if guess was too low
        if number > middle:
            del alist[0:(index+1)]
#Removes guess and numbers after it from list if guess was too high
        else:
            del alist[index:len(alist)]
