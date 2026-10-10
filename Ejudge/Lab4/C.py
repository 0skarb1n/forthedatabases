n=int(input())

vals=list(map(int,input().split()))

x=int(input())

tree={}

target=vals.index(x)

for i,v in enumerate(vals):
    tree[i]=[None,None]
    curr=0
    if i ==0:
        continue

    while True:
        dirr= 0 if v<=vals[curr] else 1

        if tree[curr][dirr]==None:
            tree[curr][dirr]=i
            break
        curr=tree[curr][dirr]

ans=[]

def tar(curr):
    if curr is None:
        return
    ans.append(vals[curr])
    tar(tree[curr][0])
    tar(tree[curr][1])
tar(target)
print(*ans)
    
