# 1. 변수선언 
score = [
    [80,90,85] ,[70,80,90],[84,92,80],[72,81,76]    
]

name = ['홍길동','유관순','이순신','김구']
total = []
# 2. 코딩
# 2 - 1) 요소 하나하나 출력해보세요 80 90 85 70 80 90 ... 
for i in range(len(score)): # i = 0,1,2,3
    # print(score[i])
    for j in range(len(score[i])): # j = 0, 1, 2 
        print(score[i][j])
# 2 - 2) 작은 요소의 합을 구해서 total 넣어주세요 
t1 = 0 
# for a in score:
#     print('리스트입니다', a) # [80,90,85] [70,80,90]
#     t1 = 0
#     for b in a :
#         print('요소입니다', b)
#         t1 = t1+ b 
#     total.append(t1)

score = [[80,90,85] ,[70,80,90],[84,92,80],[72,81,76]]
for i in range(len(score)): # i = 0,1,2,3
    s = 0 
    # print(score[i])
    # i = 0, score[0][0] + score[0][1] + score[0][2] = s 
    # i = 1, score[1][0] + score[1][1] + score[1][2] = s 
    # i = 2, score[2][0] + score[2][1] + score[2][2] = s 
    for j in range(len(score[i])): # j = 0, 1, 2 
        s= s + score[i][j]
    total.append(s)
# 3. 출력 
# 3 - 1) total = [255,240,256,229]
print(total) # [255, 240, 256, 229]
#  name = ['홍길동','유관순','이순신','김구']
# 3 - 2) 250 미만 불합격 250이상 합격 ex)홍길동님 합격입니다 출력
for i in range(4): # i = 0,1,2,3
# for i in range(len(total)):
# for i in range(len(name)):
    if total[i] >=250 :
        print('{}님 합격입니다'.format(name[i]))
    else:
        print('{}님 불합격입니다'.format(name[i]))
        
