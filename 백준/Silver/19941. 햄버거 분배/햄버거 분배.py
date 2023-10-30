import sys
input = sys.stdin.readline

from collections import deque
n, k = map(int, input().split())

burger = deque()
person = deque()
args = input().rstrip()
for i in range(len(args)):
    if args[i] == 'H':
        burger.append(i)
    else:
        person.append(i)

ret = 0
while burger and person:
    p = person.popleft()
    while burger and p - k > burger[0]:
        burger.popleft()
    if not burger:
        break

    if abs(burger[0] - p) <= k:
        ret += 1
        burger.popleft()

print(ret)