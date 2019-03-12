#!/usr/bin/perl -s
use warnings;
#use strict;

print "file edited: \n";

    
###########################################################
## Removing ',' and white space from the csv file  ########
###########################################################

open(my $in1, '<', "updated_TestResults.csv") or die "Cannot open updated_TestResults $!";
open(my $out1, '>', "TestResults.csv") or die "Cannot open output TestResults.csv $!";

while (<$in1>) {
  print $out1 $_;
}
close($in1);

system("sed -i 's/,,/,/g' TestResults.csv");
system("sed -i 's/,,,/,/g' TestResults.csv");
system("sed -i 's/,Unnamed: 2//g' TestResults.csv");
system("sed -i 's/,Unnamed: 3//g' TestResults.csv");
system("sed -i 's/,Unnamed: 4//g' TestResults.csv");
system("sed -i 's/,Unnamed: 5//g' TestResults.csv");
system("sed -i 's/ //g' TestResults.csv");
system("sed -i 's/,,/,/g' TestResults.csv");

#system("sed -i 's/,$//g' TestResults.csv");



close($out1);



 
  

