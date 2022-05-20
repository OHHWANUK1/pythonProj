import re
def customer_input(custlist):
     if choice=="I":
        customer={'name':'' , 'gender':'','email':'' ,'birthyear':''}
        customer['name']=input('이름 >>>')
        while True:
            customer['gender']=input('성별(M,F) >>>' )
            if customer['gender'] in ('M','F'):
                break
        while True:
            p = re.compile('^[a-z][a-z0-9_]{4,}@[a-z]{3,}[.][a-z]{2,}$')
            customer['email'] = ''
            while not p.search(customer['email']):
                customer['email'=input('email >>>')]

        
    check = 0
    for i in custlist:
        if i ['email'] == customer['email']:
            check = 1
            break
        print('중복되는 이메일이 있습니다')
    while True:
        customer['birthyear'] = input('생년월일(4자리) >>>')
        if len(customer['birthyear']) == 4 and customer['birthyear'].isdecima():
            break

# def customer_c(custlist,page):
#    if page < 0:
#         print('입력된 정보가 없습니다' )
#     else:
#         print(f'현재 페이지는 {page+1}입니다')
#         print(custlist[page])
# def customer_p():
#     pass
# def customer_n():
#     pass
# def customer_update():
#     passd
# def customer_delete():
#     print(custlist)
#     choice1 = input('삭제하려는 이메일 주소를 입력하세요')
#     delok = 0
#     for i in range(len(custlist)):
#         if custlist[i]['email'] == choice1:
#             print(f'{custlist[i]["name"]}님의 정보가 삭제 되었습니다')
#             if page ==len(custlist)-1:
#                 page -= 1
#             del custlist[i]
#             delok = 1
#             break
#         if delok == 0
#             print('등록되지 않은 고객입니다')
#         print(custlist)
#         return page