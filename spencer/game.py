

#question = input("Do you want to play a game? (y/n)")

print("Each piece has is labled 1 2 3 4 5...")
print("A 2 can not go on a 1")
print("A 1 can only go on a 2")

rings = 0
pole1 = []
pole2 = []
pole3 = []

while rings < 1:
	try:rings = int(input("How many rings do you want: "))
	except ValueError: print("Only numbers")


for x in range(rings):	
	pole1.append(x)


def showgame():
	print()
	print("LEFT:")
	for x in pole1:
		print(x)

	print("MID:")
	for x in pole2:
		print(x)

	print("RIGHT:")
	for x in pole3:
		print(x)
	
showgame()

def action(move1, move2):
	if(move1 == "left"):
		#ring = (len(pole1)-1)
		ring = pole1[0]
		if(move2 == "mid"):
	#		print()
	#		print(pole1[ring])
			#print(len(pole2))
	#		print(pole2[0])
	#		print()
			pole2.insert(0, ring)
			pole1.remove(ring)
		if(move2 == "right"):
			pole3.insert(0, ring)
			pole1.remove(ring)
		
	if(move1 == "mid"):
		ring = pole2[0]
		if(move2 == "left"):
			pole1.insert(0, ring)
			pole2.remove(ring)
		if(move2 == "right"):
			pole3.insert(0, ring)
			pole2.remove(ring)
			
	if(move1 == "right"):
		ring = pole3[0]
		if(move2 == "mid"):
			pole2.insert(0, ring)
			pole3.remove(ring)
		if(move2 == "left"):
			pole1.insert(0, ring)
			pole3.remove(ring)


while True:
	gogo = 0
	while gogo != 1:
		print("Enter in left right or mid")
		print()
		move1 = input("First part of move: ")
		move2 = input("Second part of move: ")

		if move1 == "left" or "right" or "mid":
			if move2 == "left" or "right" or "mid":
				gogo = 1



	print(move1, move2)
	action(move1, move2)
	showgame()

















