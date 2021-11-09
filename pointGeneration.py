import itertools
import math

import matplotlib . pyplot as plt
import numpy as np
import random

import Kmeans


def gaussian(seed):
    nextseed=seed
    mean = [3, 3]
    cov = [[1, 0], [0, 1]]
    np.random.seed(nextseed)
    a = np.random.multivariate_normal(mean, cov, 500).T
    mean = [-3, -3]
    cov = [[2, 0], [0, 5]]
    b = np.random.multivariate_normal(mean, cov, 500).T
    c = np.concatenate((a, b), axis=1)
    c = c.T
    np.random.shuffle(c)
    c = c.T
    x = c[0]
    y = c[1]
    nextseed=np.random.random()
    #printPlot(x,y)
    return [x,y,nextseed]

def gaussianLabeled(seed):
    nextseed =seed
    np.random.seed(nextseed)
    nextseed=np.random.random()
    mean = [3, 3]
    cov = [[1, 0], [0, 1]]
    a = np.random.multivariate_normal(mean, cov, 250)
    agaussian=[]
    for point in a:
        agaussian.append( [point[0],point[1],1])
    mean = [-3, -3]
    cov = [[2, 0], [0, 5]]
    b = np.random.multivariate_normal(mean, cov, 250)
    bgaussian = []
    for point in b:
        bgaussian.append([point[0], point[1], 2])
    dataset=agaussian+bgaussian
    np.random.shuffle(dataset)
    datasetArray=np.array(dataset)
    dataset=datasetArray.T
    x=dataset[0]
    y=dataset[1]
    label=dataset[2]
    #printlabeledPlot(x,y,label)
    return[x,y,label,nextseed]


def printlabeledPlot(x,y,label):
    for index in range(len(x)):
        if label[index] == 1:
            plt.plot(x[index], y[index],'b+')
        else:
            plt.plot(x[index], y[index], 'r+')

    plt.show()

def printPlotKmeans(x,y,label,r1,r2):
    for index in range(len(x)):
        if label[index] == 1:
            plt.plot(x[index], y[index],'b+')
        else:
            plt.plot(x[index], y[index], 'r+')
    plt.plot(r1[0],r1[1],'go')
    plt.plot(r2[0],r2[1],'go')
    plt.show()

def printPlot(x,y):
    plt.plot(x, y, 'x')
    plt.axis('equal')
    plt.show()

def printR(fpointList,lpointList,datasetx,datasety):
    plt.plot(datasetx, datasety, 'x')
    for x in fpointList:
        plt.plot(x[0],x[1],marker='o',color='red')
    for y in lpointList:
        plt.plot(y[0], y[1], marker='o',color='orangered')
    plt.show()

def printCommulative(pointList,datasetx,datasety):
    plt.plot(datasetx, datasety, 'x')
    for x in pointList:
        plt.plot(x[0],x[1],'ro')
    plt.show()

def printCommulativeWPath(pointList,path,datasetx,datasety):
    plt.plot(datasetx, datasety, 'x')
    for x in pointList:
        plt.plot(x[0],x[1],'ro')
    for y in path:
        plt.plot(y[0],y[1],'rx')
    plt.show()



def closestTwoPoints(datasetx,datasety):
    smallestDistance=math.inf
    indexa=None
    indexb=None
    for pair in itertools.combinations(range(len(datasetx)),2):
        distance=Kmeans.pointDistance(datasetx[pair[0]],datasety[pair[0]],datasetx[pair[1]],datasety[pair[1]])
        if distance<smallestDistance:
            smallestDistance=distance
            indexa=pair[0]
            indexb=pair[1]
    return [indexa,indexb]


def printCommulativeWColorCheme(r1,r2,datasetx,datasety,label):
    for index in range(len(datasetx)):
        distancer1=Kmeans.pointDistance(r1[0],r1[1],datasetx[index],datasety[index])
        distancer2=Kmeans.pointDistance(r2[0],r2[1],datasetx[index],datasety[index])
        if label[index]==1:
            if distancer1<=distancer2:
                plt.plot(datasetx[index],datasety[index],marker='x',color='skyblue')
            else:
                plt.plot(datasetx[index], datasety[index], marker='x', color='plum')
        else:
            if distancer2<=distancer1:
                plt.plot(datasetx[index], datasety[index], marker='x', color='palegreen')
            else:
                plt.plot(datasetx[index], datasety[index], marker='x', color='lightblue')

    plt.plot(r1[0],r1[1],'ro')
    plt.plot(r2[0], r2[1], 'ro')
    plt.show()