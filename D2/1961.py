# 1961. 숫자 배열 회전, D2

def rotate_arr(arr):
    arr_rotate = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_rotate[i][j] = arr[N-1-j][i]
    return arr_rotate

t = int(input())

for test_case in range(1, t+1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    print(f"#{test_case}")
    arr_r = [0, 0, 0]
    arr_r[0] = rotate_arr(arr)
    arr_r[1] = rotate_arr(arr_r[0])
    arr_r[2] = rotate_arr(arr_r[1])

    for i in range(N):
        for j in range(3):
            print(''.join(map(str, arr_r[j][i])), end = ' ')
        print()
