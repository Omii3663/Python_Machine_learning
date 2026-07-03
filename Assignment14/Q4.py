Minimum = lambda No1,No2:No1 if No1<No2 else No2

def main():
    print('-'*40)
    print("----Minimum Number Using Lambda----")
    print('-'*40)

    print("Enter First Number :")
    No1 = int(input())

    print("Enter Second Number :")
    No2 = int(input())

    Ret = Minimum(No1,No2)
    print("Minimum Number is :", Ret)

if __name__ == "__main__":
    main()
