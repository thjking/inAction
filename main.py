# -*- coding:utf-8 -*-
from numpy import *
import kNN
import fileLoad
import draw
import matplotlib as mpl
import matplotlib.pyplot as plt

mat = fileLoad.filematrix1('datingTestSet.txt')
draw.draw(mat)
plt.show()