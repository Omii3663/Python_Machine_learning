def Factorial(No):
    fact = 1
    for i in range(1,No+1):
        fact = fact * i
    return fact

def main():
    print("-"*30)
    print("----Factorial----")
    print("-"*30)

    print("Enter Number :")
    No = int(input())

    Ret = Factorial(No)

    print(f"Factorial of Number {No} is : {Ret}")

if __name__ == "__main__":
    main()