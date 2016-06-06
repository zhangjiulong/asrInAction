#coding=utf-8
import os 
import glob

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
            
