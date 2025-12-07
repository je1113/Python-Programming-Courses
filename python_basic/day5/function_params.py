"""
파일명: function_params.py
목적: 계산기 함수 모음 (함수 매개변수와 반환값 실습)
"""

print("=" * 70)
print("계산기 함수 모음".center(70))
print("=" * 70)

# 1. 가변 인자 (*args) - 여러 숫자의 평균
def calculate_average(*numbers):
    """
    여러 숫자의 평균을 계산합니다

    Args:
        *numbers: 가변 개수의 숫자

    Returns:
        평균값
    """
    if not numbers:
        return 0

    total = sum(numbers)
    return total / len(numbers)

print("\n[1] 여러 숫자의 평균 계산 (*args)")
print("-" * 70)

avg1 = calculate_average(10, 20, 30)
print(f"10, 20, 30의 평균: {avg1:.2f}")

avg2 = calculate_average(85, 90, 78, 92, 88)
print(f"85, 90, 78, 92, 88의 평균: {avg2:.2f}")

avg3 = calculate_average(100, 95, 88, 92, 85, 90, 93)
print(f"7개 숫자의 평균: {avg3:.2f}")

# 2. 키워드 인자 (**kwargs) - 학생 정보 출력
def print_student_info(**info):
    """
    학생 정보를 출력합니다

    Args:
        **info: 키워드 인자로 받은 학생 정보
    """
    print("\n학생 정보:")
    print("-" * 40)
    for key, value in info.items():
        print(f"  {key}: {value}")

print("\n[2] 학생 정보 출력 (**kwargs)")
print("-" * 70)

print_student_info(name="김철수", age=20, major="컴퓨터공학", grade=3)
print_student_info(name="이영희", age=22, major="경영학")
print_student_info(student_id="2024001", name="박민수", scholarship=True)

# 3. 기본값 매개변수 - 할인가 계산
def calculate_discount(price, discount_rate=0.1):
    """
    할인가를 계산합니다

    Args:
        price: 원가
        discount_rate: 할인율 (기본값 0.1 = 10%)

    Returns:
        할인 후 가격
    """
    discount_amount = price * discount_rate
    final_price = price - discount_amount
    return final_price

print("\n[3] 할인가 계산 (기본값 매개변수)")
print("-" * 70)

price1 = calculate_discount(10000)  # 기본 10% 할인
print(f"10,000원 (기본 할인): {price1:,.0f}원")

price2 = calculate_discount(10000, 0.2)  # 20% 할인
print(f"10,000원 (20% 할인): {price2:,.0f}원")

price3 = calculate_discount(50000, 0.3)  # 30% 할인
print(f"50,000원 (30% 할인): {price3:,.0f}원")

# 4. 여러 값 반환 - 통계 정보
def get_statistics(numbers):
    """
    숫자 리스트의 통계 정보를 반환합니다

    Args:
        numbers: 숫자 리스트

    Returns:
        딕셔너리 {min, max, avg, sum, count}
    """
    if not numbers:
        return None

    return {
        "min": min(numbers),
        "max": max(numbers),
        "avg": sum(numbers) / len(numbers),
        "sum": sum(numbers),
        "count": len(numbers)
    }

print("\n[4] 통계 정보 반환 (딕셔너리)")
print("-" * 70)

data = [85, 90, 78, 92, 88, 76, 95]
stats = get_statistics(data)

print(f"데이터: {data}\n")
print(f"최소값: {stats['min']}")
print(f"최대값: {stats['max']}")
print(f"평균: {stats['avg']:.2f}")
print(f"합계: {stats['sum']}")
print(f"개수: {stats['count']}")

# 5. 튜플 반환 - 몫과 나머지
def divide_with_remainder(dividend, divisor):
    """
    나눗셈의 몫과 나머지를 반환합니다

    Args:
        dividend: 피제수
        divisor: 제수

    Returns:
        (몫, 나머지) 튜플
    """
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

print("\n[5] 몫과 나머지 계산 (튜플 반환)")
print("-" * 70)

q, r = divide_with_remainder(17, 5)
print(f"17 ÷ 5 = 몫 {q}, 나머지 {r}")

q, r = divide_with_remainder(100, 7)
print(f"100 ÷ 7 = 몫 {q}, 나머지 {r}")

# 6. 혼합 매개변수
def create_report(title, *data, **options):
    """
    리포트를 생성합니다

    Args:
        title: 리포트 제목 (필수)
        *data: 데이터 항목들
        **options: 옵션 설정
    """
    print(f"\n{'=' * 50}")
    print(f"{title}".center(50))
    print(f"{'=' * 50}")

    if data:
        print("\n데이터:")
        for i, item in enumerate(data, 1):
            print(f"  {i}. {item}")

    if options:
        print("\n옵션:")
        for key, value in options.items():
            print(f"  - {key}: {value}")

    print(f"{'=' * 50}")

print("\n[6] 혼합 매개변수 사용")
print("-" * 70)

create_report(
    "월간 판매 보고서",
    "총 매출: 5,000만원",
    "신규 고객: 120명",
    "반품률: 2.5%",
    author="김철수",
    date="2024-01-15",
    department="영업팀"
)

# 7. 람다 함수 - 정렬
print("\n[7] 람다 함수 활용")
print("-" * 70)

students = [
    {"name": "김철수", "score": 85},
    {"name": "이영희", "score": 92},
    {"name": "박민수", "score": 78},
    {"name": "정지훈", "score": 95}
]

# 점수순 정렬
sorted_by_score = sorted(students, key=lambda x: x["score"], reverse=True)

print("점수 높은 순:")
for student in sorted_by_score:
    print(f"  {student['name']}: {student['score']}점")

# 이름순 정렬
sorted_by_name = sorted(students, key=lambda x: x["name"])

print("\n이름순:")
for student in sorted_by_name:
    print(f"  {student['name']}: {student['score']}점")

# 8. map() 함수
print("\n[8] map() 함수 활용")
print("-" * 70)

numbers = [1, 2, 3, 4, 5]

# 각 숫자를 제곱
squared = list(map(lambda x: x ** 2, numbers))
print(f"원본: {numbers}")
print(f"제곱: {squared}")

# 섭씨 → 화씨 변환
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))

print(f"\n섭씨: {celsius}")
print(f"화씨: {fahrenheit}")

# 9. filter() 함수
print("\n[9] filter() 함수 활용")
print("-" * 70)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 짝수만
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"전체: {numbers}")
print(f"짝수: {evens}")

# 5보다 큰 수
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"5보다 큰 수: {greater_than_5}")

# 10. 재귀 함수 - 팩토리얼
def factorial(n):
    """
    재귀 함수로 팩토리얼 계산

    Args:
        n: 양의 정수

    Returns:
        n!
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("\n[10] 재귀 함수 - 팩토리얼")
print("-" * 70)

for i in range(6):
    result = factorial(i)
    print(f"{i}! = {result:,}")

# 11. 재귀 함수 - 피보나치
def fibonacci(n):
    """
    피보나치 수열의 n번째 항을 계산

    Args:
        n: 항 번호 (0부터 시작)

    Returns:
        n번째 피보나치 수
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\n[11] 재귀 함수 - 피보나치")
print("-" * 70)

print("피보나치 수열 (처음 10개):")
fib_sequence = [fibonacci(i) for i in range(10)]
print(fib_sequence)

# 12. 중첩 함수
def outer_function(x):
    """
    중첩 함수 예제

    Args:
        x: 외부 변수

    Returns:
        내부 함수
    """
    def inner_function(y):
        """내부 함수"""
        return x + y

    return inner_function

print("\n[12] 중첩 함수")
print("-" * 70)

add_5 = outer_function(5)
print(f"5 + 3 = {add_5(3)}")
print(f"5 + 10 = {add_5(10)}")

add_10 = outer_function(10)
print(f"10 + 3 = {add_10(3)}")
print(f"10 + 10 = {add_10(10)}")

# 13. 조건부 반환
def check_age(age):
    """
    나이에 따른 분류를 반환합니다

    Args:
        age: 나이

    Returns:
        분류 문자열
    """
    if age < 0:
        return "잘못된 입력"
    elif age < 13:
        return "어린이"
    elif age < 20:
        return "청소년"
    elif age < 65:
        return "성인"
    else:
        return "노인"

print("\n[13] 조건부 반환")
print("-" * 70)

ages = [5, 15, 25, 70, -1]

print(f"{'나이':<10} {'분류':<15}")
print("-" * 25)

for age in ages:
    category = check_age(age)
    print(f"{age:<10} {category:<15}")

# 14. 가변 키워드 인자로 설정 관리
def configure_app(**settings):
    """
    앱 설정을 처리합니다

    Args:
        **settings: 설정 항목들

    Returns:
        처리된 설정 딕셔너리
    """
    # 기본 설정
    default_settings = {
        "theme": "light",
        "language": "ko",
        "notifications": True,
        "auto_save": True
    }

    # 사용자 설정으로 업데이트
    default_settings.update(settings)

    return default_settings

print("\n[14] 설정 관리 (**kwargs)")
print("-" * 70)

config1 = configure_app()
print("기본 설정:")
for key, value in config1.items():
    print(f"  {key}: {value}")

config2 = configure_app(theme="dark", language="en")
print("\n사용자 지정 설정:")
for key, value in config2.items():
    print(f"  {key}: {value}")

# 15. 종합 예제: 주문 처리 함수
def process_order(customer, *items, delivery=False, discount=0):
    """
    주문을 처리합니다

    Args:
        customer: 고객명
        *items: 주문 항목들 (name, price) 튜플
        delivery: 배송 여부 (기본값 False)
        discount: 할인율 (기본값 0)

    Returns:
        주문 요약 딕셔너리
    """
    print(f"\n{'=' * 50}")
    print(f"주문서".center(50))
    print(f"{'=' * 50}")
    print(f"고객명: {customer}")
    print(f"\n주문 내역:")

    subtotal = 0
    for i, (name, price) in enumerate(items, 1):
        print(f"  {i}. {name}: {price:,}원")
        subtotal += price

    # 할인 적용
    discount_amount = subtotal * discount
    delivery_fee = 3000 if delivery else 0

    total = subtotal - discount_amount + delivery_fee

    print(f"\n{'─' * 50}")
    print(f"소계: {subtotal:,}원")

    if discount > 0:
        print(f"할인 ({discount*100:.0f}%): -{discount_amount:,}원")

    if delivery:
        print(f"배송비: {delivery_fee:,}원")

    print(f"{'─' * 50}")
    print(f"총계: {total:,}원")
    print(f"{'=' * 50}")

    return {
        "customer": customer,
        "item_count": len(items),
        "subtotal": subtotal,
        "discount": discount_amount,
        "delivery_fee": delivery_fee,
        "total": total
    }

print("\n[15] 종합 예제: 주문 처리")
print("-" * 70)

order1 = process_order(
    "김철수",
    ("노트북", 1200000),
    ("마우스", 30000),
    ("키보드", 80000),
    delivery=True,
    discount=0.1
)

order2 = process_order(
    "이영희",
    ("헤드셋", 150000),
    ("웹캠", 80000)
)

# 마무리
print("\n" + "=" * 70)
print("함수 매개변수 실습 완료".center(70))
print("=" * 70)
