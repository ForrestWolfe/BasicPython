import re

# \d stands for digits in regex the curly's with a three just make the code shorter.
# The questionmark in the Regex indicates that if the area code isn't there that doesn't mean there isn't a phone number.
# the question mark can also be used for an extension.
phoneNumberReg = re.compile(r'(\d{3}-)?(\d{3}-\d{4})')


# This is where the varible will be applied to the search function to find the phone number in the code.
matchingObject = phoneNumberReg.search('My number is 888-888-8888, this is also another number you can reach me at 777-777-8777')


#the group function returns the group numbers and dashes combining them to return the phone number.
# group(1) returns the area code of a function.
# group(2) returns the last 7 digits of a phone number.
# group() in general will gather exactly what the regex calls for.
# groups() will return them both in a set.
print('The full number: ', matchingObject.group())
print('The area code for the number found: ', matchingObject.group(1))
print('The last 7:',  matchingObject.group(2))
print('The set of groups of regex: ', matchingObject.groups())

#A really cool way to simplify things FORREAL!
areacode, LastSeven = matchingObject.groups()
print(areacode)
print(LastSeven)

# Matching multiple groups with the pipe. The | chracter is called a pipe.
#    You can use it anywhere you want to match one of the many expressions.
#    For example: this regex will only match Spiderman or batman.
RegX = re.compile(r'Batman | Spiderman')

MO = RegX.search('This is the world of batman and Spiderman')
print('The hero that was found first in the string is: ', MO.group())

# you can use this method which is kind of the findall method where you
# can specify the different endings of a word or object that you are searching for. 
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.groups())


