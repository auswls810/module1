import pymysql
import action
#첫번쨰 화면 - 로그인 화면 (로그인/회원가입)
while True: 
    print('#'*30)
    print('1.로그인\n2.회원가입\n3.종료')
    print('#'*30)
    first_pg =input('(1-3) 메뉴를 선택해 주세요.\n >> ')    
    ####회원가입####
    if first_pg == '2': 
        action.plus()
    #####로그인######
    elif (first_pg =='1'):
        login_id = input('아이디: ')
        login_pw= input('패스워드: ')
        login = action.login(login_id,login_pw)
        #####user mode######
        if login.check() == 1: 
            print('\n'+'*'*15)
            print('로그인 성공')
            print('*'*15+'\n')
            while True:
                print('''##################################
##########!!!WELCOME!!!###########
##################################
#          1.상품 목록            #
#          2.주문 내역            #
#          3.계정 정보 수정       #
#          4.회원 탈퇴            #
#          5.로그아웃             #
##################################''')
                usr_pg =input('(1-5) 메뉴를 선택해 주세요.\n >> ')
                ####1.상품목록#####
                if usr_pg == '1':
                    while True:
                        print('\n**전체 상품 목록**')
                        print('\n 상품 \t \t 가격 \t 재고량 \t')
                        login.itemlist()
                        print('\n 1.상품찾기 2.상품주문 3.HIT ITEM 4.뒤로가기')
                        choice = input('\n 메뉴를 입력헤 주세요 >> ')
                        if choice == '1': #1)상품찾기
                            login.findlist()
                            input('뒤로가기 >> (Enter)')
                        elif choice =='2': #2)상품주문
                            login.order()
                            login.upoder()
                            login.total()
                            input(' \n !!주문완료!! >> (Enter) ')
                        elif choice =='3': #3)top3상품 보기
                            login.hotitem()                         
                        elif choice =='4': #3)뒤로가기
                            break
                        else:
                            print('\n!!잘못된 입력입니다!!\n')

                ######2.주문내역#######
                elif usr_pg =='2':
                    while True:
                        print('\n**내 주문 목록**')
                        print('\n 주문번호 \t 상품명 \t 가격 \t 주문량 \t 합계 \t\t 주문날짜')
                        login.orderlist()
                        choice1 = input('\n1.주문취소 2.종료\n메뉴를 입력헤 주세요 >> ')
                        if choice1 == '1':
                            login.ordercancel()
                            print('\n'+'*'*15)
                            print('주문 취소 성공')
                            print('*'*15+'\n')
                        elif choice1 == '2':
                            break
                        else:
                            print('\n!!잘못된 입력입니다!!\n')

                ######3.정보수정######
                elif usr_pg == '3':
                    while True:
                        print('\n**현재 내정보**')
                        print(' ID \t PW \t NAME \t ADDR \t EMAIL \t\t\t NUM \t ')
                        login.mylist()
                        change = input('\n1.패스워드 변경\n2.이름변경\n3.주소변경\n4.이메일변경\n5.전화번호변경\n6.종료\n\n 메뉴를 입력헤 주세요 >>')
                        if change == '1':
                            login.uppwlist()
                        elif change == '2':
                            login.upnamelist1()
                        elif change == '3':
                            login.upaddrlist1()
                        elif change == '4':
                            login.upemaillist1()
                        elif change =='5':
                            login.upnumlist1()
                        elif change == '6':
                            break
                        else:
                            print('\n!!잘못된 입력입니다!!\n')

                #####4.회원탈퇴######
                elif usr_pg == '4':
                    out = input("\n회원탈퇴를 원하십니까?(Y)\n>>> ")
                    if out == 'Y':
                        login.deluser()
                        print('\n'+'*'*15)
                        print('회원탈퇴 성공')
                        print('*'*15+'\n')
                    else:
                        print('\n'+'*'*15)
                        print('회원탈퇴 취소')
                        print('*'*15+'\n')
                   
                #####5.로그아웃#####
                elif usr_pg == '5':
                    print('\n'+'*'*15)
                    print('LOGOUT')
                    print('*'*15+'\n')
                    break
                else:
                    print('\n!!잘못된 입력입니다!!\n')
        #########admin mode##########
        elif login.check() == 2: 
            print('\n'+'*'*15)
            print('로그인 성공')
            print('*'*15+'\n')
            while True:
                print('''##################################
##########ADMINISTRATOR###########
##################################
#        1.회원목록 관리         #
#        2.주문목록 관리         #
#        3.상품목록 관리         #
#        4.로그아웃              #
##################################''')
                admin_pg =input('(1-4) 메뉴를 선택해 주세요.\n >> ') 
                 ##1.회원관리페이지##
                if admin_pg == '1':
                    while True:
                        print('\n**전체 회원목록**')
                        print(' ID \t PW \t NAME \t ADDR \t EMAIL \t\t NUM \t ')
                        login.memlist()
                        manage_mem = input(' \n**회원관리** \n1.회원탈퇴 \n2.회원수정 \n3.VIP회원조회\n4.종료\n\n>>(1-3)메뉴를 선택해 주세요\n')
                        if manage_mem == '1':##1)회원탈퇴
                            login.deletemem()
                        elif manage_mem =='2':##2)회원 정보 수정 
                            print('\n1.패스워드 변경\n2.이름변경\n3.주소변경\n4.이메일변경\n5.전화번호변경')
                            login.updatemem_admn()
                            if login.updatemem_admn() == 1:
                                print("잘못된 상품번호입니다. 다시 시도해 주세요.") 
                        elif manage_mem =='3':##3)vip회원조회
                            login.vipmem()
                            input('\n종료 >>(Enter)')
                        elif manage_mem =='4':
                            break    
                        else:#오류 처리
                            print('\n!!잘못된 입력입니다!!\n')
                ##2.주문관리페이지##
                elif admin_pg == '2':  
                    while True:
                        print('**전체 주문 목록**')
                        print(' No \t user_id \t product \t price \t order_qty \ttotal \t ')
                        login.orderlist_admin()
                        oder_choice=input('\n1.주문변경 \n2.주문취소 \n3.종료\n 입력>>> ')
                        if oder_choice == '1':
                            login.change_order()
                        elif oder_choice == '2':
                            login.delorder()
                        elif oder_choice == '3': 
                            break   
                        else:
                            print('\n!!잘못된 입력입니다!!\n')    
                ##3.상품관리페이지##
                elif admin_pg == '3':
                    while True:
                        print('\n**전체 상품 목록**') 
                        print('\n 상품번호 \t 상품명 \t 가격 \t 남은 수량')
                        login.itemlist_admin()   
                        choice2 = input('\n1.상품 정보 수정  2.상품 추가  3.상품 삭제 4.종료\n>>(1-4)메뉴를 선택해 주세요: ') 
                        if choice2 == '1': #1)상품 정보 수정
                            print('\n1.상품이름변경 2.상품가격변경 3.상품수량변경 [취소:(Enter)]')
                            login.updateitem()
                        elif choice2 == '2':#2)상품 추가
                            login.additem()
                        elif choice2 == '3':#3)상품 삭제
                            login.delitem()
                        elif choice2 == '4':#4)종료
                            break
                        else:# 오류처리
                            print('\n!!잘못된 입력입니다!!\n')                 
                ##4.로그아웃###
                elif admin_pg == '4':
                    print('\n'+'*'*15)
                    print('LOGOUT')
                    print('*'*15+'\n')
                    break              
                else:#예외처리
                    print("\n##잘못된 선택입니다 다시 선택해주세요.##\n")
        else:
            print('**아이디 혹은 패스워드 오류 다시 시도해 주세요**')

    elif first_pg =='3':
        break
    else:
        print('#'*30)
        print("\n##잘못된 선택입니다 다시 선택해주세요.##\n")

