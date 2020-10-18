
myTuple = (1, 10, 100, 1000)

print(myTuple[0])
print(myTuple[-1])
print(myTuple[1:])
print(myTuple[:-2])

myTuple = (1, 10, 100)

#the len() function accepts tuples, and returns the number of elements contained inside;
#the + operator can join tuples together (we've shown you this already)
#the * operator can multiply tuples, just like lists;
#the in and not in operators work in the same way as in lists

t1 = myTuple + (1000, 10000)
t2 = myTuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in myTuple)
print(-10 not in myTuple)

#One of the most useful tuple properties is their ability to appear on the left side of the assignment
#operator. You saw this phenomenon some time ago, when it was necessary to find an elegant tool to swap two variables' values.
#Take a look at the snippet below:

var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

