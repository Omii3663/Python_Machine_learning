from functools import reduce
Maximum = lambda No1,No2 : No1 if No1 > No2 else No2

def main():
    Data = [13,12,8,10,11,20]

    print("Input Data is :", Data)

    RData = reduce(Maximum,Data)
    print("Maximun Number From list is :", RData)

if __name__ == "__main__":
    main()