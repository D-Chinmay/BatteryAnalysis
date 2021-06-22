import numpy as np
import matplotlib.pyplot as plt
import json
import os.path as ospath

bdExists = ospath.exists('batterydict.txt')
if str(bdExists) == 'True':
    batteryDict = {}
    with open("batterydict.txt", "r") as bdRead:
        batteryDict = eval(bdRead.read())
    batteryDict.close
else:
    batteryDict = {'li-ion':'2.5', 'li-polymer':'5', 'low nimh':'0.25','pb-acid':'5','ni-cd':'17.5','nimh':'30'}
plt.style.use('ggplot')#Uses ggplot style

#Input for battery type
graphNumber = input("How many battery type shall be graphed? ")
Battery_input = input("Input battery type: ")

batteryTrue = batteryDict.get(Battery_input,"no-data")
if batteryTrue != "no-data":
    discharge = batteryTrue
    batteryName = Battery_input
else:
    dataQuery = input("Battery not found, would you like to input data? ")
    #Adding data
    if dataQuery == 'True':
        addType = input("Input battery type")
        addRate = input("Input battery discharge rate")
        batteryDict.update({addType:addRate})
        with open("batterydict.txt","w") as bdWrite:
            bdWrite.write(json.dumps(batteryDict))
            bdWrite.close

def dbGraph():
    time = input("How many months should be graphed? ")
    t = np.linspace(0,int(time),num=1000)
    Discharge = float(discharge)
    dischargeFrac = (100-Discharge)/100
    v_battery = 100*dischargeFrac**t

    

    print('After three months:',100*dischargeFrac**3)
    print('After twelve months:',100*dischargeFrac**12)

    #Graph Shit
    plt.plot(t,v_battery,label='Battery Charge')
    plt.ylim(bottom=0)
    plt.xlabel('Time (Months)')
    plt.xlabel('Charge Percentage')
    plt.title('Battery charge over 1 year')
    plt.legend()
    plt.show()

dbGraph()