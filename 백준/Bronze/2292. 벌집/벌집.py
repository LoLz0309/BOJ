import sys
input = sys.stdin.readline

n = int(input())

ans = 1
step = 1
while ans < n:
    ans += step * 6
    step += 1
    
print(step)