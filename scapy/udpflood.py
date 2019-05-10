from scapy.all import *
for i in range(1024,1100):
        pkt = IP(dst='192.168.1.15')/UDP(sport=i,dport=513,len=8) //UDP头部8字节
        send(pkt)