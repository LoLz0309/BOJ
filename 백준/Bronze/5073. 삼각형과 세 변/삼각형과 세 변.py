import sys
input = sys.stdin.readline

while True:
    a, b, c = sorted(map(int, input().split()))
    if (a, b, c) == (0, 0, 0):
        break
    
    if a + b <= c:
        print('Invalid')
    elif a == b or b == c:
        if a == c:
            print('Equilateral')
        else:
            print('Isosceles')
    else:
        print('Scalene')