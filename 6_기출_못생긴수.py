# 못생긴수 -> 2,3,5만을 약수로 가지는 합성수 
# 2의 배수, 3의 배수, 5의 배수 등 각 배수를 곱한 값도 '못생긴 수'가 됨
# n이 증가하면서 2,3,5의 배수를 기록
# 핵심 -> 2,3,5의 배수 인덱스를 별도로 설정해서 n이 증가함에 따라 DP 테이블을 업데이트
## elif는 XX -> 2,3,5의 최소 공배수 값들이 elif로 하면 중복해서 들어가기 때문임 -> if를 넣어 최소 공배수 값들이 하나만 들어갈 수 있도록 설정

import sys

# n번째 못생긴 수 출력
n = int(sys.stdin.readline())

ugly = [0] * n # 못생긴 수를 담기 위한 테이블 (1차원 DP 테이블)
ugly[0] = 1 # 첫 번째 못생긴 수는 1

# 몇 번쨰 인덱스까지 2, 3, 5배한 결과를 다뤘는지
i2 = i3 = i5 = 0

# 다음으로 다뤄야하는 곱셈 값
next2, next3, next5 = 2, 3, 5

# 1부터 n까지의 못생긴 수들을 찾기
for l in range(1, n):

    # 다음으로 다뤄야하는 곱셈 값들 중 최솟값을 l번째 인덱스에 저장
    ugly[l] = min(next2, next3, next5)

    # 현재 i2 인덱스 값에 2배를 곱한 값은 업데이트 되었으므로, 
    # 다음 i2 인덱스 값에 2배를 곱한 값이 무엇인지 임시 저장
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2

    # 현재 i3 인덱스 값에 3배를 곱한 값은 업데이트 되었으므로, 
    # 다음 i3 인덱스 값에 3배를 곱한 값이 무엇인지 임시 저장
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3

    # 현재 i5 인덱스 값에 5배를 곱한 값은 업데이트 되었으므로, 
    # 다음 i5 인덱스 값에 5배를 곱한 값이 무엇인지 임시 저장
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

# n번째 못생긴 수를 출력
print(ugly[n - 1])