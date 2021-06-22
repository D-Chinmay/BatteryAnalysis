import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')#Uses ggplot style

'''c_input = input("Input capacitance")
v_input = input("Input voltage")
r_input = input("Input resistance")'''

c = 10**(-6)*100 #float(c_input) #Capacitance = 100 x 10^(-6)
v = 5 #float(v_input)
r = 2000 #float(r_input)

t = np.linspace(0,1,num=1000)

#Overall derived formula: I(t) = (v/r)*e^((-1/RC)*t)

q = c*v*(1-np.exp((-1/(r*c))*t))
i = (v/r)*np.exp((-1/(r*c))*t)
v_battery = v*(10**(-4))-q

plt.plot([0,t[-1]],[c*v,c*v],label='Charge peak')
plt.plot(t,q,label='Charge of the capacitor (C)')
plt.plot(t,i,label='Current (A)')
plt.plot(t,v_battery,label='Battery Charge')

print('Tau',1/(r*c))
print('Peak current (A)',v/r)

plt.xlabel('Time (s)')
plt.title('RC circuit')
plt.legend()
plt.show()