#-------------------------------------------------------------------------------
# Name:        Acetone
# Purpose:     Thermophysical properties at saturation for acetone
#
# Author:      user
#
# Created:     29/05/2023
# Copyright:   (c) user 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#lets say log (Prop) is lprop

#For acetone
# For Pv saturation Pressure
import math
import matplotlib.pyplot as plt

e=math.exp(1)

Temp_array=[-40,-20,0,20,40,60,80,100,120,140]
Pv_array=[]

i=0

while i<10:
    T=Temp_array[i]
    a0=-2.3250
    a1=5.4550*(10**-2)
    a2=-2.0375*(10**-4)
    a3=-1.8017*(10**-6)
    a4=3.4981*(10**-8)
    a5=-1.3904*(10**-10)
    lPv=a0+a1*T+a2*(T**2)+a3*(T**3)+a4*(T**4)+a5*(T**5)
    Pv=e**lPv
    Pv_array.append(Pv)
    i=i+1

print("Saturation Pressure in 10^6 Pa")
print(Pv_array)

plt.plot(Temp_array,Pv_array)
plt.xlabel('Temperature')
plt.ylabel('Saturation Pressure')
plt.title('Acetone')
#plt.show()


# hlv is latent heat
hlv_array=[]

i=0

while i<10:
    T=Temp_array[i]
    a0=6.3491
    a1=-2.7168*(10**-3)
    a2=2.9398*(10**-5)
    a3=-1.2474*(10**-8)
    a4=-4.0319*(10**-9)
    a5=1.8757*(10**-11)
    lhlv=a0+a1*T+a2*(T**2)+a3*(T**3)+a4*(T**4)+a5*(T**5)
    hlv=e**lhlv
    hlv_array.append(hlv)
    i=i+1

print("Latent heat in KJ/Kg:")
print(hlv_array)

plt.plot(Temp_array,hlv_array)
plt.xlabel('Temperature')
plt.ylabel('latent heat')
plt.title('Acetone')
#plt.show()




# Rol is liquid density
Rol_array=[]

i=0

while i<10:
    T=Temp_array[i]
    a0=6.7037
    a1=-1.6696*(10**-3)
    a2=1.0073*(10**-6)
    a3=1.2383*(10**-7)
    a4=-2.1854*(10**-9)
    a5=8.5364*(10**-12)
    lRol=a0+a1*T+a2*(T**2)+a3*(T**3)+a4*(T**4)+a5*(T**5)
    Rol=e**lRol
    Rol_array.append(Rol)
    i=i+1
print("Liquid Density in Kg/m^3:")
print(Rol_array)

plt.plot(Temp_array,Rol_array)
plt.xlabel('Temperature')
plt.ylabel('liquid density')
plt.title('Acetone')
#plt.show()



# Rov is vapor density
Rov_array=[]

i=0

while i<10:
    T=Temp_array[i]
    a0=-1.3402
    a1=4.2408*(10**-2)
    a2=-1.7210*(10**-4)
    a3=2.1825*(10**-6)
    a4=-2.1680*(10**-8)
    a5=7.5011*(10**-11)
    lRov=a0+a1*T+a2*(T**2)+a3*(T**3)+a4*(T**4)+a5*(T**5)
    Rov=e**lRov
    Rov_array.append(Rov)
    i=i+1
print("Vapor Density in Kg/m^3:")
print(Rov_array)

plt.plot(Temp_array,Rov_array)
plt.xlabel('Temperature')
plt.ylabel('vapor density')
plt.title('Acetone')
#plt.show()


# Muv is vapor viscocity
Muv_array=[]

i=0

while i<10:
    T=Temp_array[i]
    a0=4.3519
    a1=2.6016*(10**-3)
    a2=-3.5279*(10**-6)
    a3=2.1574*(10**-7)
    a4=-3.5172*(10**-9)
    a5=1.3856*(10**-11)
    lMuv=a0+a1*T+a2*(T**2)+a3*(T**3)+a4*(T**4)+a5*(T**5)
    Muv=e**lMuv
    Muv_array.append(Muv)
    i=i+1
print("Vapor Viscoity in 10^-6 N-s/m^2")
print(Muv_array)

plt.plot(Temp_array,Muv_array)
plt.xlabel('Temperature')
plt.ylabel('vapor viscocity')
plt.title('Acetone')
#plt.show()


# Kl is liquid thermal conductivity
Kl_array=[]

i=0

while i<10:
    T=Temp_array[i]
    a0=-1.6958
    a1=-1.1504*(10**-3)
    a2=1.2496*(10**-5)
    a3=-3.0675*(10**-7)
    a4=2.9341*(10**-10)
    a5=4.9935*(10**-12)
    lKl=a0+a1*T+a2*(T**2)+a3*(T**3)+a4*(T**4)+a5*(T**5)
    Kl=e**lKl
    Kl_array.append(Kl)
    i=i+1
print("Liquid Thermal Conductivity in W/m-k:")
print(Kl_array)

plt.plot(Temp_array,Kl_array)
plt.xlabel('Temperature')
plt.ylabel('liquid thermal conductivity')
plt.title('Acetone')
#plt.show()


# Kv is vapor thermal conductivity
Kv_array=[]

i=0

while i<10:
    T=Temp_array[i]
    a0=-4.6467
    a1=7.1871*(10**-3)
    a2=-2.0976*(10**-5)
    a3=4.6070*(10**-7)
    a4=-5.4286*(10**-9)
    a5=1.9213*(10**-11)
    lKv=a0+a1*T+a2*(T**2)+a3*(T**3)+a4*(T**4)+a5*(T**5)
    Kv=e**lKv
    Kv_array.append(Kv)
    i=i+1
print("Vapor Thermal Conductivity in W/m-k:")
print(Kv_array)

plt.plot(Temp_array,Kv_array)
plt.xlabel('Temperature')
plt.ylabel('vapor thermal conductivity')
plt.title('Acetone')
#plt.show()


# Sl is vapor liquid surface tension
Sl_array=[]

i=0

while i<10:
    T=Temp_array[i]
    a0=3.2514
    a1=-3.9116*(10**-3)
    a2=-1.0745*(10**-5)
    a3=-4.2728*(10**-7)
    a4=4.4000*(10**-9)
    a5=-1.7122*(10**-11)
    lSl=a0+a1*T+a2*(T**2)+a3*(T**3)+a4*(T**4)+a5*(T**5)
    Sl=e**lSl
    Sl_array.append(Sl)
    i=i+1
print("Liquid Surface Tension in 10^-3 N/m:")
print(Sl_array)

plt.plot(Temp_array,Sl_array)
plt.xlabel('Temperature')
plt.ylabel('liquid surface tension')
plt.title('Acetone')
#plt.show()



# Cpl is liquid specific heat
Cpl_array=[]

i=0

while i<10:
    T=Temp_array[i]
    a0=7.4631*(10**-1)
    a1=1.0064*(10**-3)
    a2=6.3091*(10**-6)
    a3=3.0226*(10**-8)
    a4=-5.0475*(10**-10)
    a5=2.2060*(10**-12)
    lCpl=a0+a1*T+a2*(T**2)+a3*(T**3)+a4*(T**4)+a5*(T**5)
    Cpl=e**lCpl
    Cpl_array.append(Cpl)
    i=i+1
print("Liquid Specific heat in KJ/Kg-K:")
print(Cpl_array)

plt.plot(Temp_array,Cpl_array)
plt.xlabel('Temperature')
plt.ylabel('liquid specific heat')
plt.title('Acetone')
#plt.show()



# Cpv is vapor specific heat
Cpv_array=[]

i=0

while i<10:
    T=Temp_array[i]
    a0=1.9452*(10**-1)
    a1=2.2900*(10**-3)
    a2=-8.6330*(10**-7)
    a3=-2.0672*(10**-8)
    a4=1.9250*(10**-10)
    a5=6.5969*(10**-13)
    lCpv=a0+a1*T+a2*(T**2)+a3*(T**3)+a4*(T**4)+a5*(T**5)
    Cpv=e**lCpv
    Cpv_array.append(Cpv)
    i=i+1
print("Vapor Specific heat in KJ/Kg-k:")
print(Cpv_array)

plt.plot(Temp_array,Cpv_array)
plt.xlabel('Temperature')
plt.ylabel('vapor specific heat')
plt.title('Acetone')
#plt.show()

print('Final Table:')

array = [['T', 'Pv', 'hlv', 'Rol', 'Rov', 'Muv', 'Kl', 'Kv', 'Sl', 'Cpl', 'Cpv']]

for i in range(10):
    row = [Temp_array[i], Pv_array[i], hlv_array[i], Rol_array[i], Rov_array[i], Muv_array[i], Kl_array[i]]
    if(i==0):
        row.insert(7,'-')
    if i != 0:
        row.insert(7, Kv_array[i])
    row.extend([Sl_array[i], Cpl_array[i], Cpv_array[i]])
    array.append(row)

for i in range(11):
    for j in range(len(array[i])):
        print(array[i][j], end="   ")
    print()

sonic_array=[]

for i in range(10):
    x=Pv_array[i]*Rov_array[i]
    y=pow(x,0.5)
    sonic_array.append(0.474*hlv_array[i]*y)
print("Sonic Limit")
print(sonic_array)
plt.plot(Temp_array,sonic_array)
plt.xlabel('Temperature')
plt.ylabel('sonic heat')
plt.title('Acetone')
plt.grid(axis="both")
plt.show()

rv=0.00457
leff=0.381

boiling_array=[]
le=0.127
keff=393
ri=0.005941
DPcm=86.2
#assume Tv= 66 degrree C as bp of acetone is 56.5
Tv=340
for i in range(10):
    calc=((2*(22/7)*le*keff*Tv)/(hlv_array[i]*Rov_array[i]*math.log((ri/rv), 2.71828)))*((2*Sl_array[i]/(2.54*(10**-6)))-(2*Sl_array[i]/0.000021))
    boiling_array.append(calc)

print("Boiling limit of the Wick")
print(boiling_array)
plt.plot(Temp_array,boiling_array)
plt.xlabel('Temperature')
plt.ylabel('Boiling QbEvaporator')
plt.title('Acetone')
plt.grid(axis="both")
plt.show()

Mul_array=[0.8,0.5,0.395,0.323,0.269,0.226,0.192,0.170,0.148,0.132]
d0=0.00127
dl=7.62*(10**-4)
w=4.57*(10**-3)
rv=0.00457
lc=0.127
la=0.254
le=0.127
ri=0.005941
leff=0.005941
rc=4.572*(10**-4)
k=0.0435*(((w*dl)+(dl**0.5))**(0.5)/((2*dl)**0.5))
Aw=2.37*(10**-5)
dc=16  #drag coefficient
rhv=0.00457
Av=6.57*(10**-5)
capillary_array=[]
for i in range(10):
    Fl=(Mul_array[i])/(k*Aw*hlv_array[i]*1000*Rol_array[i])
    Fv=(dc*Muv_array[i])/(2*(rhv**2)*Av*Rov_array[i]*hlv_array[i]*1000)
    Qlcmax=((2*Sl_array[i]*(10**-3))/rc)/(Fl+Fv)
    Ql=Qlcmax/leff
    capillary_array.append(Ql)

print("Capillary limit of the Wick")
print(capillary_array)
plt.plot(Temp_array,capillary_array)
plt.xlabel('Temperature')
plt.ylabel('Capillary Ql')
plt.title('Acetone')
plt.grid(axis="both")
plt.show()

entrainment_array=[]
rhs=0.002154

for i in range(10):
    calc=(22/7)*(rv**2)*hlv_array[i]*(((Sl_array[i]*Rov_array[i])/(2*rhs))**0.5)
    entrainment_array.append(calc)

print("Entrainment limit of the Wick")
print(entrainment_array)
plt.plot(Temp_array,entrainment_array)
plt.xlabel('Temperature')
plt.ylabel('Entrainment Qemax')
plt.title('Acetone')
plt.grid(axis="both")
plt.show()





