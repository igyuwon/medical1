
id = 'admin'
pwd = '1111'

uid = input('아이디를 입력해주세요 >> ')
upw = input('비밀번호를 입력해주세요 >> ')

if (id == uid) and (pwd == upw): # and True - True 
    print('로그인 되었습니다. ')
else:
    print('아이디가 일치하지 않거나 비밀번호가 일치 하지 않습니다')
    print('다시 입력해주세요')

# 입력한 아이디가 같은면 비밀번호가 일치하는 비교해서 
# 같으면 [로그인되었습니다] 아니면[비밀번호가 일치하지 않습니다.]
# 입력한 아이디가 다르면 [아이디가 일치하지 않습니다]
if id == uid :
    
    if pwd == upw: 
        print("로그인되었습니다")
    else:
        print('아이디가 일치하지만 비밀번호가 틀렸습니다. ')
else:
    print('아이디가 일치하지 않습니다. ')