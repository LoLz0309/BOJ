import sys
input = sys.stdin.readline

p = int(input())
for _ in range(p):
    line = list()
    ans = 0
    students = list(map(int, input().split()))

    for i in range(1, 21):
        k = len(line)
        line.append(students[i])
        while k > 0:
            if line[k] > line[k - 1]:
                break
            line[k], line[k - 1] = line[k - 1], line[k]
            k -= 1
            ans += 1

    print(f'{students[0]} {ans}')