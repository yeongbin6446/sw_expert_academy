# 5789. 현주의 상자 바꾸기, D3

t = int(input())

for tc in range(1, t+1):
    N, Q = map(int, input().split())
    box = [0] * N
    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            box[j] = i + 1

    print(f"#{tc}", *box)