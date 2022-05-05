# 2005. 파스칼의 삼각형, D2

t = int(input())

for i in range(t):
    N = int(input())
    pascal = [[0] * N for _ in range(N)]
    pascal[0][0] = 1
    print(f"#{i+1}")
    for i in range(1, N):
        for j in range(i+1):
            if j == 0:
                pascal[i][j] = 1
            elif j == i:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    for i in pascal:
        for j in i:
            if j != 0:
                print(j, end=' ')
        print()
