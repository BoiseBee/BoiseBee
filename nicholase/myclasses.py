classes = []

classnum = len(classes)

def myclasses():

	vlass = input("what classes do you have: ")
	classes.append(vlass)
	
	classnum = len(classes)
	print(classes)
	print(classnum)
	
	

	
while (classnum <= 4):
	 	myclasses()
	 	if classnum > 4:
	 		break
