# 해보세요 
# 1. 나이가 10살이상이고 150 이상만 탑승가능
# 나이, 키를 입력받아 
# [탑승가능] [탑승불가능]을 출력해보세요 
# input()함수를 사용할 경우 문자열로 입력받는다. 
# print()함수는 출력
age = int(input('나이를 입력하세요 >> '))
height = int(input('키를 입력하세요 >> '))
# print(age, height) 
# age = input('나이')
# age = int(age)
if age >= 10:
    if height >= 150:
        print('탑승가능')
    else:
        print('탑승불가능') # 나이는 10살이상이나 키미달
else:
    print('탑승불가능')

# 2. 숫자3개 (정수)를 입력받고, 연산1개(+-*/)를 입력받아 
# 조건문 연산자가 + 를 입력받으면, 
# a + b + c = d의 형태로 출력   (1 + 2 + 3 = 6 )
# 연산자가 -로 입력받으면 : ( 1 - 2 - 3 = -4 )
# +++ --- *** ///  (나누기값은 둘재자리까지 표현)
# 숫자3개로 계산기
a = int(input('첫번째 숫자 >> '))
b = int(input('두번째 숫자 >> '))
c = int(input('세번째 숫자 >> '))

cal = input('연사자를 입력하세요 (+,-,*,/)')
result = 0 

if cal == '+':
    result = a + b + c
    # print('{}+{}+{}={}'.format(a,b,c,result))
elif cal == '-':
    result = a - b - c
    # print('{}-{}-{}={}'.format(a,b,c,result))
elif cal == '*':
    result = a * b * c
    # print('{}*{}*{}={}'.format(a,b,c,result))
elif cal == '/':
    result = a / b / c
    # print('{}/{}/{}={:.2f}'.format(a,b,c,result))
else:
    print('잘못입력하셨습니다.')

print('{},{},{}연산의 결과값은 : {}'.format(a,b,c,result))