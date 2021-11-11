num = int(input()) # Numbers of names
setNum = [num] # List of the numbers of names in a set
setName = [] # Used for storing the new arranged names
while num != 0:
    symNames = []
    symNames1 = []
    for k in range(num):
        name = input()
        if k % 2 == 0:
            symNames.append(name)
        else:
            symNames1.append(name)
        
    symNames1.reverse()
    for i in symNames1:
        symNames.append(i)
    
    setName.append(symNames)
    num = int(input())
    if num != 0:
        setNum.append(num)


# Output the list of name in the correct format
for k in range(len(setNum)):
    print('SET', (k+1))
    for i in setName[k]:
        print(i)
