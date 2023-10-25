import sys
input = sys.stdin.readline

from collections import defaultdict

n, m = map(int, input().split())
light = defaultdict(int)
switch = list()

for _ in range(n):
    args = list(map(int, input().split()))
    for a in args[1:]:
        light[a] += 1
    switch.append(args[1:])

ans = 0
for s in switch:
    if ans == 1:
        break
    possible = True
    for si in s:
        if light[si] == 1:
            possible = False
            break
    if possible:
        ans = 1

print(ans)
