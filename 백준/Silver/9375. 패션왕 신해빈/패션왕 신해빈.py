import sys
input = sys.stdin.readline

from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    wear = defaultdict(int)

    for _ in range(n):
        a, b = input().split()
        wear[b] += 1

    answer = 1
    for v in wear.values():
        answer *= v + 1

    print(answer - 1)
