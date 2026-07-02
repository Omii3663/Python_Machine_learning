def Addition(No1, No2):
    return No1 + No2

def Subtraction(No1, No2):
    return No1 - No2

def Multiplication(No1, No2):
    return No1 * No2

def Division(No1, No2):
    if No2 == 0:
        print("You Cannot Divide by Zero...")
    else:
        return No1 / No2
    
def main():
    print('-'*20)
    print("------Calculater ------")
    print('-'*20)

    print("Enter First Number :")
    No1 = int(input())

    print("Enter Second Number :")
    No2 = int(input())

    add = Addition(No1, No2)
    print("Addtion is :",add)

    sub = Subtraction(No1, No2)
    print("Subtraction is :",sub)

    mul = Multiplication(No1, No2)
    print("Multiplication is :",mul)

    div = Division(No1, No2)
    print("Division is :",div)
    

if __name__ == "__main__":
    main()