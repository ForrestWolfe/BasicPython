#the random module produces a gloat number coming from the range of 0.0-1.0
# this example below produces 5 random float numbers between 0 and 1

from random import random

for i in range(5):
    print(random())

#this is the actual function call
print(random())


# The seed function is able to directly set the generator's seed. We'll show you two it's
# varients

from random import random, seed
seed(0)

for i in range(5):
    print(random())

from random import randrange, randint

#The first three invocations will
# generate an integer taken (pseudorandomly) from the range (respectively):
print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
# the last function is is an equivalent of randrange(left, right+1) - it generates the integer
# value i, which falls in the range [left, right] (no exclusion on the right side).
# Look at the code in the editor. This sample program will consequently
# output a line consisting of three zeros and either a zero or one at the fourth place.
print(randint(0, 1))

# the output is either 0 0 0 1 or 0 0 0 0

# print a random number in the as many times as the range
# randint grabs a random number between the first defined number and the second one
# after each random number a comma is printed
from random import randint

for i in range(5):
    print(randint(1, 10), end=',')


from random import choice, sample

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(lst))
print(sample(lst, 5))
print(sample(lst, 10))



