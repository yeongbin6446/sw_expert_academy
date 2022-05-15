# 11736. 평범한 숫자, D3

t = int(input())

for test_case in range(1, t+1):
    N = int(input())
    p = list(map(int, input().split()))

    cnt = 0
    for i in range(1, N-1):
        max_p = max(p[i-1], p[i], p[i+1])
        min_p = min(p[i - 1], p[i], p[i + 1])
        if p[i] != max_p and p[i] != min_p:
            cnt += 1

    print(f"#{test_case} {cnt}")