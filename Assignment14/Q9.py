Multiplication = lambda No1, No2 :  No1 * No2

def main():
    print('-'*40)
    print("----Multiplication Using lambda----")
    print('-'*40)

    print("Enter First Number :")
    No1 = int(input())
    print("Enter Second Number :")
    No2 = int(input())

    Ret = Multiplication(No1,No2)
    print("The Multiplication of Number is :",Ret)

if __name__ == "__main__":
    main()