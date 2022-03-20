inta=int(input())
intb=int(input())
perfect=[]
for c in range(inta, intb+1, 1):
    product=1
    sun=0
    for e in str(c):
        sun=sun+int(e)
        product=product*int(e)
    if (product % sun) == 0:
        perfect.append(int(c))
print(len(perfect))
