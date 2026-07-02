<<<<<<< HEAD
def Factor(No):
    for i in range(1,No+1):
        if No % i == 0:
            print(i)


def main():
    print('-'*30)
    print("------Factors of a Number ------")
    print('-'*30)

    print("Enter Number :")
    No = int(input())
    
    print(f"Factors of {No} is :")
    Factor(No)

if __name__ == "__main__":
=======
def Factor(No):
    for i in range(1,No+1):
        if No % i == 0:
            print(i)


def main():
    print('-'*30)
    print("------Factors of a Number ------")
    print('-'*30)

    print("Enter Number :")
    No = int(input())
    
    print(f"Factors of {No} is :")
    Factor(No)

if __name__ == "__main__":
>>>>>>> f82048f (ok)
    main()