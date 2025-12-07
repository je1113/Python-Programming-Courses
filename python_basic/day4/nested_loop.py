"""
파일명: nested_loop.py
목적: 영화관 좌석 예매 시스템 (중첩 반복문 실습)
"""

# 좌석 설정
rows = 5  # A~E
cols = 8  # 1~8

# 예약된 좌석 (행, 열)
reserved_seats = [
    (0, 2),  # A3
    (1, 3),  # B4
    (1, 4),  # B5
    (3, 0),  # D1
    (3, 6)   # D7
]

print("===== 좌석 현황 =====")

# 열 번호 출력
print("  ", end="")
for col in range(1, cols + 1):
    print(f"{col:3}", end="")
print()

# 좌석 출력
for row in range(rows):
    # 행 문자 (A, B, C, ...)
    row_char = chr(65 + row)  # 65 = 'A'
    print(row_char, end=" ")

    for col in range(cols):
        # 예약 여부 확인
        if (row, col) in reserved_seats:
            print(" X ", end="")  # 예약석
        else:
            print(" O ", end="")  # 빈 좌석

    print()  # 줄바꿈

# 통계
total_seats = rows * cols
reserved_count = len(reserved_seats)
available_count = total_seats - reserved_count

print("-" * 21)
print(f"총 좌석: {total_seats}석")
print(f"예약석: {reserved_count}석")
print(f"잔여석: {available_count}석")
print("=" * 21)

# 추가 기능: 좌석 예약
print("\n===== 좌석 예약 =====")
seat_input = input("예약할 좌석 (예: A3): ").upper().strip()

if len(seat_input) >= 2:
    row_char = seat_input[0]
    col_num = seat_input[1:]

    # 검증
    if row_char in "ABCDE" and col_num.isdigit():
        row_index = ord(row_char) - 65  # A=0, B=1, ...
        col_index = int(col_num) - 1    # 1=0, 2=1, ...

        # 범위 확인
        if 0 <= row_index < rows and 0 <= col_index < cols:
            # 예약 확인
            if (row_index, col_index) in reserved_seats:
                print("이미 예약된 좌석입니다!")
            else:
                reserved_seats.append((row_index, col_index))
                print(f"{seat_input} 좌석이 예약되었습니다!")
        else:
            print("존재하지 않는 좌석입니다!")
    else:
        print("올바른 형식이 아닙니다!")
else:
    print("올바른 형식으로 입력하세요! (예: A3)")

# 추가 기능: 구구단 표
print("\n===== 구구단 표 =====")
print("    ", end="")
for i in range(1, 10):
    print(f"{i:4}", end="")
print()
print("-" * 40)

for dan in range(2, 10):
    print(f"{dan}단:", end="")
    for i in range(1, 10):
        result = dan * i
        print(f"{result:4}", end="")
    print()

# 추가 기능: 별 패턴
print("\n===== 별 패턴 =====")

print("\n[삼각형]")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

print("\n[역삼각형]")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print("\n[피라미드]")
for i in range(1, 6):
    # 공백
    for j in range(5 - i):
        print(" ", end="")
    # 별
    for j in range(2 * i - 1):
        print("*", end="")
    print()

print("\n[다이아몬드]")
# 상단
for i in range(1, 5):
    for j in range(5 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# 하단
for i in range(5, 0, -1):
    for j in range(5 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# 추가 기능: 달력 형식
print("\n===== 12월 달력 =====")
print("일 월 화 수 목 금 토")
print("-" * 21)

# 12월 1일이 금요일이라고 가정
first_day = 5  # 0=일요일, 5=금요일
days_in_month = 31

# 첫 주 공백
for i in range(first_day):
    print("   ", end="")

# 날짜 출력
for day in range(1, days_in_month + 1):
    print(f"{day:2} ", end="")

    # 토요일이면 줄바꿈
    if (first_day + day) % 7 == 0:
        print()

print()

# 추가 기능: 체스판 패턴
print("\n===== 체스판 패턴 =====")
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("□ ", end="")
        else:
            print("■ ", end="")
    print()
