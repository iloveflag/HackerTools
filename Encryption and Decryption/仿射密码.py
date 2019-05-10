#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Affine Cipher
#先返回26个字母对应的加密与解密的dict
def encode(a,b):
	encode_dict={}
	for i in range(26):
		encode_dict[chr(((a*i+b)%26)+97)] = chr(i+97)
	return encode_dict

def decode(a,b):
	decode_dict={}
	for i in range(26):
		decode_dict[chr(i+97)]=chr(((a*i+b)%26)+97)
	return decode_dict
	
#求最大公约数
def gcd(a,b): 
	if a%b == 0:
		return b
	else:
		return gcd(b,a%b)
if __name__ == '__main__':
	choice=input("仿射密码\n1.加密 2.解密:")
	print("请输入a和b")
	a=eval(input("a="))
	b=eval(input("b="))
	if gcd(a,b) == 1:
		pwd=input("输入字符串")
		pwd_dict={}
		pwd_list=[]
		if choice=='1':
			pwd_dict=encode(a,b)
			for i in pwd:
				pwd_list.append(pwd_dict[i])
			print("加密后的字符串为"+"".join(pwd_list))
		if choice=='2':
			pwd_dict=decode(a,b)
			for i in pwd:
				pwd_list.append(pwd_dict[i])
			print("解密后的字符串为"+"".join(pwd_list))
	else:
		print("当前最大公约数为:"+str(gcd(a, b)))
		print('请保证a和b的最大公约数为1')


	