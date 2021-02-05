# ------  list 의 요소 갯수를 dict 로 반환
# ------  많은것 부터 출력
from collections import Counter

# ------  누적 집계
from functools import reduce

# ------  sum(a, []) 로도 간단하게 가능
# import itertools
# a = [[1,2],[3,4],[5,6]]
# list(itertools.chain.from_iterable(a))
# print(a)

# ------ 2차원 리스트 뒤집기
# board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# new_board = list(map(list, zip(*board)))
# new_board2 = [e for e in zip(*board)]

# ------ list.append(list) 는 기본적으로 call by reference 인듯.
# ------ call by value 로 하고싶으면 list.append(list[:]) 이렇게 해줘
# res = []
# a = [0, 1]
# b = [2, 3]
# res.append(a)
# res.append(b)
# print(res)
# b[1] = 100
# print(res)

# ------ 2차원 리스트 중복제거
# tmp = [[1, 2], [2, 1], [1, 3]]
# list(set([tuple(set(a)) for a in tmp]))     # [1,2] [2,1] 을 같은걸로 보았을때
# list(set([tuple(a) for a in tmp]))          # [1,2] [2,1] 을 다른걸로 보았을때

# ------ 알파벳 상수
# import string
# print(string.ascii_lowercase)               # 소문자 abcdefghijklmnopqrstuvwxyz
# print(string.ascii_uppercase)               # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.ascii_letters)                 # 대소문자 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.digits)                        # 숫자 0123456789