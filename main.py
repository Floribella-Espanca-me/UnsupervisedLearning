# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

import Kmeans
import pointGeneration
import tester


def main():
    # Use a breakpoint in the code line below to debug your script.
    #exe=pointGeneration.gaussianLabeled(10)
    #exe2=Kmeans.twopointkmeans(exe[0],exe[1],10E-5,11)
    #pointGeneration.printPlotKmeans(exe[0],exe[1],exe[2],exe2[0],exe2[1])

    #tester.kmeansTester(10,10E-5,11)
    #tester.commulativeTester(10,10E-5,10)

    tester.fusionTeste(10)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
