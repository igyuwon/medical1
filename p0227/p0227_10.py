num = []
# for문을 사용해서 1-10까지 숫자를 num에 채우세요 
for i in range(1,11):
    # print(i)
    num.append(i)
print(num) # [1,2,3,4,5,6,7,8,9,10]
# 한 줄로 표현 할 수 도 있다 
num1 = [i for i in range(1,11)] 

print(num1)
num2 = []
# 1-10까지 짝수를 num2리스트에 넣으세요
for i in range(1,11):
    if i % 2 == 0 :
        num2.append(i)
        # print(i)    
print(num2) # [2,4,6,8,10]

# 1 ~ 10까지의 합 for문을 사용해서 구할 수 있음.
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num리스트 를 사용해서 1-10까지의 합을 구해보세요 
s1 = 0 # 최종 더하기에 사용될 변수 
for n in num:
    s1 += n 
    # print(n, end=' ') 
print(s1)
s2 = 0 # 최종 더하기에 사용될 변수
for i in range(len(num)): 
    s2 = s2+ num[i]
    #print(num[i],end=' ')
print(s2)
# num리스트 내 의 숫자들의 합을 구하세요 
# num2리스트 내 숫자들의 합을 구하세요 
s3 = 0 # 최종 더하기에 사용될 변수
for n in num2:
    s3 = s3 + n
    # print(n, end=' ')
s4 = 0 # 최종 더하기에 사용될 변수
for i in range(len(num2)):
    s4 = s4+num2[i]
print(s3, s4)