#!/usr/bin/python
from scapy.all import * 

dst_ip = "192.168.0.1"
pkt = IP(dst=dst_ip)/ICMP()/"Sent from scapy"
send(pkt)


