# 두 수중에서 하나라도 1 이하인 경우 -> 더하기
# 두 수가 모두 2 이상인 경우 -> 곱하기
# 02984 -> 576
# 567 -> 210 

s = input() # 문자열로 인식

result = 0 # 현재까지의 계산 결과를 담은 상태 

for i in s:
    if int(i) <= 1 or result <= 1:
        result += int(i) 
    else:
        result *= int(i) 

print(result)

## 정답 풀이

data = input()

# 첫번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num 
    else:
        result *= num 

print(result) 