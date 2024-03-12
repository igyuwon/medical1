import random

# random_num = random.randint(10000, 99999)
random_num = str(random.randint(10000, 99999))
print('[ 랜덤숫자 맞추기 ]')
print('랜덤숫자 : ', random_num)
a_input = input('숫자 5자리를 입력하세요. : ')
cnt = 0

random_num_str = str(random_num)
a_input_str = str(a_input)

# 숫자 자리로 확인해서 맞춘 개수를 출력하시오.
# for i in range(len(random_num_str), 0, -1):
#     if random_num_str[i-1] == a_input_str[i-1]:
#         cnt += 1

# print('총 {}개 맞췄습니다.'.format(cnt))

for i in range(5):
    if random_num[i] == a_input[i]:
        cnt += 1
print('총 {}개 맞췄습니다.'.format(cnt))