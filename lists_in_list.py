#### This appends WHITE_PAWN in row 8 times
row = []

for i in range(8):
    row.append("WHITE_PAWN")

print(row)
############Both of these return the same exact values

row1 = ["WHITE_PAWN" for i in range(8)]
print(row1)

####The snippet produces a ten-element list
# filled with squares of ten integer numbers starting from zero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

squares = [x ** 2 for x in range(10)]
#print(squares)

#The snippet creates an eight-element array containing the first eight powers of two (1, 2, 4, 8, 16, 32, 64, 128)
# i starts at 0 and ends at 7
twos = [2 ** i for i in range(8)]
print(twos)


#The snippet produces a ten-element list filled
#with squares of ten integer numbers starting from zero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

odds = [x for x in squares if x % 2 != 0]
print(odds)

#The snippet creates an eight-element array containing the first eight powers of two (1, 2, 4, 8, 16, 32, 64, 128)
odds = [x for x in squares if x % 2 != 0 ]
print(odds)

# This will take the remaining numbers from squares which are all even so this outputs the remaining even numbers
evens = [x for x in squares if x not in odds]
print(evens)

# This creates what is called a matrix or a two-dimmensional array
#This creates 8 lists containing 8 "EMPTY" elements

board = []

for i in range(8):
    row = ["EMPTY" for i in range(8)]
    board.append(row)

## This actually creates the same exact thing but shortens the code a lot

board = [["EMPTY1" for i in range(8)]for j in range(8)]

print(board)

print(board)

