#coding=utf-8
import os
import shutil
from fileTool import *
from BaseFormatConvertor import BaseFormatConvertor
from paAsrTools import * 

class Td2TedliumFormat(BaseFormatConvertor):

    def __init__(self, srcDir, dstDir):
        self.__srcDir = srcDir
        self.__dstDir = dstDir
    
    def __getBaseNameFromPath(self, x):
        ret = x.split('/')[-2] + '_' + os.path.splitext(x.split('/')[-1])[0]
        return ret

        
    def __readPureTxt(self, txtFile):
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
            

    def __genStmContent(self, txtFile):
        pathBase = os.path.dirname(txtFile)
        wavBaseName = self.__getBaseNameFromPath(txtFile)

        wavChannel = 'A'
        sexAndSpeakerID = os.path.basename(pathBase)
        sex = sexAndSpeakerID[0]
        speakerID = sexAndSpeakerID[1:]
        begingTime = 0.0
        endTime = getWavLen(txtFile.replace('.txt', '.wav'))
        if endTime < 0.0:
            print 'processing file ' + txtFile.replace('.txt', '.wav') + ' error'
            exit(-1)

        if sex == 'f':
            label = '<o,f0,' + 'female' + '>'
        else:
            label = '<o,f0,' + 'male' + '>'

        transcript = self.__readPureTxt(txtFile)
        transcript = transcript + '\n'
        
        stmStr = wavBaseName + ' ' + wavChannel + ' ' + speakerID + ' ' + str(begingTime) + ' ' + str(endTime) + ' ' + label + ' ' + transcript
        return stmStr
        
        

    
    def convert(self):
            
        # list all the wav file
        allSets = ['train', 'test']
        for set in allSets:
            wavPath = os.path.join(self.__dstDir, set, "wav")
            stmPath = os.path.join(self.__dstDir, set, "stm")
            def innerProcessor(txtFile):
                stmStr = self.__genStmContent(txtFile)
                #stmBaseName = os.path.splitext(os.path.basename(txtFile))[0]
                stmBaseName = self.__getBaseNameFromPath(txtFile)
                stmFile = os.path.join(stmPath, stmBaseName + '.stm')
                wf = open(stmFile, 'w')
                wf.write(stmStr)
                wf.close()

            # create wav path
            if not os.path.exists(wavPath):
                os.makedirs(wavPath)
            else :
                shutil.rmtree(wavPath)
                #os.removedirs(wavPath)
                os.makedirs(wavPath)


            # create stm path
            if not os.path.exists(stmPath):
                os.makedirs(stmPath)
            else :
                shutil.rmtree(stmPath)
                #os.removedirs(stmPath)
                os.makedirs(stmPath)

            # list all wav files
            dstPattern = os.path.join(self.__srcDir, set + '/*/*/*.wav')
            wavArray = listDir(dstPattern)
            
            # copy wav file to wav 
            map(lambda x: shutil.copy(x, os.path.join(wavPath, self.__getBaseNameFromPath(x) + '.wav')), wavArray)

            newWavArray = map(lambda x: x.replace('.wav', '.txt') , wavArray)
            map(innerProcessor, newWavArray)
            
        
        print 'covert over'

if __name__ == '__main__':
#    timitConvotor = Timit2TedliumFormat('/home/zhangjl/dataCenter/asr/timit', '/home/zhangjl/dataCenter/asr/timitTedFormat')
#    timitConvotor.convert()
    
