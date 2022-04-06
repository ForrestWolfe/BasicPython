##### EXAMPLES TO BUILD OFF OF##############

###Another way is based on using a dictionary's method named items().
# The method returns a list of tuples (this is the first example where tuples are something more than just an example
# of themselves) where each tuple is a key-value pair.

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

for english, french in dict.items():
    print(english, "->", french)

print('\n')
# There is also a method named values(), which words similarly to keys(), but returns a list of values.

dict = {"cat" : "chat", "dog" : "yak", "horse" : "lion"}

for french in dict.values():
    print(french)

# merging two dictionaries in python

x = {"hello": "World"}
y = {"milk": "1.87$"}

z = {**x, **y}
print(x)
print(y)

print("This is the merged dictionary", "\n",
      z)


#modifying a dictionary is easy too
dict = {"cat" : "chat", "dog" : "yak", "horse" : "lion"}

dict['cat'] = 'minou'
print(dict)

#adding a new key value to the dictionary
# there is the insertion method and the update() method

dict['swan'] = 'cygne'
dict.update({"duck" : "canard"})
print(dict)

# deleting  a key is just as easy
# removing a non existing key can cause an error
del dict['cat']

print(dict)

# to remove the last item in a dictioinary you can use the popitem() method:
# removes duck because of cat being removed above
dict.popitem()
print(dict)

