# -*- coding:utf-8 -*-
from numpy import *
import kNN
import fileLoad
import matplotlib as mpl
import matplotlib.pyplot as plt

def draw(returnMat):
    i = 0
    j = 0
    k = 0
    n = returnMat.shape[1]
    index1 = 0
    index2 = 0
    index3 = 0
    for key in returnMat:
        if key[n-1] == 1:
            i += 1
        elif key[n-1] == 2:
            j += 1
        elif key[n-1] == 3:
            k += 1
    plot1 = zeros((i,n - 2))
    plot2 = zeros((j,n - 2))
    plot3 = zeros((k,n - 2 ))
    for key in returnMat:
        if key[n-1] == 1:
            plot1[index1:] = key[0:2]
            index1 += 1
        elif key[n-1] == 2:
            plot2[index2:] = key[0:2]
            index2 += 1
        elif key[n-1] == 3:
            plot3[index3:] = key[0:2]
            index3 += 1
    plt.plot(plot1[:,0],plot1[:,1],'.',label=u'低吸引力')
    plt.plot(plot2[:,0],plot2[:,1],'.',label=u'中吸引力')
    plt.plot(plot3[:,0],plot3[:,1],'.',label=u'高吸引力')
    plt.xlabel(u'年飞行里程数')
    plt.ylabel(u'视频游戏所耗时间百分比')
    plt.title(u'个人特征信息')
    plt.legend(loc='upper left')
    #plt.show()