
for i in range(1,1000000):
    numList = []
    numList.append(''.join(sorted(str(i))))
    numList.append(''.join(sorted(str(i*2))))
    numList.append(''.join(sorted(str(i*3))))
    numList.append(''.join(sorted(str(i*4))))
    numList.append(''.join(sorted(str(i*5))))
    numList.append(''.join(sorted(str(i*6))))
    if len(set(numList)) == 1:
        print i


#print numList
#print len(set(numList))
