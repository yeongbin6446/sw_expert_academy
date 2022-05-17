# 10200. 구독자 전쟁, D3

t = int(input())

for tc in range(1, t+1):
    N, A, B = map(int, input().split())

    if A+B >= N:
        big = (A+B) - N
    else:
        big = 0

    small = min(A,B)

    print(f"#{tc} {small} {big}")