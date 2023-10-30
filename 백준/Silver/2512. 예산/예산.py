import sys
input = sys.stdin.readline

n = int(input())
budget = tuple(map(int, input().split()))
m = int(input())

l, r = 0, max(budget) + 1
while l < r:
    mid = (l + r) // 2

    ret = 0
    for b in budget:
        ret += min(b, mid)

    if ret <= m:
        l = mid + 1
    else:
        r = mid

print(r - 1)