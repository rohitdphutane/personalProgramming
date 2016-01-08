maxLimit = 1000
numList = []
for i in range(0,maxLimit):
    if i%3 == 0 or i%5 == 0:
        #print i
        numList.append(i)

print sum(numList)
