# This puts the list in numerical order from least to greatest
list = [54, 23, 666, 223, 12, 21]
swpped = True

while swpped:
    swpped = False
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            swpped = True
            list[i], list[i + 1] = list[i + 1], list[i]

print(list)


#However that is a far more complicated way of doing things because you can simply use the .sort() command
# This sorts this list from smallest to largest
mylist = [4, 5, 6, 23, 200, 345]

mylist.sort()
print(mylist)

# num = This asks the user how many elements they want in their list
#  the for loop runs a specified number of times that specified number it the "num" variable.
#creates a new variable named value which asks for the values to be inputted into the MyList Dictionary
# val also changes the users input into a floating point number if it already isn't equal to one
# while Swapped: enters a while loop which means while swapped is equal to True it will run
#swapped = False is how the loop gets exited once the for loop inside the while loop is completed it will
# turn swapped into false, thus exiting the while loop


myList = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    myList.append(val)

while swapped:
    swapped = False
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print("\nSorted:")
print(myList)


### for looping with lists to get the smallest value or the largest value in the list
## this is a very good way you can also assign the largest and smallest value to an index value in the list
# this allows you to compare each one to a specific list value
# The approach I took is much easier because I just define an incredibly low/high number the issue is that if numbers beyond that
# ever enter into my list it will break my program.
print('Out of this list')
list =[10, 100, 23, 123, 423,4523,]
print(list)
largest = -9e11
smallest = 9e11

for i in list[:]:
    if i > largest:
        largest = i

for i in list[:]:
    if i < smallest:
        smallest = i

print("The smallest number in the list is: ", smallest)
print("The largest number in the list is: ", largest)



####This asks a user to input a list item and in return they will get that items index value
# creating the variable found and setting it's value to false allow the list to compare itself value by value until it finds the
# inputed value, after it runs through the length of the list it stops hence the break command
# if the list value is not found the script returns Absent
# Otherwise it returns the index value
list = [1,2,3,4,5,6,7,8,9]
find = int(input("enter a value from the list to figure out its index value: "))
found = False


for i in range(len(list)):
    found = list[i] == find
    if found:
        break

if found:
    print("Element found at the index", i)
else:
    print("Absent")

## cool little snip-it that  compares to list to each other and returns a value indicating how many total mataches were made

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)

## A more advanced version of that would be like this which would allow user input and would be more like a game

