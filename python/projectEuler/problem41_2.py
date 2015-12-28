#https://projecteuler.net/problem=41

maxNum = 987654321

def is_prime(a):
    return all(a % i for i in xrange(2, a))


def isValidNum(num):
    #isValid = True
    for i in range(1,10):
        if str(i) not in str(num):
            return False
    return True

for j in range(maxNum, maxNum - 100000000, -1):
    if j%1000000 == 0:
        print j
    if isValidNum(j) and is_prime(j):
        print "Result:- "+str(j)
        break
#print isValidNum(maxNum)
        

