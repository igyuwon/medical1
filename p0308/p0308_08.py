import random

a = '1조123456'
b = '9조123456'

# print(a[0])
# print(a[-1])
# print(a[-2])

# # 방법 1
# for i in range(len(a),0,-1):
#     print(a[i-1])
# print('-'*40)
# # 방법 2
# for i in range(len(a)):
#     print(len(a)-1-i)
cnt = 0
for i in range(len(a),0,-1):
    if i==2: continue # 조는 건너뛰기
    if a[i-1]!=b[i-1]:
        break
    else:
        cnt += 1 # 맞는 횟수 1증가
if cnt == 0:
    print('완전 꽝입니다.')
elif cnt == 1:
    print('6번째 자리가 맞았습니다. 당첨금액 1만원')
elif cnt == 2:
    print('5,6번째 자리가 맞았습니다. 당첨금액 10만원')
elif cnt == 3:
    print('4,5,6번째 자리가 맞았습니다. 당첨금액 100만원')
elif cnt == 4:
    print('3,4,5,6번째 자리가 맞았습니다. 당첨금액 1000만원')
elif cnt == 5:
    print('2,3,4,5,6번째 자리가 맞았습니다. 당첨금액 1억원')
elif cnt == 6:
    print('1,2,3,4,5,6번째 자리가 맞았습니다. 당첨금액 10억원')
elif cnt == 7:
    print('조,1,2,3,4,5,6번째 자리가 맞았습니다. 당첨금액 100억원')
    



