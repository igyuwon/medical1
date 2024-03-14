# import datetime
# from datetime import datetime
import datetime

# print(datetime.now(timezone('Asia/Seoul')))

# print('현재시각 출력')
# now = datetime.now()

# print(now.year,"년")
# print(now.month,"월")
# print(now.day,"일")
# print(now.hour,"시")
# print(now.minute,"분")
# print(now.second,"초")

now = datetime.datetime.now()
print("시간을 포맷에 맞춰 출력하기")
# 일자시간의 포맷을 설정하는 함수
output_a = now.strftime("%Y년 %m월 %d일 %H %M분 %S초")
output_b = now.strftime("%Y-%m-%d %H:%M:%S")
output_c = now.strftime("%Y/%m/%d %H:%M:%S")
output_d = now.strftime("%Y/%m/%d")
print(output_a)