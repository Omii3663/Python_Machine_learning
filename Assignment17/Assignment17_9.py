def NumCouner(No):
    Count = 0
    while No != 0 :
        No = No // 10
        Count = Count + 1
    return Count

def main():
    print("Enter Number :")
    No = int(input())
    Ret = NumCouner(No)
    print(f"Count of Digits is : {Ret}")

if __name__ == "__main__":
    main()

