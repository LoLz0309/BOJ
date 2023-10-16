import sys
input = sys.stdin.readline

vowel = set('aeiou')
ok = {'e', 'o'}


def rule1(s: str) -> bool:
    for v in 'aeiou':
        if v in s:
            return True
    return False


def rule2(s: str) -> bool:
    v, c = 0, 0
    for si in s:
        if si in vowel:
            v += 1
            c = 0
        else:
            c += 1
            v = 0
        if v > 2 or c > 2:
            return False
    return True


def rule3(s: str) -> bool:
    last = ''
    for si in s:
        if si == last and si not in ok:
            return False
        last = si
    return True


while True:
    s = input().rstrip()
    if s == 'end':
        break

    if rule1(s) and rule2(s) and rule3(s):
        print(f'<{s}> is acceptable.')
    else:
        print(f'<{s}> is not acceptable.')

