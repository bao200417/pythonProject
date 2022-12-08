#Bài 1
a=input('Nhap duong dan tep.')
b=input('Nhap xau ki tu.')
f=open(a,'w')
f.write(b)
f.close()
#Bài 2
c=input('Nhap duong dan tep..')
k=open(c,'r')
m=k.read()
print(m)
#Bài 3
d=input('Nhap xau ki tu...')
e=input('Nhap duong dan tep...')
t=open(e,'a')
t.write(d)
t.close()
#Bài 4:
t=open(e,'r')
l=t.read()
print(l)

