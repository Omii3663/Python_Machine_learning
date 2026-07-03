Square = lambda No : No * No

def main():
    Data = [1,2,3,4,5,6]

    print("Input Data is :", Data)

    MData = list(map(Square, Data))

    print("List of Square is :", MData)



if __name__ == "__main__":
    main()