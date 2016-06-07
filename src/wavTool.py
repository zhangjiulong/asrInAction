#coding=utf-8
import os
import re
import sys
import wave

def getWavLen(wavName):
    try:
        f = wave.open(wavName, "rb")
        
        params = f.getparams()
        frameRate = params[2]
        nFrames = params[3]
        wavLen = (nFrames * 1.0) / (frameRate * 1.0)
    except:
        info=sys.exc_info() 
        print info
        return -1.0
    return wavLen

def getWavDirSounds(dirStr, listPattern = '.*'):

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


def getAllSoundsLong(dir):
    wavList = getWavDirSounds(dir, '.*wav')
    totalLen = 0.0

    for item in wavList:
        tmpLen = getWavLen(item)
        totalLen += tmpLen

    return totalLen

if __name__ == '__main__':
    
    dir = '/home/zhangjl/dataCenter/asr/td/vx/vx'
    #ret = getWavDirSounds(dir, '*.wav')
    #print len(ret)
    ret = getAllSoundsLong(dir)
    print 'total len is ' + str(ret)
