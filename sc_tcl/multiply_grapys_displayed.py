#!/usr/bin/python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

## set up the display
fig = plt.figure(figsize = (13, 13))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(224)
ax4 = fig.add_subplot(223)
plt.suptitle("Data from Configured Design", size=16)

# Read in the data from the TestResults.csv
df =  pd.read_csv('TestResults.csv')

## this prints out the transmitted and received pkts to the console
#df.head()

# select just the transmit and received sections from the csv
name = (df['Addr'][0:2])
value = (df['Name'][0:2])
addressColors = ['#034694','#001C58']  

ax1.bar(name,value,color=addressColors, edgecolor='black')

#Give the x and y axes a title
ax1.set_title("Transmitted and Recieved Packets")

#########################################################

df =  pd.read_csv('TestResults.csv')

name = (df['Addr'][0:2])
value = (df['Name'][0:2])
colors = ['#034694','#001C58'] 	      

ax2.pie(value, labels=name, colors=colors,
autopct=lambda p : '{:.2f}%  ({:,.0f})'.format(p,p * sum(value)/100),
shadow=True, startangle=140)
ax2.set_title("Ethernet TransmittedOK and ReceivedOK Packets")

############################################


# Read in the data from the TestResults.csv
df =  pd.read_csv('TestResults.csv')

# select just the transmit and received sections from the csv
name = (df['Addr'][22:29])
value = (df['Name'][22:29])
addressColors = ['#034694','#001C58','#5CBFEB','#D00027',
              '#EF0107','#DA020E','#274488']  

ax4.bar(name,value, color=addressColors, edgecolor='black')

plt.xticks(rotation=15)
#Give the x and y axes a title
ax4.set_title("Ethernet Stats Packets")


##########################################

df =  pd.read_csv('TestResults.csv')

name = (df['Addr'][22:29])
value = (df['Name'][22:29])
colors = ['#034694','#001C58','#5CBFEB','#D00027',
              '#EF0107','#DA020E','#274488'] 

ax3.pie(value, labels=name, labeldistance=9999999, colors=colors,
autopct='%1.1f%%', 
shadow=True, startangle=140)
ax3.set_title("Ethernet Stats Packets")

handles, labels = ax3.axes.get_legend_handles_labels()
#ax3.set(adjustable='box-forced', aspect='equal')
ax3.legend(handles, labels, prop={'size':9},
          bbox_to_anchor=(0.8,0.2),
          bbox_transform=fig.transFigure)



plt.show()



