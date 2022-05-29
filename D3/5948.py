# 5948. 새샘이의 7-3-5 게임, D3
import itertools
t = int(input())

for tc in range(1, t+1):
    nums = list(map(int,input().split()))

    com = list(itertools.combinations(nums, 3))
    res = []
    for c in com:
        if sum(c) not in res:
            res.append(sum(c))

    res.sort(reverse=True)
    print(f"#{tc} {res[4]}")