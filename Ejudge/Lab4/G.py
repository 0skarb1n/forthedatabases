n = int(input())
vals = list(map(int, input().split()))

tree = {}

for i, v in enumerate(vals):
    curr = 0
    tree[i] = [None, None]
    if i == 0:
        continue  # Исправлено: continue вместо break
    while True:
        if v == vals[curr]:
            break  # Исправлено: break вместо continue
        dirr = 0 if v < vals[curr] else 1
        if tree[curr][dirr] is None:
            tree[curr][dirr] = i
            break
        curr = tree[curr][dirr]

ans = 0   

def get_max(curr):
    global ans
    if curr is None:
        return 0
    Left = get_max(tree[curr][0])
    Right = get_max(tree[curr][1])

    ans = max(ans, Left + Right + 1) 
    return 1 + max(Left, Right)

get_max(0)
print(ans)