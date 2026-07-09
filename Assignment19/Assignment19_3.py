from functools import reduce
def filterout(No):
    lst = []
    if No >= 70 and No <= 90:
        lst.append(No)
    
    return lst

def AddTen(No):
    return No + 10 

def product(No1,No2):
    return No1 * No2

def main():
    print("Enter How many Numbers You Want to Enter :")
    No = int(input())
    Data = []
    for i in range(No):
        Data.append(int(input("Enter Number : ")))

    FData = list(filter(filterout,Data))
    print("List After Filter :", FData)

    MData = list(map(AddTen,FData))
    print("List After Map :", MData)

    RData = reduce(product,MData)
    print("List After Reduce :", RData)

if __name__ == "__main__":
    main()
    
