#!/usr/bin/python


#import matplotlib.pyplot as plt
#import pandas as pd
#df =  pd.read_csv('TestResults.csv')

#df.plot()
#df.plot(kind='scatter', x='Name', y='Read_Value') 
#Name = df["Name"]
#Read_Value = df["Read_Value"]
#colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
#explode = (0.1, 0, 0, 0, 0)  
#plt.pie(Read_Value, labels=Name, explode=explode, colors=colors,
#autopct='%1.1f%%', shadow=True, startangle=140)





#plt.title("Opended JTAG Master Serviece\n"+"TSE MAC Statistics Counter Map")
#plt.show()

################################
import pandas

df = pandas.read_csv('TestResults.csv', skiprows=4, header=None, names=[
    'Name', 'Read_Value'])
print(df2['Name'])
print(df2['Read_Value'])

#######################

#import pandas as pd
#array = pd.read_csv('TestResults.csv', index_col=[0]).values
#print(array)

##########################################
