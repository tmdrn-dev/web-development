# comment
long_text = """multi line comment free s't"ring"""
print(long_text)

# if condition
if False:
    print('true')
elif False:
    print('false')
else:
    print('else')

# define function
def cordinate():
    return 5, 10
x, y = cordinate()
print('{}, {}'.format(x,y))

# for
i = 0
for i in range(3):
    print(i+1)
    i+=1

# while
selected = ''
while selected != 'y':
    selected = input('exit?(y/n) ')

print(selected)
