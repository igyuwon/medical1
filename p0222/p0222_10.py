# 동전 교환 

money = 1275
print('입력한 금액 : {}원'.format(money))

c500 = 0
c100 = 0
c50 = 0
c10 = 0 

# 500원 
c500 = money//500  # // 몫
money %= 500 # money = money%500  # % 나머지 270
print('500원 : {} 개'.format(c500))
print(money)

# 100원
c100 = money//100 
print('100원 : {} 개'.format(c100))
money %= 100
print(money)

# 50원
c50 = money//50 
print('50원 : {} 개'.format(c50))
money %= 50
print(money)

# 10원
c10 = money//10 
print('10원 : {} 개'.format(c10))
money %= 10 
print('잔돈 : {}'.format(money))