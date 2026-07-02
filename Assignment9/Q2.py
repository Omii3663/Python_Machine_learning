def ChkGreater(No1,No2):
    if No1 > No2 :
        print(f"{No1} is Greater")
    else:
        print(f"{No2} is Greater")


def main():
    print('-'*40)
    print("----Check Which Number is Greater----")
    print('-'*40)

    print("Enter First Number :")
    No1 = int(input())

    print("Enter Second Number :")
    No2 = int(input())

    GreaterNo = ChkGreater(No1,No2)
    


if __name__ == "__main__":
    main()


    
