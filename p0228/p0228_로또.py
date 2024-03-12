from random import *
# 1. 변수 선언
mynum = [] # 입력을 1- 45 사이의 숫자를 입력을 받음 (6개)
lotto = [] # 1- 45사이의 랜덤한 숫자 6자리 저장 
ok = []
# 2. 입력받은 숫자 6개 : 
# mynum = [] input()를 통해서 숫자 6개를 넣을 예정
for i in range(6):
    n = int(input('{}번째 숫자를 입력하세요 (총 6개) >> '.format(i+1)))
    mynum.append(n)
# 3. 로또 번호 생성하기 :
# 1 - 45 까지의 숫자
l = []
for i in range(1,46):
    l.append(i)
# l 리스트에 1-45 중복이 없는 1- 45까지의 숫자가 들어있음. 
# [1,2,3................, 45]
#  0번방                   44번방
# l[0] = 0                   l[44] = 45
# print('로또 숫자 : {}'.format(l))
for i in range(200):
    tmp = randint(0,44) # l[0], l[1] , l[2] ... l[44]
    l[0],l[tmp] = l[tmp],l[0]
    
# print('로또 숫자 : {}'.format(l))
# l 잘섞여있고, 중복없음 
for i in range(6):
    lotto.append(l[i])
# 랜덤하고 중복이 없는 숫자 6개 생성 

# 4. 입력숫자와 랜덤숫자 비교 같은거 출력
# 매치하는 숫자, 개수, 
# m = [1, 2, 3] l = [3, 6, 7] 3, 1개 [3]
#  lotto =  [1,2,3,4,5,6]
#  mynum =  [7,8,9,10,5,7]
for i in range(6): # i = 0 ,1,2,3,4,5,
    if mynum[i] in lotto:
        ok.append(mynum[i])
# 5. 출력 
print('입력한숫자 : {}'.format(mynum))
print('로또 숫자 : {}'.format(lotto))
print('당첨된 숫자 : {}'.format(ok))

