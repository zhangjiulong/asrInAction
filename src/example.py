from features import mfcc
from features import logfbank
import scipy.io.wavfile as wav

(rate,data) = wav.read("demo.wav")
mfcc_feat = mfcc(data,rate)
fbank_feat = logfbank(data,rate)

print fbank_feat[1:3,:]
