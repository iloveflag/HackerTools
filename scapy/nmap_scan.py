#ubuntu 16.04 python2.7 require:
#pip install python-nmap,nmap
#sudo apt install nmap
import nmap
import optparse
def nmap_scan(target_host,target_port):
	scanner=nmap.PortScanner()
	rst=scanner.scan(target_host,target_port)
	product=rst['scan'][target_host]['tcp'][int(target_port)]['product']
	state=rst['scan'][target_host]['tcp'][int(target_port)]['state']
	print "[*]"+target_host+" tcp/"+target_port+" "+product+" "+state
def main():
	parser = optparse.OptionParser('%prog -H <target_host> -p <target_port>\nexample:%prog -H www.baidu.com -p 80,443')
	parser.add_option('-H',dest='target_host',type='string')
	parser.add_option('-p',dest='target_port',type='string')
	(options,args) = parser.parse_args()
	target_host = options.target_host
	target_port = options.target_port
	if (target_host == None) | (target_port == None):
		parser.print_help()
		exit(0)
	target_port=str(options.target_port).split(',')
	for port in target_port:
		nmap_scan(target_host,port)
main()
	
	
