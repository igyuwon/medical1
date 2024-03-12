import datetime

now = datetime.datetime.now() # 현재를 가져옴 
print(now)
# 2024-02-23 13:03:09.195335
month = 6 # now.month # 현재 월 
# 현재가 봄 여름 가을 겨울 
# . 3,4,5 봄. 6,7,8 여름. 9, 10, 11 가을 . 12,1,2  겨울 
# elif를 사용하세요 
if 3 <= month <= 5: # 3,4,5
    print('봄')
elif 6 <= month <= 8:
    print('여름')
elif 9 <= month <= 11:
    print('가을')
else:
    print('겨울')
    
if (month == 3) or (month ==4) or (month == 5): # 3,4,5
    print('봄')
elif month == 6 or month ==7 or month == 8:
    print('여름')
elif month == 9 or month ==10 or month == 11:
    print('가을')
else:
    print('겨울')