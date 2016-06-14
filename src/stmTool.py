#coding=utf-8
import codecs
import os
import re

from fileTool import *

def collectTxt(dir, saveFile):
    sf = codecs.open(saveFile, 'w', 'utf-8')
    stmList = listDirWithPattern(dir, '.*\.stm')
    for item in stmList:
        f = codecs.open(item, encoding='utf-8')
        while 1:
            line = f.readline()
            if not line:
                break
                
            splits = line.split()
            txt = ' '.join(splits[6:])
            #txt = txt.replace('[NOISE] ', '')
            txt = re.sub(r'\[NOISE\] ?', '', txt)
            txt = txt.strip()
            if len(txt) <= 0:
                continue
            
            sf.write(txt + '\n')
        
if __name__ == '__main__':
    stmDir = '/home/zhangjl/dataCenter/asr/td/vx/stm'
    saveFile = '/home/zhangjl/dataCenter/lm/td/td.txt'
    collectTxt(stmDir, saveFile)
    
