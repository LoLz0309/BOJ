import sys
input = sys.stdin.readline

import heapq
n = int(input())
heap = list()

for _ in range(n):
    arg = int(input())
    if arg != 0:
        heapq.heappush(heap, (abs(arg), arg))
        continue

    if heap:
        print(heapq.heappop(heap)[1])
    else:
        print(0)

