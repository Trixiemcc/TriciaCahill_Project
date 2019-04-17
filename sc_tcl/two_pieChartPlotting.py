#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df =  pd.read_csv('TestResults.csv')
name = (df['Addr'][0:2])
value = (df['Name'][0:2])
colors = ['#034694','#001C58'] 
	      
fig1 = plt.figure(figsize = (13, 10))
ax1 = fig1.add_subplot(111)

plt.pie(value, labels=name, colors=colors,
autopct=lambda p : '{:.2f}%  ({:,.0f})'.format(p,p * sum(value)/100),
shadow=True, startangle=140)
#plt.legend(pie[0], labels, loc="upper corner")
plt.title("Ethernet TransmittedOK and ReceivedOK Packets")



addressColors = ['#034694','#001C58']

plt.show()

# print some values to see some data & daatatypes\u200b
print(df['Addr'][0:2])
print(df['Name'][0:2])
