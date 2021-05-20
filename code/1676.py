def find2(N):
  C = 0
  while N:
    N = N//2
    C+= N
  return C
def find5(N):
  C =0
  while N:
    N= N//5
    C+= N
  return C
N = int(input())
print(min(find2(N),find5(N)))
