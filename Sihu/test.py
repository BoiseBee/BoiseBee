
Status = True
try:
	while Status:
			num = int(input('Type a number: ')) #Gets user input
			num2 = int(input('Number two: ')) #Gets 2nd number

			if type(num) == int:
				Status = False
			elif type(num2) == int:
				Status = False

	print(num + num2)
	print(num / num2)

except:
	print('Something has gone wrong, please try again')






