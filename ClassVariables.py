#A class variable is a property which exists in just one copy and is stored outside any object.

# no instance variable exists if there is no object in the class; a class variable exists in one copy even
# if there are no objects in the class.

# class variables are created differently to their instance siblings. The example will tell you more.

class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1


exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)
exampleObject3 = ExampleClass(4)

print(exampleObject1.__dict__, exampleObject1.counter)
print(exampleObject2.__dict__, exampleObject2.counter)
print(exampleObject3.__dict__, exampleObject3.counter)

print(" '\n' ####################################################################### '\n' ")

#there is an assignment in the first list of the class definition - it sets the variable named counter to 0;
# initializing the variable inside the class but outside any of its methods makes the variable a class variable;
#accessing such a variable looks the same as accessing any
#instance attribute - you can see it in the constructor body; as you can see, the constructor increments the variable by
#one; in effect, the variable counts all the created objects.


class ExampleClass1:
    __counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass1.__counter += 1    #this is the only difference between the two
                                        # the counter cannot be changed

exampleObject1 = ExampleClass1()
exampleObject2 = ExampleClass1(2)
exampleObject3 = ExampleClass1(4)

print(exampleObject1.__dict__, exampleObject1._ExampleClass1__counter)
print(exampleObject2.__dict__, exampleObject2._ExampleClass1__counter)
print(exampleObject3.__dict__, exampleObject3._ExampleClass1__counter)

#class variables aren't shown in an object's __dict__ (this is natural as class variables aren't parts of an object)
# but you can always try to look into the variable of the same name, but at the class level - we'll show you this very soon;
#a class variable always presents the same value in all class instances (objects)



