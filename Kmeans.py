import math
import random

import numpy

import pointGeneration


def twopointkmeans(datasetx,datasety,alpha,runs,seed):
    nextseed=seed
    random.seed(nextseed)
    nextseed=random.random()
    randomindex=math.floor(nextseed*len(datasetx))
    r1=[datasetx[randomindex],datasety[randomindex]]
    nextseed= random.random()
    randomindex = math.floor(nextseed * len(datasetx))
    r2=[datasetx[randomindex],datasety[randomindex]]
    while r1==r2:
        nextseed = random.random()
        randomindex = math.floor(nextseed * len(datasetx))
        r2 = [datasetx[randomindex], datasety[randomindex]]
    firstpass=[r1[:],r2[:]]
    lastpoints=[]
    for run in range(runs):
        for index in range(len(datasetx)):
            x=datasetx[index]
            y=datasety[index]
            distance1=pointDistance(x,y,r1[0],r1[1])
            distance2=pointDistance(x,y,r2[0],r2[1])
            if distance1<distance2:
                r1[0]=(1-alpha)*r1[0]+alpha*x
                r1[1] = (1 - alpha) * r1[1] + alpha * y
                if run==0:
                    firstpass.append(r1[:])
            else:
                r2[0] = (1 - alpha) * r2[0] + alpha * x
                r2[1] = (1 - alpha) * r2[1] + alpha * y
                if run==0:
                    firstpass.append(r2[:])
        lastpoints.append(r2[:])
        lastpoints.append(r1[:])
    return [firstpass,lastpoints,nextseed]

def accumulativekmeans(datasetx,datasety,alpha,runs,seed):
    nextseed = seed
    random.seed(nextseed)
    nextseed = random.random()
    randomindex = math.floor(nextseed * len(datasetx))
    r1 = [datasetx[randomindex], datasety[randomindex]]
    nextseed = random.random()
    randomindex = math.floor(nextseed * len(datasetx))
    r2 = [datasetx[randomindex], datasety[randomindex]]
    rList = [r1[:], r2[:]]
    for run in range(runs):
        d1=[0,0]
        d2=[0,0]
        for index in range(len(datasetx)):
            x = datasetx[index]
            y = datasety[index]
            distance1 = pointDistance(x, y, r1[0], r1[1])
            distance2 = pointDistance(x, y, r2[0], r2[1])
            if distance1 < distance2:
                d1[0]=d1[0]+(x-r1[0])
                d1[1] = d1[1]  + (y-r1[1])
            else:
                d2[0] = d2[0]  +(x-r2[0])
                d2[1] = d2[1]  + (y-r2[1])

        r1[0] = r1[0] + (alpha / len(datasetx)) * d1[0]
        r1[1] = r1[1] + (alpha / len(datasetx)) * d1[1]
        r2[0] =r2[0]+(alpha/len(datasetx))*d2[0]
        r2[1] = r2[1] + (alpha / len(datasetx)) * d2[1]
        rList.append(r2[:])
        rList.append(r1[:])
    print('centroid: '+str(r2) )
    print('centroid: '+str(r1))
    return [rList, nextseed,r1,r2]


def fusionPoint(datasetx,datasety):
    originalx=datasetx[:]
    originaly=datasety[:]
    path=[]

    while len(datasetx)>2:

        exe=pointGeneration.closestTwoPoints(datasetx,datasety)
        indexa=exe[0]
        indexb=exe[1]
        newPoint=[(datasetx[indexa]+datasetx[indexb])/2,(datasety[indexa]+datasety[indexb])/2]

        #print('point a: '+str(datasetx[indexa])+'|'+str(datasety[indexa]))
        #print('point b: '+str(datasetx[indexb]) + '|' + str(datasety[indexb]))
        #print('new point: '+str(newPoint))

        datasetx=numpy.delete(datasetx, [indexa,indexb])
        datasety=numpy.delete(datasety, [indexa,indexb])



        datasetx=numpy.append(datasetx,newPoint[0])
        datasety=numpy.append(datasety, newPoint[1])
        path.append([newPoint[0],newPoint[1]])

    pointa=(datasetx[0],datasety[0])
    pointb = (datasetx[1], datasety[1])
    #print(str(pointa))
    #print(str(pointb))
    pointGeneration.printCommulative([pointa,pointb],originalx,originaly)

def DBScan(datasetx,datasety,epsilon,mininumpoints):
    unvisitedindex=range(len(datasetx))
    clusterList=[]
    outliers=[]
    while len(unvisitedindex)>0:
        print(help)


def pointDistance(x1,y1,x2,y2):
    a=(x1-x2)**2
    b=(y1-y2)**2
    return math.sqrt(a+b)

