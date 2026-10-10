n=int(input())

vals=list(map(int,input().split()))

tree={}

for i,v in enumerate:
    curr=0
    tree[i]==[None,None]
    if i==0:continue

    while True:
        dirr=0 if v<=vals[curr] else 0
        if tree[curr][dirr] is None:
            tree[curr][dirr] =i
            break
        curr=tree[curr][dirr]

ans=0

def bst(curr):
    global ans
    if curr is None:
        return

    if tree[curr][0] is not None and tree[curr][1] is not None:
        ans+=1
    bst(tree[curr][0])
    bst(tree[curr][1])

bst(0)

print(ans)