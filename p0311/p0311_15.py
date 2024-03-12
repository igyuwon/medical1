# 함수 선언
def cal(num1,num2):
    sum = 0
    if num1>num2:
        num1,num2 = num2,num1
    for i in range(num1, num2+1):
        sum += i
    return sum
# 두 수를 입력받아, 입력한 사이의 합계를 구하는 프로그램을 구현하세요.
# 1,10 -> 55 1+2+3...+10 = 55

sum = 0
num1 = int(input('첫번째 숫자를 입력하세요. : '))
num2 = int(input('두번째 숫자를 입력하세요. : '))

sum = cal(num1,num2)

print('합계 : ',sum)

