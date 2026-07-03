Maximum = lambda No1,No2:No1 if No1>No2 else No2

def main():
    print('-'*40)
    print("----Maximum Number Using Lambda----")
    print('-'*40)

    print("Enter First Number :")
    No1 = int(input())

    print("Enter Second Number :")
    No2 = int(input())

    Ret = Maximum(No1,No2)
    print("Maixmum Number is :", Ret)

if __name__ == "__main__":
    main()
