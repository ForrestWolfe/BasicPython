#list comprehensions is very interesting because its a conditional express otherwise known as a way of selecting one of
#two different values based on the result of a Boolean expression


listOne = []

for ex in range(6):
    listOne.append(10 ** ex)


listTwo = [10 ** ex for ex in range(6)]

print(listOne)
print(listTwo)

#good example
#expression_one if condition else expression_two


lst = []

for x in range(10):
    lst.append(1 if x % 2 == 0 else 0)

print(lst)

# if the x value is odd then the element is set to 0 and otherwise the element is equal to 1

lst = [1 if x % 2 == 0 else 0 for x in range(10)]

print(lst)
#shortened code and prints out the same thing