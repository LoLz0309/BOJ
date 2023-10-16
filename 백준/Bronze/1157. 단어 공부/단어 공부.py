import sys
input = sys.stdin.readline

from collections import Counter

s = Counter(input().rstrip().upper())
if len(s) <= 1:
    print(s.most_common(1)[0][0])
else:
    m = s.most_common(2)
    if m[0][1] == m[1][1]:
        print('?')
    else:
        print(m[0][0])