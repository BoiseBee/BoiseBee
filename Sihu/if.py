pets = ['dog', 'cat', 'fish', 56, 42, 0, 'cat']

y  = 0
for x in pets:
	if x == 'cat':
		y = y + 1
		print(pets.index('cat'))

