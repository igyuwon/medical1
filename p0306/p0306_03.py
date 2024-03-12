import operator

# numbers에 있는 숫자들이 몇번 나왔는지
# 딕셔너리로 출력하시오.
numbers = [1,2,4,6,4,3,6,7,1,3,4,3,4,7,7,7,7,1,1,1,7]

counter = {}

for number in numbers:
    if number not in counter:
        counter[number] = 0
    counter[number] += 1

print(counter)
print(sorted(counter.items(),key = operator.itemgetter(1), reverse=True))

a_dic = {}
array = ["F", "D", "A", "C", "A", "C", "F", "B", "C", "E", "C", "C", "F", "A", "B", "E", "F", "E"]

for alpa in array:
    if alpa not in a_dic:
        a_dic[alpa] = 0
    a_dic[alpa] += 1

print(a_dic)
print(sorted(a_dic.items(),key = operator.itemgetter(1), reverse=True))