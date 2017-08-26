# -*- coding:utf-8 -*-
from numpy import *
import kNN
import fileLoad
import draw
import matplotlib as mpl
import matplotlib.pyplot as plt

mat,lab = fileLoad.filematrix0('datingTestSet.txt')
print mat,lab