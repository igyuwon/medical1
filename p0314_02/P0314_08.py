# medical_1.csv 파일을 읽어와서 출력하시오.

f = open('medical_1.csv','r',encoding='UTF-8')
cnt = 0
sum = 0
s_list = []
while True:
    content = f.readline()
    if cnt == 0 :
        cnt+=1
        continue
    if content == '': break
    c_list = content.split(',')
    c_list[1] = int(c_list[1])
    sum +=  c_list[1]
    print(c_list,len(c_list))
print('기초생활수급대상자 전체 수 : ',sum)

# 파일 닫기
f.close()


# f = open('medical_1.csv','r',encoding='UTF-8')
# cnt = 0s
# s_list = []
# while True:
#     content = f.readline()
#     if cnt == 0 :
#         cnt+=1
#         continue
#     s_list.append(content.strip().split(','))
#     if content == '': break
#     # print(content,end='')
# f.close()
# del s_list[len(s_list)-1]
# print(s_list)
# sum = 0
# for i in s_list:
#     sum += int(i[1])
#     print(i[1])
# print(sum)


