def Cube(No):
    return No * No * No

def main():
    print('-'*30)
    print("------Cube of a Number------")
    print('-'*30)

    print("Enter Number :")
    No1 = int(input())

    Sqr = Cube(No1)
    print(f"Cube of Number {No1} is ", Sqr)

if __name__ == "__main__":
    main()