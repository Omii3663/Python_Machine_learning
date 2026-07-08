def AddtionOfDigits(No):
    Sum = 0
    while No != 0 :
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum

def main():
    print("Enter Number :")
    No = int(input())
    Ret = AddtionOfDigits(No)
    print(f"Addition of Digits is : {Ret}")

if __name__ == "__main__":
    main()
