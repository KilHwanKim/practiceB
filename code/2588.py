a=input()
b=input()
a=int(a)
b=int(b)
x100=b//100
x10=(b-x100*100)//10
x1=(b-x100*100-x10*10)
print('%d'%(x1*a))
print('%d'%(x10*a))
print('%d'%(x100*a))
print('%d'%(x1*a+x10*a*10+100*x100*a))
