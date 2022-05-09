# 1959. 두 개의 숫자열, D2

t = int(input())

for test_case in range(1, t+1):
    N, M = map(int, input().split())

    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    if N >= M:
        big = N
        small = M
        big_arr = A
        small_arr = B
    else:
        big = M
        small = N
        big_arr = B
        small_arr = A

    d = (big - small) + 1
    result = []
    for i in range(d):
        m = 0
        for j in range(small):
            m += big_arr[j+i] * small_arr[j]
        result.append(m)

    print(f"#{test_case} {max(result)}")




