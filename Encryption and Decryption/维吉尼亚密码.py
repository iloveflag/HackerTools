#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Vigenere Cipher


def encode(plain_text,secret_key):
	result=""
	#去除空格
	plain_text=plain_text.replace(" ","")
	#密钥重复排列
	plain_text_len=len(plain_text)
	secret_key_len=len(secret_key)
	secret_key=secret_key*(plain_text_len//secret_key_len)
	for i in range(plain_text_len%secret_key_len):
		secret_key=secret_key+secret_key[i]
	#开始加密
	for i in range(len(plain_text)):
		encode_text=number_dict[list(plain_text)[i]]+number_dict[list(secret_key)[i]]
		if encode_text>25:
			encode_text=encode_text-26
		result=result+chr(encode_text+97)
	return result

def decode(plain_text,secret_key):
	result=""
	#去除空格
	plain_text=plain_text.replace(" ","")
	#密钥重复排列
	plain_text_len=len(plain_text)
	secret_key_len=len(secret_key)
	secret_key=secret_key*(plain_text_len//secret_key_len)
	for i in range(plain_text_len%secret_key_len):
		secret_key=secret_key+secret_key[i]
	#开始解密
	for i in range(len(plain_text)):
		encode_text=number_dict[list(plain_text)[i]]-number_dict[list(secret_key)[i]]
		if encode_text<0:
			encode_text=encode_text+26
		result=result+chr(encode_text+97)
	return result

if __name__ == '__main__':
	number_dict={}
	for i in range(26):
		number_dict[chr(i+97)]=i
	print(number_dict)
	choice=input("维吉尼亚密码\n1.加密 2.解密")
	plain_text=input("请输入明文:")
	secret_key=input("请输入密钥:")
	if choice=='1':
		print("加密后的字符串为:"+encode(plain_text,secret_key))
	if choice=='2':
		print("解密后的字符串为:"+decode(plain_text,secret_key))



