from scapy.all import *
pkt=Ether(src=RandMAC(),dst=RandMAC())/IP()
sendp(pkt,loop=1)