import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
m = int(input())
s = deque(list(input().rstrip()))

ans = 0
st = False
nio = ''
ren = 0
while s:
    io = s.popleft()

    if not st:
        if io == 'I':
            st = True
            nio = 'O'
            ren = 0
        continue

    if io == nio:
        if io == 'O':
            nio = 'I'
        else:
            nio = 'O'
            ren += 1
        continue

    ans += max(ren - n + 1, 0)
    st = False
    s.appendleft(io)
if st:
    ans += max(ren - n + 1, 0)

print(ans)