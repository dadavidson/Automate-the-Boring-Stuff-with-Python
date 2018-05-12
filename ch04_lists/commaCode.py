spam = ['apples', 'bananas', 'tofu', 'cats']
test = ['manjaro', 'ubuntu', 'linux mint', 'debian']

def commaCode(list):
	tempStr = ""
	for i in range(len(list) - 1):
		tempStr += "%s, " % list[i]
	tempStr += 'and %s' % list[-1]
	return tempStr

print commaCode(test) 