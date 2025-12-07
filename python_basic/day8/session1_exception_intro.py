"""
파일명: session1_exception_intro.py
목적: 예외 소개 및 기본 개념
"""

print("=" * 70)
print("예외(Exception) 소개".center(70))
print("=" * 70)

# 1. 예외란?
print("\n[1] 예외란 무엇인가?")
print("-" * 70)

print("""
예외(Exception)는 프로그램 실행 중 발생하는 오류입니다.

종류:
1. 문법 오류 (Syntax Error): 코드 작성 실수
   예: if True print("Hi")  # SyntaxError

2. 예외 (Exception): 실행 중 발생
   예: 10 / 0  # ZeroDivisionError
""")

# 2. 예외 발생 예시
print("\n[2] 다양한 예외 상황")
print("-" * 70)

# ValueError
print("ValueError 예시:")
try:
    number = int("abc")  # 문자열을 정수로 변환 불가
except ValueError as e:
    print(f"✗ ValueError 발생: {e}")

# TypeError
print("\nTypeError 예시:")
try:
    result = "2" + 2  # 문자열과 숫자 더하기 불가
except TypeError as e:
    print(f"✗ TypeError 발생: {e}")

# ZeroDivisionError
print("\nZeroDivisionError 예시:")
try:
    result = 10 / 0  # 0으로 나누기 불가
except ZeroDivisionError as e:
    print(f"✗ ZeroDivisionError 발생: {e}")

# IndexError
print("\nIndexError 예시:")
try:
    my_list = [1, 2, 3]
    print(my_list[10])  # 인덱스 범위 초과
except IndexError as e:
    print(f"✗ IndexError 발생: {e}")

# KeyError
print("\nKeyError 예시:")
try:
    my_dict = {"name": "John", "age": 30}
    print(my_dict["address"])  # 존재하지 않는 키
except KeyError as e:
    print(f"✗ KeyError 발생: {e}")

# FileNotFoundError
print("\nFileNotFoundError 예시:")
try:
    with open("존재하지_않는_파일.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"✗ FileNotFoundError 발생: {e}")

# AttributeError
print("\nAttributeError 예시:")
try:
    my_str = "Hello"
    my_str.append("!")  # 문자열에는 append 메서드가 없음
except AttributeError as e:
    print(f"✗ AttributeError 발생: {e}")

# 3. 예외 처리의 중요성
print("\n[3] 예외 처리의 중요성")
print("-" * 70)

print("❌ 예외 처리 없이 (프로그램 중단):")
print("""
def divide(a, b):
    return a / b

result = divide(10, 0)  # 여기서 프로그램 종료!
print("이 코드는 실행되지 않음")
""")

print("\n✅ 예외 처리 있음 (안정적 실행):")

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다!")
        return None

result = safe_divide(10, 0)
print(f"결과: {result}")
print("이 코드는 실행됨!")

# 4. 예외 객체 정보
print("\n[4] 예외 객체 정보 확인")
print("-" * 70)

try:
    number = int("abc")
except ValueError as e:
    print(f"예외 메시지: {e}")
    print(f"예외 타입: {type(e).__name__}")
    print(f"예외 클래스: {e.__class__}")

# 5. 실습: 다양한 예외 경험하기
print("\n[5] 실습: 예외 상황 체험")
print("-" * 70)

def test_exception(exception_type):
    """다양한 예외를 발생시켜 봅니다"""
    try:
        if exception_type == "ValueError":
            int("abc")
        elif exception_type == "ZeroDivisionError":
            10 / 0
        elif exception_type == "IndexError":
            [][0]
        elif exception_type == "KeyError":
            {}['key']
        elif exception_type == "TypeError":
            "2" + 2
        else:
            print("알 수 없는 예외 타입")
            return

    except (ValueError, ZeroDivisionError, IndexError, KeyError, TypeError) as e:
        print(f"예외 발생: {type(e).__name__}")
        print(f"메시지: {e}")

# 테스트
print("다양한 예외 테스트:\n")
for exc_type in ["ValueError", "ZeroDivisionError", "IndexError", "KeyError", "TypeError"]:
    print(f"{exc_type}:")
    test_exception(exc_type)
    print()

# 6. 주요 내장 예외 정리
print("\n[6] 주요 내장 예외 정리")
print("-" * 70)

exceptions_info = {
    "ValueError": "잘못된 값 (예: int('abc'))",
    "TypeError": "잘못된 타입 (예: '2' + 2)",
    "ZeroDivisionError": "0으로 나누기",
    "IndexError": "인덱스 범위 초과",
    "KeyError": "딕셔너리에 키가 없음",
    "FileNotFoundError": "파일이 존재하지 않음",
    "AttributeError": "속성/메서드가 없음",
    "ImportError": "모듈을 import할 수 없음",
    "NameError": "정의되지 않은 변수 사용",
    "IOError": "입출력 오류"
}

print(f"{'예외 타입':<25} {'발생 원인':<40}")
print("-" * 70)
for exc, desc in exceptions_info.items():
    print(f"{exc:<25} {desc:<40}")

# 7. 예외 vs 문법 오류
print("\n[7] 예외 vs 문법 오류")
print("-" * 70)

print("""
문법 오류 (Syntax Error):
- 코드 작성 단계에서 발생
- 프로그램 실행 전에 감지
- 예: if True print("Hi")

예외 (Exception):
- 프로그램 실행 중 발생
- 실행 시점에 감지
- 예외 처리로 복구 가능
- 예: 10 / 0
""")

# 8. 예외 처리가 필요한 상황
print("\n[8] 예외 처리가 필요한 상황")
print("-" * 70)

situations = [
    "파일 읽기/쓰기",
    "네트워크 통신",
    "데이터베이스 연결",
    "사용자 입력 처리",
    "외부 API 호출",
    "데이터 형 변환",
    "파일 다운로드",
    "JSON 파싱"
]

print("예외 처리가 반드시 필요한 상황:")
for i, situation in enumerate(situations, 1):
    print(f"  {i}. {situation}")

# 9. 실전 예제
print("\n[9] 실전 예제: 안전한 사용자 입력")
print("-" * 70)

def get_integer_input(prompt):
    """안전한 정수 입력 받기"""
    while True:
        try:
            user_input = input(prompt)
            number = int(user_input)
            return number
        except ValueError:
            print("✗ 정수를 입력하세요!")

def get_positive_integer(prompt):
    """양수 정수 입력 받기"""
    while True:
        try:
            number = int(input(prompt))
            if number <= 0:
                print("✗ 양수를 입력하세요!")
                continue
            return number
        except ValueError:
            print("✗ 정수를 입력하세요!")

# 시뮬레이션 (실제 입력 대신 예시)
print("예시: get_positive_integer('숫자 입력: ')")
print("  - 'abc' 입력 → ✗ 정수를 입력하세요!")
print("  - '-5' 입력 → ✗ 양수를 입력하세요!")
print("  - '10' 입력 → ✓ 10 반환")

# 10. 예외 처리 미리보기
print("\n[10] 다음 세션 미리보기: try-except")
print("-" * 70)

print("""
기본 구조:

try:
    # 예외가 발생할 수 있는 코드
    risky_operation()
except ExceptionType:
    # 예외 처리 코드
    handle_error()

예시:
try:
    number = int(input("숫자: "))
    result = 10 / number
    print(f"결과: {result}")
except ValueError:
    print("숫자를 입력하세요!")
except ZeroDivisionError:
    print("0은 입력할 수 없습니다!")
""")

print("\n" + "=" * 70)
print("핵심 정리".center(70))
print("=" * 70)

print("""
✅ 예외는 프로그램 실행 중 발생하는 오류
✅ 예외 처리하지 않으면 프로그램 중단
✅ try-except로 예외를 안전하게 처리
✅ 적절한 예외 타입 선택이 중요

주요 예외:
- ValueError: 잘못된 값
- TypeError: 잘못된 타입
- ZeroDivisionError: 0으로 나누기
- FileNotFoundError: 파일 없음
- KeyError: 딕셔너리 키 없음
""")

print("\n💡 Tip: 다음 세션에서 try-except 문법을 자세히 배웁니다!")
