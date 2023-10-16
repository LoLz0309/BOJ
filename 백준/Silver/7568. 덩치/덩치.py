import sys
input = sys.stdin.readline

n = int(input())
info = list()
rank = [1] * n
for i in range(n):
    info.append(tuple(map(int, input().split())))
    for j in range(i):
        if info[j][0] > info[i][0] and info[j][1] > info[i][1]:
            rank[i] += 1
            continue
        if info[j][0] < info[i][0] and info[j][1] < info[i][1]:
            rank[j] += 1

print(*rank)
