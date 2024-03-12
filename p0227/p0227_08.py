# 반복문
'''
for 변수 in range(시작값, 끝값+1, 증가값) :
'''
for i in range(3): # i = 0 , 1, 2
    print('안녕')
    # i = 0 일때
    # i = 1 일때
    # i = 2 일때 

for i in range(3): # i = 0, 1, 2
    print(i)

# i = 0,1,2,3... 
# i = 1,2,3,4,5.. 
for i in range(100):
    print(i+1)

sum1 = 0 
for i in range(1,6,1):
    sum1 = sum1 + i 
    
# 1. 숫자 한개를 입력받아서 1부터 입력한 수 까지의 합을 구하세요 
n1 = 100 #int(input('숫자를 입력해주세요 >> '))#100 # 1에서 100까지 (1 + ... + 100 )
# for i in range (1,   ): 
#     합계
# 합계 출력
sn = 0 # 총합을 넣을 변수 선언 
for i in range(1,n1+1):
    sn = sn+i # i = 1, i = 2, i =3 
    # print(i, end=' ') 
print('{}부터 {}까지의 총합은 {}입니다.'.format(1,n1,sn))
# 짝수의 합만 구함 (2+4+6+8+..+100)
# 짝수만 출력
s1 = 0 # 짝수의 합을 넣을 변수 
for i in range(1,n1+1):
    if i % 2 == 0: # 짝수일때 
        s1 = s1 + i # i = 2, i =4, i= 6
        # print(i, end=' ')
print('{}부터 {}까지의 짝수의 총합은 {}입니다.'.format(1,n1,s1))

# 1-10까지의 곱 
s2 = 1 
for i in range(1,11):
    s2 = s2 * i 
    # i = 1 > 1*1 > 1
    # i = 2 > 1*2 > 2
    # i = 3 > 2*3 >6

print(s2)