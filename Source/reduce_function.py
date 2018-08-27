# reduce(실행할 함수, 입력할 리스트)
# reduce 함수는 Python 3 이상부터 내장 함수가 아님
# reduce 함수는 두 매개변수를 가진 함수를 순차적으로 누적하여 반환된 값을 반환함

from functools import reduce

reduce(lambda a,b: a if a > b else b, [1, 294, 19, 492, 590])

# 첫번째: a = 1, b = 294 -> a < b -> 294 리턴
# 두번째: a = 294, b = 19 -> a > b -> 294 리턴
# 세번째: a = 294, b = 492 -> a < b -> 492 리턴
# 네번째: a = 492, b = 590 -> a < b -> 590 리턴
# 최댓값은 590
