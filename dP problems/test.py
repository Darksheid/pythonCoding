amount=4
n=2
dp=[[1 if k==0 else 0 for k in range(1,amount)] for _ in range(n+1)]
print(dp)
