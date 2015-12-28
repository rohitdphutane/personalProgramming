from itertools import product
from fractions import gcd

def lcm(a, b):
	return a*b/gcd(a, b)

def lcmm(*args):
	return reduce(lcm, args)
	
def fun(n, l, r, x):
	ls = [i for i in xrange(l, r+1)]
	prod = list(product(ls, repeat=n))
	return len([0 for i in prod if lcmm(*i)%x==0])
	
t = int(raw_input())
while t>0:
	t-=1
	n, l, r, x = map(int, raw_input().split())
	print fun(n, l, r, x)
