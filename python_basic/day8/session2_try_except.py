"""
파일명: session2_try_except.py
목적: try-except 기본 문법
"""

print("=" * 70)
print("try-except 기본".center(70))
print("=" * 70)

# 1. 기본 문법
print("\n[1] try-except 기본 문법")
print("-" * 70)

print("""
기본 구조:

try:
    # 예외가 발생할 수 있는 코드
    risky_operation()
except ExceptionType:
    # 예외 처리 코드
    handle_error()
""")

# 예시
print("예시 1: 0으로 나누기")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("✗ 0으로 나눌 수 없습니다!")
    result = None

print(f"결과: {result}")

# 2. 예외 객체 받기
print("\n[2] 예외 객체 활용 (as)")
print("-" * 70)

try:
    number = int("abc")
except ValueError as e:
    print(f"✗ ValueError 발생!")
    print(f"   메시지: {e}")
    print(f"   타입: {type(e).__name__}")

# 3. 실전 예제: 안전한 나눗셈
print("\n[3] 실전 예제: 안전한 나눗셈")
print("-" * 70)

def safe_divide(a, b):
    """안전한 나눗셈 함수"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print(f"✗ 0으로 나눌 수 없습니다!")
        return None
    except TypeError:
        print(f"✗ 숫자만 입력하세요!")
        return None

# 테스트
print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / '2' = {safe_divide(10, '2')}")

# 4. 파일 읽기 예외 처리
print("\n[4] 파일 읽기 예외 처리")
print("-" * 70)

def read_file_safe(filename):
    """안전한 파일 읽기"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        print(f"✗ '{filename}' 파일을 찾을 수 없습니다")
        return None
    except PermissionError:
        print(f"✗ '{filename}' 파일에 접근 권한이 없습니다")
        return None

# 테스트
content = read_file_safe("존재하지_않는_파일.txt")
print(f"파일 내용: {content}")

# 5. 사용자 입력 검증
print("\n[5] 사용자 입력 검증")
print("-" * 70)

def get_integer():
    """정수 입력 받기 (반복)"""
    while True:
        try:
            user_input = input("정수 입력: ")
            number = int(user_input)
            return number
        except ValueError:
            print("✗ 정수를 입력하세요!")

def get_age():
    """나이 입력 받기 (검증 포함)"""
    while True:
        try:
            age = int(input("나이 입력 (0~150): "))

            if age < 0 or age > 150:
                print("✗ 나이는 0~150 사이여야 합니다!")
                continue

            return age

        except ValueError:
            print("✗ 숫자를 입력하세요!")

# 시뮬레이션
print("예시: get_age()")
print("  - 'abc' 입력 → ✗ 숫자를 입력하세요!")
print("  - '200' 입력 → ✗ 나이는 0~150 사이여야 합니다!")
print("  - '25' 입력 → ✓ 25 반환")

# 6. 실습: 계산기
print("\n[6] 실습: 안전한 계산기")
print("-" * 70)

def calculator(num1, operator, num2):
    """안전한 계산기"""
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
        else:
            print("✗ 올바른 연산자를 사용하세요 (+, -, *, /)")
            return None

    except ZeroDivisionError:
        print("✗ 0으로 나눌 수 없습니다!")
        return None
    except TypeError:
        print("✗ 숫자를 입력하세요!")
        return None

# 테스트
print(f"10 + 5 = {calculator(10, '+', 5)}")
print(f"10 / 2 = {calculator(10, '/', 2)}")
print(f"10 / 0 = {calculator(10, '/', 0)}")
print(f"10 % 3 = {calculator(10, '%', 3)}")

# 7. 리스트 접근 예외 처리
print("\n[7] 리스트 접근 예외 처리")
print("-" * 70)

def safe_get_item(my_list, index):
    """안전한 리스트 항목 가져오기"""
    try:
        return my_list[index]
    except IndexError:
        print(f"✗ 인덱스 {index}는 범위를 벗어났습니다")
        return None
    except TypeError:
        print(f"✗ 인덱스는 정수여야 합니다")
        return None

# 테스트
numbers = [10, 20, 30, 40, 50]
print(f"numbers[2] = {safe_get_item(numbers, 2)}")
print(f"numbers[10] = {safe_get_item(numbers, 10)}")
print(f"numbers['a'] = {safe_get_item(numbers, 'a')}")

# 8. 딕셔너리 접근 예외 처리
print("\n[8] 딕셔너리 접근 예외 처리")
print("-" * 70)

def safe_get_dict_value(my_dict, key, default=None):
    """안전한 딕셔너리 값 가져오기"""
    try:
        return my_dict[key]
    except KeyError:
        print(f"✗ 키 '{key}'가 존재하지 않습니다")
        return default

# 테스트
user = {"name": "김철수", "age": 28, "city": "서울"}
print(f"name: {safe_get_dict_value(user, 'name')}")
print(f"email: {safe_get_dict_value(user, 'email', '없음')}")

# 9. 데이터 변환 예외 처리
print("\n[9] 데이터 변환 예외 처리")
print("-" * 70)

def parse_numbers(data_str):
    """문자열을 숫자 리스트로 변환"""
    try:
        numbers = [int(x) for x in data_str.split()]
        return numbers
    except ValueError as e:
        print(f"✗ 숫자 변환 실패: {e}")
        return []

# 테스트
print(f"'10 20 30' → {parse_numbers('10 20 30')}")
print(f"'10 abc 30' → {parse_numbers('10 abc 30')}")

# 10. 종합 예제: 사용자 등록
print("\n[10] 종합 예제: 사용자 등록")
print("-" * 70)

def register_user(username, email, age):
    """사용자 등록 (검증 포함)"""
    try:
        # 나이 검증
        age_int = int(age)
        if age_int < 0 or age_int > 150:
            print("✗ 유효하지 않은 나이입니다")
            return False

        # 이메일 검증
        if "@" not in email:
            print("✗ 유효하지 않은 이메일 형식입니다")
            return False

        # 사용자명 검증
        if len(username) < 3:
            print("✗ 사용자명은 3자 이상이어야 합니다")
            return False

        print(f"✓ {username} 등록 완료!")
        return True

    except ValueError:
        print("✗ 나이는 숫자여야 합니다")
        return False

# 테스트
print("\n테스트 케이스:")
register_user("김철수", "kim@example.com", "28")
register_user("이영희", "lee@example.com", "abc")
register_user("박", "park@example.com", "25")
register_user("정지훈", "jung", "30")

print("\n" + "=" * 70)
print("핵심 정리".center(70))
print("=" * 70)

print("""
✅ try-except 기본 구조:
   try:
       risky_code()
   except ExceptionType:
       handle_error()

✅ 예외 객체 활용:
   except ValueError as e:
       print(f"오류: {e}")

✅ 실무 활용:
   - 파일 읽기/쓰기
   - 사용자 입력 검증
   - 데이터 변환
   - API 호출

✅ 베스트 프랙티스:
   - 구체적인 예외 타입 지정
   - 적절한 오류 메시지 제공
   - 기본값 또는 대안 제공
""")

print("\n💡 Tip: 다음 세션에서 여러 예외를 처리하는 방법을 배웁니다!")
