import sys
input = sys.stdin.readline

n = int(input())

dp = [4] * (n + 1)
for i in range(int(n ** 0.5) + 1):
    dp[i ** 2] = 1

if dp[n] == 1:
    print(1)
    exit()

for i in range(1, n + 1):
    if dp[i] == 1:
        continue

    for j in range(1, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], dp[i - (j ** 2)] + 1)

print(dp[n])
