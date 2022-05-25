fruit=[{'name':'사과', 'price': 3000, 'stock':10},
         {'name':'딸기', 'price': 5000, 'stock':10},
         {'name':'두리안', 'price': 20000, 'stock':10},        
         {'name':'아보카도', 'price': 12000, 'stock':10},
         {'name':'스타후르츠', 'price': 30000, 'stock':10},
         {'name':'체리자두', 'price': 15000, 'stock':10},
         {'name':'애플수박', 'price': 30000, 'stock':10},
         {'name':'샤인머스켓', 'price': 20000, 'stock':10}
         ]

import json

f=open('fruit.json','r')
json.load(fruit,f)
f.close()

#오라클 db와 연동을 위한 라이브러리 설치
