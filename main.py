# -*- coding:utf-8 -*-
from numpy import *
import kNN
import fileLoad
import draw
import matplotlib as mpl
import matplotlib.pyplot as plt
import normalization as norm

# mat = fileLoad.filematrix1('datingTestSet.txt')
# draw.draw(mat)
# plt.show()
mat,label = fileLoad.filematrix0('datingTestSet.txt')
mat = norm.normal(mat)
kNN.classify0([0.2,0.4,0.6],mat,label,3)