#!/usr/bin/python
from scapy.all import * 


for packet in pkts:   
    if(packet.haslayer(ICMP)):
        print("ICMP code: {packet.getlayer(ICMP).code}")
