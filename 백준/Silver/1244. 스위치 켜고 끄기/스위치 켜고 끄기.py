import sys
input = sys.stdin.readline

n = int(input())
switch = [0] + list(map(int, input().split()))
m = int(input())
for _ in range(m):
    s, num = map(int, input().split())
    if s == 1:
        for i in range(num, n + 1, num):
            switch[i] ^= 1
    else:
        switch[num] ^= 1
        for d in range(1, n):
            l, r = num - d, num + d
            if l < 1 or r > n:
                break
            if switch[l] != switch[r]:
                break
            switch[l] ^= 1
            switch[r] ^= 1

for i in range(1, n + 1, 20):
    print(*switch[i:i + 20])
