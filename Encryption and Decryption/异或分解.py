l=r"`-=[]\,./<>?:{}|++_)(*&^$#@!~)"
string=input("请输入要分解的字符串:")
y1=""
y2=""
def jisuan(l,s):
	for i in l:
		for j in l:
			if(chr(ord(i)^ord(j))==s):
				return(i,j)
for s in list(string):
	i,j=jisuan(l,s)
	y1+=i
	y2+=j
print("结果为:"+'"'+y1+'"'+"^"+'"'+y2+'"'+"="+string)
