def Pattern(No):
    for i in range(No+1):
        for j in range(No-i):
            print("*", end=" ")
        print()


def main():
    print("Enter Number :")
    No = int(input())
    Pattern(No)

if __name__ == "__main__":
    main()