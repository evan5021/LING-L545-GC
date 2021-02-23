import sys, re

line = sys.stdin.readline()
while line != '':
	for token in line.strip().split(' '):
		if token.strip() == '':
			continue
		if re.match('^http*', token):
			continue
		elif token[-1] in '!?':
			sys.stdout.write(token + '\n')
		elif token[-1] == '.':
			if token in ['etc.', 'i.e.', 'e.g.', 'dott.', 'prof.', 'ecc.', 'es.', '...']:
				sys.stdout.write(token + ' ')
			else:
				sys.stdout.write(token + '\n')
		else:
			sys.stdout.write(token + ' ')
	line = sys.stdin.readline()
