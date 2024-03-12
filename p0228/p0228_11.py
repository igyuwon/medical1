'''
주석 여러줄 쓸때
한줄 주석 # 주석 쓰셔도되고
control + / : 커서 있는 문장 주석 
tab :들여쓰기
shift + tab (들여쓰기 삭제 )
alt + shift + 위아래 방향키 (커서있는 문장 복사 )
'''
num = [100,200,300,400]
#       0   1    2   3
# for 문을 사용해서 하나씩 출력해보세요 2가지 방법 다 쓰기 
# in num
for n in num:
    print(n,end='\t')
print()
# in range(len(num))
for i in range(len(num)): # i = 0 1 2 3 
    print(num[i],end='\t')
print()
numlist = [[1,2],[3,4],[5,6]]
# [num[0][0],num[0][1]], [num[1][0],num[1][1]], num[2][0],num[2][1]]
# 변수 in 리스트이름 
for n in numlist: # [1, 2]  [3, 4]  [5, 6]
    for a in n:
        print(a, end=' ')
    print()
    # print(n,end='\t')
# in range 
for i in range(len(numlist)) : # for i in range(3)
    # print(i) # i = 0, 1, 2 
    # print(numlist[i])
    for j in range(len(numlist[i])):
        print(numlist[i][j], end=' ')
    print()

f = [['딸기',100,1000],['수박',100,500],['사과',100,1200],
     ['귤',100,300]]
# 요소 한개한개를 출력해보세요

# 과일 이름만 출력 
print(f[0][0], f[1][0], f[2][0], f[3][0])
for i in range(len(f)):
    print(f[i][0])
    
for i in range(len(f)): # i = 0, 1,2,3
    for j in range(len(f[i])): # j = 0 ,1 ,2
        print(f[i][j] , end= ' ') 
    # i =0, j = 0,1,2 f[0][0]  f[0][1]  f[0][2]
    # i =1, j = 0,1,2
    # i = 2, j = 0,1,2    
    print()

score = [90,80,70,100,95,85,100] 
#         0  1  2  3   4  5  6 
#   score[0] = 90
total = []
# 점수의 총합을 구하세요 숫자1개
sum = 0 
for s in score:
    sum = sum + s
print(sum)

sum1 = 0 
for i in range(len(score)): # for i in range(7): 
    sum1 += score[i]
    # print(i) # 0,1,2,3,4,5,6
    # print(score[i])
print(sum1)
# 그 점수를 total리스트에 넣어주세요
total.append(sum)
print(total) # [ 620 ]



