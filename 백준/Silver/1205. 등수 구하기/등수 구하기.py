import sys
input = sys.stdin.readline

n, s, p = map(int, input().split())
score = list(map(int, input().split()))
rank = n + 1

for i in range(n - 1, -1, -1):
    if score[i] >= s:
        break
    rank -= 1

if rank <= p:
    for i in range(rank - 2, -1, -1):
        if score[i] > s:
            break
        rank -= 1
    print(rank)
else:
    print(-1)