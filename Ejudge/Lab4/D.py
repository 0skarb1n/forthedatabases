n = int(input())
vals = list(map(int, input().split()))

tree = {}

for i, v in enumerate(vals):
    tree[i] = [None, None]
    if i == 0:
        continue
    curr = 0

    while True:
        dirr = 0 if v <= vals[curr] else 1

        if tree[curr][dirr] is None:
            tree[curr][dirr] = i
            break
        curr = tree[curr][dirr]

level_sum = {}

def dfs(curr, level):
    if curr is None:
        return
    level_sum[level] = level_sum.get(level, 0) + vals[curr]

    dfs(tree[curr][0], level + 1)
    dfs(tree[curr][1], level + 1)

dfs(0, 0)

max_val = len(level_sum)
print(max_val)

ans = [level_sum[lvl] for lvl in range(max_val)]
print(*ans)