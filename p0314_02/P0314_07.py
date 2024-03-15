# str.txt 파일의 내용을 모두 출력하시오.
import os
# # str.txt 파일 내용을 읽어와서
# # str1.txt에 그 내용을 추가해보세요.

# 파일 열기
f = open('str.txt','r',encoding='utf8')

# 파일 읽기
while True:
    content = f.readline()
    if content.strip() == '': break # 빈공백 enter키 삭제
    print(content,end = '')
# 파일 닫기
f.close()

f = open('str.txt','r',encoding = 'utf8')
ff = open('str1.txt','a',encoding='utf8')
while True:
    content = f.readline() # 파일 내용을 읽어오기
    if content.strip() == "": break
    ff.write(content+"") # 파일 내용을 추가하기
f.close()
ff.close()

fff = open('str1.txt','r',encoding='utf8')
while True:
    content = fff.readline()
    if content.strip() == '': break
    print(content,end='')
fff.close()
#============내가 한거 ==================
# f = open('str.txt','r',encoding='utf8')
# while True:
#     con = f.readline()
#     if con == "": break
#     print(con, end = '')
#     ff = open('str1.txt','a',encoding='utf8')
#     ff.write(con+'')
# f.close()
# ff.close()
# print('='*40)

# fff = open('str1.txt','r',encoding='utf8')
# while True:
#     con = fff.readline()
#     if con == "": break
#     print(con, end = '')
# fff.close()

# f = open('str1.txt','r',encoding='utf8')
# while True:
#     con = f.readline()
#     if con == "": break
#     print(con, end = '')
#     ff = open('str2.txt','a',encoding='utf8')
#     ff.write(con+'')
# f.close()
# ff.close()
# print('='*40)
# # str.txt 파일 내용을 읽어와서
# # str1.txt에 그 내용을 추가해보세요.

# fff = open('str2.txt','r',encoding='utf8')
# while True:
#     con = fff.readline()
#     if con == "": break
#     print(con, end = '')
# fff.close()

