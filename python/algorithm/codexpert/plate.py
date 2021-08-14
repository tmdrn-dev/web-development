'''
((((
'''

def Input_Data():
    s = input().strip()
    return s

sol = -1

# 입력받는 부분
s = Input_Data()

# 여기서부터 작성
prev = ''
for i in s:
    if i == prev:
        sol += 5
    else:
        sol += 10
    prev = i

# 출력하는 부분
print(sol+1)