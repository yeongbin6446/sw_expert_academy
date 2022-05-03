# 2072. 홀수만 더하기, D1

t = int(input())


for i in range(t):
    sum = 0
    nums = list(map(int, input().split()))
    for num in nums:
        if num % 2 == 1:
           sum += num

    print(f"#{i+1} {sum}")