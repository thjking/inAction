# -*- coding:utf-8 -*-
from numpy import *
def filematrix0(filename):      #从文本解析数据
    fr = open(filename)
    arrayOfLines = fr.readlines()        #按行读取
    numberOfLines = len(arrayOfLines)    #保存行数
    returnMat = zeros((numberOfLines,3))#依据文本内数据创建numberOfLines行3列训练样本的矩阵（numpy内的zeros数组，不同于python自带数组）
    classLabelVector = []               #创建类标签矩阵
    label = []
    index1 = 0
    index2 =0
    for line in arrayOfLines:            #按行处理文本数据
        line = line.strip()             #去除空格
        listFromLine = line.split('\t') #去除制表符
        if listFromLine[-1] == 'didntLike':
            label.append(1)
        elif listFromLine[-1] == 'smallDoses':
            label.append(2)
        elif listFromLine[-1] == 'largeDoses':
            label.append(3)
        returnMat[index1,:] = listFromLine[0:3]      #将前三元素赋予训练样本矩阵之一行
        classLabelVector.append(label[index2])   #将最后一个元素赋予标签列表
        index1 += 1
        index2 += 1                                  #训练矩阵行数加一，为之后赋值
    return returnMat,classLabelVector               #返回训练矩阵与标签列表

def filematrix1(filename):
    fr = open(filename)
    arrayOfLines = fr.readlines()
    numberOfLines = len(arrayOfLines)
    returnMat = zeros((numberOfLines,4))
    index1 = 0
    index2 = 0
    label = []
    for line in arrayOfLines:
        line = line.strip()
        listFromLine = line.split('\t')
        if listFromLine[-1] == 'didntLike':
            label.append(1)
        elif listFromLine[-1] == 'smallDoses':
            label.append(2)
        elif listFromLine[-1] == 'largeDoses':
            label.append(3)
        returnMat[index1,:3] = listFromLine[0:3]
        returnMat[index1,3:] = label[index2]
        index1 += 1
        index2 += 1

    return returnMat
        
