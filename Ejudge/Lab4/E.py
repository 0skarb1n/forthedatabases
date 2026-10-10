n = int(input())

tree = {i: [None, None] for i in range(1, n + 1)}

for _ in range(n - 1):
    u, v, t = map(int, input().split())
    tree[u][t] = v  # в узел u в ветку t кладём ребёнка v

level_count = {}

def bst(curr, level):
    if curr is None:
        return
    level_count[level] = level_count.get(level, 0) + 1

    bst(tree[curr][0], level + 1)
    bst(tree[curr][1], level + 1)

bst(1, 0)

print(max(level_count.values()))