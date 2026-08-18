import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

Boreder = '-'*40
# step 1 : Load Data
#----------------------------------------------------
# Funcation Name : LoadData
# Description    : Load the data from csv
# Input          : Name of csv file
# output         : Data frame
# Author         : Omkar Ramchandra Kolte
# Date           : 18/08/2026
#-----------------------------------------------------
def LoadData(DataPath):

    df = pd.read_csv(DataPath)

    print("Data Set Load Succesfully...")

    print(df.head())
    print(Boreder)

    return df

# step 2 : PreProcess Data
#----------------------------------------------------
# Funcation Name : PreProcessData
# Description    : Process Data Its Perform EDA
# Input          : Data frame
# output         : Updated Data frame
# Author         : Omkar Ramchandra Kolte
# Date           : 18/08/2026
#-----------------------------------------------------

def PreProcessData(df):

    print(f"Null Values in Datasets Are :{df.isnull().sum()}")
    print(Boreder)

    before = df.shape[0]

    df.dropna(inplace=True)

    after = df.shape[0]

    print("Rows removed :", before - after)

    print("Shape Of Dataset : ",df.shape)
    print(Boreder)

    print("List Of Colums :\n", list(df.columns))
    print(Boreder)

    print("Satatical report of Dataset :")
    print(df.describe())
    print(Boreder)

    return df

# step 3 : Spliting Data
#----------------------------------------------------
# Funcation Name :  SplitData
# Description    :  Its Perofrom Data Spliting
# Input          :  Data frame
# output         :  4 subset for Traing & Testing
# Author         :  Omkar Ramchandra Kolte
# Date           :  18/08/2026
#-----------------------------------------------------

def SplitData(df):

    # feacturs_col = [
    #     'Alcohol','Malic','acid','Ash','Alcalinity of ash',
    #     'Magnesium','Total phenols','Flavanoids',Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue','OD280/OD315 of diluted wines','Proline'
    # ]
    #X = [feacturs_col]

    X = df.drop(columns = ["Class"])
    Y = df["Class"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
        )

    print("Spliting Data for Training & Testing Compelte")

    print(Boreder)

    return X_train, X_test, Y_train, Y_test

# step 4 : Train the Model
#----------------------------------------------------
# Funcation Name :  TrainModel
# Description    :  it perform Model Training 
# Input          :  Training Fetures & Labels
# output         :  Trained Model
# Author         :  Omkar Ramchandra Kolte
# Date           :  18/08/2026
#-----------------------------------------------------

def TrainModel(X_train,Y_train):

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train) # --> for KNN 
    # print(X_train_scaled)
    #X_test_scaled = scalar.fit_transform(X_test)
    
    DecTree = DecisionTreeClassifier(max_depth=5)

    KNNModel = KNeighborsClassifier(n_neighbors=7)

    DecTree = DecTree.fit(X_train,Y_train)

    KNNModel = KNNModel.fit(X_train_scaled,Y_train)

    print("Model Train Succesfully...")
    print(Boreder)

    return DecTree , KNNModel, scaler

# step 5 : Evaluate model
#----------------------------------------------------
# Funcation Name :  TestModel
# Description    :  it perform Model Testing
# Input          :  model, testing data (Fetures & Labels)
# output         :  None
# Author         :  Omkar Ramchandra Kolte
# Date           :  18/08/2026
#-----------------------------------------------------

def TestModel(DecTree, KNNModel,scaler,X_test,Y_test):

    # scalar = StandardScaler()
    X_test_scaled = scaler.fit_transform(X_test) #--> For KNN

    Y_pred = DecTree.predict(X_test)

    accuracy_DecTree = accuracy_score(Y_test,Y_pred)

    print("Accuracy of DecisionTreeClassifier is :", accuracy_DecTree * 100 , "%")

    print(Boreder)

    Y_pred2 = KNNModel.predict(X_test_scaled)

    accuracy_KNNModel = accuracy_score(Y_test,Y_pred2)

    print("Accuracy of KNeighborsClassifier is :", accuracy_KNNModel * 100 , "%")

    print(Boreder)

    if(accuracy_DecTree > accuracy_KNNModel):
        print("Accuracy of DecisionTreeClassifier High")
    elif(accuracy_KNNModel > accuracy_DecTree):
        print("Accuracy of KNeighborsClassifier High")
    else:
        print("Same Accuracy")

    print(Boreder)
    
# step 6 : Perserve model
#----------------------------------------------------
# Funcation Name :  PreserveModel
# Description    :  it perform Model preservation into .pkl file
# Input          :  Model
# output         :  None
# Author         :  Omkar Ramchandra Kolte
# Date           :  18/08/2026
#-----------------------------------------------------

def PreserveModel(model,filename):
    joblib.dump(model,filename)

    print("Model preserved with name :", filename)

#----------------------------------------------------
# Funcation Name :  main
# Description    :  Entry point function
# Input          : "MarvellousTitanicDataset.csv"
# output         :  Data frame
# Author         :  Omkar Ramchandra Kolte
# Date           :  16/08/2026
#-----------------------------------------------------
def main():
    # Step1 : Load the Data form csv
    df = LoadData("WinePredictor.csv")

    # Step 2: PreProcess Data
    df = PreProcessData(df)

    # Step3 : Spliting For Traning & Testing
    X_train, X_test, Y_train, Y_test = SplitData(df)

    # Step 4 : Train model
    DecTree, KNNModel, scaler = TrainModel(X_train,Y_train)

    # step 5 : Evaluate model
    TestModel(DecTree, KNNModel,scaler,X_test,Y_test)

    # step 6 : Perserve model
    PreserveModel(DecTree, "DecisionTree.pkl")
    PreserveModel(KNNModel, "KNNModel.pkl")
    PreserveModel(scaler, "Scaler.pkl") # -> for same Scales use after

if __name__ == "__main__":
    main()