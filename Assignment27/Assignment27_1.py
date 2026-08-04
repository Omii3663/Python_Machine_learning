class BookStore:
    NoOfBooks = 0

    def __init__(self):
        self.Name = ""
        self.Author = ""
        BookStore.NoOfBooks += 1

    def Display(self):
        print(f"Book Name : {self.Name} by {self.Author}")
        print("Number of Books in Store : ", BookStore.NoOfBooks)


def main():
    bobj1 = BookStore()
    bobj1.Name = "Python Programming"
    bobj1.Author = "piyush khairnar"
    bobj1.Display()
    #print("Total Number of Books : ", BookStore.NoOfBooks)   

    No = int(input("Enter number of books to add : "))
    for i in range(No):
        bobj = BookStore()
        bobj.Name = input("Enter Book Name : ")
        bobj.Author = input("Enter Author Name : ")
        bobj.Display()

    #print("Total Number of Books : ", BookStore.NoOfBooks)

if __name__ == "__main__":
    main()

    
