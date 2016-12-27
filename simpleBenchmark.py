import subprocess
import sys
import time
import matplotlib.pyplot as plt

def executeTarget(target, count):
    totTime = 0
    for i in range(count):
        startTime = time.time()
        subprocess.call(sys.argv[1])
        endTime = time.time()
        totTime += endTime - startTime
        sys.stdout.write('.')

    return totTime


def makeGraph(timeList):
    x = range(len(timeList))
    y = timeList
    plt.plot(x,y)
    #plt.show()


def saveGraphImage(outFile):
    plt.savefig(outFile)
    plt.close()  #if close plt


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage ( " + sys.argv[0] + " ) : <target program> <count>")
        sys.exit()
    measureNumber = 50 #To do> config file
    outFile = "output_file"
    timeList = []

    for num in range(measureNumber):
        totTime = executeTarget(target = sys.argv[1], count = int(sys.argv[2]))
        timeList.append(totTime)
    print("")

    timeList.sort()
    makeGraph(timeList)
    saveGraphImage(outFile)

    
