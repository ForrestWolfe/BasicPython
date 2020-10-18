# Regex Character Codes
# \d any numeric digit 0-9
# \D any char that is not a numeric digit from 0-9
# \w Any letter, numeric digit, or the underscore character. (Think of this as matching "word" characters.)
# \W Any character that is not a letter, numeric digit, or the underscore character.
# \s Any space, tab, or newline character. (Think of this as matching "spcae" characters.)
# \S Any character that is not a space, tab, or newline.
# you can also do re.compile(r'[0-5]') if your only searching for digits zero thru five

# Enter all of this in an interactive shell or add print method

import re



xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans,'
                  ' 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
# by placing a caret char just after the characters class's opening bracket,
# you can make a negative character class. A negatibe character class will match all the
# characters that are not in the character class. For example, enter the folling into
# the interactive shell / or with print

consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('Robocop eats baby food. BABY FOOD.'))

# you can use the carat symbol at the start of a regex to indicate that a
# match must occur at the beginning of the searched text. Likewise, you can put a dollar sign
# at the end of the regex to indicate the string must end with this regex pattern
# you can use the ^ and $ together to indicate that the entire string much match
# the regex patten.

beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello world!'))
x = True
sentence = beginsWithHello.search('he said hello')
if sentence is None:
    x = True
    print(x, ', Hello was not said at the beginning of the sentence')
else:
    x = False
    print(beginsWithHello.search('he said Hello'))

"-------------------------------------------------------"
# checks whether the string ends in a number
endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))

"-------------------------------------------------------"
#checks whether the whole string is digits
wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')


# the wildcard character is the "." because it will match any character except for a newline.
# This will match any three letter word that ends with at
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

# sometimes you want to match anything and everything

name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = name_regex.search('First Name: Forrest Last Name: Wolfe')

