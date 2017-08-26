# -*- coding:utf-8 -*-
from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def classify0(inX,dataSet,labels,k):
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
 
def file2matrix(filename):      #从文本解析数据
    fr = open(filename)
    arrayOLines = fr.readlines()        #按行读取
    numberOfLines = len(arrayOLines)    #保存行数
    returnMat = zeros((numberOfLines,3))#依据文本内数据创建numberOfLines行3列训练样本的矩阵（numpy内的zeros数组，不同于python自带数组）
    classLabelVector = []               #创建类标签矩阵
    index = 0
    for line in arrayOLines:            #按行处理文本数据
        line = line.strip()             #去除空格
        listFromLine = line.split('\t') #去除制表符
        print listFromLine
        returnMat[index,:] = listFromLine[0:3]      #将前三元素赋予训练样本矩阵之一行
        classLabelVector.append(listFromLine[-1])   #将最后一个元素赋予标签列表
        index += 1                                  #训练矩阵行数加一，为之后赋值
    return returnMat,classLabelVector               #返回训练矩阵与标签列表