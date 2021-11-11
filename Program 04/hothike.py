days = int(input())

# Temperature List
tempList = input().split()

# Changing the items in the list into integers
for i, j in enumerate(tempList):
    tempList[i] = int(j)

# Maximum Temperature
maxTemp = 40

# First Day
day = 1

for  k in range(days - 2):
    # First hiking day temperature
    firstTemp = tempList[k]

    # Second hiking day temperature
    secondTemp = tempList[k+2]

    if max(firstTemp, secondTemp) < maxTemp:
        maxTemp = max(firstTemp, secondTemp)
        day = k + 1

print(day, maxTemp)