# 해보세요 
# 1. 숫자 두개를 입력받아서 나누기값 몫값 나머지값을 출력
# 나누기 : / , 몫: //, 나머지 %
n1 = int(input('첫번째 숫자를 입력해주세요 >> '))
n2 = int(input('두번째 숫자를 입력해주세요 >> '))

r1 = n1/n2
r2 = n1//n2
r3 = n1%n2

print(r1,r2,r3)


# 2. 3개의 수의 합을 구하세요
s1 = '100' # => input('숫자입력 >> ')
s2 = '100.123'
s3 = '99.9'

a1 = int(s1) 
a2 = float(s1)

result = int(s1) + float(s2) + float(s3)
print('합은 {}입니다'.format(result))