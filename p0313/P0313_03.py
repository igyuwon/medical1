# 랜덤으로 숫자 1개 생성
# 입력한 숫자보다 크면 작을 수를 입력하세요.
# 입력한 숫자보다 작은면 큰수를 입력하시오. 멘트
# 정답을 맞추면
# 총 입력한 횟수 : 7회
# 현재까지 입력한 숫자 : 1,5,7,6,8,4,50
# 현재까지 입력했던 숫자를 모두 출력하세요.
import random
ran_num = random.randint(1,100)
print(ran_num)
in_num = 0
cnt = 1
save_list = []
while True:
    print('[ 랜덤숫자 맞추기 게임 ]')
    in_num = int(input(f"{cnt}번째 도전! 숫자를 입력하세요. : "))
    save_list.append(in_num)
    
    if ran_num > in_num:
        print('입력한 숫자보다 큰 수를 입력해주세요.')
    elif ran_num < in_num:
        print('입력한 숫자보다 작은 수를 입력해주세요.')
    else:
        print('정답입니다.')
        break
    cnt += 1

# ====종료====
print('총 입력한 횟수 : ', cnt,'회')
print('현재까지 입력한 숫자 : ', save_list)