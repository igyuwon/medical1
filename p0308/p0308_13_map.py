# map -> 문자열을 정수형으로 모두 변환해서 리스트 저장
# today_list = ['2024','03','08']
# # today_list[0] = today_list[0]+10
# # print(today_list[0])
# print(today_list)
# t_list = list(map(int,today_list))
# print(t_list)

# nums = [1,2,3,4,5]
# nums2 = list(map(nums+5,nums))
# print(nums2)

# list = []
# 5개의 숫자를 입력하시오.
# for i in range(5):
#     list(map(int,input('숫자를 입력하세요. : ')))
#     # list.append(int(input('숫자를 입력하세요. : ')))

# print(list)

# map -> 정수형을 문자열로 모두 변환해서 리스트 저장
# int_list = [10,20,30,40,50]
# str_list = list(map(str,int_list))
# print(str_list)

# 함수를 사용해서 리스트의 값을 *10 변경 mapㄴ


# 리스트의 데이터 타입 : int
# list = []
# for i in range(5):
#     list.append(i) # 데이터타입 : int
# print(list)

# 리스트의 데이터 타입 : str
a_list = list(map(str,range(10)))
print(a_list)

# input의 데이터 int 변경해서 list 저장
a_list = list(map(int,input('숫자입력 : ')))
print(a_list)