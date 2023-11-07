import sys
input = sys.stdin.readline

n = int(input())

rn = [i ** 2 for i in range(225)]
dp = [0]

for i in range(1, n + 1):
    dp.append(4)

    j = 1
    while rn[j] <= i:
        dp[i] = min(dp[i], dp[i - rn[j]] + 1)
        j += 1

print(dp[n])