import sys
input = sys.stdin.readline

n = int(input())
req = list(map(int, input().split()))
total = int(input())

if sum(req) <= total:
    print(max(req))
    exit()

# binary search
limit_min, limit_max = 0, total
bef_min, bef_max = 0, total

while True:
    limit_mid = int((limit_min + limit_max) // 2)
    
    calc = 0
    for r in req:
        if r > limit_mid:
            calc += limit_mid
        else:
            calc += r

    bef_min, bef_max = limit_min, limit_max

    if calc > total:
        limit_max = limit_mid
    else:
        limit_min = limit_mid

    if bef_min == limit_min and bef_max == limit_max:
        print(limit_min)
        break