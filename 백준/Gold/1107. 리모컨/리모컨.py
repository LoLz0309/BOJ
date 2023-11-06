import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
b = set(range(10))
if m:
    b = b - set(map(int, input().split()))


from collections import deque
nums = deque([num for num in b])
last_nums = deque()
for _ in range(1, len(str(n)) + 1):
    next_nums = deque()

    while nums:
        num = nums.pop()
        last_nums.append(num)
        for next_num in b:
            next_nums.append(num * 10 + next_num)
    nums = next_nums
nums += last_nums
answer = abs(n - 100)
while nums:
    num = nums.pop()
    answer = min(answer, len(str(num)) + abs(n - num))

print(answer)
