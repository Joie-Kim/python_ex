# readline.py

# 1번째 줄만 읽어온다.
"""
f = open("new_file.txt", 'r')
line = f.readline()
print(line)
f.close()
"""

# 모든 줄을 읽어온다.
"""
f = open("new_file.txt", 'r')
while True:
    line = f.readline() #readline()은 더 이상 읽을 줄이 없는 경우, None을 출력한다.
    if not line: break
    print(line)
f.close
"""

# 여러 줄을 한 번에 읽어온다. (각각의 줄을 요소로 갖는 리스트로 돌려줌)
"""
f = open("new_file.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
"""

# 파일 전체 내용을 읽어온다.
"""
f = open("new_file.txt", 'r')
data = f.read()
print(data)
f.close()
"""

# with 구문 사용해보기 (자동으로 파일 객체 닫아줌)
with open("new_file.txt", 'r') as f:
    data = f.read()
    print(data)

