#https://projecteuler.net/problem=16

resultSum = 0
value = str(2**1000)
i=0
while i < len(value):
    resultSum = resultSum + int(value[i])
    print value[i]
    i = i + 1
    
print resultSum
