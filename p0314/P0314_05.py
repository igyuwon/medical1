numbers = [1,2,3,4,5,6,7,8,9,10]

print(numbers.index(5))
try:
    print(numbers.index(11))
except Exception as e:
    print('존재하지 않습니다.')
    print(e)

# index_list에 존재하면 위치값을 리턴
if 7 in numbers:
    print('7은 리스트에 존재합니다.')
else:
    print('리스트에 없습니다.')