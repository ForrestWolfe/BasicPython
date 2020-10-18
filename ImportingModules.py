
#import math
# this is the way to import any module for example the math module and all of the entities inside of it.
###################################################################

# Here is a selected import from a specified module named math.
# This is so much more efficient then what is done below.
# the point is you can redefine the modules.
from math import sin, pi

print(sin(pi/2))


#by defining pi and sin we change its original definitions
pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return none

print(sin(pi/2))
###############################


#As you can see, the name of an entity (or the list of entities' names) is replaced with a single asterisk (*).
#Such an instruction imports all entities from the indicated module.
#Is it convenient? Yes, it is, as it relieves you of the duty of enumerating all the names you need.
#Is it unsafe? Yes, it is - unless you know all the names provided by the module, you may not be able to avoid name
# conflicts. Treat this as a temporary solution, and try not to use it in regular code.

#from module import *

######
# using alias's to rename the module incase you dont like the name or so you can avoid name conflicts

#import module as alias

#If you need to change the word math, you can introduce your own name, just like in the example:
import math as m
print(m.sin(m.pi/2))

################
# if you need to change the name of an entity inside of a module you import the entity name as alias like so.

#from module import name as alias

# the phase "name is alias" can be repeated - use comma's to separete the multiplied phrases like this:

#from module import n as a, m as b, o as p
# or for a better example

from math import pi as PI, sin as sine

print(sine(pi/2))

####################

# here is a couple ways to figure out all of the entities inside of a module

import math

for name in dir(math):
    print(name + "\t")

# and the other way is to go to the shell and run these commands
import math
dir(math)

######################



