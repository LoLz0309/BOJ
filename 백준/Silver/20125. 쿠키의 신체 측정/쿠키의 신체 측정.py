import sys
input = sys.stdin.readline

n = int(input())
body = [input().rstrip() for _ in range(n)]
hx, hy = 0, 0
la, ra, wa, ll, rl = 0, 0, 0, 0, 0
for r in range(n):
    if '*' in body[r]:
        hx, hy = r + 1, body[r].index('*')
        break

la, ra = body[hx][:hy].count('*'), body[hx][hy + 1:].count('*')

for r in range(hx + 1, n):
    if body[r][hy] == '_':
        break
    wa += 1

for r in range(hx + wa + 1, n):
    leg = False
    if body[r][hy - 1] == '*':
        ll += 1
        leg = True
    if body[r][hy + 1] == '*':
        rl += 1
        leg = True

    if not leg:
        break

print(hx + 1, hy + 1)
print(la, ra, wa, ll, rl)
