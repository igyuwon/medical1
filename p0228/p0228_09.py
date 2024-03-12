# 중첩 for
# for 안에 for 
for i in range(3): # i = 0,1,2
    print('i = ',i)
    for j in range(5): # j = 0,1
        print('j = ',j)
# i = 0 일때 
   # j = 0 , j = 1
# i = 1 일때
   # j = 0, j =1 
# i =2 일때
   # j = 0, j=1 




# for 문을 사용해서 2단을 출력
# 입력받은 숫자의 단을 출력하세요 >>
# 3을 입력받으면 3단 출력 4를 입력받으면 4단 출력 

n = 9 # 2 - 9

for i in range(1,10):
    print('{}*{}={}'.format(n,i,n*i)) # n단 
    
for i in range(2,10): # 2단부터 9단까지 출력 
    for j in range(1,10) : # *1 ~ *9
        print('{} * {} = {}'.format(i, j, i*j))
        
# 출력 형태 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
for j in range(5): # j = 0 1 2 3 4 
    print(j+1 ,'번째 출력')
    for i in range(1,6): # i = 1 2 3 4 5
        print(i, end=' ') # 1 2 3 4 5 를 한줄로 출력
    print() # 줄바꿈
print('for 끝')
# 전체 구구단
for i in range(2,10): # i = 2,3,4,5,6,7,8,9
    print('[{} 단]'.format(i))
    for j in range(1,10):
        print('{}*{}={}'.format(i,j,i*j),end= ' ')
    print()
# 짝수단만 출력해주세요
for i in range(2,10): # i = 2,3,4,5,6,7,8,9
    if i%2 == 0 : # i가 짝수라면
        print('[{} 단]'.format(i))
        for j in range(1,10):
            print('{}*{}={}'.format(i,j,i*j),end= ' ')
        print()
# 홀수단만 출력해보세요
for i in range(2,10): # i = 2,3,4,5,6,7,8,9
    if i%2 == 1 : # i가 홀수라면
        print('[{} 단]'.format(i))
        for j in range(1,10):
            print('{}*{}={}'.format(i,j,i*j),end= ' ')
        print()
# (* 1 , 3, 5, 7, 9 ) 출력
for i in range(2,10): # i = 2,3,4,5,6,7,8,9
    print('[{} 단]'.format(i))
    for j in range(1,10):
        if j%2 == 1:
            print('{}*{}={}'.format(i,j,i*j),end= ' ')
    print()
# ex) 3*1=3 3*3=9  3*5=15  3*7=21  3*9=27

