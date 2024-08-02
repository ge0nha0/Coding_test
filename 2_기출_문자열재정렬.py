# 있는 그대로 구현
# 숫자인 경우 따로 합계 계산 
# 알파벳인 경우 별도의 리스트 저장 

s = input()
number = 0 # 숫자 저장
result = [] # 알파벳 저장

for i in s:
    if i.isalpha():
        result.append(i)
    else:
        number += int(i)
    
result.sort() # 오름차순 정렬

if number != 0: # 숫자를 맨 끝으로 보내기
    result.append(str(number))

print(''.join(result)) # 리스트를 문자열로 변환하여 출력