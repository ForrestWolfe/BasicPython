#The whole matrix is filled with zeros now. You can assume that it's updated automatically using special hardware agents.
# The thing you have to do is to wait for the matrix to be filled with measurements.

#Now it's time to determine the monthly average noon temperature. Add up all 31 readings recorded at noon and divide the
# sum by 31. You can assume that the midnight temperature is stored first. Here's the relevant code:
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# the matrix is magically updated here
#

print(temps)

sum = 0.0

for day in temps:
    sum += day[11]

average = sum / 31

print("Average temperature at noon:", average)


#Now find the highest temperature during the whole month - see the code:
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# the matrix is magically updated here
#

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)

#Now count the days when the temperature at noon was at least 20 ℃:
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# the matrix is magically updated here
#

hotDays = 0

for day in temps:
    if day[11] > 20.0:
        hotDays += 1

print(hotDays, "days were hot.")

