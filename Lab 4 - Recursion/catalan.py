import sys

#C0 = 1 and Cn+1 = Sum (i=0, n) Ci*Cn-1 for n >= 0
def catalan(num):
	#base case
	if num <= 1:
		return 1
	ret = 0
	#compute catalan number
	for i in range(num):
		ret += catalan(i) * catalan(num-i-1)
	return ret

#get argument from command line and convert to an integer
print(catalan(eval(sys.argv[1])))