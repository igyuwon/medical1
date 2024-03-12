# 입력 : 이름, 아이디, 비밀번호 (input) 
# 5명을 입력받아서 member리스트를 만드세요 
member = [] # [[홍길동, aaaa,1111],[유관순, bbbb, 2222]]
for i in range(5):
    name = input('이름을 입력하세요 >> ')
    uid = input('아이디를 입력하세요 >> ')
    upw = input('비밀번호를 입력하세요 >> ')
    m = [name, uid, upw]
    member.append(m)
# n명 입력은 ?? 
print(member) #[[홍길동, aaaa,1111],[유관순, bbbb, 2222], ...]
'''  member리스트를 
이름    아이디  비밀번호 
홍길동   aaaa    11111
이순신   bbbb    22222
유관순
김구   
형식으로 출력해보세요
for문을 사용
''' 
# member리스트를 사용해서 출력
a = len(member) # 5 
print('이름\t아이디\t비밀번호')
for i in range(len(member)): # i 0 1 2 3 4 
    print('{}\t{}\t{}'.format(member[i][0],member[i][1],member[i][2]))
    
print('{}\t{}\t{}'.format(member[0][0],member[0][1],member[0][2]))
print('{}\t{}\t{}'.format(member[1][0],member[1][1],member[1][2]))
print('{}\t{}\t{}'.format(member[2][0],member[2][1],member[2][2]))
print('{}\t{}\t{}'.format(member[3][0],member[3][1],member[3][2]))
print('{}\t{}\t{}'.format(member[4][0],member[4][1],member[4][2]))