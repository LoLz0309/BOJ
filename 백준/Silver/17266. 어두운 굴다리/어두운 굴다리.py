import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
x = list(map(int, input().split()))
ans = max(x[0], n - x[-1])
for i in range(m - 1):
    ans = max(ans, (x[i + 1] - x[i]) // 2 + (x[i + 1] - x[i]) % 2)

print(ans)

