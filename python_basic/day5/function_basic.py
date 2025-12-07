"""
파일명: function_basic.py
목적: 유틸리티 함수 모음 (함수 정의 실습)
"""

print("=" * 70)
print("유틸리티 함수 모음".center(70))
print("=" * 70)

# 1. 인사말 출력 함수
def greet(name):
    """사용자에게 인사하는 함수"""
    print(f"안녕하세요, {name}님!")
    print("좋은 하루 되세요!")

print("\n[1] 인사말 함수")
print("-" * 70)
greet("김철수")
greet("이영희")

# 2. 사각형 넓이 계산 함수
def calculate_rectangle_area(width, height):
    """
    사각형의 넓이를 계산합니다.

    Args:
        width: 가로 길이
        height: 세로 길이

    Returns:
        넓이 (width × height)
    """
    area = width * height
    return area

print("\n[2] 사각형 넓이 계산")
print("-" * 70)

rect1_area = calculate_rectangle_area(10, 20)
print(f"가로 10, 세로 20인 사각형 넓이: {rect1_area}")

rect2_area = calculate_rectangle_area(15, 25)
print(f"가로 15, 세로 25인 사각형 넓이: {rect2_area}")

# 3. 섭씨 → 화씨 변환 함수
def celsius_to_fahrenheit(celsius):
    """
    섭씨 온도를 화씨로 변환합니다.

    Args:
        celsius: 섭씨 온도

    Returns:
        화씨 온도
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print("\n[3] 온도 변환 (섭씨 → 화씨)")
print("-" * 70)

temps_c = [0, 10, 20, 25, 30, 37]

print(f"{'섭씨(°C)':<12} {'화씨(°F)':<12}")
print("-" * 24)

for temp_c in temps_c:
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f"{temp_c:>8}°C  {temp_f:>8.1f}°F")

# 4. 학점 계산 함수
def get_grade(score):
    """
    점수를 입력받아 학점을 반환합니다.

    Args:
        score: 점수 (0~100)

    Returns:
        학점 (A, B, C, D, F)
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print("\n[4] 학점 계산")
print("-" * 70)

students_scores = [
    ("김철수", 95),
    ("이영희", 88),
    ("박민수", 76),
    ("정지훈", 62),
    ("최민지", 54)
]

print(f"{'이름':<10} {'점수':<10} {'학점':<10}")
print("-" * 30)

for name, score in students_scores:
    grade = get_grade(score)
    print(f"{name:<10} {score:<10} {grade:<10}")

# 5. 비밀번호 강도 검사 함수
def check_password_strength(password):
    """
    비밀번호 강도를 검사합니다.

    Args:
        password: 비밀번호 문자열

    Returns:
        강도 ("강함", "보통", "약함")
    """
    # 조건 검사
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    is_long = len(password) >= 8

    # 강도 판정
    strength_count = sum([has_upper, has_lower, has_digit, is_long])

    if strength_count >= 4:
        return "강함"
    elif strength_count >= 2:
        return "보통"
    else:
        return "약함"

print("\n[5] 비밀번호 강도 검사")
print("-" * 70)

test_passwords = [
    "Password123",    # 강함
    "password",       # 약함
    "Pass12",         # 보통
    "HELLO123",       # 보통
    "SecurePass2024"  # 강함
]

print(f"{'비밀번호':<20} {'강도':<10}")
print("-" * 30)

for pwd in test_passwords:
    strength = check_password_strength(pwd)
    print(f"{pwd:<20} {strength:<10}")

# 6. 소수 판별 함수
def is_prime(n):
    """
    소수인지 판별합니다.

    Args:
        n: 판별할 숫자

    Returns:
        True (소수) 또는 False (소수 아님)
    """
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

print("\n[6] 소수 판별")
print("-" * 70)

numbers = [2, 3, 4, 5, 10, 17, 20, 23, 29, 30]

print(f"{'숫자':<10} {'소수 여부':<15}")
print("-" * 25)

for num in numbers:
    result = "소수" if is_prime(num) else "소수 아님"
    print(f"{num:<10} {result:<15}")

# 7. 최대공약수 계산 함수
def gcd(a, b):
    """
    최대공약수를 계산합니다 (유클리드 호제법)

    Args:
        a: 첫 번째 숫자
        b: 두 번째 숫자

    Returns:
        최대공약수
    """
    while b:
        a, b = b, a % b
    return a

print("\n[7] 최대공약수 계산")
print("-" * 70)

number_pairs = [(12, 8), (24, 36), (17, 19), (48, 18)]

print(f"{'숫자1':<10} {'숫자2':<10} {'최대공약수':<15}")
print("-" * 35)

for a, b in number_pairs:
    result = gcd(a, b)
    print(f"{a:<10} {b:<10} {result:<15}")

# 8. 팩토리얼 계산 함수
def factorial(n):
    """
    팩토리얼을 계산합니다 (n!)

    Args:
        n: 양의 정수

    Returns:
        n! (n × (n-1) × ... × 2 × 1)
    """
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result

print("\n[8] 팩토리얼 계산")
print("-" * 70)

print(f"{'n':<10} {'n!':<20}")
print("-" * 30)

for n in range(0, 11):
    fact = factorial(n)
    print(f"{n:<10} {fact:<20,}")

# 9. 이메일 검증 함수
def is_valid_email(email):
    """
    간단한 이메일 형식 검증

    Args:
        email: 이메일 주소

    Returns:
        True (유효) 또는 False (무효)
    """
    # 기본 검증만 수행
    if not email:
        return False

    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    if not username or not domain:
        return False

    if "." not in domain:
        return False

    return True

print("\n[9] 이메일 검증")
print("-" * 70)

test_emails = [
    "user@example.com",
    "invalid.email",
    "@example.com",
    "user@",
    "user@@example.com",
    "test@test.co.kr"
]

print(f"{'이메일':<30} {'유효성':<10}")
print("-" * 40)

for email in test_emails:
    valid = "✓ 유효" if is_valid_email(email) else "✗ 무효"
    print(f"{email:<30} {valid:<10}")

# 10. 문자열 역순 함수
def reverse_string(text):
    """
    문자열을 역순으로 뒤집습니다

    Args:
        text: 입력 문자열

    Returns:
        역순 문자열
    """
    return text[::-1]

print("\n[10] 문자열 역순")
print("-" * 70)

words = ["Python", "Hello", "12345", "안녕하세요"]

print(f"{'원본':<20} {'역순':<20}")
print("-" * 40)

for word in words:
    reversed_word = reverse_string(word)
    print(f"{word:<20} {reversed_word:<20}")

# 11. 리스트 합계 함수
def sum_list(numbers):
    """
    리스트의 모든 숫자를 합산합니다

    Args:
        numbers: 숫자 리스트

    Returns:
        합계
    """
    total = 0
    for num in numbers:
        total += num
    return total

print("\n[11] 리스트 합계")
print("-" * 70)

test_lists = [
    [1, 2, 3, 4, 5],
    [10, 20, 30],
    [100, 200, 300, 400]
]

for lst in test_lists:
    total = sum_list(lst)
    print(f"{lst} → 합계: {total}")

# 12. 평균 계산 함수
def calculate_average(numbers):
    """
    숫자 리스트의 평균을 계산합니다

    Args:
        numbers: 숫자 리스트

    Returns:
        평균값
    """
    if not numbers:
        return 0

    total = sum_list(numbers)
    return total / len(numbers)

print("\n[12] 평균 계산")
print("-" * 70)

scores = [85, 90, 78, 92, 88]
avg = calculate_average(scores)
print(f"점수: {scores}")
print(f"평균: {avg:.2f}점")

# 13. 짝수/홀수 판별 함수
def is_even(n):
    """숫자가 짝수인지 판별"""
    return n % 2 == 0

def is_odd(n):
    """숫자가 홀수인지 판별"""
    return n % 2 != 0

print("\n[13] 짝수/홀수 판별")
print("-" * 70)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [n for n in numbers if is_even(n)]
odds = [n for n in numbers if is_odd(n)]

print(f"전체: {numbers}")
print(f"짝수: {evens}")
print(f"홀수: {odds}")

# 14. 할인가 계산 함수
def calculate_discount_price(price, discount_rate):
    """
    할인가를 계산합니다

    Args:
        price: 원가
        discount_rate: 할인율 (0~1 사이, 예: 0.2 = 20%)

    Returns:
        할인 적용 후 가격
    """
    discount_amount = price * discount_rate
    final_price = price - discount_amount
    return final_price

print("\n[14] 할인가 계산")
print("-" * 70)

products = [
    ("노트북", 1000000, 0.15),
    ("마우스", 30000, 0.10),
    ("키보드", 80000, 0.20)
]

print(f"{'상품':<10} {'원가':<15} {'할인율':<10} {'할인가':<15}")
print("-" * 50)

for name, price, rate in products:
    discounted = calculate_discount_price(price, rate)
    print(f"{name:<10} {price:>10,}원  {rate*100:>5.0f}%  {discounted:>10,.0f}원")

# 15. 절대값 함수
def absolute(n):
    """
    숫자의 절대값을 반환합니다

    Args:
        n: 숫자

    Returns:
        절대값
    """
    if n >= 0:
        return n
    else:
        return -n

print("\n[15] 절대값 계산")
print("-" * 70)

numbers = [-10, -5, 0, 5, 10, -3.14, 2.71]

print(f"{'원본':<10} {'절대값':<10}")
print("-" * 20)

for num in numbers:
    abs_val = absolute(num)
    print(f"{num:<10} {abs_val:<10}")

# 16. 문자 개수 세기 함수
def count_char(text, char):
    """
    문자열에서 특정 문자의 개수를 셉니다

    Args:
        text: 대상 문자열
        char: 찾을 문자

    Returns:
        문자 개수
    """
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

print("\n[16] 문자 개수 세기")
print("-" * 70)

text = "Hello, World! Welcome to Python Programming!"
chars_to_count = ['o', 'l', 'e', '!']

print(f"텍스트: {text}\n")

for char in chars_to_count:
    cnt = count_char(text, char)
    print(f"'{char}' 개수: {cnt}개")

# 17. 리스트 최대값 찾기 함수
def find_max(numbers):
    """
    리스트에서 최대값을 찾습니다

    Args:
        numbers: 숫자 리스트

    Returns:
        최대값
    """
    if not numbers:
        return None

    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num

    return max_val

print("\n[17] 최대값 찾기")
print("-" * 70)

test_data = [
    [3, 7, 2, 9, 1],
    [100, 50, 75, 200, 150],
    [-5, -2, -10, -1]
]

for data in test_data:
    max_val = find_max(data)
    print(f"{data} → 최대값: {max_val}")

# 종합 예제: 사용자 입력 처리
print("\n" + "=" * 70)
print("종합 예제: 성적 관리 시스템".center(70))
print("=" * 70)

def process_score(score):
    """
    점수를 입력받아 학점과 평가를 반환합니다

    Args:
        score: 점수

    Returns:
        (학점, 평가) 튜플
    """
    grade = get_grade(score)

    if score >= 90:
        comment = "우수"
    elif score >= 70:
        comment = "양호"
    elif score >= 60:
        comment = "보통"
    else:
        comment = "노력 필요"

    return grade, comment

# 테스트
scores = [95, 88, 76, 62, 54]

print(f"\n{'점수':<10} {'학점':<10} {'평가':<15}")
print("-" * 35)

for score in scores:
    grade, comment = process_score(score)
    print(f"{score:<10} {grade:<10} {comment:<15}")

print("\n" + "=" * 70)
print("함수 실습 완료".center(70))
print("=" * 70)
