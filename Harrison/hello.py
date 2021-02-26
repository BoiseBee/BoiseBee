def program():
    pass
    
    
while True:
	try:
		num1 = int(input("Type a number: ")) #Gets user input
		num2 = int(input("Type a number: ")) #Gets 2nd number
		

		print("addition")
		print(num1+num2)
		print(" ")
		print("division")
		print(num1/num2)
		print(" ")
		print("subtraction")
		print(num1-num2)
		print(" ")
		print("multiplication")
		print(num1*num2)

		print(" ")

		print("Thank you for using the calculator")

		print(" ")
		
	except ValueError:
		print("You need to input number...")

	answer = str(input('Would you like to use the calculator again? (y/n): '))
	if answer in ('y'):
		if answer == "y":
		    program()
	else:
		print("Goodbye")
		break

#program()
