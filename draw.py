# -*- coding:utf-8 -*-
from numpy import *
import kNN
import fileLoad
import matplotlib as mpl
import matplotlib.pyplot as plt

x = datingDataMat[900:,0]
y = datingDataMat[900:,1]
plt.plot(x,y,'.')
plt.xlabel(u'年飞行里程数')
plt.ylabel(u'视频游戏所耗时间百分比')
plt.title(u'个人特征信息')
#plt.show()