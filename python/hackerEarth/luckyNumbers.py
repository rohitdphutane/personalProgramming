#https://www.hackerearth.com/craftsvilla-hiring-challenge/algorithm/lucky-numbers-20/
import sys
k1=int(sys.stdin.readline())
def calculateResult(n):
    result = 0
    init = 1
    while init <= n:
        #print bin(init)[2:]
        binaryVal = bin(init)
        setCount = binaryVal.count("1")
        if setCount == 2:            
            print(str(init)+", count is 2 -"+str(binaryVal))
            result = result + init
        init = init + 1
    print(result%1000000007)
    
while k1>0:
    calculateResult(int(sys.stdin.readline()))
    k1=k1-1

