# 1284. 수도 요금 경쟁, D2

t = int(input())

for test_case in range(1, t+1):
    P, Q, R, S, W = map(int, input().split())

    A = P * W

    if R >= W:
        B = Q
    else:
        B = Q + (S * (W - R))

    print(f"#{test_case} {min(A,B)}")

