def Pattern(No):
    for i in range(1,No+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()

def main():
    print("-"*30)
    print("----Pattern Printer----")
    print("-"*30)

    print("Enter Number :")
    No = int(input())
 
    Pattern(No)

if __name__ == "__main__":
    main()
