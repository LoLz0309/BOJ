import sys
input = sys.stdin.readline

from collections import defaultdict
n, x = map(int, input().split())
hits = list(map(int, input().split()))

sub_sum = sum(hits[:x])
max_hit = sub_sum
max_hit_cnt = 1
l, r = 0, x
while r < n:
    sub_sum += hits[r] - hits[l]
    r += 1
    l += 1

    if sub_sum > max_hit:
        max_hit = sub_sum
        max_hit_cnt = 1
    elif sub_sum == max_hit:
        max_hit_cnt += 1

if max_hit:
    print(max_hit)
    print(max_hit_cnt)
else:
    print('SAD')