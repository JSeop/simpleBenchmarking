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
    print("Makeing Graph Start")
    x = range(len(timeList))
    y = timeList
    plt.plot(x,y)
    #plt.show()
    print("Makeing Graph End")

def saveGraphImage(outFile):
    print("Saving GraphImage Start")
    plt.savefig(outFile)
    plt.close()  #if close plt
    print("Saving GraphImage END")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage ( " + sys.argv[0] + " ) : <target program> <count>")
        sys.exit()
    measureNumber = 50 #To do> config file
    outFile = "output_file"
    timeList = []

    for num in range(measureNumber):
        print("\n%d / %d :%d\n" %(num+1, measureNumber ,num+1))
        totTime = executeTarget(target = sys.argv[1], count = int(sys.argv[2]))
        timeList.append(totTime)

    print("")

    print("sorting")
    timeList.sort()
    makeGraph(timeList)
    saveGraphImage(outFile)

    
