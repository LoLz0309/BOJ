import sys
input = sys.stdin.readline

p = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

t = int(input())
for _ in range(t):
    n = int(input())

    for i in range(len(p), n):
        p.append(p[i - 1] + p[i - 5])

    print(p[n - 1])
# print(*p)