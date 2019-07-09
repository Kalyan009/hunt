p=int(input())
a=input();flag=0
a=list(map(int,a.split(" ")))
for n in range(p):
	if (n==a[n]):
		flag=1
		print(n,end=" ")
if (flag==0):
	print("-1")
