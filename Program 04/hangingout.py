# Input for the number of spots available and for events
numSE = (input()).split() 
numEvents = int(numSE[1])

# Count of number of groups rejected
count = 0

# Spots available
spots = int(numSE[0])

# People present on the terrace
pp = 0

for k in range(numEvents):
    event = (input()).split()
    if event[0] == "enter":
        if (int(event[1]) + pp) <= spots:
            pp += int(event[1])
        else:
            count += 1
            
    elif event[0] == "leave":
        pp -= int(event[1])
        #spots += int(event[1])

print(count)