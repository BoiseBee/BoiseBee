def program():
    while True:
        num1 = int(input("Type a number: ")) #Gets user input

        num2 = int(input("Type a number: ")) #Gets 2nd number
<<<<<<< HEAD
    
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

=======

        print (str(Addition))
        print(num1+num2)
        print (str(Division))
        print(num1/num2)
        print (str(Subtraction))
        print(num1-num2)
        print (str(multiplication))
        print(num1*num2)

        print(" ")

        print("Thank you for using the calculator")

        print(" ")

>>>>>>> 0bbd757c3ee7ed2644f202d15b8352371aa59366
        answer = str(input('Would you like to use the calculator again? (y/n): '))
        if answer in ('y', 'n'):
            break
            print("invalid input")
        if answer == 'y':
            program()
        else:
            print("Goodbye")
            break

<<<<<<< HEAD
program()
=======
program()
>>>>>>> 0bbd757c3ee7ed2644f202d15b8352371aa59366
