# random 함수 
from random import * 

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성 
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성 
print(int(random()*10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random()*10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random()*10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random()*10)+1)# 1~10이하의 임의의 값 생성 
print(int(random()*10)+1)# 1~10이하의 임의의 값 생성 
print(int(random()*10)+1)# 1~10이하의 임의의 값 생성 
print(int(random()*45)+1)# 1 ~ 45 이하의 임의의 값 생성 
print(int(random()*45)+1)# 1 ~ 45 이하의 임의의 값 생성 
print(int(random()*45)+1)# 1 ~ 45 이하의 임의의 값 생성 

print(randrange(1,46)) # 1~46 미만의 임의의값 생성 
print(randrange(1,46)) # 1~46 미만의 임의의값 생성 
print(randrange(1,46)) # 1~46 미만의 임의의값 생성 
print(randint(1,45)) # 1~45이하의 임의의 값 생성 


# 해보세요 >>
# 1~10사이의 숫자를 입력받아서 변수1
# 변수2 1-10사이의 랜덤한숫자
# 랜덤한 숫자와 비교해 같은면 [당첨] 
# 다르면 [랜덤숫자는 {}로 일지하지 않습니다. ]
n1 = int(input('1-10사이의 수 입력하세요 >> ')) # 입력받는 숫자 
n2 = randint(1,10) # 랜덤한 숫자 (1-10)

if n1 == n2 :
    print('당첨')
else:
    print('랜덤 숫자는 {}로 일치하지 않습니다.'.format(n2))
