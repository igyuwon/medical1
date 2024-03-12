member = []

# 입력 : 이름, 점수 (input) ['홍길동', 90]
# 총 3명의 정보를 member리스트에 넣으세요 

# 1. 이름, 점수 입력을 받아 리스트를 만듦 
# for i in range(3):
#     name = input('이름을 입력하세요 > ')
#     score = int(input('점수를 입력하세요 >'))
#     m = [name, score]
#     member.append(m)

'''
name = input('두번째 학생의 이름을 입력하세요 > ')
score = int(input('두번째 학생의 점수를 입력하세요 >'))
m = [name, score]
member.append(m)

name = input('세번째 학생의 이름을 입력하세요 > ')
score = int(input('세번째 학생의 점수를 입력하세요 >'))
m = [name, score]
member.append(m)
'''

# m1 = []
# m1.append(name)
# m1.append(score)

# print(m)
# print(m1)

member = [['홍길동', 55], ['유관순', 80], ['이순신', 90]]
# 이름들을 먼저 출력해보고
print(member[0][0]) # 홍길동
print(member[1][0]) # 유관순
print(member[2][0]) # 이순신
# 점수들도 출력해보고 
print(member[0][1]) # 55
print(member[1][1]) # 80
print(member[2][1]) # 90
print(member) # [['홍길동', 90],['유관순', 91],['이순신', 95]]

# 60점 이상이면 홍길동님 불합격입니다. 유관순님 합격입니다
# member 변수 사용, for, if

for i in range(3): # i = 0,1,2
    name = member[i][0]
    score = member[i][1]
    # print('{}님 {}점입니다'.format(name, score)) 
    if score >= 60:
        print('{}님 합격입니다.'.format(name))
    else:
        print('{}님 불합격입니다.'.format(name))
        
