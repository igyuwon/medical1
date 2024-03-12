# 점수를 입력받아서
# 1. 90점이상이면 A 80점이상이면 B 
# 70점이상이면 C 나머지는 F를 출력해보세요 (elif)
num = int(input('점수를 입력하세요 >> '))

# 90점이상이 시작
if num >= 90:
    print('90점이상입니다 ')
    if num >= 98:
        print('A+')  
    elif num > 93 :
        print('A') 
    else:
        print('A-') # 91
        
    print('AAAA')
# 90점이상 끝
elif num >= 80:
    print('B')
elif num >=70:
    print('C')
else:
    print('F')


# 2. 98점이상 A+ 90-93사이는 A- 
# B+, B-, C+, C- (중첩 if)