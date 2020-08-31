# ex2.py 변형 (해보고 싶어서..)
# 1. 사용자에게 key 값을 입력 받아서 해당 key에 있는 value 출력
# 2. 만약 key가 없을 경우, 'Error' 출력

a = {'A': 100, 'B': 90, 'C': 80}

key = input("key : ")

if key not in a :
    print('Error')
else :
    print(a.get(key))