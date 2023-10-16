import sys
input = sys.stdin.readline

CMD_ADD = 'add'
CMD_REM = 'remove'
CMD_CHK = 'check'
CMD_TOG = 'toggle'
CMD_ALL = 'all'
CMD_EMP = 'empty'

s = [0] * 21
m = int(input())
for _ in range(m):
    args = list(input().split())
    if args[0] == CMD_ADD:
        s[int(args[1])] = 1
    elif args[0] == CMD_REM:
        s[int(args[1])] = 0
    elif args[0] == CMD_CHK:
        print(s[int(args[1])])
    elif args[0] == CMD_TOG:
        s[int(args[1])] ^= 1
    elif args[0] == CMD_ALL:
        s = [1] * 21
    else:
        s = [0] * 21
