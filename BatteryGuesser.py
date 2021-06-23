import numpy as np
import matplotlib.pyplot as plt
import json
import os.path as ospath
import math



'''bdExists = ospath.exists('batterydict.txt')
if str(bdExists) == 'True':
    batteryDict = {}
    with open("batterydict.txt", "r") as bdRead:
        batteryDict = eval(bdRead.read())
    batteryDict.close
else:
    batteryDict = {'li-ion':'2.5', 'li-polymer':'5', 
    'low nimh':'0.25','pb-acid':'5','ni-cd':'17.5','nimh':'30'}'''

plt.style.use('ggplot')#Uses ggplot style


batteryDict = {'li-ion':'2.5', 'li-polymer':'5', 'low nimh':'0.25',
'pb-acid':'5','ni-cd':'17.5','nimh':'30'}
key_list = list(batteryDict.keys())
rate_list = list(batteryDict.values())

nameDict = {'li-ion':'Lithium-Ion', 'li-polymer':'Lithium-Polymer', 
'low nimh':'Low self-discharge Ni-MH','pb-acid':'Lead-acid','ni-cd':'Nickel-Cadmium',
'nimh':'Nickel-Metal Hydride'}

monthInput = input("How many months shall the battery be isolated for? ")
batteryCharge = input("Input exact percentage of battery charge remaining after " 
+ monthInput + "months: ")
def reverseAnal():
    global dischargeRate
    preLog = float(batteryCharge)/100
    b = np.exp((math.log(float(preLog))/(float(monthInput))))
    '''logFunc = math.log(float(preLog),float(monthInput))
    print(batteryCharge)
    print(preLog)
    print(str(b))'''
    dischargeRate = 100-100*b
    print(dischargeRate)
    
def closest(lst, K):
      
     lst = np.asarray(lst)
     idx = (np.abs(lst - K)).argmin()
     return lst[idx]

reverseAnal()

# Driver code
lst = []
K = float(dischargeRate)

for item in rate_list:
    lst.append(float(item))

x = (closest(lst, K))

rateLoc = lst.index(float(x))
pos = key_list[rateLoc]
trueName = nameDict.get(pos,"sos")
print("The closest battery type to your rate is:",trueName)
#54.0360087663


