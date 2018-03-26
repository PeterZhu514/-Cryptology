#!/usr/bin/env python
#-*-coding=utf-8 -*-
__author__='peterzhu514@gmail.com'

class Group(object):
	def __init__(self,value1,value2):
		self.value1=str(value1)
		self.value2=str(value2)

	def SetPoint(self,x1,y1,x2,y2):
		self.x1=x1
		self.y1=y1
		self.x2=x2
		self.y2=y2


	def FindPos(self):
		global P
		for i in range(0,5):
			for j in range(0,5):
				if self.value1==P[i][j]:
					self.x1=i
					self.y1=j
				if self.value2==P[i][j]:
					self.x2=i
					self.y2=j

	def FindC(self):
		if self.y1==self.y2:
			self.x1=(self.x1+1)%5
			self.x2=(self.x2+1)%5
		if self.x1==self.x2:
			self.y1=(self.y1+1)%5
			self.y2=(self.y2+1)%5
		if self.x1!=self.x2 and self.y1!=self.y2:
			temp=self.y1
			self.y1=self.y2
			self.y2=temp





def main():

	global P
	P=[['c','i','p','h','e'],['r','a','b','d','f'],['g','k','l','m','n'],['o','q','s','t','u'],['v','w','x','y','z']]
	global m
	m="PlayFair cipher was actually invented by Wheatstone"
	c=[]
	m=m.lower().replace(" ","")


	if len(m)%2!=0:
		m=m+'a'

	for i in range(0,len(m)-1,2):
		group=Group(m[i],m[i+1])
		group.FindPos()
		group.FindC()
		c.append(P[group.x1][group.y1])
		c.append(P[group.x2][group.y2])

	cstr="".join(c)
	print("加密后：%s"%cstr)

if __name__=='__main__':
	main()



