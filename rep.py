af=int(input())
fp=list(map(int,input().split()))[:af]
a=len(fp)
l1=[]
for i in range(a):
  b=i+1
  for j in range(b,a):
    if fp[i]==fp[j] and fp[i] not in l1:
      l1.append(fp[i])
l1.sort()
if len(l1)==0:
    print("unique")
else:
    print(*l1,end=' ')
