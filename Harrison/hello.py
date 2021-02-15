while True:
num1 = int(input("Type a number: ")) #Gets user input

num2 = int(input("Type a number: ")) #Gets 2nd number

print(num1+num2)
print(num1/num2) 
print(num1-num2)
print(num1*num2)

print(" ")

print("Thank you for using the calculator")

print(" ")

    while True:
        answer = str(input('Would you like to use the calculator again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break