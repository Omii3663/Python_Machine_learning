def BinaryEquivalent(No):
    if No > 1 :
        BinaryEquivalent(No // 2)
    print(No % 2, end = '')

def main():
    print('-'*30)
    print("------Binary Equivalent ------")
    print('-'*30)

    print("Enter Number :")
    No = int(input())

    BinaryEquivalent(No)
    print()  # Print a newline after the binary equivalent

if __name__ == "__main__":
    main()