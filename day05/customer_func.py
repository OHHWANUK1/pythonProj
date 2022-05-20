import function_customer as fc

custlist = []
page = 1
custlist = [{'name': '홍길동' , 'gender': 'M', 'email': 'hong123@gmail.com', 'birthyear': '1993'}]
           [{'name': '김나리' , 'gender': 'F', 'email': 'kim123@gmail.com' , 'birthyear': '1997'}]
page = 2
while True:
    choice=input('''
다음 중에서 하실 일을 골라주세요 :
I - 입력 C - 현재 P - 이전 N - 다음 U - 수정 D - 삭제 Q - 종료
>>>''').upper()
    
    if choice=="I":
        fc.customer_input()                
                                     
                                     
    
    elif choice=="C":
    elif choice=="P":
    elif choice=="N":   
    elif choice=="U":
    elif choice=="D":
    elif choice=="Q":