# 1984. 중간 평균값 구하기, D2

t = int(input())

for i in range(t):
    nums = list(map(int, input().split()))

    nums.sort()

    nums = nums[1:-1]
    result = round(sum(nums) / 8)
    print(f"#{i+1} {result}")