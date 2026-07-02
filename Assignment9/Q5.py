def CheckDivisible(No):
    if No%3 & No%5 == 0 :
        print(f"{No} is Divisble by 5 & 3")
    else:
        print(f"{No} is Not Divisble by 5 & 3")

def main():
    print('-'*50)
    print("------Check Number is Divisble by 5 & 3------")
    print('-'*50)

    print("Enter Number :")
    No = int(input())

    Check = CheckDivisible(No)

if __name__ == "__main__":
    main()