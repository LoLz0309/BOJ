import sys
input = sys.stdin.readline

n = int(input())

s = [1, 3]
for i in range(2, n):
    s.append(s[i - 1] + s[i - 2] * 2)

print(s[n - 1] % 10007)