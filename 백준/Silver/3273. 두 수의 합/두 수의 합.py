import sys
input = sys.stdin.readline

n = int(input())
nums = set(map(int, input().split()))
x = int(input())
x2 = x / 2

ans = 0
for num in nums:
    if num >= x2:
        continue
    if x - num in nums:
        ans += 1
print(ans)