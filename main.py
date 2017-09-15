# -*- coding:utf-8 -*-
from numpy import *
import kNN
import fileLoad
import draw
import matplotlib as mpl
import matplotlib.pyplot as plt
import normalization as norm

def draw():
    mat = fileLoad.filematrix1('datingTestSet.txt')
    draw.draw(mat)
    plt.show()

def datingClassTest():
    x = 0.10
    Mat, Labels = fileLoad.filematrix0('datingTestSet.txt')
    normMat, ranges, minVals = norm.normal(Mat)
    m = normMat.shape[0]
    numTestVecs = int(m * x)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = kNN.classify0(normMat[i,:],normMat[numTestVecs:m,:],\
                                         Labels[numTestVecs:m],3)
        print "the classifier came back with: %d, the real answer is: %d"\
                                                %(classifierResult,Labels[i])
        if (classifierResult != Labels[i]): errorCount += 1.0
    print "the total error rate is %f" %(errorCount / float(numTestVecs))
        
datingClassTest()
