#encoding=utf-8

import os
import re
import shutil

from fileTool import *

def __readPureTxt(txtFile):
    f = open(txtFile)
    line = f.readline()
    newLine = ''
    if not line:
        print 'read error from ' + txtFile
        return ''
    splits = line.split()
    for i in range(2,len(splits)):
        newLine = newLine + ' ' + splits[i]
        
    # rm the blank one the start and end
    newLine = newLine.strip()
    
    return newLine


def extractingTimit(inDir, outFile):
    
    dstPattern = os.path.join(inDir,  '*/*/*/*.txt')
    txtArray = listDir(dstPattern)
    if os.path.exists(outFile):
        os.remove(outFile)
        print 'file ' + outFile + ' exist and deleted'

    f = open(outFile, 'w')
    def lambdaForMap(x):
        txt = __readPureTxt(x)
        # replace special note
        txt = txt.replace('--', '').replace('''"''','')
        
        if len(txt) == 0:
            exit(3)
        f.write(txt.lower() + '</s>\n')

    map(lambdaForMap, txtArray)

def splitDicLine(dicStr):
    splits = dicStr.split()
    if len(splits) < 2:
        print 'dic line error'
        exit (33)

    retStr = ''
    key = splits[0].lower()
    for i in range(1, len(splits)):
        retStr = retStr + ' ' + splits[i]
    
    return key, retStr.strip()
        
    
def mergeDicts(dic1, dic2, outputDic):
    fullDic = {}
    
    # first merge two dic file
    f1 = open(dic1)
    while 1:
        line = f1.readline()
        if not line:
            break
        
        
        if line.strip()[0] == ';':
            continue

        line = line.replace('  ', ' ')
        line = line.replace('/', '')
        line = line.strip()
        
        key,value = splitDicLine(line)
        value = value.upper()
        fullDic[key] = value

    f2 = open(dic2)
    while 1:
        line = f2.readline()
        if not line:
            break

        if line.strip()[0] == ';':
            continue        

        line = line.replace('  ', ' ')
        line = line.replace('/', '')
        line = line.strip()

        key,value = splitDicLine(line)
        value = value.upper()
        fullDic[key] = value
        
    wf = open(outputDic, 'w')
    # write dic result to file
    for item in fullDic:
        tkey = item.strip()
        tvalue = fullDic[tkey].strip()
        
        wf.write(tkey + ' ' + tvalue + '\n')
    wf.flush()
    wf.close()

def rmPunc(inFile, outFile):
    f = open(inFile)
    of = open(outFile, 'w')
    while 1:
        line = f.readline()
        if not line:
            break
        
        line = re.sub('[^a-zA-Z <>/] ', ' ', line)
        of.write(line)
        
    f.close()
    of.flush()
    of.close()

def genStr4Lm(inStr):
    
    ret = inStr

    # to lower
    ret = ret.lower()
    
    # rm prunc
    ret = re.sub('[^a-zA-Z <>/] ', ' ', ret)

    return ret

def genTxt4Lm(inFile, outFile):
    f = open(inFile)
    of = open(outFile, 'w')
    while 1:
        line = f.readline()
        if not line:
            break
        
        line = genStr4Lm(line)
        of.write(line)
        
    f.close()
    of.flush()
    of.close()
    
def genOOV(dicFile, txtFile, oovFile):
    
    oovF = open(oovFile, 'w')

    # gen dic hash
    dicF = open(dicFile)
    line = ''
    dicTable = {}
    while 1:
        line = dicF.readline()
        if not line:
            break
        splits = line.split()
        dicTable[splits[0].strip()] = '0'

    # txtFile
    txtF = open(txtFile)
    while 1:
        line = txtF.readline()
        if not line:
            break
        splits = line.split()
        for i in range(1, len(splits) - 1):
            if not (splits[i] in dicTable): # dicTable.contains_key(splits[i]):
                oovF.write(splits[i] + '\n')

    oovF.flush()
    oovF.close()

if __name__ == '__main__':
    inDir = '/home/zhangjl/dataCenter/asr/timit'
    outFile = '/home/zhangjl/dataCenter/asr/timit/txtInOne.txt'
    outFile = '/home/zhangjl/dataCenter/lm/engLMData/txtInOne.txt'

    #extractingTimit(inDir, outFile)
    
    dic1 = '/home/zhangjl/dataCenter/asr/timit/timitdic.txt'
    dic2 = '/home/zhangjl/dataCenter/asr/tedlium/cantab-TEDLIUM/cantab-TEDLIUM.dct'
    dstDic = '/home/zhangjl/dataCenter/lm/engLMData/timit.4lm.dic'
    
    mergeDicts(dic1, dic2, dstDic)
'''
    #inFile = '/home/zhangjl/dataCenter/lm/engLMData/timit.txt'
    inFile = '/home/zhangjl/dataCenter/lm/engLMData/timit.txt'
    outFile = '/home/zhangjl/dataCenter/lm/engLMData/timit.lower.txt'
    #transFileLower(inFile, outFile)

    # rm prun from files
    inFile = '/home/zhangjl/dataCenter/lm/engLMData/timit.txt'
    outFile = '/home/zhangjl/dataCenter/lm/engLMData/timit.rmpunc.txt'
    #rmPunc(inFile, outFile)
    
    # gen lm txt file
    inFile = '/home/zhangjl/dataCenter/lm/engLMData/timit.txt'
    outFile = '/home/zhangjl/dataCenter/lm/engLMData/timit.4lm.txt'
    #genTxt4Lm(inFile, outFile)

    # gen oov file
    txtFile = '/home/zhangjl/dataCenter/lm/engLMData/timit.4lm.txt'
    dicFile = '/home/zhangjl/dataCenter/lm/engLMData/timitAndCantab.dic'
    oovFile = '/home/zhangjl/dataCenter/lm/engLMData/oovlist.txt'
    genOOV(dicFile, txtFile, oovFile)

'''
