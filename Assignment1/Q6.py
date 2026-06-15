print("-"*28)
print("----Maths Program Module----")
print("-"*28)


print("Enter a First Number:")
No1 = int(input())

print("Enter a Second Number:")
No2 = int(input())

Addition = No1 + No2
print(f"The Addition of {No1} + {No2} is :", Addition)

Subtraction = No1 - No2
print(f"Subtration of {No1} - {No2} is :", Subtraction)

Multiplication = No1 * No2
print(f"Multiplication Of {No1} x {No2} is :", Multiplication)

if (No2 == 0):
    print("Cannot divide by zero")
else:
    Divide = No1/No2
    print(f"Division of {No1} & {No2} is :", Divide)
