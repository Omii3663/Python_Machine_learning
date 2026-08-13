import pandas as pd
import matplotlib.pyplot as plt

def StudentPerformance(DataPath):
    # Read the dataset
    df = pd.read_csv(DataPath)

    # 1. Create a Scatter Plot
    plt.figure(figsize=(8, 5))
    plt.scatter(df['SleepHours'],
                df['FinalResult'],
                alpha=0.6,
                color='coral',
                edgecolors='k')

    # 2. Add Titles and Labels
    plt.title("Relationship Between Sleep Hours & Final Result", fontsize=14, pad=15)
    plt.xlabel("Sleep Hours (per night)", fontsize=11)
    plt.ylabel("Final Result (Score)", fontsize=11)
    
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout() # Automatically adjusts the padding around subplots and text
    plt.show()

if __name__ == "__main__":
    StudentPerformance("student_performance_ml.csv")
