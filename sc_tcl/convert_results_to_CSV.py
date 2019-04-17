#!/usr/bin/python

import csv
import pandas
import subprocess
import sh
import fileinput
import display_consol_results  # imported the display python script


# read in the TestResults file
dataframe = pandas.read_csv("TestResults",delimiter="\t")

# replace multiple comma's with single ones
# send the output to the updated_TestResults.csv
dataframe.to_csv("updated_TestResults.csv", encoding='utf-8', index=False)

#calls the perl script to tidy up the TestResults.csv file
pipe = subprocess.Popen(["perl", "replace_script.pl"], stdout=subprocess.PIPE)


# display the consol output, by calling the function
# data_no_headers.head() from inside the display_consol_results script
display_consol_results.data_no_headers.head()
