# Day 8: 예외 처리 및 실전 프로젝트

## 📋 강의 개요

**학습 목표:**
- 예외 처리를 통한 안정적인 프로그램 작성
- try-except-finally 완벽 이해
- 사용자 정의 예외 생성
- 실무 프로젝트를 통한 종합 실습

**소요 시간:** 4시간 (240분)

**세션 구성:**
- 전반부: 예외 처리 (8개 세션 × 25분)
- 후반부: 실전 프로젝트 (4개 프로젝트)

---

## 💡 Day 8을 배워야 하는 이유

### 1. 안정적인 프로그램 작성

**예외 처리가 중요한 이유:**
- 프로그램 중단 방지
- 사용자 경험 개선
- 디버깅 용이성

### 2. 실무 필수 스킬

**실무에서:**
- 파일 처리 시 예외 처리 필수
- 네트워크 통신 오류 대응
- 데이터베이스 연결 실패 처리

### 3. Python다운 코드

**EAFP (Easier to Ask for Forgiveness than Permission):**
- Python의 철학
- 더 간결하고 읽기 쉬운 코드

---

## 세션 1: 예외란 무엇인가? (25분)
**중요도:** ★★★★★

### 📖 이론 (10분)

#### 1.1 예외 (Exception)

**예외**는 프로그램 실행 중 발생하는 오류입니다.

**예시 1: 예외 발생 상황**
```python
# ValueError - 잘못된 값
number = int("abc")  # ValueError: invalid literal for int()

# ZeroDivisionError - 0으로 나누기
result = 10 / 0  # ZeroDivisionError: division by zero

# FileNotFoundError - 파일이 없음
file = open("없는파일.txt")  # FileNotFoundError

# IndexError - 인덱스 범위 초과
my_list = [1, 2, 3]
print(my_list[10])  # IndexError: list index out of range

# KeyError - 딕셔너리 키 없음
my_dict = {"name": "John"}
print(my_dict["age"])  # KeyError: 'age'
```

**예시 2: 예외 처리의 중요성**
```python
# ❌ 예외 처리 없음 - 프로그램 중단!
def divide(a, b):
    return a / b

result = divide(10, 0)  # 프로그램 종료!
print("이 코드는 실행되지 않음")

# ✅ 예외 처리 있음 - 안정적으로 실행
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다!")
        return None

result = safe_divide(10, 0)  # 예외 처리
print("이 코드는 실행됨")  # 계속 실행
```

**예시 3: 주요 내장 예외**
```python
# ValueError
try:
    age = int("스물다섯")
except ValueError as e:
    print(f"ValueError: {e}")

# TypeError
try:
    result = "2" + 2
except TypeError as e:
    print(f"TypeError: {e}")

# FileNotFoundError
try:
    with open("없는파일.txt") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

# AttributeError
try:
    text = "hello"
    text.append("!")  # 문자열에는 append 없음
except AttributeError as e:
    print(f"AttributeError: {e}")
```

#### 1.2 Java와 비교

| 구분 | Python | Java |
|------|--------|------|
| 예외 처리 | 선택적 (모든 예외) | Checked/Unchecked 구분 |
| 문법 | `try-except` | `try-catch` |
| 선언 | 불필요 | `throws` 필요 (Checked) |

### 💻 실습 (10분)

**[실습 파일: session1_exception_intro_practice.py](./session1_exception_intro_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session1_exception_intro_solution.py](./session1_exception_intro_solution.py)**

**핵심 포인트:**
1. 예외는 실행 중 발생하는 오류
2. 예외 처리하지 않으면 프로그램 중단
3. `as e`로 예외 객체 받아서 정보 확인 가능

---

## 세션 2: try-except 기본 (25분)
**중요도:** ★★★★★

### 📖 이론 (10분)

#### 2.1 try-except 구문

**예시 1: 기본 문법**
```python
# 기본 형태
try:
    # 예외가 발생할 수 있는 코드
    risky_operation()
except ExceptionType:
    # 예외 처리 코드
    handle_error()

# 예제: 안전한 나누기
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다!")
        return None

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # None
```

**예시 2: 예외 객체 활용**
```python
def get_integer_input():
    try:
        number = int(input("숫자 입력: "))
        return number
    except ValueError as e:
        print(f"오류 발생: {e}")
        print(f"오류 타입: {type(e).__name__}")
        return None

# 사용
num = get_integer_input()
if num is not None:
    print(f"입력한 숫자: {num}")
```

**예시 3: 실무 활용 - 파일 읽기**
```python
def read_file_safely(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        print(f"'{filename}' 파일을 찾을 수 없습니다.")
        return None
    except PermissionError:
        print(f"'{filename}' 파일에 접근 권한이 없습니다.")
        return None

# 사용
content = read_file_safely("data.txt")
if content:
    print(content)
```

### 💻 실습 (10분)

**[실습 파일: session2_try_except_practice.py](./session2_try_except_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session2_try_except_solution.py](./session2_try_except_solution.py)**

**핵심 포인트:**
1. try 블록에는 예외가 발생할 수 있는 코드
2. except 블록에는 예외 처리 코드
3. 여러 예외를 각각 처리 가능

---

## 세션 3: 여러 예외 처리 (25분)
**중요도:** ★★★★★

### 📖 이론 (10분)

#### 3.1 다중 except 블록

**예시 1: 여러 예외 개별 처리**
```python
def process_data(data_str):
    try:
        # 정수 변환
        number = int(data_str)
        # 100으로 나누기
        result = 100 / number
        # 리스트 접근
        items = [1, 2, 3]
        item = items[number]
        return result, item

    except ValueError:
        print("ValueError: 숫자로 변환할 수 없습니다.")
    except ZeroDivisionError:
        print("ZeroDivisionError: 0으로 나눌 수 없습니다.")
    except IndexError:
        print("IndexError: 인덱스 범위를 벗어났습니다.")
    except Exception as e:
        print(f"예상치 못한 오류: {e}")

    return None

# 테스트
process_data("abc")   # ValueError
process_data("0")     # ZeroDivisionError
process_data("10")    # IndexError
```

**예시 2: 여러 예외를 한 번에 처리**
```python
def read_and_convert(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            numbers = [int(x) for x in content.split()]
            return numbers

    except (FileNotFoundError, PermissionError) as e:
        # 파일 관련 오류를 한 번에 처리
        print(f"파일 오류: {e}")
    except ValueError as e:
        # 데이터 변환 오류
        print(f"데이터 오류: {e}")

    return []

# 사용
numbers = read_and_convert("numbers.txt")
print(numbers)
```

**예시 3: 예외 계층 구조 활용**
```python
def process_user_input(value):
    try:
        # 복잡한 처리
        result = complex_operation(value)
        return result

    except ValueError:
        # 구체적인 예외 먼저
        print("값 오류")
    except TypeError:
        # 그 다음 구체적인 예외
        print("타입 오류")
    except Exception as e:
        # 마지막에 일반 예외 (catch-all)
        print(f"기타 오류: {e}")

# 예외 계층
# BaseException
# ├── Exception
# │   ├── ValueError
# │   ├── TypeError
# │   ├── ZeroDivisionError
# │   └── ...
# ├── KeyboardInterrupt
# └── SystemExit
```

### 💻 실습 (10분)

**[실습 파일: session3_multiple_exceptions_practice.py](./session3_multiple_exceptions_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session3_multiple_exceptions_solution.py](./session3_multiple_exceptions_solution.py)**

**핵심 포인트:**
1. 구체적인 예외를 먼저 처리
2. `Exception`은 마지막에 (catch-all)
3. 각 예외에 맞는 처리 제공

---

## 세션 4: finally와 else (25분)
**중요도:** ★★★★★

### 📖 이론 (10분)

#### 4.1 finally와 else

**예시 1: finally - 항상 실행**
```python
def read_file_with_cleanup(filename):
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        return content

    except FileNotFoundError:
        print(f"'{filename}' 파일을 찾을 수 없습니다.")
        return None

    finally:
        # 예외 발생 여부와 무관하게 항상 실행
        if file:
            file.close()
            print("파일이 닫혔습니다.")

# 사용 (with 문이 더 좋지만 학습을 위해)
content = read_file_with_cleanup("data.txt")
```

**예시 2: else - 예외 없을 때만 실행**
```python
def get_user_age():
    try:
        age = int(input("나이 입력: "))

    except ValueError:
        print("숫자가 아닙니다!")

    else:
        # 예외가 없었을 때만 실행
        print(f"입력한 나이: {age}")
        if age >= 19:
            print("성인입니다.")
        else:
            print("미성년자입니다.")

    finally:
        print("입력 처리 완료")

# 실행 순서:
# 1. try 블록 실행
# 2. 예외 발생 → except 블록
# 3. 예외 없음 → else 블록
# 4. 항상 finally 블록
```

**예시 3: 전체 구조**
```python
def process_transaction(amount):
    try:
        # 거래 처리
        if amount <= 0:
            raise ValueError("금액은 0보다 커야 합니다")
        balance = perform_transaction(amount)

    except ValueError as e:
        # 예외 처리
        print(f"거래 실패: {e}")
        balance = None

    else:
        # 성공 시에만 실행
        print(f"거래 성공! 잔액: {balance:,}원")

    finally:
        # 항상 실행 (로그 기록 등)
        print("거래 처리 완료")

    return balance

# with 문으로 더 간단하게
with open("data.txt") as f:
    content = f.read()
# 자동으로 파일 닫힘 (finally 불필요)
```

### 💻 실습 (10분)

**[실습 파일: session4_finally_else_practice.py](./session4_finally_else_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session4_finally_else_solution.py](./session4_finally_else_solution.py)**

**핵심 포인트:**
1. `finally`는 항상 실행 (리소스 정리)
2. `else`는 예외 없을 때만 실행
3. `with` 문을 사용하면 `finally` 불필요 (자동 정리)

---

## 세션 5: raise로 예외 발생 (25분)
**중요도:** ★★★★★

### 📖 이론 (10분)

#### 5.1 예외 발생시키기

**예시 1: 기본 raise**
```python
def withdraw(balance, amount):
    """출금 처리"""
    if amount <= 0:
        raise ValueError("출금액은 0보다 커야 합니다!")
    if amount > balance:
        raise ValueError("잔액이 부족합니다!")

    return balance - amount

# 사용
try:
    new_balance = withdraw(10000, 50000)
except ValueError as e:
    print(f"오류: {e}")
```

**예시 2: 검증 패턴**
```python
def set_age(age):
    """나이 설정 (검증 포함)"""
    # 타입 검증
    if not isinstance(age, int):
        raise TypeError("나이는 정수여야 합니다!")

    # 범위 검증
    if age < 0:
        raise ValueError("나이는 0 이상이어야 합니다!")
    if age > 150:
        raise ValueError("나이는 150 이하여야 합니다!")

    return age

# 사용
try:
    age = set_age("25")  # TypeError
except (TypeError, ValueError) as e:
    print(f"오류: {e}")
```

**예시 3: 예외 재발생**
```python
def process_critical_data(data):
    try:
        # 중요한 처리
        result = critical_operation(data)
        return result

    except Exception as e:
        # 로그 기록
        print(f"[ERROR] 처리 실패: {e}")
        # 예외를 상위로 전달
        raise  # 같은 예외를 다시 발생

# 사용
try:
    process_critical_data(some_data)
except Exception:
    print("상위에서 예외 처리")
```

### 💻 실습 (10분)

**[실습 파일: session5_raise_practice.py](./session5_raise_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session5_raise_solution.py](./session5_raise_solution.py)**

**핵심 포인트:**
1. `raise`로 조건 검증
2. 적절한 예외 타입 선택
3. 명확한 오류 메시지 제공

---

## 세션 6: 사용자 정의 예외 (25분)
**중요도:** ★★★★★

### 📖 이론 (10분)

#### 6.1 커스텀 예외 클래스

**예시 1: 기본 사용자 정의 예외**
```python
# 사용자 정의 예외
class InsufficientFundsError(Exception):
    """잔액 부족 예외"""
    pass

class InvalidAgeError(Exception):
    """유효하지 않은 나이 예외"""
    def __init__(self, age, message="나이가 유효하지 않습니다"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.age}"

# 사용
def check_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError(age)
    return True

try:
    check_age(-5)
except InvalidAgeError as e:
    print(f"오류: {e}")
```

**예시 2: 예외 계층 구조**
```python
# 기본 예외
class ApplicationError(Exception):
    """애플리케이션 기본 예외"""
    pass

# 하위 예외들
class DatabaseError(ApplicationError):
    """데이터베이스 오류"""
    pass

class ValidationError(ApplicationError):
    """검증 오류"""
    pass

class NetworkError(ApplicationError):
    """네트워크 오류"""
    pass

# 사용
try:
    # 데이터베이스 작업
    raise DatabaseError("연결 실패")
except ApplicationError as e:
    # 모든 애플리케이션 예외를 잡음
    print(f"애플리케이션 오류: {e}")
```

**예시 3: 상세 정보가 있는 예외**
```python
class OutOfStockError(Exception):
    """재고 부족 예외"""
    def __init__(self, product, requested, available):
        self.product = product
        self.requested = requested
        self.available = available
        message = f"'{product}' 재고 부족 (요청: {requested}, 재고: {available})"
        super().__init__(message)

def order_product(product, quantity, stock):
    if quantity <= 0:
        raise ValueError("수량은 1 이상이어야 합니다")
    if quantity > stock:
        raise OutOfStockError(product, quantity, stock)

    print(f"✓ '{product}' {quantity}개 주문 완료")
    return stock - quantity

# 사용
try:
    remaining = order_product("노트북", 10, 3)
except OutOfStockError as e:
    print(f"주문 실패: {e}")
    print(f"재고: {e.available}개")
except ValueError as e:
    print(f"입력 오류: {e}")
```

### 💻 실습 (10분)

**[실습 파일: session6_custom_exceptions_practice.py](./session6_custom_exceptions_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session6_custom_exceptions_solution.py](./session6_custom_exceptions_solution.py)**

**핵심 포인트:**
1. `Exception` 상속
2. 의미 있는 예외 이름
3. 추가 정보를 예외 객체에 포함

---

## 세션 7: 예외 처리 실무 패턴 (25분)
**중요도:** ★★★★★

### 📖 이론 (10분)

#### 7.1 EAFP vs LBYL

**예시 1: Python다운 예외 처리 (EAFP)**
```python
# LBYL (Look Before You Leap) - Java 스타일
# ❌ Python답지 않음
def get_value_lbyl(data, key):
    if key in data:
        return data[key]
    else:
        return None

# EAFP (Easier to Ask for Forgiveness than Permission) - Python 스타일
# ✅ Pythonic!
def get_value_eafp(data, key):
    try:
        return data[key]
    except KeyError:
        return None

# 파일 존재 확인
# ❌ LBYL
import os
if os.path.exists("file.txt"):
    with open("file.txt") as f:
        content = f.read()

# ✅ EAFP
try:
    with open("file.txt") as f:
        content = f.read()
except FileNotFoundError:
    content = None
```

**예시 2: 컨텍스트 매니저 활용**
```python
# ❌ 수동으로 정리
file = open("data.txt")
try:
    data = file.read()
    process(data)
finally:
    file.close()

# ✅ with 문 사용 (권장!)
with open("data.txt") as file:
    data = file.read()
    process(data)
# 자동으로 파일 닫힘!

# 여러 리소스
with open("input.txt") as infile, open("output.txt", "w") as outfile:
    data = infile.read()
    outfile.write(data.upper())
```

**예시 3: 로깅과 함께 사용**
```python
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)

def process_transaction(amount):
    try:
        # 거래 처리
        result = perform_transaction(amount)

    except ValueError as e:
        logging.error(f"거래 실패 (값 오류): {e}")
        raise  # 상위로 전달

    except Exception as e:
        logging.critical(f"예상치 못한 오류: {e}")
        raise

    else:
        logging.info(f"거래 성공: {amount:,}원")
        return result

    finally:
        logging.debug("거래 처리 완료")
```

### 💻 실습 (10분)

**[실습 파일: session7_best_practices_practice.py](./session7_best_practices_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session7_best_practices_solution.py](./session7_best_practices_solution.py)**

**핵심 포인트:**
1. EAFP 패턴 사용 (Pythonic)
2. with 문으로 리소스 관리
3. 적절한 예외만 잡기 (catch-all 피하기)
4. 예외를 무시하지 않기

---

## 세션 8: 디버깅 팁 (25분)
**중요도:** ★★★★☆

### 📖 이론 (10분)

#### 8.1 디버깅 도구

**예시 1: traceback 활용**
```python
import traceback

def function_a():
    function_b()

def function_b():
    function_c()

def function_c():
    # 오류 발생
    return 10 / 0

# 전체 스택 트레이스 출력
try:
    function_a()
except Exception as e:
    print("오류 발생!")
    traceback.print_exc()  # 전체 호출 스택 출력

# 스택 트레이스를 문자열로
try:
    function_a()
except Exception:
    error_msg = traceback.format_exc()
    print(error_msg)
```

**예시 2: assert 문**
```python
def calculate_average(numbers):
    # 개발 중 가정 검증
    assert len(numbers) > 0, "리스트가 비어있으면 안 됩니다"
    assert all(isinstance(n, (int, float)) for n in numbers), "모두 숫자여야 합니다"

    return sum(numbers) / len(numbers)

# 사용
avg = calculate_average([1, 2, 3, 4, 5])
# calculate_average([])  # AssertionError
# calculate_average([1, "2", 3])  # AssertionError

# 주의: python -O로 실행하면 assert 비활성화
```

**예시 3: 디버깅 정보 출력**
```python
def debug_function(data):
    print(f"[DEBUG] 입력 데이터: {data}")
    print(f"[DEBUG] 데이터 타입: {type(data)}")

    try:
        result = process(data)
        print(f"[DEBUG] 처리 결과: {result}")
        return result

    except Exception as e:
        print(f"[ERROR] 예외 발생: {e}")
        print(f"[ERROR] 예외 타입: {type(e).__name__}")
        import sys
        print(f"[DEBUG] Python 버전: {sys.version}")
        raise

# 더 나은 방법: logging 사용
import logging
logging.basicConfig(level=logging.DEBUG)

def better_debug_function(data):
    logging.debug(f"입력 데이터: {data}")
    logging.info("처리 시작")

    try:
        result = process(data)
        logging.info(f"처리 성공: {result}")
        return result
    except Exception as e:
        logging.error(f"처리 실패: {e}", exc_info=True)
        raise
```

### 💻 실습 (10분)

**[실습 파일: session8_debugging_practice.py](./session8_debugging_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session8_debugging_solution.py](./session8_debugging_solution.py)**

**핵심 포인트:**
1. `traceback.print_exc()` - 전체 스택 트레이스
2. `assert` - 개발 중 가정 검증
3. `logging` - 체계적인 로그 관리

---

## 🚀 후반부: 실전 프로젝트 (2시간)

### 프로젝트 선택 가이드

| 프로젝트 | 난이도 | 주요 기술 | 추천 대상 |
|----------|--------|-----------|-----------|
| 1. 업무 자동화 도구 | ⭐⭐⭐ | pandas, openpyxl | Excel 자동화 관심 |
| 2. 파일 정리 프로그램 | ⭐⭐ | os, shutil, pathlib | 파일 관리 자동화 |
| 3. 데이터 분석 리포트 | ⭐⭐⭐⭐ | pandas, matplotlib | 데이터 분석 |
| 4. 재고 관리 시스템 | ⭐⭐⭐⭐ | SQLite, OOP | 시스템 개발 |

---

### 프로젝트 1: 업무 자동화 도구

**개요:** 여러 Excel 파일의 데이터를 하나로 병합하고 분석 리포트를 생성

**요구사항:**
1. 데이터 병합 (여러 Excel 파일 읽기)
2. 데이터 검증 (필수 컬럼, 타입 검증)
3. 리포트 생성 (통계 계산, Excel 저장)
4. 예외 처리 (파일 없음, 잘못된 형식, 권한 오류)

**[실습 파일: project1_excel_automation.py](./project1_excel_automation.py)**

---

### 프로젝트 2: 파일 정리 프로그램

**개요:** 다운로드 폴더의 파일을 확장자별로 자동 분류

**요구사항:**
1. 파일 스캔 (대상 폴더 탐색, 확장자 분류)
2. 자동 정리 (폴더 생성, 파일 이동, 중복 처리)
3. 로깅 (이동 기록, 오류 로그)
4. 예외 처리 (권한, 중복 파일명, 디스크 공간)

**[실습 파일: project2_file_organizer.py](./project2_file_organizer.py)**

---

### 프로젝트 3: 데이터 분석 리포트

**개요:** CSV 데이터를 분석하고 시각화 리포트 생성

**요구사항:**
1. 데이터 로드 (CSV 읽기, 전처리)
2. 통계 분석 (기술 통계량, 그룹별 분석)
3. 시각화 (텍스트 기반 차트)
4. 예외 처리 (데이터 형식 오류, 결측치)

**[실습 파일: project3_data_report.py](./project3_data_report.py)**

---

### 프로젝트 4: 재고 관리 시스템

**개요:** 상품 재고를 관리하는 콘솔 기반 시스템

**요구사항:**
1. 상품 관리 (추가/수정/삭제/조회)
2. 재고 관리 (입고/출고/재고 경고)
3. 데이터 저장 (SQLite, 자동 백업)
4. 예외 처리 (재고 부족, 중복, DB 오류)

**[실습 파일: project4_inventory_system.py](./project4_inventory_system.py)**

---

## 🎯 Day 8 마무리

### 학습 내용 요약

| 세션 | 주제 | 중요도 | 핵심 키워드 |
|-----|------|--------|-----------|
| 1 | 예외 소개 | ★★★★★ | Exception, 주요 예외 타입 |
| 2 | try-except | ★★★★★ | 기본 문법, 예외 객체 |
| 3 | 여러 예외 처리 | ★★★★★ | 다중 except, 예외 계층 |
| 4 | finally와 else | ★★★★★ | 리소스 정리, with 문 |
| 5 | raise | ★★★★★ | 예외 발생, 검증 패턴 |
| 6 | 사용자 정의 예외 | ★★★★★ | 커스텀 예외 클래스 |
| 7 | 실무 패턴 | ★★★★★ | EAFP, 로깅 |
| 8 | 디버깅 | ★★★★☆ | traceback, assert, logging |

### 예외 처리 베스트 프랙티스

```python
# ✅ 좋은 예외 처리
try:
    result = process_data(data)
except FileNotFoundError as e:
    logger.error(f"파일 없음: {e}")
    # 대안 처리
except ValueError as e:
    logger.error(f"잘못된 값: {e}")
    raise  # 상위로 전달
else:
    logger.info("처리 성공")
    return result
finally:
    cleanup()
```

### 예외 처리 체크리스트

✅ 구체적인 예외 먼저 처리
✅ `Exception`을 마지막에 (최소한으로)
✅ 예외 무시하지 않기 (`pass` 금지)
✅ 적절한 로깅
✅ 리소스는 항상 정리 (`with` 문 사용)
✅ 사용자 정의 예외로 의미 명확하게

---

**축하합니다!**

8일간의 Python 기초 과정을 완료하셨습니다!

이제 여러분은:
- ✅ Python 기본 문법 완벽 이해
- ✅ 객체지향 프로그래밍 구현
- ✅ 예외 처리로 안정적인 프로그램 작성
- ✅ 실전 프로젝트 개발 경험

**다음 단계:**
1. Django/Flask 웹 개발
2. 데이터 분석 (pandas, NumPy, matplotlib)
3. 머신러닝 (scikit-learn)
4. 자동화 스크립트 (Selenium, BeautifulSoup)

**Happy Coding!** 🐍
