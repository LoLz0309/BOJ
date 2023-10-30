import sys
input = sys.stdin.readline

from collections import defaultdict
n = int(input())
ans = input().rstrip()
ans_len = len(ans)
ans_dict = defaultdict(int)
for a in ans:
    ans_dict[a] += 1

result = 0
for _ in range(1, n):
    s = input().rstrip()
    if abs(len(s) - ans_len) > 1:
        continue

    limit = 1
    if len(s) == ans_len:
        limit = 2

    s_dict = defaultdict(int)
    for si in s:
        s_dict[si] += 1

    diff = 0
    for k in s_dict.keys() | ans_dict.keys():
        diff += abs(ans_dict[k] - s_dict[k])

    if diff <= limit:
        result += 1

print(result)