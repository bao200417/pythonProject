import random
l = [random.randint(-1000,1000) for i in range(1000)]
print(l)
tt = input('Nhập tên tập tin: ')
k =[]
for i in range(0,len(l),10):
   k.append(l[i:i+10])
for i in range(len(k)):
    k[i] = str(k[i])
    i = i + 1
with open(tt,'w') as f:
    f.write('\n'.join(k))
