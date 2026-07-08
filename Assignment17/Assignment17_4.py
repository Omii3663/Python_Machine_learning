def Factor(No):
    fact = 0
    for i in range(1,No):
        if No % i == 0 :
            fact = fact + i
        
    return fact

def main():
    print("-"*30)
    print("----Factors Addition----")
    print("-"*30)

    print("Enter Number :")
    No = int(input())

    Ret = Factor(No)

    print(f"Addition of Factor is : {Ret}")

if __name__ == "__main__":
    main()

        
