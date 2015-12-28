numList = []
for i in range(0,100):
    numList.append(raw_input())

numList = map(int, numList)
print numList
print sum(numList)
