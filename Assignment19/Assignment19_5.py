from functools import reduce

def Prime(No):
    for i in range(2, No):
        if No % i == 0:
            return False
    return True

def Multtwo(No):
    return No * 2

def Maximun(No1,No2):
    if No1 > No2 :
        return No1
    else:
        return No2
    
def main():
    print("How many Number Do you Want to Enter :")
    No = int(input())
    lst = []
    for i in range(No):
        lst.append(int(input("Enter Number :")))

    FData = list(filter(Prime,lst))
    print("List After Filter :", FData)

    MData = list(map(Multtwo,FData))
    print("List After Map :", MData)

    RData = reduce(Maximun,MData)
    print("List After Reduce :", RData)

if __name__ == "__main__":
    main()
