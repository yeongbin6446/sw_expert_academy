# 1979. 어디에 단어가 들어갈 수 있을까, D2

t = int(input())

for i in range(t):
    N, K = map(int, input().split())
    puzzle = []
    for j in range(N):
        puzzle.append(list(map(int, input().split())))

    row_cnt = 0
    for j in range(len(puzzle)):    # row 탐색
        st = ''
        for k in range(len(puzzle[j])):
            st += str(puzzle[j][k])

        for l in st.split('0'):
            if l == '1' * K:
                row_cnt += 1

    col_cnt = 0
    for j in range(len(puzzle)):
        st = ''
        for k in range(len(puzzle[j])):
            st += str(puzzle[k][j])

        for l in st.split('0'):
            if l == '1' * K:
                col_cnt += 1

    print(f"#{i+1} {row_cnt + col_cnt}")

