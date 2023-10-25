n = int(input())

if n <= 2:
    print(1)
    exit()

ans = 1
l, r = 0, int(n ** (1/2)) // 2
while l <= n // 2:
    rn = r * (r + 1) // 2
    ln = l * (l + 1) // 2
    lrn = rn - ln

    # print(f'check {l + 1}~{r}: {lrn}')
    if lrn == n:
        ans += 1
        # print('ok')

    if lrn <= n:
        r += 1
    else:
        l += 1

print(ans)