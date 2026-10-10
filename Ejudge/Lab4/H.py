n = int(input())
vals = sorted(map(int, input().split()))

ans = [sum(vals[i:]) for i in range(n)]

print(*ans)