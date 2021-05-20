n= int,input().split()
card = map(int,input().split())
card_dic ={}
for val in card:
    if val not in  card_dic.keys():
        card_dic[val]=1
    else:
        card_dic[val]+=1
m = int(input())
my = list(map(int,input().split()))
answer=[]
for val in my:
    if val not in card_dic.keys():
        answer.append(str(0))
    else:
        answer.append(str(card_dic[val]))
print(" ".join(answer))
