#!/usr/bin/env python
# coding: utf-8

# # Data Import and Model
# #### txPower = RSSI at 1m from device
# #### Scanning sessions are imported as scan 1, scan2, ..., scan5.
# #### Each RSSI is transformed into meters.
# #### The mean distance is compared to the real result.
#  
# 

# In[ ]:


import math
import os
import numpy as np
import pandas as pd
from decimal import *
import statistics
from statistics import mean
import matplotlib.pyplot as plt 


# In[ ]:


data =pd.read_csv ('DataT/txPow.csv')
no = data['txPower'].count()
txPower = data['txPower']
# print(txPower)


# In[ ]:


meantx = round(data['txPower'].mean(),2)
print(meantx)


# In[ ]:


df =pd.DataFrame(data, columns = ['txPower'])
# print(df)


# In[ ]:


rssi_data = pd.read_csv('DataT/rssiw.csv')


# In[ ]:


scan1 = rssi_data['scan5']
print(scan1)


# In[ ]:


# n = 1.8967
# Xo = 8.25023
ls =  []


# In[ ]:


def distance_calc():
    for i, row in rssi_data.iterrows():
        ro = row['scan1']
#     print(ro)
        ratio = (ro * 1.0 /meantx)
#     print(ratio)
#         if ratio > 1:
#             ans = math.pow(ratio, 10)
#             print(ans)
#         else:
        ans2 = (0.89976 * math.pow(ratio, 8.25023)) + 0.111
        print(ans2) # distance in meters
        ls.append(ans2)
    


# In[ ]:


distance_calc()


# In[ ]:


print(ls)


# In[ ]:


mean_dist = mean(ls)
print(mean_dist)


# ### Calculate Distances from scenarios.csv

# In[ ]:


scenarios_data = pd.read_csv("DataT/Scenarios.csv")


# In[ ]:


ls_1 = []


# In[ ]:


def distance_calc():
    for i, row in scenarios_data.iterrows():
        if row['Case'] == 2:
            ro_case = row['B3']
            ratio_case = (ro_case * 1.0 /meantx)
            ans2_case = (0.89976 * math.pow(ratio_case, 8.25023)) + 0.111
            print(ans2_case) # distance in meters
#             ls_1 = []
            ls_1.append(ans2_case)


# In[ ]:


for i, row in scenarios_data.iterrows():
    if row['Case'] == 2:
        ro = row['B3']
        print(ro)


# In[ ]:


distance_calc()


# In[ ]:


mean_dist_case = mean(ls_1)
print(mean_dist_case)


# ### Scenario 1 - Same Room

# ### Case 1 

# In[ ]:


x1 = 0
y1 = 0

x2 = -3.80
y2 = 0

x3 = -3.8
y3 = 3.70


# ### Calculated distances

# In[ ]:


r1 = 1.8467580026714963
r2 = 2.4496355555268305
r3 = 3.452710797577248


# In[ ]:


def draw_circle():
    t = np.linspace(0, 2*np.pi, 100)
    x_1 = r1*np.cos(t) + x1
    y_1 = r1*np.sin(t) + y1
    plt.plot(x_1,y_1, 'r')
    x_2 = r2*np.cos(t) + x2
    y_2 = r2*np.sin(t) + y2
    plt.plot(x_2,y_2, 'g')
    x_3 = r3*np.cos(t) + x3
    y_3 = r3*np.sin(t) + y3
    plt.plot(x_3,y_3, 'b')


# In[ ]:


draw_circle()
plt.xlim(-8, 6)
plt.ylim(-4, 8)
plt.title('Test Case 1')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.savefig('Test_Case1.png', dpi = 300)


# In[ ]:


#A function to apply trilateration formulas to return the (x,y) intersection point of three circles
def trackR(x1,y1,r1,x2,y2,r2,x3,y3,r3):
    A = 2*x2 - 2*x1
    B = 2*y2 - 2*y1
    C = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2
    D = 2*x3 - 2*x2
    E = 2*y3 - 2*y2
    F = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2
    x = (C*E - F*B) / (E*A - B*D)
    y = (C*D - A*F) / (B*D - A*E)
    return x,y

#Apply trilateration algorithm to locate receiver
x,y = trackR(x1,y1,r1,x2,y2,r2,x3,y3,r3)

#Output location / coordinates
print("Calculated Location:")
print(x,y)


# In[ ]:


x_r = -1.45
y_r = 1.00


# In[ ]:


err_1 = math.sqrt(math.pow((x_r - x), 2) + math.pow((y_r - y), 2))
print(err_1, 'Meters')


# ### Case 2 

# In[ ]:


r1 = 4.014053789425482
r2 = 2.425516765591159
r3 = 1.3073567602126066


# In[ ]:


draw_circle()
plt.xlim(-8, 6)
plt.ylim(-4, 8)
plt.title('Test Case 2')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.savefig('Test_Case2.png', dpi = 300)


# In[ ]:


x,y = trackR(x1,y1,r1,x2,y2,r2,x3,y3,r3)


# In[ ]:


print("Calculated Location:")
print(x,y)


# In[ ]:


x_r = -2.90
y_r = 2.70


# In[ ]:


err_2 = math.sqrt(math.pow((x_r - x), 2) + math.pow((y_r - y), 2))
print(err_2, 'Meters')


# ### Scenario 2 - Different Rooms

# ### Case 3

# In[ ]:


# Room 3
x1 = - 1.55
y1 = 5.10

# Room 2 
x2 = 0
y2 = 2.20

# Room 1
x3 = -4.97
y3 = 0


# In[ ]:


r1 = 5.977171058493173
r2 = 3.079465169386043
r3 = 4.346795441735072


# In[ ]:


draw_circle()
plt.xlim(-12, 5)
plt.ylim(-5, 12)
plt.title('Test Case 3')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.savefig('Test_Case3.png', dpi = 300)


# In[ ]:


x,y = trackR(x1,y1,r1,x2,y2,r2,x3,y3,r3)


# In[ ]:


print("Calculated Location:")
print(x,y)


# In[ ]:


x_r = 0
y_r = 0


# In[ ]:


err_3 = math.sqrt(math.pow((x_r - x), 2) + math.pow((y_r - y), 2))
print(err_3, 'Meters')


# ### Case 4

# In[ ]:


# Room 3
x1 = - 1.55
y1 = 5.10

# Room 2 
x2 = 0
y2 = 2.20

# Room 4
x3 = 6.20
y3 = -2.25


# In[ ]:


r1 = 5.015575342103839
r2 = 2.680463077595574
r3 = 9.484158552729756


# In[ ]:


draw_circle()
plt.xlim(-12, 17)
plt.ylim(-12, 12)
plt.title('Test Case 4')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.savefig('Test_Case4.png', dpi = 300)


# In[ ]:


x,y = trackR(x1,y1,r1,x2,y2,r2,x3,y3,r3)


# In[ ]:


print("Calculated Location:")
print(x,y)


# In[ ]:


x_r = 0
y_r = 0


# In[ ]:


err_4 = math.sqrt(math.pow((x_r - x), 2) + math.pow((y_r - y), 2))
print(err_4, 'Meters')

