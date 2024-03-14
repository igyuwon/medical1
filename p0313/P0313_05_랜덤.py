import math
from random import * # random 모듈명을 안붙여도 됨.

# # 0.00000~0.999999 랜덤으로 소수점의 결과값 리턴
# print(random.random())

# # 10~20 사이의 랜덤 float 결과값을 리턴
# print(random.uniform(10,20))

# # 1~2까지의 랜덤숫자 리턴
# print(random.randrange(1,3))

# # 리스트 내에 랜덤 선택
# print(random.choice([1,2,3,4,5]))

# # 리스트 내에 랜덤으로 k개를 선택, k가 리스트 개수보다 많으면 에러
# print(random.sample([1,2,3,4,5], k = 1))

# # 리스트의 요소를 랜덤으로 섞음
# a_list = [1,2,3,4,5]
# random.shuffle(a_list)
# print(a_list)

# # 1~10 10 포함, 범위 내 랜덤 int를 선택
# print(random.randint(1,10))

# print(math.sin(1))
# print(math.cos(1))
# print(math.tan(1))