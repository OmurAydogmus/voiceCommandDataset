# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 17:12:23 2023
@author: omur aydogmus
"""

import matplotlib.pyplot as plt
import librosa
import numpy as np
import soundfile
import os 
from os import path

# librosa icin numppy i downgrade yap   1.21.5        
# import subprocess
# subprocess.call(['ffmpeg', '-i', file, 'ind1.wav'])

gain_noise = 0.5 
dir = <yout path>

# factory noise
noiseFile = dir + '\\factoryNoise.wav'
noise, sr = librosa.load(noiseFile) 
  
file = dir + '\\clippedWAV'
caseNum = len(os.listdir(file))
  
for fol in range(1,caseNum+1):
    Num = len(os.listdir(file + f'\\case{fol}'))
    for cs in range(1,Num+1):

        
        audio_file = file + f'\\case{fol}\\{fol}_{cs}.wav' 
        sound, sr = librosa.load(audio_file, mono=True)
                
        getNoise = np.random.randint(15000, len(noise)-len(sound)-1)
        noisy =  gain_noise * noise[getNoise:getNoise+len(sound)] + sound
        # soundfile.write('F:\speechRecognize\\noisyData\\orginal.wav',sound,sr)
        
        folder = dir + f'\\noisyData_{int(gain_noise*100)}\\case{fol}'
        isExist = os.path.exists(folder)
        if isExist==False:
            os.mkdir(folder)
            
        soundfile.write(folder+f'\\{fol}_{cs}.wav',noisy,sr)
        print(fol,cs)

