from sklearn.cluster import KMeans
import numpy as np
x=np.array([[1,2],[1,4],[1,0],[10,2],[10,4],[10,0]])
kmeans=KMeans(n_clusters=2, random_state=0).fit(x)
kmeans.labels_
kmeans.predict([[0,0],[12,3]])
print(kmeans.cluster_centers_)