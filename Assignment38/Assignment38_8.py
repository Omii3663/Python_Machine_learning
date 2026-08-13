import pandas as pd
import matplotlib.pyplot as plt

def StudentPerformance(DataPath):
    Border = "-"*40
    #Read CSV
    df = pd.read_csv(DataPath)

    print(Border)

    Attendance = df['Attendance']


    plt.boxplot(
        Attendance
    )

    plt.title("Box Plot of Attendance")
    plt.xticks([1], ['Attendance']) 
    plt.ylabel("Frequency")

    #plt.grid(True)

    #plt.legend()
    plt.show()




def main():
    StudentPerformance("student_performance_ml.csv")

if __name__ == "__main__":
    main()