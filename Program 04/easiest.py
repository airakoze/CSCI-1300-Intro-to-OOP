# Function to calculate the sum of the elements in the list
def sumResult(num):
    numList = list(num)
    total = 0
    for k in numList:
        total += int(k)
    return total 

num = input()
p = 11 # p has to be greater than 10
while num != "0":
    result = str(int(num) * p)
    resultSumDigit = sumResult(result)
    if resultSumDigit == sumResult(num):
        print(p)
    else:
        p += 1
        continue
    
    p = 11
    num = input()
    