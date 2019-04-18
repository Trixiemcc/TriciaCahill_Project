Run the software

Programme the board with the .pof file from the tse dir

open the Tools, System console-Toolkits

cd ../tse/sc_tcl

run main.tcl

Test Loopback - TEST_MAC_LB 1000M, TEST_MAC_PHY_LB 1000M, TEST_ST_LB 1000M

Check status - stats_chk

write status to log file - stats_chk_res, this creats the TestResults file

******************************************************


***CONVERT_RESULTS_TO_CSV.PY***

in this script it reads in the TestResults text file and converts it to a csv file call updated_TestResults.csv.

the a perl script is called.  This replace_script.pl removes commas and unwanted headings and white space.

the display_consol_results.py script is called this will display the results on to the consol 

Then the Multiply_graphs_displayed.py scritp is called, inside this is pie and bar charts displaying different data from our results
