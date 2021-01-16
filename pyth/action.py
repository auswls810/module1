import pymysql
conn = pymysql.connect(host='172.17.0.2', user='root', password='',port=3306, db='mydb')
cursor = conn.cursor()
def plus(): #회원가입 함수
    user_id = input('아이디: ')
    user_pw= input('패스워드: ')
    user_name= input('이름: ')
    user_addr= input('주소: ')
    user_email= input('이메일: ')
    user_num= input('전화번호: ')
    checksql = 'select id from users where id=%s'
    cursor.execute(checksql,user_id)
    data = cursor.fetchall()
    if len(data)>0:
        return print('이미 존재하는 아이디입니다. 다시 시도해 주세요')
    else:
        addsql = '''INSERT INTO users(id, pw, name, addr, email, num) VALUES(%s, %s, %s,%s, %s, %s)'''
        cursor.execute(addsql,(user_id,user_pw,user_name,user_addr,user_email,user_num))
        conn.commit()
        print("회원가입 완료!")

class login():  
    def __init__(self,lo_id,lo_pw):
       self.lo_id = lo_id
       self.lo_pw = lo_pw
    
    def check(self): #유저계정인지 관리자 계정인지 체크하는 함수
        loginsql ='SELECT id, pw FROM users WHERE id=%s and pw=%s'
        cursor.execute(loginsql,(self.lo_id, self.lo_pw))
        data = cursor.fetchall()
        if len(data)>0:
            return 1
        elif self.lo_id == 'admin' and self.lo_pw=='admin1234':
            return 2
        else:
            return 3

    def memlist(self): #관리자 -전체 유저 조회 함수
        memlsitsql = 'select * from users'
        cursor.execute(memlsitsql)
        data = cursor.fetchall()
        for row in data:
            print(" {0} \t {1} \t {2} \t {3} \t {4} \t {5} \t ".format(row[0],row[1],row[2],row[3],row[4],row[5]))
    
    def deletemem(self): #관리자 -회원 탈퇴 함수
        del_id = input('\n>> 삭제할 회원의 아이디를 입력하세요\n')
        seldelsql= 'select id from users where id = %s'
        cursor.execute(seldelsql,del_id)
        data = cursor.fetchall()
        if len(data)>0:
            deletesql = 'delete from users where id = %s'
            cursor.execute(deletesql,del_id)
            conn.commit()
            print('\n'+'*'*15)
            print('삭제완료')
            print('*'*15+'\n')
        else:
            print('존재하지 않은 유저입니다')
    def updatemem_admn(self):#관리자 -회원 수정 함수
        print('')
        up_id = input('\n(1-5)메뉴를 선택하세요')
        upload = input('\n>>수정할 아이디를 입력하세요: ')
        upload1 = input('\n>>수정할 내용을 입력하세요: ')
        if up_id == '1':
            updatesql = 'update users set pw=%s where id=%s '
        elif up_id =='2':
            updatesql = 'update users set name=%s where id=%s'
        elif up_id =='3':
            updatesql = 'update users set addr=%s where id=%s'
        elif up_id =='4':
            updatesql = 'update users set email=%s where id=%s'
        elif up_id =='5':
            updatesql = 'update users set num=%s where id=%s'  
        elif up_id == '6':
            return 1
        else:
            return print('존재하지 않은 선택지 입니다.') 
        cursor.execute(updatesql,(upload1,upload))
        conn.commit()
        
    def itemlist(self): #유저 - 전체 상품 항수
        itemsql = 'select * from product '
        cursor.execute(itemsql)
        data = cursor.fetchall()
        for row in data:
            print(" {0} \t {1} \t {2} ".format(row[1],row[2],row[4]))
    
    def additem(self): #관리자 - 상품 추가 함수
        prid = input('상품의 이름을 입력하세요: ')
        prpr = input('상품의 가격을 입력하세요: ')
        prqty = input('상품의 재고량을 입력하세요: ')
        addsql = 'insert into product(pr_name,pr_price,pr_qty,rest_qty) values(%s,%s,%s,pr_qty)'
        cursor.execute(addsql,(prid,prpr,prqty))
        conn.commit()
        print('\n**상품 추가 완료**')

    def updateitem(self): #관리자 -상품 수정 함수
        up_id = input('\n(1-3)메뉴를 선택하세요\n>>>')
        upload = input('\n>>수정할 상품번호를 입력하세요: ')
        upload1 = input('\n>>수정할 내용을 입력하세요: ')
        if up_id == '1':
            updatesql = 'update product set pr_name=%s where no=%s '
        elif up_id =='2':
            updatesql = 'update product set pr_price=%s where no=%s '
        elif up_id =='3':
            updatesql = 'update product set pr_qty=%s, rest_qty=pr_qty where no=%s '
        else:
            return print('\n##잘못된 입력값입니다. 다시 시도해 주세요.##')
        cursor.execute(updatesql,(upload1,upload))
        conn.commit()
    
    def delitem(self): # 관리자 -상품 삭제 함수
        delinput = input('\n>>삭제할 상품번호를 입력하세요(취소:(Enter)): ')
        delsql='delete from product where no=%s '
        cursor.execute(delsql,delinput)
        conn.commit()


    def findlist(self): #유저 - 상품 검색 함수
        find = input('검색할 상품의 이름을 입력해 주세요: ')
        itemsql = '''select * from product where pr_name=%s '''
        cursor.execute(itemsql,find)
        print('\n 상품 \t \t 가격 \t 재고량')
        data = cursor.fetchall()
        for row in data:
            print(" {0} \t {1} \t {2} \n".format(row[0],row[1],row[4]))
    
    def order(self): #유저 - 상품 주문 함수
        oder = input('주문할 상품이름을 입력해 주세요: ')
        oder_qty = input('주문할 상품의 갯수를 입력해 주세요: ')
        zerosql = 'select rest_qty from product where pr_name = %s'
        cursor.execute(zerosql,oder)
        data = cursor.fetchall()
        dataint = list(data[0])
        print(dataint[0])
        if dataint[0]== 0: ## 재고가 없는 상태에서 상품 주문시 실패 ##
            print('\n***재고 소진!***')
        else:               ## 재고가 있으면 상품 주문##
            ordersql = 'insert into orders(order_id,order_product,order_qty) values(%s,%s,%s)'
            cursor.execute(ordersql,(self.lo_id,oder,oder_qty))
            conn.commit()
            minussql = 'update product set product.rest_qty=pr_qty-(select sum(orders.order_qty) from orders where orders.order_product=product.pr_name) where pr_name=%s'
            cursor.execute(minussql,oder)
            conn.commit()
        

    def upoder(self):#유저 - 상품 주문 함수#2-
        upsql = '''update orders, product, users 
        set order_price=product.pr_price, order_addr=users.addr, order_email=users.email,order_num=users.num  
        where orders.order_product=product.pr_name'''
        cursor.execute(upsql)
        conn.commit()
    def total(self):##연산함수(주문한 총 가격 합계)
        totalsql = 'update orders set total=(order_price*order_qty) where order_id=%s'
        cursor.execute(totalsql,self.lo_id)
        conn.commit()
    
    def orderlist(self):##유저 - 주문 내역 조회 함수
        oderlistsql = 'select no, order_product, order_price, order_qty, total, reg_date from orders where order_id=%s'
        cursor.execute(oderlistsql,self.lo_id)
        data = cursor.fetchall()
        if len(data)==0:
            print('\n'+'*'*15)
            print('주문내역이 없습니다')
            print('*'*15+'\n')
        for row in data:
            print(" {0} \t\t {1} \t {2} \t {3} \t\t {4} \t\t{5} ".format(row[0],row[1],row[2],row[3],row[4],row[5]))
    
    def uppwlist(self):#유저 - 비밀번호 변경함수
        up = input('변경할 내용을 입력하세요: ')
        upusersql = 'update users set pw=%s where id=%s'
        cursor.execute(upusersql,(up,self.lo_id))
        conn.commit()
    
    def upnamelist1(self):#유저 - 이름변경함수
        up = input('변경할 내용을 입력하세요: ')
        upusersql = 'update users set name=%s where id=%s'
        cursor.execute(upusersql,(up,self.lo_id))
        conn.commit()

    def upaddrlist1(self):#유저 - 주소변경함수
        up = input('변경할 내용을 입력하세요: ')
        upusersql = 'update users set addr=%s where id=%s'
        cursor.execute(upusersql,(up,self.lo_id))
        conn.commit()

    def upemaillist1(self):#유저 - 이메일변경함수
        up = input('변경할 내용을 입력하세요: ')
        upusersql = 'update users set email=%s where id=%s'
        cursor.execute(upusersql,(up,self.lo_id))
        conn.commit()

    def upnumlist1(self):#유저 - 전화번호 변경함수
        up = input('변경할 내용을 입력하세요: ')
        upusersql = 'update users set num=%s where id=%s'
        cursor.execute(upusersql,(up,self.lo_id))
        conn.commit()

    def ordercancel(self):#유저 -주문 취소 함수
        cancel = input('\n취소할 주문 번호를 입력해 주세요: ')
        plussql = 'update product set product.rest_qty=rest_qty+(select orders.order_qty from orders where orders.no=%s) ' # 취소할경우 취소한 재고량 만큼 다시 남은 재고량 증가
        cursor.execute(plussql,cancel)
        conn.commit()
        cancelsql = 'delete from orders where order_id = %s and no=%s'
        cursor.execute(cancelsql,(self.lo_id,cancel))
        conn.commit()

    def hotitem(self):#유저 -인기상품 조회
        sumsql ='select order_product,sum(order_qty) as sum_qty from orders group by order_product order by sum_qty desc LIMIT 3'
        cursor.execute(sumsql)
        data = cursor.fetchall()
        print('''**********************
*     !!HIT ITEM!!   *
**********************''')
        for row in data:
            print(" {0} ".format(row[0]))


    def deluser(self):#관리자 - 회원탈퇴
        delsql1= 'delete from users where id = %s'
        cursor.execute(delsql1,self.lo_id)
        conn.commit()

    def itemlist_admin(self):# 관리자 - 전체상품목록
        memlsitsql = 'select * from product'
        cursor.execute(memlsitsql)
        data = cursor.fetchall()
        for row in data:
            print(" {0} \t\t {1} \t {2} \t {3} ".format(row[0],row[1],row[2],row[4]))
    
    def vipmem(self):#관리자 -vip회원조회
        vipsql ='select order_id,sum(order_qty) as sum_qty from orders group by order_id order by sum_qty desc LIMIT 3'
        cursor.execute(vipsql)
        data = cursor.fetchall()
        print('''**********************
*     !!VIP USER!!   *
**********************''')
        for row in data:
            print(" {0} ".format(row[0]))
    
    def orderlist_admin(self):# 관리자 -전체주문내역
        oderlistsql = 'select * from orders'
        cursor.execute(oderlistsql)
        data = cursor.fetchall()
        for row in data:
            print(" {0} \t {1} \t\t {2} \t {3} \t {4} \t\t{5}".format(row[0],row[1],row[2],row[3],row[4],row[5]))
    def change_order(self):#관리자 - 주문변경
        print('\n1.제품변경 2.수량변경 3.주소변경')
        up_id = input('\n(1-3)메뉴를 선택하세요\n>>>')
        upload = input('\n>>수정할 주문번호를 입력하세요: ')
        upload1 = input('\n>>수정할 내용을 입력하세요: ')
        if up_id == '1':
            updatesql = 'update orders set order_product=%s where no=%s '
        elif up_id =='2':
            updatesql = 'update product set order_qty=%s where no=%s '
        elif up_id =='3':
            updatesql = 'update product set order_addr=%s where no=%s'
        else:
            return print('\n##잘못된 입력값입니다. 다시 시도해 주세요.##')
        cursor.execute(updatesql,(upload1,upload))
        conn.commit()
    def delorder(self):#관리자 - 주문취소
        delid = input('\n삭제할 주문번호를 입력하세요: ')
        delsql1= 'delete from orders where no = %s'
        cursor.execute(delsql1,delid)
        conn.commit()
    def mylist(self):# 유저 -내정보 조회
        mylistsql='select * from users where id =%s'
        cursor.execute(mylistsql,self.lo_id)
        data = cursor.fetchall()
        for row in data:
            print(" {0} \t {1} \t {2} \t {3} \t {4} \t\t{5}".format(row[0],row[1],row[2],row[3],row[4],row[5]))