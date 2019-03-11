#!/usr/bin/python

import pandas as pd
import csv

print(pd.__version__)



with open('TestResults', 'r') as infile, open('TestResults.csv', 'w') as outfile:
       #next(infile)	# skip the header line
       stripped = (line.strip() for line in infile)
       lines = (line.split(",") for line in stripped if line)
       writer = csv.writer(outfile)
       writer.writerows(lines)
         
	    
df = pd.read_csv('TestResults.csv')

#Sdf.drop(df.head(2).index)
#df.drop(df.tail(1).index)

df.drop(df.head(2).index, inplace=True)
df.drop(df.tail(1).index, inplace=True)
#print(df.to_string(index=False))

df.to_csv('TestResults.csv')


