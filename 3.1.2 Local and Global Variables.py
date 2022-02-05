def L(x, n):
	s = 0
	for i in range(1, n+1):
		s += (1/i)*(x/(1+x))**i
	value_of_sum = s
	first_neglected_term = (1/(n+1))*(x/(1+x))**(n+1)
	from math import log
	exact_error = log(1+x) - value_of_sum
	return value_of_sum, first_neglected_term, exact_error

def table(x):
	from math import log
	print ('x={}, ln(1+x)={}'.format(x, log(1+x)))
	for n in [1, 2, 10, 100, 500]:
		value, next, error = L(x,n)
		print( 'n =%-4d %-10g (next term: %8.2e error: %8.2e)' % (n, value, next, error))
#table(10)

def count_v2(dna, base):
	i = 0 
	for c in dna:
		if c == base:
			i += 1
	return i
dna = 'ATGCGGACCTAT'
base = 'C'
n = count_v2(dna, base)
print('%s appears %d times in %s' % (base, n, dna))
print('{} appears {} times in {}'.format(base, n, dna))
print('{base} appears {n} times in {dna}'.format(base=base, n=n, dna=dna))