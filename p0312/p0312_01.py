# 두수를 입력받아, 두수 사이의 합계를 구하시오.

# 1. 두수 입력
# 2. 함수호출
# 3. 1,10 1+2+3+4..0+10
# 4. 합계를 리턴 받아서
# 5. 합계 : 55 출력

# 1,10 1-10까지의 더하기, 빼기, 곱하기의 결과값을 출력하시오.
# 파이썬 언어는 인터프리터 언어, 컴파일러 언어

def cal(s_list):
    if s_list[0] > s_list[1]:
        s_list[0],s_list[1] = s_list[1],s_list[0]
    
    for i in range(s_list[0]+1,s_list[1]+1):
        s_list[2] += i
        s_list[3] -= i # 0-1 = -1 -1-2 = -3
        s_list[4] *= i

num1 = int(input('첫번째숫자 : '))
num2 = int(input('두번째숫자 : '))
# 함수호출
s_list = [num1,num2,0,0,1]
# sum = plus(num1,num2) # 전역변수
cal(s_list) # 전역변수

print('s_list :',s_list)
print(f'더하기 결과값 : {s_list[2]}')
print(f'빼기 결과값 : {s_list[3]}')
print(f'곱하기 결과값 : {s_list[4]}')