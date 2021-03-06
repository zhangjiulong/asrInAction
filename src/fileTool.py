#coding=utf-8
import os 
import glob
import re

def listDir(pathWithPattern):
    return glob.glob(pathWithPattern)

def transFileLower(inFile, outFile):
    f = open(inFile)
    of = open(outFile, 'w')
    while 1:
        line = f.readline()
        if not line:
            break
        
        line = line.lower()
        
        of.write(line)
    of.flush()
    of.close()
            
def listDirWithPattern(dirStr, listPattern = '.*'):

    if not os.path.exists(dirStr):
        print 'dir ' + dirStr + ' not exist'
        return []
 
    openList = []
    closeSet = {}
    pattern = re.compile(listPattern)
    
    ret = []
    closeSet[dirStr] = 1
    openList.append(dirStr)

    while len(openList) > 0:
        tmpDir = openList.pop()
        midList = os.listdir(tmpDir)
        for item in midList:
            fullPath = os.path.join(tmpDir, item)
            if os.path.isdir(fullPath):
                if not item in closeSet:
                    openList.append(fullPath)
                    closeSet[fullPath] = 1
            else:
                match = pattern.match(fullPath)
                if match:
                    ret.append(fullPath)
    
    return ret

if __name__ == '__main__':
    print 'k'
