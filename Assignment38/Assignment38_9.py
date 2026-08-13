import pandas as pd
import matplotlib.pyplot as plt

def StudentPerformance(DataPath):
    df = pd.read_csv(DataPath)

    # 1. Create a Scatter Plot
    plt.figure(figsize=(8, 5))
    plt.scatter(
        df['AssignmentsCompleted'],
        df['FinalResult'],
        alpha=0.6,
        color='darkcyan',  #colors purple black....
        edgecolors='k')   # k means black in matplot    

    # 2. Add Titles and Labels
    plt.title("Relationship Between Assignments Completed & Final Score", fontsize=14, pad=15)
    plt.xlabel("Number of Assignments Completed", fontsize=11)
    plt.ylabel("Final Result (Score)", fontsize=11)
    
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

    # # 2. Create a Box Plot grouped by finalResult categories
    # plt.figure(figsize=(7, 5))
    # df.boxplot(column='AssignmentsCompleted', by='FinalResult', 
    #            patch_artist=True, 
    #            boxprops=dict(facecolor='lightblue', color='navy'),
    #            medianprops=dict(color='red', linewidth=2))

    # # 2. Clean up Titles and Labels
    # plt.title("Assignments Completed across Final Results", fontsize=14, pad=15)
    # plt.suptitle("") # Clears Pandas automatic subtitle default
    # plt.xlabel("Final Result", fontsize=11)
    # plt.ylabel("Assignments Completed", fontsize=11)
    
    # plt.grid(True, linestyle='--', alpha=0.3)
    # plt.tight_layout()
    # plt.show()


    # plt.bar(df['AssignmentsCompleted'], df['FinalResult'])
    
    # plt.title("Assignments Completed across Final Results")
    # plt.xlabel("AssignmentsCompleted")
    # plt.ylabel("FinalResult of students")

    # plt.grid(True)
    # plt.legend()
    # plt.show()
if __name__ == "__main__":
    StudentPerformance("student_performance_ml.csv")
