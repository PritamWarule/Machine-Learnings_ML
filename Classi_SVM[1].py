import numpy as np
x=np.array([[-1,-1],[-2,-1],[1,1],[2,1]])
y=np.array([1,1,2,2])
from sklearn.svm import SVC
clf=SVC()
clf.fit(x,y)
y_predi=clf.predict([[-0.8,-1]])
#accuracy check
from sklearn.metrics import accuracy_score
print(accuracy_score(y,y_predi))