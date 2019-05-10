s=input('请输入密文:')
s_list=list(s)
rst_list=list(s_list)
choice=input('1.爆破 2.指定移位值:')
def encry_shift(s,k):
	for i in range(len(s)):
		if ord(s_list[i]) < 123-k:
			rst_list[i]=chr(ord(s_list[i])+k)
		else:
			rst_list[i]=chr(ord(s_list[i])+k-26)
	print(str(k)+'.'+"".join(rst_list))
def encry_burst(s):
	for k in range(26):
		encry_shift(s,k)
if choice=='1':
	encry_burst(s)
else:
	k=eval(input("请输入移位值:"))
	encry_shift(s,k)
