sqr = lambda no : no * no

def main():
    print('-'*40)
    print("----Square of Number Using Lambda----")
    print('-'*40)

    print("Enter a Number :")
    no = int(input())
    Ret = sqr(no)
    print("Square of Number is:",Ret)

if __name__ == "__main__":
    main()

