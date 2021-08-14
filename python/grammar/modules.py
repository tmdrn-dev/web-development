#문자열 세기
my_str = sorted('aabbbbccc')
import collections
answer = collections.Counter(my_str)
print(answer)

#itertools
import itertools

#product #곱집합
iterable1 = 'xy'
iterable2 = 'ABCD'
print(list(itertools.product(iterable1, iterable2)))

#chain #반복자 연결
my_list = [[1, 2], [3, 4], [5, 6]]
print(list(itertools.chain.from_iterable(my_list)))
print(list(itertools.chain(*my_list)))

#순열, 조합
my_list = [1,2,3]
print(list(map(list, itertools.permutations(my_list))))
print(list(map(list, itertools.combinations(my_list,2))))

#이진탐색
import bisect
my_list = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(my_list, 3))