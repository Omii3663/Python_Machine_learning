class Numbers:
    def __init__(self, Value):
        self.Value = Value

    def ChkPirme(self):
        if self.Value <= 1:
            return False
            
        
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False  
                
        return True  

    def Factors(self):
        lst = []
        for i in range(1, self.Value):
            if self.Value % i == 0:
                lst.append(i)
        return lst

    def SumFActors(self):
        return sum(self.Factors())

    def ChkPerfect(self):
        return self.SumFActors() == self.Value


def main():
    No = int(input("Enter Number : "))
    nobj = Numbers(No)
    
    if nobj.ChkPirme():
        print(f"{No} is Prime Number")
    else:
        print(f"{No} is Not Prime Number")

    if nobj.ChkPerfect():
        print(f"{No} is Perfect Number")
    else:
        print(f"{No} is Not Perfect Number")

    print(f"Factors of {No} are : ", nobj.Factors())
    print(f"Sum of Factors of {No} are : ", nobj.SumFActors())

if __name__ == "__main__":
    main()
