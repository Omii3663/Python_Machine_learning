import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler


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

    print("Data Set Load Succesfully")

    print(df.head())

    print(Boreder)

    return df

# step 2 : PreProcess Data
#----------------------------------------------------
# Funcation Name : PreProcessData
# Description    : Process Data Its Perform EDA (Cleaing,prepare,Manipulate)
# Input          : Data frame
# output         : Updated Data frame
# Author         : Omkar Ramchandra Kolte
# Date           : 18/08/2026
#-----------------------------------------------------

def PreProcessData(df):

    df = df.drop(columns=['Unnamed: 0'], errors='ignore')

    print(df.head())
    print(Boreder)

    print(f"Null Values in Datasets Are : \n {df.isnull().sum()}")

    print(Boreder)

    le = LabelEncoder()

    df['Wether'] = le.fit_transform(df['Wether'])

    df['Temperature'] = le.fit_transform(df['Temperature'])

    df['Play'] = le.fit_transform(df['Play'])

    scale = StandardScaler()

    print(df.head())

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

    X = df.drop(columns = ['Play'])
    Y = df['Play']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print("Data Spliting Succesfull...")
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


    model = KNeighborsClassifier(n_neighbors=3)

    scale = StandardScaler()
    X_train_scale = scale.fit_transform(X_train)

    model = model.fit(X_train_scale,Y_train)

    print("Model Train Succesfully...")
    print(Boreder)

    return model, scale

# step 5 : Evaluate model
#----------------------------------------------------
# Funcation Name :  TestModel
# Description    :  it perform Model Testing
# Input          :  model, testing data (Fetures & Labels)
# output         :  None
# Author         :  Omkar Ramchandra Kolte
# Date           :  18/08/2026
#-----------------------------------------------------

def TestModel(model,X_test,Y_test,scale):

    X_test_scale = scale.transform(X_test) #--> scale 

    Y_pred = model.predict(X_test_scale)

    accuracy = accuracy_score(Y_test,Y_pred)

    print("accuracy of model is :", accuracy*100, "%")

    print(Boreder)

    print("Confusion Matrix :\n")
    print(confusion_matrix(Y_test,Y_pred))

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
# Input          : "MarvellousInfosystems_PlayPredictor.csv"
# output         :  Data frame
# Author         :  Omkar Ramchandra Kolte
# Date           :  18/08/2026
#-----------------------------------------------------
def main():
    #step 1
    df = LoadData("MarvellousInfosystems_PlayPredictor.csv")

    #step 2
    df = PreProcessData(df)

    #step 3
    X_train, X_test, Y_train, Y_test =SplitData(df)

    #step 4
    model, scale = TrainModel(X_train,Y_train)

    #step 5
    TestModel(model,X_test,Y_test,scale)

    PreserveModel(model, "PlayPredictor")

if __name__ == "__main__":
    main()