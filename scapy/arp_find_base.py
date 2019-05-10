#!/usr/bin/python
#!coding:utf-8
from scapy.all import *
for n in range(1,254):
	ip="192.168.1."+str(n)
	pkt=Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip,hwdst='00:00:00:00:00:00')
	result=srp1(pkt,timeout=1,verbose=0)
	if result:
		print("IP="+result.psrc+"MAC="+result.hwsrc)
