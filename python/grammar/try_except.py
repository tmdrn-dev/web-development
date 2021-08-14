try:
    import my_module
except:
    print("cannot find module")

try:
    a = 3/0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다')

# get error type
try:
    a = 3/0
except Exception as ex:
    print('error:', ex)

# raise: emit signal
def rsp(mine, yours):
    rspList = ['가위', '바위', '보']
    if mine not in rspList:
        raise ValueError
    elif yours not in rspList:
        raise ValueError

try:
    rsp('바', '가위')
except ValueError:
    print('잘못된 값 입력')

# my Exception
class MyException(Exception):
    '''user exception'''
try:
    raise MyException
except MyException:
    print('error:', 'my exception')