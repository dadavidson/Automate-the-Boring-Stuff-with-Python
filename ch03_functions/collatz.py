# The Collatz Sequence

def collatz(number):
	if (number % 2) == 0:
		# print 'The number %d is even' % number 
		evenValue = number // 2
		# print '%d // 2 = %d' % (number, evenValue)
		return evenValue
	else:
		# print 'The number %d is odd' % number
		oddValue = (3 * number) + 1
		# print '3 * %d + 1 = %d' % (number, oddValue)
		return oddValue

try:
	value = int(raw_input('Enter number:\n'))
except:
	print 'Error: Invalid input. Input must be an integer.'

while True:
	value = collatz(value)
	print value
	if value == 1:
		print 'Amazingly enough, you arrived at 1'
		break