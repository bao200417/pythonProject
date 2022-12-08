a=float(input('Nhập a= '))
import random
i=1
j=1
x=[]
for i in range(10):
  b=random.normal(-10,10,(0,10))
  x.append(b)
  i=i+1
print('a=',a)
print('x=',x)
for j in range(0,10,1):
  x[j]=x[j]*a
print('a*x= ',x)