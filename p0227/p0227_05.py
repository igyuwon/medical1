# 0 - 20 사이의 5의 배수로 이루어진 리스트를 만들어보세요
# 출력 : [0,5,10,15,20]
num = []
# for, append
for i in range(21):    
    if i % 5 == 0 :
        num.append(i)
        # print(i) # i의 값이 0,5,10,15,20...
print(num)

lan = ['c','python','java','jquery','css']

# 1. 하나하나 출력해보기  - for 사용
#    1) in 리스트명 사용
for language in lan:
    print(language) 
#    2) in range() 사용
for i in range(len(lan)): # for i in range(5) i = 0,1,2,3,4..
    print(lan[i])
# 2. 카운터변수 i 사용해서.
#    1. c
#    2. python
#    3. java 
#    4. jquery
#    5. css 
#    이렇게 출력해보기

for i in range(5): #  i = 0,1,2,3,4..
    # print(i)
    # print(lan[i])
    print('{}. {} '.format(i+1,lan[i]))
    
for i in range(1,6,1): #  i = 0,1,2,3,4..
    # print(i)
    # print(lan[i])
    print('{}. {} '.format(i,lan[i-1]))


num = [1,-1,2,3,-4,5,6,-8,9,-10]
# 양수면 양수 음수면 음수 출력 for사용
# 1: 양수
# -1: 음수
# 2: 양수 ..
# for 변수 in 리스트명:
for n in num:
    print(n , end=' : ')
    if n >= 0 :
        print('양수')
    else:
        print('음수')

for n in num:
    if n >= 0 :
        print('{} : 양수'.format(n))
    else:
        print('{} : 음수'.format(n))

for i in range(len(num)):  # i : 0,1,2,3.. 
    if num[i] >= 0 :
        print('{} : 양수'.format(num[i]))
    else:
        print('{} : 음수'.format(num[i]))

    

