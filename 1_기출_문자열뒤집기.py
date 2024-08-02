# 앞뒤 문자열이 다를 때 count 
# 전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중에서 더 적은 횟수를 가지는 경우 계산

s = input()
changes = [s[0]]

for i in range(1, len(s)):
    if s[i] != changes[-1]:
        changes.append(s[i])

zero_cnt = changes.count('0') 
one_cnt = changes.count('1')

print(min(zero_cnt, one_cnt))

## 정답 풀이
# s = input()
# zero_cnt = 0 # 1 -> 0으로 바꾸는 횟수
# one_cnt = 0 # 0 -> 1로 바꾸는 횟수 

# if s[0] == '1':
#     zero_cnt += 1
# else:
#     one_cnt += 1 

# for i in range(len(s) -1):
#     if s[i] != s[i+1]:
#         if s[i+1] == '1':
#             zero_cnt += 1 
#         else:
#             one_cnt += 1 

# print(min(zero_cnt, one_cnt))

