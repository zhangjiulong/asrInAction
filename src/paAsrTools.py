#coding=utf-8

import math

def calMels(freq):
    ret = 1125.0 * math.log(1.0 + freq / 700.0, math.e)
    return ret

def calHz(mel):
    ret = 700.0 * (math.exp(mel / 1125.0) - 1.0)
    return ret

def calBin(hz):
    ret = math.floor((256.0 + 1.0) * hz/ 8000) # need to check 256 why not 512 
    return ret
