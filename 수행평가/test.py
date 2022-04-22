# 자료구조 수행평가 4/25(월)

list1 = []
list2 = []   # 리스트 3개 선언
list3 = []

import random as r # r로 random 모듈을 불러옴

for _ in range(4):
    list1.append(r.randint(1, 100))
    list2.append(r.randint(1, 100)) # list1과 list2에 1~100 사이의 정수 4개를 삽입

list3.extend(list1 + list2) # list1과 list2를 연결한 리스트를 list3에 extend함수로 확장 

print(f"list3 의 길이는 {len(list3)} 입니다") # len 함수를 이용해 길이를 출력

def ma(list): # 최대값을 구하기위해 list를 매개변수로 불러오는 ma() 함수 선언
    max = 1 # 리스트에 존재할수 있는 가장 작은값인 1을 max에 저장
    for i in list: 
        if i > max: # list안 값 하나씩 max값과 비교
            max = i
    
    return max # 최댓값(max)을 리턴

def mi(list): # 최솟값을 구하기 위해 list를 매개변수로 불러오는 mi()함수 선언
    min = 100 # 리스트에 존재할수 있는 가장 큰값인 100을 min에 저장
    for i in list:
        if i < min: # list안 값 하나씩 min값과 비교
            min = i
    
    return min # 최솟값(min)을 리턴

print(f"제일 작은 값 {list3.pop(list3.index(mi(list3)))} 를 삭제 했습니다.") # mi()함수를 이용해 최소값을 구한뒤, index로 최솟값의 위치를 알아내 list3의 최솟값을 제거(pop) 한다

list3.insert(0, ma(list3)+10) # insert함수로 list3의 첫번째주소 즉, 0번지에 ma()함수로 구한 최댓값 + 10 을 하여 삽입(insert) 한다

list3.sort() # list3을 sort()함수를 이용해 오름차순 정렬
print(list3) # 정렬한 list3을 출력