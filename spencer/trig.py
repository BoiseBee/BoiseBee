import math

SSS = input("SSS? (y/n): ")
SAS = input("SAS? (y/n): ")

if(SSS == "y"):
	print("Using Heron's Formula...")
	print("s = (a+b+c)/2")
	print("A = sqrt(s(s-a)(s-b)(s-c))")

	a = float(input("Side a: "))
	b = float(input("Side b: "))
	c = float(input("Side c: "))

	s = (a+b+c)/2
	A = math.sqrt(s*(s-a)*(s-b)*(s-c))
	print(s)
	print("Area:", round(A, 1))
	print("s = ({0}+{1}+{2})/2".format(a, b, c))
	print("A = sqrt({3}({3}-{0})({3}-{1})({3}-{2}))".format(a, b, c, s))



if(SAS == "y"):
	print("Using SAS...")

	a1 = float(input("Angle 1: "))
	s1 = float(input("Side 1: "))
	s2 = float(input("Side 2: "))
	print()
	print("A=1/2*(a*b)*sin(C)")
	print()
	print("A=1/2({1})({2})sin({0})".format(a1, s1, s2))


	A = round((.5*s1*s2)*(math.sin(math.radians(a1))), 1)
	print("Area:", A)

	print()

	print("A=1/2*(a*b)*sin(C)")


