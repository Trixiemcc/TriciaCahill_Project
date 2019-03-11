#!/usr/bin/python

import pandas as pd
import csv

print(pd.__version__)


#df = pd.read_fwf('TestResults')
#df.to_csv('TestResults.csv')
#print(df.head(100))

with open('TestResults', 'r') as infile, open('TestResults.csv', 'w') as outfile:
       stripped = (line.strip() for line in infile)
       lines = (line.split(",") for line in stripped if line)
       writer = csv.writer(outfile)
       writer.writerows(lines)
