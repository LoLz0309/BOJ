import sys
input = sys.stdin.readline

n = int(input())
gap = list(map(int, input().split()))
gas = list(map(int, input().split()))

citygas = [(0, gas[0])]
for i in range(n - 2):
    citygas.append((citygas[i][0] + gap[i], gas[i + 1]))
fincity = citygas[-1][0] + gap[-1]
ans = 0

citygas.sort(key=lambda x: (x[1], x[0]))
for c, g in citygas:
    if c > fincity:
        continue
    ans += (fincity - c) * g
    fincity = c

print(ans)