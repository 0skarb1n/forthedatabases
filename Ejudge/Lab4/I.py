n = int(input())
vals = list(map(int, input().split()))

tree = {}

# Build BST
for i, v in enumerate(vals):
    tree[i] = [None, None]
    if i == 0:
        continue
    curr = 0
    while True:
        dirr = 0 if v < vals[curr] else 1
        if tree[curr][dirr] is None:
            tree[curr][dirr] = i
            break
        curr = tree[curr][dirr]

# Count leaves
ans = 0

def dfs(curr):
    global ans
    if curr is None:
        return
    
    # Лист = нет ни левого (0), ни правого (1)
    if tree[curr] == [None, None]:
        ans += 1

    dfs(tree[curr][0])
    dfs(tree[curr][1])

dfs(0)
print(ans)