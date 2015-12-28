#https://www.hackerrank.com/contests/101hack30/challenges/four-primes
import math
def primeSieve(sieveSize):
     # Returns a list of prime numbers calculated using
     # the Sieve of Eratosthenes algorithm.

     sieve = [True] * sieveSize
     sieve[0] = False # zero and one are not prime numbers
     sieve[1] = False

     # create the sieve
     for i in range(2, int(math.sqrt(sieveSize)) + 1):
         pointer = i * 2
         while pointer < sieveSize:
             sieve[pointer] = False
             pointer += i

     # compile the list of primes
     primes = []
     for i in range(sieveSize):
         if sieve[i] == True:
             primes.append(i)

     return primes

def isFourPrimeBitwise(inputVal):
    result = 0
    miniPrimeList = primeSieve(inputVal)
    
    #print(miniPrimeList)
    if len(miniPrimeList) < 1:
        print('NO')
        return 1

    for num1 in miniPrimeList:
        for num2 in miniPrimeList:
            if num1 < num2 and num1|num2 == inputVal:
                print('YES')
                result = 1
                return 1
                for num3 in miniPrimeList:
                    if num2 < num3 and num1|num2|num3 == inputVal:
                        print('YES')
                        result = 1
                        return 1
                    for num4 in miniPrimeList:
                        if num3 < num4 and num1|num2|num3|num4 == inputVal:
                            print('YES')
                            result = 1
                            return 1


    
    if not result:
        print('NO')
    return 1
    
    
for inp in range(int(input())):
    isFourPrimeBitwise(int(input()))


