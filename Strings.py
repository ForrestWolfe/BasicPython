


#/n breaks the code and starts it on the next line
#print("Giraffe\nAcademy")

#\" will allow you to add in quotations in a string
#print("Giraffe\" academy")

phrase = "GARAGE bAnd"
# The plus is called concatonation basically apending another string onto that string
print(phrase.lower()+ "is cool")
# a function is a block of code that will preform a specific operation
#modify strings and get info about strings using functions
#can be ran together such as 
#you can get the length of a string using the 
#you can also grab specified characters  indexs always start with zero
# You can also get a number refering the string so (phrase.index"G") returns 0
# you can also get a number refering to the string so  
# you can also use .replace and it replaces Giraffe with the word Elephant
print(phrase.upper())
phrase.isupper()
phrase.upper.isupper()
len(phrase)
phrase[0]
phrase.index("G")
phrase.index("Garage")
phrase.replace("Giraffe", "bAnd")
      

      
# when you use a function and you give a value to a function that is called a parameter
# for example (phrase.index("a") the "a" is the parameter
stay = "oh no, please stay over one more night"
print(stay.upper.isupper())


str1 = " Mission "
str2 = "Accomplished"
status = str1 + str2
print (status)

# you can use print to display a value in the console window the print() method takes lots of different types but we
#can't mix them without converting them

string = "scene "
number = 24
print(string + str(number))

#while we can't preform arithmetic on a string we can use the * operator to repeat it.

phrase = "awright "
print(phrase * 3)
# THIS PRINTS THE PHRASE 3 TIMES  ON THE SAME EXACT LINE

# YOU COULD MAKE THIS MORE COMPLICATED you can add in more variables which could come in handy

laugh = "yah yah yah "
smile = "huhuhu huhuhu "
print(laugh * 3 + smile * 3)

# strings can get long in fact they can get so long that it become hard to count the number of character they have
#we use len to count the length of chararcters that are used
title = "Monty Python's High Flying Circus"
print(len(title))

#if we assign "" to an empty string literal to a variable it becomes a sting variable even though there is nothing in it
nationality = ""
print(type(nationality))
#see that nationality is a string variable and has a value of "" which means its length is 0

#every character in a string has a postion or index that we can put in brackets to access the character
name = "Captian America"
character = name[0]
print(character)
name1 = "batman"
character1 = name1[1]
print(character + character1)
# the characters in a string start at an index of zero this would essentially pick the first letter out of captain America
#Which is "C" and then since [1] is bracketed it takes the second letter of Hunter "U" and since I "+" the strings together
# it started to form a word out of the first two letter of Captain and hunter making the console produce "CU"

#we can separate two of these indices with a colon to extract or slice chunks of a string#
name2 = "captian future"
rank = name2[0:20]
print(rank)
# that indices the whole name captain because it is character 0 - 7 which would be captian

# we can replace parts of a string with the replace() method

q = "What is your name"
q = q.replace("name", "quest?")
print(q)
# this replaces what is your name and makes it say "what is your quest?"

#WHATEVER QUOTES WE USE FOR STRING LITERAL WE CAN'T USE THE SAME QUOTES WITHIN THE LITERAL BECAUSE THEY'D END IT.
q1 = "whats your name?"
q2 = 'what\'s your quest?'
print(q1)
print(q2)
#we can enclose a string in the other kind of quotes or use a backslash to escape the quotes

# if we want to include a line break in a string we can't just hit return because that would end the statement so we need
# This is creating an escape character which will allow use to have a line break

a = "Arthur, king of the Britons"
a += "\n"
a += "I seek the holy grail"
print(a)
#"\n" creates an escape character which allows a line break A LINE BREAK CONTINUES A LINE ON THE NEXT LINE AFTER THE LINE BREAKS@


# WE CAN USE TRIPLE QUOTES TO AUTOMATICALLY INCLUDE LINE BREAKS IN LONGER STRONGS. WHAT IF WE DON'T WANT A  LINE TO END?
a1 = """what do you mean ?
An african or a european \
swallow"""
print(a1)
#esssentially everything that is after the "\" is included on the same line as the "\""
path = r"C:\notes"
print(path)
#if we dont want the character that follow a backslash to be seen as escape characters we nee to add an R before the string literal

#THIS IS WHAT WE SHOULD BE ABLE TO COMPLETE THUS FAR
q4 = 'what\'s the air speed \
veocity of an unladen swallow?'
word = q4[-8:-1]
q4 = q4.replace(word, "rabbit")
print(q4)

# you can put strings in single or double qutoes but we cant use them until we escape the string
#for example ""jolly"" "if life seems" or ' there\'s something wrong'

#to show the understanding of strings this is what a little more complex one would look like

s = """Dear letter-friend,
My name is Helmut"""
s += "\n"
s += 'I\'m from Germany'
print(s)

print("This is nothing but an example,"
      "\n"
      "I like sour skittles"
      "I also like M&M's")