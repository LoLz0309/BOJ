import sys
input = sys.stdin.readline

from collections import defaultdict
n, m = map(int, input().split())
words = defaultdict(int)
for _ in range(n):
    s = input().rstrip()
    if len(s) < m:
        continue
    words[s] += 1

for w in sorted(words.keys(), key=lambda x: (-words[x], -len(x), x)):
    print(w)
