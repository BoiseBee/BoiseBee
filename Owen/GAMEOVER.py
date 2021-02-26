   

#question = input("Do you want to play a game? (y/n)")
import sys
print("Each piece has is labled 1 2 3 4 5...")
print("A 2 can not go on a 1")
print("A 1 can only go on a 2")

rings = 0
pole1 = []
pole2 = []
pole3 = []
count = 0

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
	global count
	ifWin()
	count = count + 1
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

		
def check(): 
	if(move1 == move2):
		print("Why?")
		showgame()
	while(move2 == "right" or "left" or "mid"):
		if(pole1[0] > pole2[0] or pole3[0]):
			print("This is not an allowed legal move")
			print("GAME OVER")
			sys.exit()
		elif(pole2[0] > pole3[0] or pole2[0]):
			print("This is not a legal move")
			print("GAME OVER")
			sys.exit()
		elif(pole3[0] > pole1[0] or pole2[0]):
			print("This isn't a legal move")
			print("GAME OVER")
			sys.exit()
		else:
			break
def ifWin():
	polew = len(pole3) - 1
	if(polew == rings):
		print("Congradulations You Won!!!!!")
		print("It took you " + count + " Moves to finish")
		sys.exit()
		

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
	if(count >= 2):
		check()
	action(move1, move2)
	showgame()

















