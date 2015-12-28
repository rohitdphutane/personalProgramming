def sumOfSquares(num):
    result = 0
    for i in range(1,num+1):
        result = result + i*i
    return result

def squareOfSum(num):
    result = 0
    for i in range(1,num+1):
        result = result + i
    return result*result

inputNum = 100
print sumOfSquares(inputNum)
print squareOfSum(inputNum)
print squareOfSum(inputNum) - sumOfSquares(inputNum)

