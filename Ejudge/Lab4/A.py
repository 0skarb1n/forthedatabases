n,m=map(int,input().split())

vals=list(map(int,input().split()))

tree={}

for i,v in enumerate(vals):
    tree[i]=[None,None]
    curr=0
    if i == 0:
        continue

    while True:
        dirr= 0 if v <= vals[curr] else 1
        if tree[curr][dirr] is None:
            tree[curr][dirr] = i
            break
        curr=tree[curr][dirr]
ans=[]
for _ in range(m):
    path=input().strip()
    curr=0

    for step in path:
        if curr is None:
            break
        curr=[curr][0 if step=="L" else 1]
    ans.append("YES" if curr is not None else "NO")


for i in ans:
    print(i)