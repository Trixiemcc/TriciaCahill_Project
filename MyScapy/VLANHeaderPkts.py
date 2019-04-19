#!/usr/bin/python
from scapy.all import * 


#Scapy generates an ICMP echo request (ping) with two 802.1Q 
#headers (VLAN 1 and VLAN 10):

sendp(Ether(dst='ff:ff:ff:ff:ff:ff', src='00:01:02:03:04:05')/Dot1Q(vlan=1)/Dot1Q(vlan=10)/
 IP(dst='255.255.255.255', src='192.168.0.1')/ICMP())
