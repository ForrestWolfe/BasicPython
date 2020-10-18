class Test:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


TestObject = Test(1)

print(TestObject.a)
print(TestObject.b) # This will return an AttributeError Therefore it will not run correctly
##############################################################################################
##############################################################################################

##############################################################################################
##############################################################################################
class Test1:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


Test1Object = Test1(1)
print(Test1Object.a)
try:                               # in order to fix what is above you need to implement Try and Except for an AttErr
    print(Test1Object.b)
except AttributeError:
    pass


### fortunately there is otehr ways of doing this

#using the function hasattr and it needs two arguments to be passed to it
#The class of the object being checked
# The name of the property whose existence has to be reported(note: it has to be a string containing the attrib name
# not just the name alone

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

exampleObject = ExampleClass(1)
print(exampleObject.a)

if hasattr(exampleObject, 'b'):
    print(exampleObject.b)

##########################################################