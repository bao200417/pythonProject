import math
k=int(input('Nhập số nguyên a= '))
def isbevis(n):
    if (n < 2):
        return False;
    squareRoot = int(math.sqrt(n))
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False
    return True;
ihatepython = []
print("Các số nguyên tố nằm trong khoảng [ 0 ;",k,"] là:")
for i in range(0, k+1):
    if (isbevis(i)):
        ihatepython.append(i)
print(ihatepython)