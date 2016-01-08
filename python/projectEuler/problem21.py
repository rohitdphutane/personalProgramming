import math

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def isAmicableNum(number, sumOfDivisors):
    secondDivisors = list(divisorGenerator(sumOfDivisors))
    del secondDivisors[-1]
    if sum(secondDivisors) == number:
        print str(number)+" - "+str(sum(secondDivisors))
        return True
    else:
        return False

resultList = []    

for number in range(2,10000):
    divisors = list(divisorGenerator(number))
    del divisors[-1]
    sumOfDivisors = sum(divisors)
    if isAmicableNum(number, sumOfDivisors) and number != sumOfDivisors:
        print "number is amicable:- "+str(number)
        if number not in resultList:
            resultList.append(number)

print resultList
print sum(resultList)
 
