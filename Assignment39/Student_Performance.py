from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    
)

def Student_Perf(DataPath):
    Border = "-"*40
    # Read CSV

    df = pd.read_csv(DataPath)

    # Decide independent & dependent variables

    feature_col = [             #Independent Variables
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
               ]

    X = df[feature_col]
    Y = df["FinalResult"]       # Depedent Variable

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.5, random_state=42)

    #####################################################
    # Step 1 : Train the model
    ####################################################

    print(Border)
    print("Step 1 : Train the model ")
    print(Border)

    model = DecisionTreeClassifier(max_depth=None)

    print("Model gets Created succesfully")

    model.fit(X_train,Y_train)

    print("Model tranaied sucssfully")

    #####################################################
    # Step 2 : Predication X_test with Actual values
    ####################################################
    
    print(Border)
    print("Step 2 : Predication X_test with Actual values ")
    print(Border)

    Y_pred = model.predict(X_test)        #  ----> Use for Testing Accu...

    print("Model testing done")

    print("Expected Answer :")
    print(Y_test)

    print("Predicted answer :")
    print(Y_pred)

    print(Border)

    #####################################################
    # Step 3 : Calculate Madel Accuracy
    ####################################################
    
    print(Border)
    print("Step 3 : Calculate Madel Accuracy ")
    print(Border)

    accuracy = accuracy_score(Y_test,Y_pred)
    print("accuracy of model is :", accuracy*100)

    print(Border)

    #####################################################
    # Step 4 : Confusion Matrix
    ####################################################
    
    print(Border)
    print("Step 4 : Confusion Matrix ")
    print(Border)

    print("Confustion matrix")
    cm = confusion_matrix(Y_test,Y_pred)

    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["Negative","Positive"]
    )

    disp.plot(cmap="Blues")
    plt.title("Confusion Matrix")
    plt.show()

    #####################################################
    # Step 5 : Calulating & Comparing (Overfit or underfit)
    ####################################################
    
    print(Border)
    print("Step 5 : Calulating & Comparing (Overfit or underfit) acc ")
    print(Border)
    # Training Prediction
    Y_train_pred = model.predict(X_train)

    # Training Accuracy
    Training_Accuracy = accuracy_score(Y_train,Y_train_pred)

    # Testing Accuracy
    Testing_Accuracy = accuracy_score(Y_test,Y_pred)

    print("Training Accuracy is :",Training_Accuracy*100 , "%")
    print("Testing Accuracy is :",Testing_Accuracy*100, "%")

    diff = Training_Accuracy - Testing_Accuracy
    print("Accuracy Differnce :", diff*100,"%")

    # Check Overfitting / Underfitting
    if(Training_Accuracy < 0.70 and Testing_Accuracy < 0.70 ):
        print("Model is UnderFitting")
    elif(Training_Accuracy > 0.90 and diff > 0.10):
        print("Model is OverFitting")
    else:
        print("Model Performe Well Good fit...")

    print(Border)

    #####################################################
    # Step 6 : Changing max_depth
    ####################################################
    
    print(Border)
    print("Step 6 : Changing max_depth ")
    print(Border)

    print("No Changes After Altering Depth")

    #####################################################
    # Step 7 : Check model Perdication with given data
    ####################################################
    
    print(Border)
    print("Step 7 : Check model Perdication with given data ")
    print(Border)

    Data = {
        "StudyHours" : [6],
        "Attendance" : [85] ,
        "PreviousScore" : [66],
        "AssignmentsCompleted" : [7],
        "SleepHours" : [7]
    }
    Data = pd.DataFrame(Data)
    Data = model.predict(Data)
    if (Data == 1):
        print(" Student is Pass")
    elif(Data == 0):
        print("Student is Fail")

    
def main():
    Student_Perf("student_performance_ml.csv")

if __name__ == "__main__":
    main()
