# 1947. 스도쿠 검증, D2

t = int(input())

for i in range(t):
    flag = True
    s = []
    for j in range(9):
        s.append(list(map(int, input().split())))
    print(f'#{i+1}', end=' ')
    row = []
    for j in range(9):
        row.append(list(set(s[j])))
        if len(row[j]) != 9:
            flag = False

    col = []
    for j in range(9):
        c = []
        for k in range(9):
            c.append(s[k][j])
        col.append(c)
    for j in range(9):
        col[j] = list(set(col[j]))
        if len(col[j]) != 9:
            flag = False

    area = []
    for j in range(2, 9, 3):
        for k in range(2, 9, 3):
            a = []
            for l in range(3):
                for m in range(3):
                    a.append(s[j - l][k - m])
            area.append(a)

    for j in range(9):
        area[j] = list(set(area[j]))
        if len(area[j]) != 9:
            flag = False

    if flag:
        print(1)
    else:
        print(0)