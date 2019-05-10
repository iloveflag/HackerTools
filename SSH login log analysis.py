#python3
import re
def get_dist(dist,file,string):
	try:
		with open(file) as f:
			for line in f.readlines():
				if re.search(string,line):
					rst=re.findall(r'(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)',line)
					rst=''.join(rst)
					if rst in dist.keys():
						dist[rst][0]=dist[rst][0]+1   #Failuers+1
						dist[rst][2]=line[0:15]        #Update the LastTime
					else:
						dist.update({rst:[1,line[0:15],line[0:15]]})  #ip:['Failures,StartTime,LastTime']
		return dist
	except:
		print('NO This File!')
		exit()

def sort_dist(dist):
	data=sorted(dist.items(), key=lambda x: x[1], reverse=True)
	dist = {i[0]: i[1] for i in data} 
	return dist

def main():
	failed_dist={}
	success_dist={}
	file=input("Where is your ssh_log?\n")
	failed_dist=sort_dist(get_dist(failed_dist,file,': Failed password'))
	success_dist=sort_dist(get_dist(success_dist,file,': Accepted password'))
	tplt="{0:<20}\t{1:<10}\t{2:<20}\t{3:<20}"
	choose=input('1.Get Failed IP Informations 2.Get Success IP Informations\n')
	if choose == '1':
		print(tplt.format("Failed IP"," Failures","Start Time","Last Time",chr(12288)))
		for ip,msg in failed_dist.items():
			print(tplt.format(ip,msg[0],msg[1],msg[2],chr(12288)))
	elif choose == '2':
		print(tplt.format("Success IP","Success times","Start Time","Last Time",chr(12288)))
		for ip,msg in success_dist.items():
			print(tplt.format(ip,msg[0],msg[1],msg[2],chr(12288)))
	else:
		print('Type error!')

if __name__ == '__main__':
	main()