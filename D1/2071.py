# 2071. 평균값 더하기, D1

t = int(input())

for i in range(t):
    nums = list(map(int, input().split()))
    avg = round(sum(nums) / 10)


    print(f"#{i+1} {avg}")