import os
print('현재 운영체제 : ',os.name)
print('현재 폴더 위치 : ', os.getcwd())
print('현재 폴더 내 파일들 표시 : ',os.listdir())

# # 폴더 생성
# os.mkdir('hello')
# # 폴더 삭제
# os.rmdir('hello')

with open('students.txt','w') as f:
    f.write("1,'홍길동',100,99,87,286,95.33,2")

str = "1,'홍길동',100,99,87,286,95.33,2"
s_list = str.split(',')

for i in s_list:
    print(i)