def Table(No):
    for i in range(1,11):
        print(i * No)


def main():
    print('-'*40)
    print("------Multiplication Table ------")
    print('-'*40)

    print("Enter Number :")
    No = int(input())
    print(f" Multiplication Table of {No} is")
    tb = Table(No)

if __name__ == "__main__":
    main()