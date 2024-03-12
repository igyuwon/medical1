n1 = int(input('첫번째 숫자를 입력해주세요 >> '))
n2 = int(input('두번째 숫자를 입력해주세요 >> '))
sum = 0
# 만약에, n1이 n2보다 크다면 둘의 값을 바꿔라 
if n1 > n2: # n1,n2를 비교해서 n1이 작을경우
    n1,n2 = n2,n1 # n2의 값과 n1의 값을 서로 바꿔줌 
# 1. n1 부터 n2까지의 합 
for i in range(n1,n2+1): # range(시작, 끝+1, 1 )
    sum = sum + i 
print(sum)
# a ,b = 10, 8
# a, b = b, a # 숫자 바꾸기
# print('a',a,'b',b)
odd_list = [] # 3. n1-n2까지의 홀수 값을 저장
for i in range(n1, n2+1):
    if i%2 == 1:
        odd_list.append(i)
        #print(i)


print(odd_list) # [1,3,5,7,9]