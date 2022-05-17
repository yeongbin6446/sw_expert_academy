# 10580. 전봇대, D3

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    wires = []
    for i in range(N):
        wires.append(list(map(int, input().split())))

    cross = 0
    for i in range(N-1):
        for j in range(i+1 , N):
            if wires[i][0] > wires[j][0] and wires[i][1] > wires[j][1]:
                pass
            elif wires[i][0] < wires[j][0] and wires[i][1] < wires[j][1]:
                pass
            else:
                cross += 1

    print(f"#{tc} {cross}")


