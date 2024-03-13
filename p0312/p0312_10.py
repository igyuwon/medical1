# 카드 종류 : SPADE,DIAMOND,HEART,CLOVER 4종류
# 카드 숫자 : A,2,3,4,5,6,7,8,9,10,J,Q,K 13장
# 카드 총 수 : 52

import random

shape_list = ['SPADE','DIAMOND','HEART','CLOVER']
num_list = [0] * 13
card_list = [[0] * 2 for i in range(52)]

for i in range(1, 14):
    num_list[i - 1] = i

num_list[0] = 'A'
num_list[10] = 'J'
num_list[11] = 'Q'
num_list[12] = 'K'

my_card = []

def card_creat():
    cnt = 0

    for i in shape_list:
        for j in range(13):
            card_list[cnt] = [i, num_list[j]]
            cnt += 1
    print(card_list)

def card_shuffle():
    random.shuffle(card_list)
    print(card_list)

def card_share():
    arr_num = 0
    for i in range(5):
        print(card_list[arr_num])
        my_card.append(card_list[arr_num])
        arr_num += 1

def card_print():
    print(my_card)

while True:
    print('-' * 40)
    print('[ 카드 프로그램 ]')
    print('1. 카드생성')
    print('2. 카드섞기')
    print('3. 카드 5장 나눠주기')
    print('4. 카드 5장 확인주기')
    print('0. 종료')
    print('-' * 40)

    choice = int(input('원하는 번호를 입력하세요 : '))
    print('-' * 40)

    if choice == 1:
        card_creat()
    elif choice == 2:
        card_shuffle()
    elif choice == 3:
        card_share()
    elif choice == 4:
        card_print()
    else:
        print('프로그램을 종료합니다.')
        break