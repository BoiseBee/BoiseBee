pets = ["dog", "cat", "fish", 56, 42, 0, "cat"]

#print(pets[3])

y = 0
a = 0
for x in pets:
	if (x == "cat"):
		y = y + 1
#		break
		print(str(y) + ", " + str(a))
	a = a + 1
