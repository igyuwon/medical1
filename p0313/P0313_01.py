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
    sum = num1 + num2
    min = num1 - num2
    mul  = num1 * num2
    div = num1 / num2

    return sum,min,mul,div
num1 = int(input('숫자 입력: '))
num2 = int(input('숫자 입력: '))
sum,min,mul,div = cal(num1,num2)
print("결과값 : sum : {}, min : {}, mul : {}, div : {}".format(sum,min,mul,div))


