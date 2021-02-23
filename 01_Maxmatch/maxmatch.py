import sys

f = open("dict.txt","r").read()
lists = f.split('\n')
#print(list)


translate = open("final.segmented", "r")
correct = open("th_pud-ud-test.segmented", "r")
#print(translate.readline())
#current = translate.readline()

#while current != '':
#	toPrint = ''

def checkPart(currentString, lists):
	for x in range(len(currentString), 0, -1):
#		print(currentString[0:x] + ' and ' + str(x))
		if x == 1:
			return [currentString[0:1], currentString[1:len(currentString)]]
		else:
			for check in lists:
				if currentString[0:x] == check:
					return [currentString[0:x], currentString[x:len(currentString)]]
	return [currentString[0], currentString[1:len(currentString)]]

def compare(response, key):
	r = response.split(" ")
	k = key.split(" ")
#	print( r )
#	print( k )
	total = 0
	failures = 0
	for bit in r:
		total = total + 1
		if bit not in k:
			failures = failures + 1
	return failures / total

current = translate.readline().strip()

while current != '':
	print('Orginal line\t' + current)
	toPrint = ''
	finish = False
	while finish == False:
		temp = checkPart(current, lists)
#		print('newCurrent is currently ' + newCurrent)
#		print('the value at temp[1] is currently ' + str(temp))
		newCurrent = temp[1]
		toPrint = toPrint + ' ' + temp[0]
		current = newCurrent
		if current == '':
			finish = True
	toPrint = toPrint.strip()
	print('Generated line\t' + toPrint)
	correctLine = correct.readline()
	print("Correct line\t" + correctLine.strip())
	print("Word error rate = " + str(compare(toPrint, correctLine)) + '\n')
	current = translate.readline().strip()
