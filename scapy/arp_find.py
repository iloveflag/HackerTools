import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import  optparse
from threading import *
def arp_scan(pkt):
	try:
		rst = srp1(pkt,timeout=1,verbose=0)
		print 'Found ip:'+rst.psrc+' MAC:'+rst.hwsrc
	except:
		pass
def main():
	parser = optparse.OptionParser('%prog -H <target>\nExample:%prog -H 172.16.1.')
	parser.add_option('-H',dest='target',type='string')
	(options,args) = parser.parse_args()
	host = options.target
	if host == None:
		parser.print_help()
	for i in xrange(1,255):
		pkt = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=host+str(i))
		t = Thread(target=arp_scan,args=(pkt))
		t.start()
main()
