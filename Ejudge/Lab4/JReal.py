n, k = map(int, input().split())
vals = list(map(int, input().split()))

tree = {}

# 1. Твоё привычное построение BST
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

sorted_elements = []

# 2. Стандартный In-Order DFS (Левый -> Узел -> Правый)
def dfs(curr):
    if curr is None:
        return
    
    dfs(tree[curr][0])                  # Лево
    sorted_elements.append(vals[curr])  # Узел
    dfs(tree[curr][1])                  # Право

dfs(0)

# K-й наименьший элемент (индекс K - 1)
print(sorted_elements[k - 1])