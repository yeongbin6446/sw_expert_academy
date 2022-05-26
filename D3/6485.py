# 6485. 삼성시의 버스 노선, D3

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    route = []

    for i in range(N):
        route.append(list(map(int,input().split())))

    P = int(input())
    C = []
    for i in range(P):
        C.append(int(input()))

    li = [0] * max(C)

    for r in route:
        for i in range(r[0],r[1]+1):
            li[i-1] += 1

    print(f"#{tc}", end = ' ')
    print(*li)
