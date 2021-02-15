def program():
    while True:
        num1 = int(input("Type a number: ")) #Gets user input

        num2 = int(input("Type a number: ")) #Gets 2nd number

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

        answer = str(input('Would you like to use the calculator again? (y/n): '))
        if answer in ('y', 'n'):
            break
            print("invalid input.")
        if answer == 'y':
            program()
        else:
            print("Goodbye")
            break

program()