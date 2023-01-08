#7
import numpy as np
from sklearn import datasets 
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.mixture import GaussianMixture 
import matplotlib.pyplot as plt

iris = datasets.load_iris() 

plt.figure(figsize=(14,7))
colormap=np.array(['red','lime','black'])

plt.subplot(1,3,1)
plt.title('Real')
plt.scatter(iris.data[:,2],iris.data[:,3],c=colormap[iris.target])

model =KMeans(n_clusters=3,random_state=0).fit(iris.data) 
plt.subplot(1,3,2)
plt.title('KMeans')
plt.scatter(iris.data[:,2],iris.data[:,3],c=colormap[model.labels_])
print('K-Mean: ',metrics.accuracy_score(iris.target,model.labels_))

model2 = GaussianMixture(n_components=3,random_state=0).fit(iris.data)
model2_labels=model2.predict(iris.data)
plt.subplot(1,3,3)
plt.title('GMM Classification')
plt.scatter(iris.data[:,2],iris.data[:,3],c=colormap[model2_labels])
plt.show()
print('EM Algorithm:',metrics.accuracy_score(iris.target,model2_labels))
