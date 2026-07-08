from Arthmatic import Add,Sub,Mult,Div

def main():
    print("-"*30)
    print("Arthmatic Opration \ Calculater")
    print("-"*30)

    print("Enter First Number :")
    No1 = int(input())

    print("Enter Second Number :")
    No2 = int(input())

    Ret1 = Add(No1,No2)
    print(f"Addition is : {Ret1}")

    Ret2 = Sub(No1,No2)
    print(f"Substraction is : {Ret2}")

    Ret3 = Mult(No1,No2)
    print(f"Multiplication is : {Ret3}")

    Ret4 = Div(No1,No2)
    print(f"Division is : {Ret4}")

if __name__ == "__main__":
    main()
