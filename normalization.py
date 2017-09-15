# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 19:07:14 2017

@author: Acer
"""
from numpy import *
import operator

def normal(data):
    # 获取数据矩阵每列最小值，返回列表形式
    minVals = data.min(0)
    # 最大值，同上
    maxVals = data.max(0)
    ranges = maxVals - minVals
    # 依原数据行列创建归一化数据矩阵
    normData = zeros(shape(data))
    m = data.shape[0]
    normData = data - tile(minVals,(m,1))
    normData = normData / tile(ranges,(m,1))
    return normData, ranges, minVals