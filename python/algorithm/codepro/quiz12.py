# https://codepro.lge.com/exam/18/%EA%B5%AD%EB%82%B4-%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C/quiz/12
'''
7
3 3 3 3 3 3 3 3 3 3

267
12 5 3 2 1 0 0 0 0 0
'''

from sys import stdin
read = stdin.readline

n = int(input())
packages = [1, 5, 10, 50, 100, 500, 1000, 3000, 6000, 12000]
cis = list(map(int, read().split()))
stock = {package: ci for package, ci in zip(packages, cis)}

#총 갯수 - sol = 재고
# 총 갯수 - 재고 = sol !!!!!!

num = n
minBoxes = list()
for i in reversed(packages):
    if num-i < 0:
        continue

    num = num-i
    minBoxes.append(i)
    while num >= i:
        num = num-i
        minBoxes.append(i)

maxBoxes = dict()
for target in reversed(minBoxes):
    for i in stock:
        if i*stock[i] >= target:
            maxBoxes[i]

print(stock)
print(n, minBoxes)
