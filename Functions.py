# A FUNCTION IS A SEEQUENCE OF STATEMENTS THAT BELONG TOGETHER. THE PRINT() AND STR() FUNCTIONS ARE EXAMPLE S OF BUILT-IN-FUNCTIONS
# PARAMENTERS WITHIN THEIR FUNCTIONS CAN BE USED LIKE VARIABLLES, THEY ARE OPTIONAL AND CAN BE OF ANY TYPE
# CREATING A FUNCTION: DEFINE THE FUNCTION CREATE ARE RETURN THE VARIABLE WITHIN THE FUNCTION ASSIGN THE RETURN VALUE TO  THE SECOND VARIABLE AND THEN FINALLY DISPLAY IT USING PRINT(THE NAME OF THE SECOND VARIABLE)
print("hello world ")

#WHEN WE WANT TO USE A FUNCTION WE WRITE ITS NAME FOLLOWED BY PARENTHESIS WITHIN WHICH WE SOMETIMES PUT VALUES
#BUILT IN FUNCTIONS ARE GREAT BUT WE CANT USE THEM FOR EVERYTHING SO THATS WHY WE DEFINE/CREATE CUSTOM FUNCTIONS
#within the custom functions parenthesis you can define more parameters like temporary variables that allow you to pass values or arguements to a function like so.
#sometimes we want the custom function to return a value the keyword for that is return by puttin in a  variable or value after
# the return keyword it will return a value that we can store in a different function
def to_farenheit(celsius):
    f = celsius *9 / 5 + 32
    return f

temp = int(input("what is the temperature? :    "))
degrees = to_farenheit(temp)
print(str(degrees)+ " degrees")

#How about another conversion? hthis time, let's convert kilometers into miles!

def to_miles(km):
    miles = km / 1.609
    return miles

km = float(input("How many Kilometers? "))
miles =to_miles(km)
print(str(miles) + " miles")


#you can return multiple values by returning a list

def encode(numbers):
    ns = []
    for n in numbers:
        ns.append(n * 8.15)
    return ns

numbers1 = [4, 8, 15, 16, 23, 42]
numbers2 = encode(numbers1)
print(numbers2)

#That is exactly how you return a signle valuie

# you can also put functions inside of functions

def say_hi(name):
    print("hey there, " + name + "!")

def greet(name, adj):
    say_hi(name)
    print("you look " + adj + " today!")
greet(input("What is the name you would like to input  "), input ("  what is the adjective used to describe them today?  "))

#FUNCTIONS CAN'T JUST CALL OTHER FUNCTIONS BBUT ALSO THEMSELVES
# This is a recursive function (characterized by recoccurence or repetition)
# for example below this recursive function multiplies n with the factorial of n - 1, until n equals 1
def factorial(n):
    if n == 1:
        return 1
    else:
        return (n*factorial(n-1))

number = factorial(3)
print(number)

## so far in the functions chapter we have successfully used built-in-functions, defined custom functions, used parameters and return values
# we define functions with the def keyword and call them using their name in parenthesis with or without arguements
def to_characters(string):
#this puts the characters in [ ,  ,  ,] format
    characters = [ ]
    for d in string():
        characters.append(d)
    return(characters)

characters = to_characters("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(characters)


###################### countdown is a recursive function becuase it counts down to a specified number
# so a recursive function is one that defines where the function will end so if we were counting and wanted it to end on 10 that would be a recursive funtion or doing the abc's it's the same concept
def countdown(start):
    if start<= 0:
        return 0
    print(start)
    countdown(start-1)
countdown(10)
