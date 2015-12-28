#https://www.hackerrank.com/challenges/two-strings
numberOfInputs = int(input())
inputList = []
for inp in range(numberOfInputs * 2):
    inputList.append(input())

evenCount = 0
while evenCount < numberOfInputs * 2:
    str1 = inputList[evenCount]
    str2 = inputList[evenCount+1]
    result = 0
    for s1 in str1:
        if s1 in str2:
            result = 1
            break
        
    if result:
        print('YES')
    else:
        print('NO')
    evenCount = evenCount + 2
                
        
    
        
