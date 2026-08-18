import numpy as np
import math 

Border = '-'*40

def EuclideanDistance(P1,P2):
    #d=sqrt((x2​−x1​)**2+(y2​−y1​)**2) # --> Formula
    Ans = math.sqrt((P1['X']-P2['X'])**2+(P1['Y']-P2['Y'])**2)
    return Ans

def KNNClassifierData():

    Data = [
        {'point':'A','X':1,'Y':2,'label':'Red'},
        {'point':'B','X':2,'Y':3,'label':'Red'},
        {'point':'C','X':3,'Y':1,'label':'Blue'},
        {'point':'D','X':6,'Y':5,'label':'Blue'}
    ]

    print(Border)
    print("KNN Classifier")
    print(Border)

    for i in Data:
        print(i)

    print(Border)

    return Data

def Predict(X,Y,Data,k=3):
    new_point = {'X':X,'Y':Y}

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
        label = neighbours['label']
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
    print("Final predication is : ", Name)

def main():

    Data = KNNClassifierData()

    print("Enter Co-ordinates of Point X :")
    X = int(input())

    print("Enter Co-ordinates of Point Y :")
    Y = int(input())

    print("Enter K :")
    n = int(input())

    Predict(X,Y,Data,k=n)


if __name__ == "__main__":
    main()