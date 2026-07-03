Addition = lambda No1, No2 :  No1 + No2

def main():
    print('-'*30)
    print("----Addition Using lambda----")
    print('-'*30)

    print("Enter First Number :")
    No1 = int(input())
    print("Enter Second Number :")
    No2 = int(input())

    Ret = Addition(No1,No2)
    print("The Addition of Number is :",Ret)

if __name__ == "__main__":
    main()