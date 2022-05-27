# 6485. 삼성시의 버스 노선, D3

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    route = []

    for i in range(N):
        route.append(list(map(int,input().split())))

    P = int(input())
    C = {}
    C_list = []
    for i in range(P):
        b = int(input())
        C[b] = 0
        C_list.append(b)

    for r in route:
        for i in range(r[0],r[1]+1):
            if i in C.keys():
                C[i] += 1

    print(f"#{tc}", end=' ')
    for c in C_list:
        print(C[c],end=' ')
    print()