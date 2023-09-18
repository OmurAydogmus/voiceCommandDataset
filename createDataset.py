# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 15:20:13 2023
@author: omur aydogmus
"""
 
import os  
import pyttsx3
 
from os import path
import numpy as np
 

engine = pyttsx3.init()
 
# """ RATE"""
# engine.setProperty('rate', 125)     # setting up new voice rate
# rate = engine.getProperty('rate')   # getting details of current speaking rate

# """VOLUME"""
# engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

# """VOICE"""
# voices = engine.getProperty('voices')       #getting details of current voice
# #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

# run motor {number} at {per}% 
# text = [f'run motor {number} at {per}%']
 
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
 
def genS(tx,nr,sy,rt,gr,ph,ss,per):
    engine.setProperty('rate', rt)     # setting up new voice rate
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[gr].id)  #changing index, changes voices. o for male 1 for famale
    number =  nr 
    print(tx,nr)
    if tx==0:
        text = [f'enable motor {number}',
                  f'start motor {number}',
                  f'activate motor {number}',
                  f'enable {ordinal(number)} motor',
                  f'start {ordinal(number)} motor ',
                  f'activate {ordinal(number)} motor'] 
    elif tx==1:    
        text = [f'disable motor {number}',
                  f'stop motor {number}',
                  f'deactivate motor {number}',
                  f'disable {ordinal(number)} motor',
                  f'stop {ordinal(number)} motor ',
                  f'deactivate {ordinal(number)} motor'] 
    else:
        text = [f'run motor {number} at {per}%',
                f'run {ordinal(number)} motor at {per}%',
                f'adjust motor {number} speed to {per}%',
                f'set motor {number} capacity to {per}%',
                f'set {ordinal(number)} motor capacity to {per}%',
                f'operate motor {number} at {per}%']
         
    engine.say(f'<pitch middle="{ph}">{text[sy]}!</pitch>')
    folderInx = int(nr+10*tx+(int(per>0)*10*(per-25)/25))
    folder = f'D:\\Works_new\\PLCSound\\fullData\\wav\\case{folderInx}'
    isExist = os.path.exists(folder)
    if isExist==False:
        os.mkdir(folder)
    print(f'{text[sy]}')  
    # engine.save_to_file('deneme.wav') 
    engine.save_to_file(f'<pitch middle="{ph}">{text[sy]}!</pitch>', f'{folder}\\{folderInx}_{ss}.wav') 
    engine.runAndWait()
    engine.stop()
    
for tx in range(2):
    for nr in range(1,11):  
        ss = 0
        for sy in range(6):
            for rt in range(80,140,20):
                for gr in range(2):
                    for ph in range(-8,11,4):
                        ss += 1  
                        genS(tx,nr,sy,rt,gr,ph,ss,0) 
                        # print(f'{ss}______N{nr}_T{tx}_S{sy}_R{rt}_G{gr}_P{ph}')         
         
tx = 2
for per in range(25,125,25):  
    for nr in range(1,11):  
        ss = 0
        for sy in range(6):
            for rt in range(80,140,20):
                for gr in range(2):
                    for ph in range(-8,11,4):
                        ss += 1  
                        genS(tx,nr,sy,rt,gr,ph,ss,per) 
                    # print(f'{ss}______N{nr}_T{tx}_S{sy}_R{rt}_G{gr}_P{ph}') 
    
# for tx in range(2):
#     for nr in range(1,11):  
#         ss = 0
#         for sy in range(6):
#             for rt in range(100,175,25):
#                 for gr in range(2):
#                     for ph in range(-10,15,5):
#                         ss += 1  
#                         genS(tx,nr,sy,rt,gr,ph,ss,0) 
#                         # print(f'{ss}______N{nr}_T{tx}_S{sy}_R{rt}_G{gr}_P{ph}')         
         
# tx = 2
# for per in range(25,125,25):  
#     for nr in range(1,11):  
#         ss = 0
#         for sy in range(6):
#             for rt in range(100,175,25):
#                 for gr in range(2):
#                     for ph in range(-10,15,5):
#                         ss += 1  
#                         genS(tx,nr,sy,rt,gr,ph,ss,per) 
#                     # print(f'{ss}______N{nr}_T{tx}_S{sy}_R{rt}_G{gr}_P{ph}') 
