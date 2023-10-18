import sys
input = sys.stdin.readline

from collections import defaultdict, Counter
T = int(input())
for _ in range(T):
    n = int(input())
    result = list(map(int, input().split()))
    p = Counter(result)

    score = defaultdict(list)
    s = 1
    for i in range(n):
        t = result[i]
        if p[t] < 6:
            continue
        score[t].append(s)
        s += 1

    answer = sorted([x for x in score.keys()], key=lambda x: (sum(score[x][:4]), score[x][4]))
    print(answer[0])

