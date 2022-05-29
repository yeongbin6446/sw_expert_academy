# 6019. 기차 사이의 파리, D3

t = int(input())

for tc in range(1, t+1):
    D, A, B, F = map(int, input().split())

    print(f"#{tc} {F * (D / (A+B)):0.6f}")