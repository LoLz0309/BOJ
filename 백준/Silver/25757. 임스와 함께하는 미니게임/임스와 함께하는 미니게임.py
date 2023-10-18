import sys
input = sys.stdin.readline

game = {'Y': 1, 'F': 2, 'O': 3}

n, g = input().split()
ans = set([input().rstrip() for _ in range(int(n))])
print(len(ans) // game[g])