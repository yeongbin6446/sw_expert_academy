# 2058. 자릿수 더하기, D1

N = int(input())

sum = (N // 1000) + ((N % 1000) // 100) + (((N % 1000) % 100) // 10) + (((N % 1000) % 100) % 10)

print(sum)
