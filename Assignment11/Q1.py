def Prime(num):

    if num <= 1:
        print("Not a Prime Number")
    else:
        for i in range(2, num):
            if num % i == 0:
                print("Not a Prime Number")
                break
        else:
            print("Prime Number")


def main():
    print('-'*30)
    print("------Prime Numbers ------")
    print('-'*30)

    print("Enter Number :")
    No = int(input())
    Prime(No)

if __name__ == "__main__":
    main()