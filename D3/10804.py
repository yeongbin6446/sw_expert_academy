# 10804. 문자열의 거울상, D3

t = int(input())

for test_case in range(1, t+1):
    words = input()
    li = list(words)
    li.reverse()
    answer = ''
    for i in li:
        if i == 'p':
            answer += 'q'
        elif i == 'q':
            answer += 'p'
        elif i == 'b':
            answer += 'd'
        else:
            answer += 'b'

    print(f"#{test_case} {answer}")