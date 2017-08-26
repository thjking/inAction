# -*- coding:utf-8 -*-
import kNN
import matplotlib
import matplotlib.pyplot as plt

datingDataMat,datingLabels = kNN.file2matrix('datingTestSet.txt')
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
plt.show()