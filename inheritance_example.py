class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy


    def __str__(self):
        return self.name+ ' in ' + self.galaxy


sun = Star('Sun', 'Milky Way')
print(sun)

# output is Sun in a Milky Way


class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass

#issubclass(x,y) function checks whether a particular class is a subclass of any other class.
for class1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for class2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(class1, class2), end='\t')
    print()

#output is separated using \t which tabs the responses
# first line is T, F, F;     T, T, F;    T, T,T;

class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass

myVehicle = Vehicle()
myLandVehicle = LandVehicle()
myTrackedVehicle = TrackedVehicle()

#issubclass(x,y) function checks whether a particular class is a subclass of any other class.
for class1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for class2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(class1, class2), end='\t')
    print()

# Same thing as before except this time we created an object. The object is the variables listed
# objects are technically variables

x = '1'
y = '1'
z = '23'

if x is y:
    print('hello')

print( x is y)
print(z is x)
#output ello mate, True and False  the is statement is the same exact thing as the == operator basically
