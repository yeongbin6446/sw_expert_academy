# 2001. 파리 퇴치, D2

t = int(input())

for i in range(t):
    area = []
    fly = []
    N, M = map(int, input().split())

    for i in range(N):
        area.append(list(map(int,input().split())))

    for i in range(M-1, N):
        for j in range(M-1,N):
            sum = 0
            for k in range(M):
                for l in range(M):
                    sum += area[i-k][j-l]
            fly.append(sum)
    print(f"{i+1} {max(fly)}")