class  BankAccount:
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print(f"Account Holder Name : {self.Name}")
        print(f"Account Balance : {self.Amount}")

    def Deposit(self,DepositAmount):
        self.Amount += DepositAmount
        print(f"Deposited Amount : {DepositAmount}")
        print(f"Updated Balance : {self.Amount}")

    def Withdraw(self,WithdrawAmount):
        if WithdrawAmount > self.Amount:
            print("Insufficient Balance")
        else:
            self.Amount -= WithdrawAmount
            print(f"Withdrawn Amount : {WithdrawAmount}")
            print(f"Updated Balance : {self.Amount}")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI ) / 100
        return Interest


def main():
    bobj = BankAccount("Piyush", 10000)
    bobj.Display()
    bobj.Deposit(5000)
    bobj.Withdraw(2000)
    Interest = bobj.CalculateInterest()
    print(f"Interest on Current Balance : {Interest}")

    aobj = BankAccount("Omkar", 20000)
    aobj.Display()
    aobj.Deposit(10000)
    aobj.Withdraw(5000)
    Interest = aobj.CalculateInterest()
    print(f"Interest on Current Balance : {Interest}")

if __name__ == "__main__":
    main()