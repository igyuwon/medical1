# k001.csv 파일에서 전국 인원수를 출력하시오.
f = open('k001.csv','r',encoding='UTF-8')
cnt = 0
sum = 0
while True:
    content = f.readline()
    if cnt == 0 :
        cnt+=1
        continue
    if content == '': break
    c_list = content.split(',')
    c_list[4] = int(c_list[4])
    sum +=  c_list[4]
print(c_list)
print('전국인원 수 : ',sum)

# 파일 닫기
f.close()