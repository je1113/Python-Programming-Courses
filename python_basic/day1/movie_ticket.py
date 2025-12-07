"""
파일명: movie_ticket.py
목적: 영화관 입장 및 할인 가능 여부 판단 (불린 자료형 실습)
"""

print("=" * 30)
print("테스트 케이스 1: 미성년자")
print("=" * 30)

# 테스트 케이스 1: 미성년자
age = 17
is_student = True
is_weekday = True

# 입장 가능 여부 (19세 이상)
can_enter = age >= 19

# 할인 가능 여부
# (학생 and 평일) or (65세 이상)
can_discount = (is_student and is_weekday) or (age >= 65)

# 출력용 텍스트 변환
student_text = "예" if is_student else "아니오"
weekday_text = "예" if is_weekday else "아니오"
enter_text = "가능" if can_enter else "불가"

# 결과 출력
print("====== 영화관 입장 시스템 ======")
print(f"나이: {age}세")
print(f"학생: {student_text}")
print(f"평일: {weekday_text}")
print("-" * 31)
print(f"입장 가능: {enter_text}")

# 입장 가능한 경우에만 할인 여부 표시
if can_enter:
    discount_text = "가능" if can_discount else "불가"
    print(f"할인 가능: {discount_text}")
else:
    print("할인 가능: -")
print("-" * 31)

print("\n" + "=" * 30)
print("테스트 케이스 2: 성인 학생")
print("=" * 30)

# 테스트 케이스 2: 성인 학생
age = 22
is_student = True
is_weekday = True

can_enter = age >= 19
can_discount = (is_student and is_weekday) or (age >= 65)

student_text = "예" if is_student else "아니오"
weekday_text = "예" if is_weekday else "아니오"
enter_text = "가능" if can_enter else "불가"

print("====== 영화관 입장 시스템 ======")
print(f"나이: {age}세")
print(f"학생: {student_text}")
print(f"평일: {weekday_text}")
print("-" * 31)
print(f"입장 가능: {enter_text}")

if can_enter:
    discount_text = "가능" if can_discount else "불가"
    print(f"할인 가능: {discount_text}")
else:
    print("할인 가능: -")
print("-" * 31)

# 추가 테스트 케이스
print("\n" + "=" * 30)
print("테스트 케이스 3: 노인")
print("=" * 30)

age = 70
is_student = False
is_weekday = False

can_enter = age >= 19
can_discount = (is_student and is_weekday) or (age >= 65)

student_text = "예" if is_student else "아니오"
weekday_text = "예" if is_weekday else "아니오"
enter_text = "가능" if can_enter else "불가"

print("====== 영화관 입장 시스템 ======")
print(f"나이: {age}세")
print(f"학생: {student_text}")
print(f"평일: {weekday_text}")
print("-" * 31)
print(f"입장 가능: {enter_text}")

if can_enter:
    discount_text = "가능" if can_discount else "불가"
    print(f"할인 가능: {discount_text}")
else:
    print("할인 가능: -")
print("-" * 31)

# 불린 연산 연습
print("\n" + "=" * 40)
print("불린 연산 연습")
print("=" * 40)

print("\nAND 연산:")
print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"False and False = {False and False}")

print("\nOR 연산:")
print(f"True or True = {True or True}")
print(f"True or False = {True or False}")
print(f"False or False = {False or False}")

print("\nNOT 연산:")
print(f"not True = {not True}")
print(f"not False = {not False}")

print("\n비교 연산:")
print(f"10 > 5 = {10 > 5}")
print(f"10 < 5 = {10 < 5}")
print(f"10 == 10 = {10 == 10}")
print(f"10 != 5 = {10 != 5}")
