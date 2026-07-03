from functools import reduce
Addition = lambda No1, No2 : No1 + No2

def main():
    Data = [13,12,8,10,11,20]

    print("Input Data is :", Data)

    
    RData = reduce(Addition, Data)

    print("Addtion of List Elements is : :", RData)

if __name__ == "__main__":
    main()