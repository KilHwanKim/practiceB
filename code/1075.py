## ³ª´©±â 
N = int(input())
F = int(input())
N =  (N//100)*100
print("%02d"%((F-N%F)%F))
