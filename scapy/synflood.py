from scapy.all import *
for sport in range(1024,1100):
        IPlayer = IP(dst='192.168.1.15')
        TCPlayer = TCP(sport=sport, dport=513)
        pkt = IPlayer / TCPlayer
        send(pkt)