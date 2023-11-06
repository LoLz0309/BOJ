import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    mn = m * n

    ans = -1
    while x <= mn and y <= mn:
        if x == y:
            ans = x
            break

        if x < y:
            x += m
        else:
            y += n

    print(ans)