# 1983. 조교의 성적 매기기, D2

t = int(input())

for i in range(t):
    N, K = map(int, input().split())
    scores = []
    total = []
    grade = ['A+' , 'A0' , 'A-' , 'B+' , 'B0' , 'B-' , 'C+' , 'C0' , 'C-', 'D0']
    for n in range(N):
        scores.append(list(map(int, input().split())))

    for i in range(N):
        t = 0
        for j in range(3):
            if j == 0:
                t += scores[i][j] * (35 / 100)
            elif j == 1:
                t += scores[i][j] * (45 / 100)
            else:
                t += scores[i][j] * (20 / 100)

        total.append(t)
    target_total = total[K-1]
    total.sort(reverse=True)
    a = N // 10
    print(grade[total.index(target_total) // a])



