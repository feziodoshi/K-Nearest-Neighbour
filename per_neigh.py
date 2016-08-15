from math import sqrt
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import warnings

style.use('fivethirtyeight')

def k_near(data,predict,k=3):
    if(len(data)>=k):
        warnings.warn("Stupid action")
    euc_distances=[]
    for i in data:
        for ii in data[i]:
            distance=sqrt((ii[0]-predict[0])**2 + (ii[1]-predict[1])**2)
            euc_distances.append([distance,i])
    votes=[]
    for i in sorted(euc_distances)[:k]:
        votes.append(i[1])

    vote_result=Counter(votes).most_common(1)[0][0]
    return vote_result

dataset={'k':[[1,2],[2,3],[3,1]],'y':[[6,5],[7,7],[8,6]]}
new_feature=[5,7]

for i in dataset:
    for ii in dataset[i]:
        plt.scatter(ii[0],ii[1],s=100,color=i)

plt.scatter(new_feature[0],new_feature[1],s=100)
x=k_near(dataset,new_feature)

plt.show()


