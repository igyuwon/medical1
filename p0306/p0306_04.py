fruit = {'peach' : '복숭아','orange' : '오렌지','apple' : '사과', 
         'pear' : '배', 'grapes' : '포도', 'mango' : '망고', 'kiwi' : '키위'}
# cnt = 0
answer = 0
wrong = 0
# 복숭아 영어로 입력하시오.
for f in fruit:
    # print('key : ',f,'value : ',fruit[f])
    eng_in = input('{}를 영어로 입력하세요. : '.format(fruit[f]))
    print('입력한 단어 : {}'.format(eng_in))
    # 프로그램 하시오.
    if f == eng_in:
        print('정답입니다.')
        # cnt += 1
        answer += 1
    else:
        print('오답입니다. 정답은 {}입니다.'.format(f))
        wrong += 1

# print('총 {}개 맞히셨습니다. 정답 : {}, 오답 : {}'.format(cnt, cnt, len(fruit)-cnt))

print('총 {}개 맞히셨습니다. 정답 : {}, 오답 : {}'.format(answer, answer, wrong))