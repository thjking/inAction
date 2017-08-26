# -*- coding:utf-8 -*-
from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def classify0(inX,dataSet,labels,k):    #分类函数（待分类向量，训练数据，标签数据，k值）
    dataSetSize = dataSet.shape[0]      #计算dataSet矩阵行数           
    diffMat = tile(inX, (dataSetSize,1)) - dataSet       #复制inX矩阵后与dataSet矩阵相减
    sqDiffMat = diffMat ** 2    #平方（计算欧式距离的其中一步）
    sqDistances = sqDiffMat.sum(axis = 1)       #累加各维度距离差
    distance = sqDistances ** 0.5       #开根号（欧式距离）
    sortedDistIndicies = distance.argsort()     #对距离进行正排序，返回序列号形式
    classCount = {}
    for i in range(k):      #依照K值对距离最近类别进行计数
        voteIlabel = labels[sortedDistIndicies[i]]      #获取类别
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1       #创建以类别为关键字的字典，值为类别所属次数并随循环不断更新
    sortedClassCount = sorted(classCount.iteritems(),
    key = operator.itemgetter(1),reverse = True)        #对上述字典进行逆排序
    return sortedClassCount[0][0]       #返回次数最多的类别
 