import sys
input = sys.stdin.readline

from collections import deque

t = int(input())
for _ in range(t):
    order = deque(list(input().rstrip()))
    n = int(input())
    x = deque(list(input()[1:-2].split(',')))
    if n == 0:
        x = deque()

    rev = 0
    error = False
    while order:
        o = order.popleft()
        if o == 'R':
            rev ^= 1
            continue

        if not x:
            error = True
            break

        if rev:
            x.pop()
        else:
            x.popleft()

    if error:
        print('error')
        continue
    if rev:
        x.reverse()
    print(f'[{",".join(x)}]')

