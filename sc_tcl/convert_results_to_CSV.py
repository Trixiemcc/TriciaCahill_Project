#!/usr/bin/python

#import pandas as pd
import csv
import pandas
import subprocess
import sh
import fileinput

#print(pd.__version__)

dataframe = pandas.read_csv("TestResults",delimiter="\t")

@staticmethod
def strip_characters(input_string):
    return str(input_string).lower().replace(",,,", ",").replace(",,", ",").replace("Unnamed:","")

dataframe.to_csv("updated_TestResults.csv", encoding='utf-8', index=False)


pipe = subprocess.Popen(["perl", "replace_script.pl"], stdout=subprocess.PIPE)
#replace_script.pl
