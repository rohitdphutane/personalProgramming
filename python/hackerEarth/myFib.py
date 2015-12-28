#https://www.hackerearth.com/november-easy-15/algorithm/myfibonacci-easy-contest/
a,b,n = map(int,raw_input().split())
fib = [a,b]
if n < 3:
    print fib[n-1]
else:
    for idx in range(2,n+1):
        fib.append(fib[idx-2] + fib[idx-1])
        if (len(fib) == int(n)):
            print fib[idx]
            break
    

