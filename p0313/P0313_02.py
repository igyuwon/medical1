# 함수선언 def 이름() 정의
# 함수값은 return
# 함수호출 이름()
# 매개변수 함수로 데이터전달하는 변수, 매개변수 개수는 항상 같아야함.
# 가변매개변수는 *values, 일치하지 않아도 됨.
# 리스트, 딕셔너리는 주소값이 전달이 된다

# 퀴즈.1
# 함수를 사용하여 두수를 입력받아, 더하기, 빼기, 곱하기, 나누기 결과값을 출력하시오.

# def cal(num1, num2, c):
#     if c == '+':
#         result = num1 + num2
#     elif c == '-':
#         result = num1 - num2
#     elif c == '*':
#         result = num1 * num2
#     elif c == '/':
#         result = num1 / num2
#     return result

# # 두 수 입력을 받아 값을 리턴 받은 다음, 출력하시오.
# num1 = int(input('숫자 입력: '))
# num2 = int(input('숫자 입력: '))
# print('1. +, 2. -, 3. *, 4. /')
# c = input('원하는 사칙연산을 입력하세요: ')
# result = cal(num1, num2, c)
# print(f"결과값: {result}")


def cal(num1,num2):
    r_list = [0] * 6
    r_list[0] = num1
    r_list[1] = num2
    r_list[2] = num1 + num2
    r_list[3] = num1 - num2
    r_list[4]  = num1 * num2
    r_list[5] = num1 / num2
    return r_list

save_list = []

while True:

    num1 = int(input('첫번째 숫자 입력(0. 종료): '))
    if num1 == 0:
        break
    num2 = int(input('두번째 숫자 입력: '))

    r_list = cal(num1,num2)
    # save_list에 r_list를 저장
    save_list.append(r_list)

    # list 일 경우 *list = list[0],list[1],list[2],list[3]
    print("{},{} 결과값 : sum : {}, min : {}, mul : {}, div : {}".format(*r_list))

# 현재까지 입력한 숫자와 결과값을 모두 출력을 해보세요
print('[ 현재까지 입력한 숫자, 결과값 ]')
#print(save_list)
# 10, 20 결과값 : 30, -10, 200, 0.5

for i in save_list:
    print("{},{} 결과값 : {}, {}, {}, {}".format(*i))