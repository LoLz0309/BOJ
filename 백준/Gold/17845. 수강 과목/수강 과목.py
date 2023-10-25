import sys
input = sys.stdin.readline

n, k = map(int, input().split())

score = [0] * (n + 1)
for _ in range(k):
    i, t = map(int, input().split())
    for s in range(n, t - 1, -1):
        score[s] = max(score[s], score[s - t] + i)

print(score[n])