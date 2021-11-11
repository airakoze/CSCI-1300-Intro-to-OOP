# Test Cases
testCases = int(input())

for j in range(testCases):
    numTrips = int(input())
    cityVisited = []
    for k in range(numTrips):
        city = input()
        if city in cityVisited:
            continue
        else:
            cityVisited.append(city)
    print(len(cityVisited))