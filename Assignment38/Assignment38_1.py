import pandas as pd

def StudentPerformance(DataPath):
    Boreder = "-"*40

    #read DataSet
    print(Boreder)
    print("Step 1: Read CSV File")
    print(Boreder)

    df = pd.read_csv(DataPath)

    print(Boreder)
    print("First five Recoreds")
    print(df.head(5))

    print(Boreder)
    print("Last five Recoreds")
    print(df.tail(5))

    print(Boreder)
    print("Name of each Columns")
    print(df.columns)
    
    print(Boreder)
    print("DataType of each Columns Are :")
    print(df.info())

    


def main():
    StudentPerformance("student_performance_ml.csv")

if __name__ == "__main__":
    main()