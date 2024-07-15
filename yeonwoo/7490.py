# 7490
# 0 만들기

from itertools import product

M = int(input()) # 테스트 케이스의 숫자

for _ in range(M): # 각 테스트 케이스마다 실행
    N = int(input())
    outputs = [] # 수식의 결과가 0이 되는 수식

    numbers = [x for x in range(1, N+1)] # 1부터 N까지의 수를 오름차순으로 쓴 수열
    operations = list(product(['+', '-', ' '], repeat=N-1)) # 연산을 하는 경우의 수
    for operation in operations:
        if calculate(numbers, operation) == 0: # 결과값이 0이라면
            output = ''
            for i in range(N-1):
                output += str(numbers[i])
                output += operation[i]
            output += str(numbers[N-1])
            outputs.append(output)
    
    outputs.sort() # ASCII 순서에 따라 정렬
    for output in outputs: print(output)
    print()