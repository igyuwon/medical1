# 1 -3 까지의 합
sum1 = 0+1+2+3

sum2 = 0 
sum2 = sum2 + 1 # 0 + 1 > 1
sum2 = sum2 + 2 # 1 + 2 > 3
sum2 = sum2 + 3 # 3 + 3 > 6

sum3 = 0 
for i in range(1,4,1): # i = 1,2,3
    sum3 = sum3 + i

print(sum1,sum2,sum3)
# 1- 100 까지의 합
s1,s2,s3 = 0,0,0
# 1 - 100 까지 짝수의 합 = (2로 나눳을때 나머지가 0인애들)
# 홀수 (2로 나눳을대 나머지가 1인애들) 의 합 if절을 사용
for i in range(1,101):
    s1 = s1 + i
    # print(i,end=' ')
    if i%2 == 0: # 짝수
        s2 = s2+i
    else: # 홀수
        s3 += i 

print('1-100까지의 합은 {}입니다'.format(s1))
print('1-100까지의 짝수 합은 {}입니다'.format(s2))
print('1-100까지의 홀수 합은 {}입니다'.format(s3))


# 1. 1-10 합
s = 0
for i in range(1,11):
    s += i

print('1-10 합 : {}'.format(s))


# num리스트 안에 있는 값들의 합
num = [1,2,3,4,5,6,7,8,9,10]
#  num[0]
t = 0 
for n in num:
    t += n
    #print(n)
print('num리스트의합 : {}'.format(t))

t1 = 0
for i in range(len(num)):
    t1 += num[i]
    #print(num[i])
print('num리스트의합 : {}'.format(t1))



