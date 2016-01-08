pentaNumbers=[]

def calculatePentaNumber(num):
    return num * (3*num - 1)/2

for num in range(1,10000):
    pentaNumbers.append(calculatePentaNumber(num))

print pentaNumbers

for p1 in pentaNumbers:
    print p1
    for p2 in pentaNumbers:
        if p2 > p1 and p1+p2 in pentaNumbers and p2-p1 in pentaNumbers:
            print str(pentaNumbers[p1]) +" - "+str(pentaNumbers[p2])
