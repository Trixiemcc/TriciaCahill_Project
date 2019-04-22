#!/usr/bin/python
from scapy.all import * 


#this sniffs out the traffic on the network eno1
sniff(iface="eno1", prn=lambda x:x.summary) 

