# filter(실행할 함수, 입력할 리스트)
# filter 함수는 bool 값을 반환하는 함수에서 *참을 반환하는 리스트 요소*만을 모음

# 1부터 100까지 중에서 짝수만을 모은 리스트 할당하기
even_number = list(filter(lambda x: x % 2 == 0, list(range(1, 101))))

# even_number = [2, 4, 6, 8, 10, 12, 14, 16, 18, ..., 98, 100]
