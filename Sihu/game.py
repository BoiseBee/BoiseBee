

#question = input("Do you want to play a game? (y/n)")

print("Each piece has is labled 1 2 3 4 5...")
print("A 2 can not go on a 1")
print("A 1 can only go on a 2")

rings = 0
poleleft = []
polemid = []
poleright = []

while rings < 1:
	try:
		rings = int(input("How many rings do you want: "))
	except ValueError: 
		print("Only numbers")


for x in range(rings):	
	poleleft.append(x)


def showgame():
	print()  
	print("LEFT:")
	for x in poleleft:
		print(x)

	print("MID:")
	for x in polemid:
		print(x)

	print("RIGHT:")
	for x in poleright:
		print(x)
	
showgame()

def check():
	if polemid.pop(0) != 0 or poleright.pop(0) != 0:
		print('You can not make that move')
	elif polemid == [] or poleright == []:
		pass

def action(move1, move2):
	if move1 == "left":
		ring = poleleft[0]
		if move2 == "mid":
			polemid.insert(0, ring)
			poleleft.remove(ring)
		if move2 == "right":
			poleright.insert(0, ring)
			poleleft.remove(ring)
		check()
		
	if move1 == "mid":
		ring = polemid[0]
		if move2 == "left":
			poleleft.insert(0, ring)
			polemid.remove(ring)
		if move2 == "right":
			poleright.insert(0, ring)
			polemid.remove(ring)
		check()
			
	if move1 == "right":
		ring = poleright[0]
		if move2 == "mid":
			polemid.insert(0, ring)
			poleright.remove(ring)
		if move2 == "left":
			poleleft.insert(0, ring)
			poleright.remove(ring)
		check()
			
			
			
			







			
def win():
	pass
	
	

while True:
	gogo = 0
	while gogo != 1:
		print("Enter in left right or mid")
		print()
		move1 = input("First part of move: ")
		move2 = input("Second part of move: ")

		if move1.lower() == "left" or "right" or "mid":
			if move2.lower() == "left" or "right" or "mid":
				gogo = 1



	print(move1, move2)
	action(move1, move2)
	showgame()



















