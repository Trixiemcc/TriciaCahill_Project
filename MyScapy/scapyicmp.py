#!/usr/bin/python
from scapy.all import * 

dst_ip = "192.168.0.1"
pkt = IP(dst=dst_ip)/ICMP()/"Sent from scapy"
send(pkt)


send(IP(src="192.168.1.103", dst="192.168.1.1")/ICMP()/"This is also sent from scapy but ahs a different source address")

