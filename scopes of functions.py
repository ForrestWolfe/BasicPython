# This prints "i got 1" and "I have 2" then it prints the variable 1 because it is outside of the function and actually
# shadows it meaning that it comes after the function itself which means the varible inside the function would be changed
# if we were to be appending that variable to a list or something like that.
def myFunction(n):
    print("I got", n)
    n += 1
    print("I have", n)

var = 1
myFunction(var)
print(var)



# this actually changes the interior of the function itself
# This isn't a permanant change but it will change the function for the time being
def myFunction(myList1):
    print(myList1)
    myList1 = [0, 1]

myList2 = [2, 3]
myFunction(myList2)
print(myList2)

# this one is a little tricky because the parameter actually has no value so creating list2 and making it the parameter
# gives it a value then inside that function the original list gets printed and then the first index in that list
# is deleted leaving nothing but the 3
def myFunction(myList1):
    print(myList1)
    del myList1[0]

myList2 = [2, 3]
myFunction(myList2)
print(myList2)