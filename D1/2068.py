# 2068. 최대수 구하기, D1

t = int(input())


for i in range(t):
    nums = list(map(int, input().split()))
    result = max(nums)

    print(f"#{i+1} {result}")