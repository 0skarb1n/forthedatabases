n=int(input())

vals=list(map(int,input().split()))

x=int(input())

target=vals.index(x)

tree={}

for i,v in enumerate(vals):
    tree[i]=[None,None]

    curr=0

    if i == 0:
        continue

    while True:
        dirr=0 if v<=vals[curr] else 1

        if tree[curr][dirr] is None:
            tree[curr][dirr]=i
            break
        curr=tree[curr][dirr]

def finder(curr):
    if curr is None:
        return 0
    return 1 + finder(tree[curr][0])+finder(tree[curr][1])
print(finder(target))