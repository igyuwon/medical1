students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
]
cnt = len(students) + 1
while True:
    print("="*70)
    print('[학생성적프로그램]')
    print("="*70)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램 종료')
    print("="*70)
    choice = input('원하는 번호를 입력하세요:  ')
    print("="*70)

    if choice == '1':
        while True:
            name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요.(0. 취소) : ")
            if name == '0':
                print('학생 입력을 취소합니다.')
                break
            student = {}
            student['stuNo'] = 'S'+'{:03d}'.format(cnt)
            student['name'] = name
            kor = int(input('국어점수를 입력하세요. : '))
            student['kor'] = kor
            eng = int(input('영어점수를 입력하세요. : '))
            student['eng'] = eng
            math = int(input('수학점수를 입력하세요. : '))
            student['math'] = math
            total = kor + eng + math
            student['total'] = total
            avg = total/3
            student['avg'] = float("{:.2f}".format(avg))
            students.append(student)
            cnt += 1
            print("입력데이터 : ",student)
        
    elif choice == '2':
        while True:
            go = input('학생 성적 전체출력 하시겠습니까?.(1. ㄱㄱ, 0. 취소) : ')
            if go == '0':
                break
            print('[학생 성적 전체출력]')
            print("="*70)
            print('번호\t이름\t국어\t영어\t수학\t합계\t평균')
            print("="*70)
            for stu_dic in students:
                for stu_key in stu_dic:
                    print(stu_dic[stu_key],end = '\t')
                print()
            print("="*70)
        
    elif choice == '3':
        while True:
            search = input('찾을 학생의 이름을 입력하세요(0. 취소) : ')
            chk = 0
            if search == '0':
                break
            for stu_dic in students:
                if stu_dic['name'] == search:
                    print(f'[ {search} 학생의 데이터 ]')
                    print("="*70)
                    print('번호\t이름\t국어\t영어\t수학\t합계\t평균')
                    print("="*70)
                    for stu_key, stu_value in stu_dic.items():
                        print(stu_value, end='\t')
                    print()
                    print("="*70)
                    break
                chk += 1

            if chk == len(students):
                print(f'{search} 학생은 없습니다. 다시 입력하세요.')
        
    elif choice == '4':
        s_title = ['','국어','영어','수학']
        while True:
            search = input('찾을 학생의 이름을 입력하세요(0. 취소) : ')
            chk = 0
            if search == '0':
                break
            for stu_dic in students:
                if stu_dic['name'] == search:
                    break
                chk += 1
            if chk == len(students):
                print(f'{search} 학생은 없습니다. 다시 입력하세요.')
            else:
                print(f'{search} 학생의 데이터를 수정합니다.')
                while True:
                    print('[ 수정할 과목 선택 ]')
                    print("="*70)
                    print('1. 국어\t2. 영어\t3. 수학')
                    subject = int(input('수정하려는 과목을 선택하세요.(0. 취소) : '))

                    if subject == 1:
                        s_1 = 'kor'
                        print('[ {} 수정 ]'.format(s_title[subject]))
                        print('현재 {} 점수 : {}'.format(s_title[subject],students[chk]['kor']))
                        print("="*70)
                        score = int(input('수정할 국어점수를 입력하세요. : '))
                        students[chk][s_1] = score
                        # 수정 파트
                        students[chk]['total'] = students[chk]['kor'] +students[chk]['eng'] +students[chk]['math']
                        students[chk]['avg'] = float("{:.2f}".format(students[chk]['total']/3))
                        print('{}점수 : {}점으로 수정이 완료되었습니다.'.format(s_title[subject],students[chk][s_1]))
                        print("="*70)
                        print(students[chk])
                    elif subject == 2:
                        s_1 = 'eng'
                        print('[ {} 수정 ]'.format(s_title[subject]))
                        print('현재 {} 점수 : {}'.format(s_title[subject],students[chk]['eng']))
                        print("="*70)
                        score = int(input('수정할 영어점수를 입력하세요 : '))
                        students[chk][s_1] = score

                        # 수정 파트
                        students[chk]['total'] = students[chk]['kor'] +students[chk]['eng'] +students[chk]['math']
                        students[chk]['avg'] = float("{:.2f}".format(students[chk]['total']/3))
                        print('{}점수 : {}점으로 수정이 완료되었습니다.'.format(s_title[subject],students[chk][s_1]))
                        print("="*70)
                        print(students[chk])

                    elif subject == 3:
                        s_1 = 'math'
                        print('[ {} 수정 ]'.format(s_title[subject]))
                        print('현재 {} 점수 : {}'.format(s_title[subject],students[chk]['math']))
                        print("="*70)
                        score = int(input('수정할 영어점수를 입력하세요 : '))
                        students[chk][s_1] = score
                        
                        # 수정 파트
                        students[chk]['total'] = students[chk]['kor'] +students[chk]['eng'] +students[chk]['math']
                        students[chk]['avg'] = float("{:.2f}".format(students[chk]['total']/3))
                        print('{}점수 : {}점으로 수정이 완료되었습니다.'.format(s_title[subject],students[chk][s_1]))
                        print("="*70)
                        print(students[chk])
                    else:
                        print('과목 수정을 취소합니다.')
                        break
        if chk == len(students):
            print(f'{search} 학생은 없습니다. 다시 입력하세요.')

    elif choice == '5':
        while True:
            go = input('등수 처리를 하시겠습니까?(1.ㄱㄱ, 0. 취소) : ')
            if go == "0":
                break
            for i, stu_dic in enumerate(students):
                rank_cnt = 1
                for i_dic in students:
                    if stu_dic['total'] < i_dic['total']:
                        rank_cnt += 1
                stu_dic['rank'] = rank_cnt
            print('등수처리 완료.')
    elif choice == '6':
        while True:
            search = input("삭제하고자 하는 학생의 이름을 입력하세요.(0. 취소) : ")
            chk = 0
            if search == "0":
                break
            for s_dic in students:
                if s_dic["name"] == search:
                    break
                chk += 1
            if chk >= len(students):
                print("찾고자 하는 학생이 없습니다.")
            else:
                print("{} 학생을 찾았습니다.".format(search))
                s_input = input("{} 학생 성적을 삭제하시겠습니까?(1. ㄱㄱ, 0. 취소) : ".format(search))
                # 삭제
                if s_input != "1":
                    print("삭제를 취소합니다.")
                    break
                else:
                    del students[chk]
                    print("{} 학생성적이 삭제 되었습니다.".format(search))
                    print(students)
    elif choice == '0':
        print('프로그램을 종료합니다.')
        break