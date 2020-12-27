x=[[0],[1],[2],[3]]
y=[0,0,1,1]
from sklearn.neighbors import KNeighborsClassifier
neigh=KNeighborsClassifier(n_neighbors=3)
neigh.fit(x,y)
y_pred=neigh.predict([[0.9],[1.1],[2.1],[3.3]])
print("Predicted data: ",y_pred)
#To check accuracy of result
from sklearn.metrics import accuracy_score
print("Accuracy  (%) :",accuracy_score(y,y_pred)*100)
