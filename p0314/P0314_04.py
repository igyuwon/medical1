# 파일 1개 생성

# file open
file = open('memo.txt', 'w', encoding = 'utf8')

try:
    # file write
    file.write('안녕하세요1.\n')
    file.write('안녕하세요2.\n')
    print(1/0)
    file.write('안녕하세요3.\n')
    file.write('안녕하세요4.\n')
except Exception as e: # Exception : 예외에 대한 설명을 출력
    print('저장시 에러가 났습니다.')
    print(e)
finally:
    # 파일닫기
    file.close() # 예외 발생 시, 예외 발생하지 않아도 무조건 실행

# 파일 닫기
