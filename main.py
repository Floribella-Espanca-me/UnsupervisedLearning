# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

import Kmeans
import pointGeneration
import tester


def main():

    #exercicio 1
    tester.kmeansTester(10,10E-4,13)

    #exercicio 2
    #tester.commulativeTester(30,1,11)

    #exericicio 3
    #tester.fusionTester(10)

    #exercicio 4
    #tester.DBScanTester(0.75,7,10)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
