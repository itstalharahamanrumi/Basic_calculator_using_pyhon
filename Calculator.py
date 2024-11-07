print("welcome to claculator Project")
print("1. Additon")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division \n")
#Print all the operatons.

Operation = int(input("Select the operation in basic Calculator: "))
#Select the calculating Operation.  

#Conditions applies to check the inputs were right or wrong.
if Operation == 1:
    a = int(input("Enter The Frist Number: "))
    b = int(input("Enter The Second Number: "))
    c = a+b
    print(c)

elif Operation == 2:
    a = int(input("Enter The Frist Number: "))
    b = int(input("Enter The Second Number: "))
    c = a-b
    print(c)

elif Operation == 3:
    a = int(input("Enter The Frist Number: "))
    b = int(input("Enter The Second Number: "))
    c = a*b
    print(c)

elif Operation == 4:
    a = int(input("Enter The Frist Number: "))

    b = int(input("Enter The Second Number: "))
    c = a/b
    print(c)

else:
    print("Invalid Inputs.")

