# 해보세요
# 성별, 키를 입력받아서 
# 남자일 경우 (m)  172.5이상이면 [평균이상] 이하면 [평균이하]
# 여자일 경우 (f) 159.6 이상이면 [평균이상] 이하면 [평균이하]
# 그외는 [잘못입력하셨습니다] 라고 출력해보세요 
gender = input('성별을 입력하세요 (m M / f F)>> ')
height = float(input('키를입력하세요 >> ') ) #172.6

if gender == 'm' or gender == 'M' :
    print('남자')
    # 남자일 경우만 
    if height >= 172.5: 
        print('평균이상입니다')
    else: 
        print('평균이하입니다')
elif gender == 'f' or gender =='F':
    print('여자')
    if height >= 159.6 :
        print('평균이상입니다')
    else:
        print('평균이하입니다')
else:
    print('잘못입력하셨습니다. ')
