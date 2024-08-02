# N: 현재 캐릭터의 점수  # 자리수는 항상 짝수형태임 
# 123,402 -> 123:6 / 402:6

n = input()

number = len(n) // 2 

left_value = 0 
for i in range(number):
    left_value += int(n[i])

right_value = 0
for i in range(number, len(n)):
    right_value += int(n[i])

if left_value == right_value:
    print("LUCKY")
else:
    print("READY")