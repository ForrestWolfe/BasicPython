######## OBJECTS ##########
#An object is a structure that can have attributes and methods
#objects can have attributes and methods
#objects are instances of classes

######## METHODS#############
#Methods are functions that belong to a class
# they use the self parameter to point to the instance they belong to

#######
my_list = [1, 2, 3, 4, 5]
my_list.pop()
print(my_list)

# Classes are like templates for objects of a particular kind, so we can create a or define a class with the class keyword
class Car:
    wheels = 4
# we can also define a special method called __init__(self, parameter): this is when we create an instance of a class.
# the __init__() method always needs a self parameter that we can use to set initial values for instance variables.
# the __init__() method can store more than just self parameters; arguments that we add to car() the instantiation ar
    def __init__ (self, color):
     self.color = color
     self.running = False

# defines the method is which the car
    def start_engine(self):

# the self parameter stands for th einstance that's calling the method, which makes running a so-called instance variable.
       self.running = True
    print("Vroom!")

# Defining a class doesn't create an object though. in order to do that, we need to create an instance of a class.
# with the Car(), we're creating an instance of the Car class that we can store in a variable.
# Functions that we define within classes are also known as methods we call a method using the name of the instance it belongs to a dot and the methods name
# the self parameter points to my_car because my_car.start_engine() is short for Car.start_engine(my_car)

my_car = Car("red")
my_car.start_engine()
##################################################################################

#FUNCTIONS THAT WE DEFINE WITHIN CLASSES ARE ALSO KNOWN AS METHODS
#WHILE ATTRIBUTES ARE SHARED BETWEEN ALL INSTANCES, VARIABLES THAT WE DEFINE FOR SELF BELONG OT A PARTICULAR INSTANCE

# THE SELF PARAMETER STANDS FOR THE INSTANCE THAT'S CALLING THE METHOD WHICH MAKES RUNNING A SO CALLED INSTANCE VARIABLE self.running
#YOU CAN ALSO DEFINE A SPECIAL METHOD CALLED __INIT__ WHICH IS CALLED WHEN WE CREATE AN INSTANCE OF A CLASS
#THE __INIT__ METHOD ALWAYS NEEDS A SELF PARAMETER THAT WE CAN USE TO SET INITAL VALUES FOR INSTANCE VARIABLES
#THE __INIT__ METHOD CAN USE MORE PARAMETERS THAN SELF FOR EXAMPLE

#def __INIT__(SELF, COLOR):
#CAR("RED")


#Classes are the blueprints for objects they define how objects of a kind behave and what attribute they have

class Car:


    def __init__(self, vehicle, color):
        self.vehicle = vehicle
        self.color = color
        self.running = False
        self.wheels = 4

    def start_engine(self):
        self.running = True
        car = {"Car":self.vehicle, "Color":self.color, "Amount of Wheels":self.wheels, "Running":self.running}
        print("Car :", car.get("Car"))
        print("color :", car.get("color"))
        print("Wheels :", car.get("Amount of Wheels"))
        print("Running :", car.get("Running"))
        #print(car.values())
        print("Vroom!")

car = Car("Mustang", 'red')
car.start_engine()
