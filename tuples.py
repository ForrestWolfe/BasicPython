tup1 = ("America", "conq.1492")
tup2 = ("light speed", "299,792,458 meters per second")
tup3 = ("slammer", "jammer")
print(tup3[1])      # this prints pussy sauce
print(tup3[0:4])  #This prints the entire thing including ("pussy sauce", "white cream")

# This transforms a tuple into a list
my_list = list(tup1)
my_list[1] = "Constantine"
print(my_list)

# This transforms a list into a tuple

my_tuple = tuple(my_list)
print("Democrats don't understand" + str(my_tuple))

#as you can see you can append any of the following to a list
my_list.append([3, "a", True])
print(my_list)


popular = ["super long time", "incredibily slow"]
popular.append("1.3 characters")
if len(popular) == 3:           # the if statement works because there is three values its not the index
    popular.append('hello please')
    print(popular)

## tuples and list can store multiple values
## list are enclosed with brackets and tuples are enclosed with parentheis
## The only difference other than the enclosure is that
##you can modify a list and you cannot modify a tuple

