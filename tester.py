import Kmeans
import pointGeneration


def kmeansTester(numberOfRuns,alpha,seed):
    nextseed=seed
    exe = pointGeneration.gaussianLabeled(nextseed)
    nextseed = exe[3]
    exe2=Kmeans.twopointkmeans(exe[0],exe[1],alpha,numberOfRuns,nextseed)
    pointGeneration.printR(exe2[0],exe2[1],exe[0],exe[1])


def commulativeTester(numberOfRuns,alpha,seed):
    nextseed = seed
    exe = pointGeneration.gaussianLabeled(nextseed)
    nextseed = exe[3]
    exe2 = Kmeans.accumulativekmeans(exe[0],exe[1],alpha,numberOfRuns,nextseed)
    pointGeneration.printCommulativeWPath([exe2[2],exe2[3]],exe2[0],exe[0],exe[1])
    pointGeneration.printCommulativeWColorCheme(exe2[2],exe2[3],exe[0],exe[1],exe[2])

def fusionTester(seed):
    nextseed = seed
    exe = pointGeneration.gaussianLabeled(nextseed)
    nextseed = exe[3]
    Kmeans.fusionPoint(exe[0],exe[1])

def DBScanTester(epsilon,minimumpoints,seed):
    exe=pointGeneration.gaussianLabeled(seed)
    exe2=Kmeans.DBScan(exe[0],exe[1],epsilon,minimumpoints)
    pointGeneration.printClusterList(exe[0],exe[1],exe2[0],exe2[1],seed)