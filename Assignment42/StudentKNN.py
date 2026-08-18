import numpy as np
import math 

Border = '-'*40

def EuclideanDistance(P1,P2):
    #d=sqrt((x2​−x1​)**2+(y2​−y1​)**2) # --> Formula
    Ans = math.sqrt((P1['Study Hours']-P2['Study Hours'])**2+(P1['Attendance']-P2['Attendance'])**2)
    return Ans

def KNNClassifierData():

    Data = [
        {'Study Hours':2,'Attendance':60,'Result':'Fail'},
        {'Study Hours':5,'Attendance':80,'Result':'Pass'},
        {'Study Hours':6,'Attendance':85,'Result':'Pass'},
        {'Study Hours':1,'Attendance':50,'Result':'Fail'}
    ]

    print(Border)
    print("KNN Classifier")
    print(Border)

    for i in Data:
        print(i)

    print(Border)

    return Data

def Predict(X,Y,Data,k=3):
    new_point = {'Study Hours':X,'Attendance':Y}
    
    print("Distances of 3 near points :")
    print(Border)

    for d in Data:
        d['distance'] = EuclideanDistance(d,new_point)

    sorted_data = sorted(Data,key=lambda item :item['distance'])
    nearest = sorted_data[:k]

    for d in nearest:
        print(d)

    print(Border)

    votes = {}
    
    for neighbours in nearest:
        label = neighbours['Result']
        votes[label] = votes.get(label,0)+1
            
    print(Border)
    print("Voting result :")
    print(Border)
    
    for d in votes:
        print("Name :",d,"Number of votes:",votes[d])

    print(Border)
    
    iMax = 0
    Name = ""
    
    for d in votes:
        if(votes[d]>iMax):
            iMax = votes[d]
            Name = d
    print("Result predication is : ", Name)

def main():

    Data = KNNClassifierData()

    print("Enter Study Hours :")
    X = int(input())

    print("Enter Attendance :")
    Y = int(input())

    print("Enter K (1/2/3) :")
    n = int(input())

    Predict(X,Y,Data,k=n)


if __name__ == "__main__":
    main()