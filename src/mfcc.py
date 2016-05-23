#coding=utf-8

import math
from paAsrTools import *
lowFre = 300
upFre = 8000

mels = 2834.99
mfLow = calMels(lowFre)
mfUp = calMels(upFre)

#mft = 700.0 * (math.exp(mels / 1125.0) - 1)
print 'mf is ' + str(mfLow)
print 'mf is ' + str(mfUp)

#print 'mft is ' + str(mft)

melArray = (401.25, 622.50, 843.75, 1065.00, 1286.25, 1507.50, 1728.74, 1949.99, 2171.24, 2392.49, 2613.74, 2834.99)
hzArray = (300, 517.33, 781.90, 1103.97, 1496.04, 1973.32, 2554.33, 3261.62, 4122.63, 5170.76, 6446.70, 8000)

#for item in hzArray:
#    print calBin(item)
print calBin(8000)
