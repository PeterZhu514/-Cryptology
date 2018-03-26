dic='abcdefghijklmnopqrstuvwxyz'
m=str(input("加密前："))
c=[]
for i in range(len(m)):
	c.append(dic[(dic.index(m[i])+3)%26])
cstr="".join(c)
print("加密后：%s"%cstr)
