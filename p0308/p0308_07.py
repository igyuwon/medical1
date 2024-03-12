import random
# 주택복권
# 2조711
# 1조740942
# 조 : 1~9
# 뒷자리 : 0~999999

f_num = random.randint(1,9)
last_num = random.randint(100000,999999)

# lotto = '1조740042'
lotto = str(f_num)+'조'+"{:06d}".format(last_num)
print(lotto)
# 1조 10
# 예: 2조 711010 -> 1개 번호가 맞았습니다.
l_input = input('복권을 입력하세요.(예:1조111) : ')
# 비교하는 프로그램을 구현하시오.
# 자리수를 활용하세요.
cnt = 0
# for i in range(len(lotto)):
#     if lotto[i] == l_input[i]:
#         cnt += 1
# print('맞는 개수 : ',cnt-1) # 조는 항상 맞으니 -1

for i in range(len(lotto),0,-1):
    if lotto[i-1] == l_input[-1]:
        print('1만원')
    

# 6번째자리 1개 1만원
# 5,6째자리 10만원
# 4,5,6번째자리 100만원
# ...
# 조까지 맞으면 100억