# 8일차: 예외 처리 및 실전 프로젝트

## 📚 학습 목표
- 예외 처리를 통한 안정적인 프로그램 작성
- try-except-finally 완벽 이해
- 사용자 정의 예외 생성
- 실무 프로젝트를 통한 종합 실습

---

## 🎯 오늘의 주요 내용

### ⏰ 일정 (총 4시간, 240분)

#### 전반부: 예외 처리 (2시간, 120분)
| 세션 | 주제 | 시간 | 실습 파일 |
|------|------|------|-----------|
| 1 | 예외란 무엇인가? | 25분 | [session1_exception_intro.py](session1_exception_intro.py) |
| 2 | try-except 기본 | 25분 | [session2_try_except.py](session2_try_except.py) |
| 3 | 여러 예외 처리 | 25분 | [session3_multiple_exceptions.py](session3_multiple_exceptions.py) |
| 4 | finally와 else | 25분 | [session4_finally_else.py](session4_finally_else.py) |
| 5 | raise로 예외 발생 | 25분 | [session5_raise.py](session5_raise.py) |
| 6 | 사용자 정의 예외 | 25분 | [session6_custom_exceptions.py](session6_custom_exceptions.py) |
| 7 | 예외 처리 실무 패턴 | 25분 | [session7_best_practices.py](session7_best_practices.py) |
| 8 | 디버깅 팁 | 25분 | [session8_debugging.py](session8_debugging.py) |

#### 후반부: 실전 프로젝트 (2시간, 120분)
| 프로젝트 | 설명 | 파일 |
|----------|------|------|
| 1 | 업무 자동화 도구 | [project1_excel_automation.py](project1_excel_automation.py) |
| 2 | 파일 정리 프로그램 | [project2_file_organizer.py](project2_file_organizer.py) |
| 3 | 데이터 분석 리포트 | [project3_data_report.py](project3_data_report.py) |
| 4 | 재고 관리 시스템 | [project4_inventory_system.py](project4_inventory_system.py) |

---

## 📖 전반부: 예외 처리

### Session 1: 예외란 무엇인가? (25분)

#### 이론 (10분)

##### 개념 ★★★★★
**예외(Exception)**는 프로그램 실행 중 발생하는 오류입니다.

```python
# 예외 발생 예시
number = int("abc")  # ValueError: invalid literal for int()
result = 10 / 0      # ZeroDivisionError: division by zero
file = open("없는파일.txt")  # FileNotFoundError
```

**오류 vs 예외:**
| 구분 | 설명 | 예시 |
|------|------|------|
| 문법 오류 (Syntax Error) | 코드 작성 실수 | `if True print("Hi")` |
| 예외 (Exception) | 실행 중 발생하는 오류 | `10 / 0` |

---

##### 왜 예외 처리가 중요한가? ★★★★★

**예외 처리 없이:**
```python
# ❌ 프로그램 중단!
def divide(a, b):
    return a / b

result = divide(10, 0)  # ZeroDivisionError로 프로그램 종료!
print("이 코드는 실행되지 않음")
```

**예외 처리 있음:**
```python
# ✅ 안정적으로 실행
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다!")
        return None

result = divide(10, 0)  # 예외 처리
print("이 코드는 실행됨")  # 계속 실행
```

---

##### Java와 비교
```java
// Java - Checked Exception
try {
    FileReader file = new FileReader("file.txt");
} catch (FileNotFoundException e) {
    e.printStackTrace();
}
```

```python
# Python - 모든 예외는 선택적
try:
    file = open("file.txt")
except FileNotFoundError:
    print("파일이 없습니다")
```

**Python의 특징:**
- Checked Exception 없음 (모든 예외가 선택적)
- 더 간결한 문법
- Duck Typing으로 유연함

---

##### 주요 내장 예외 ★★★★

| 예외 | 발생 원인 |
|------|-----------|
| `ValueError` | 잘못된 값 (예: `int("abc")`) |
| `TypeError` | 잘못된 타입 (예: `"2" + 2`) |
| `ZeroDivisionError` | 0으로 나누기 |
| `FileNotFoundError` | 파일이 없음 |
| `KeyError` | 딕셔너리에 키가 없음 |
| `IndexError` | 인덱스 범위 초과 |
| `AttributeError` | 속성이 없음 |
| `ImportError` | 모듈 import 실패 |

---

#### 실습 (10분)
**문제:** 다양한 예외 상황을 경험해보세요.

**요구사항:**
1. 정수 변환 오류 (ValueError)
2. 0으로 나누기 (ZeroDivisionError)
3. 리스트 인덱스 오류 (IndexError)
4. 딕셔너리 키 오류 (KeyError)

**실습 파일:** [session1_exception_intro.py](session1_exception_intro.py)

---

#### 해설 (5분)

##### 모범 답안
```python
# 1. ValueError
try:
    number = int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

# 2. ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

# 3. IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError as e:
    print(f"IndexError: {e}")

# 4. KeyError
try:
    my_dict = {"name": "John"}
    print(my_dict["age"])
except KeyError as e:
    print(f"KeyError: {e}")
```

##### 주요 포인트
✅ 예외는 프로그램 실행 중 발생하는 오류
✅ 예외 처리하지 않으면 프로그램 중단
✅ `as e`로 예외 객체 받아서 정보 확인 가능

---

### Session 2: try-except 기본 (25분)

#### 이론 (10분)

##### 기본 문법 ★★★★★
```python
try:
    # 예외가 발생할 수 있는 코드
    risky_operation()
except ExceptionType:
    # 예외 처리 코드
    handle_error()
```

**예제:**
```python
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다!")
        return None

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # 0으로 나눌 수 없습니다! → None
```

---

##### 예외 객체 활용 ★★★★
```python
try:
    number = int(input("숫자 입력: "))
except ValueError as e:
    print(f"오류 발생: {e}")
    print(f"오류 타입: {type(e).__name__}")
```

---

##### 실무 활용 사례 ★★★★★

**파일 읽기:**
```python
def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"'{filename}' 파일을 찾을 수 없습니다.")
        return None
```

**사용자 입력 검증:**
```python
def get_positive_number():
    while True:
        try:
            number = int(input("양수 입력: "))
            if number <= 0:
                print("양수를 입력하세요!")
                continue
            return number
        except ValueError:
            print("숫자를 입력하세요!")
```

---

#### 실습 (10분)
**문제:** 안전한 계산기를 만들어보세요.

**요구사항:**
1. 두 숫자와 연산자 입력받기
2. 계산 수행 (+, -, *, /)
3. 예외 처리:
   - ValueError (숫자 변환 실패)
   - ZeroDivisionError (0으로 나누기)
4. 계산 성공 시 결과 출력

**실습 파일:** [session2_try_except.py](session2_try_except.py)

---

#### 해설 (5분)

##### 모범 답안
```python
def calculator():
    try:
        num1 = float(input("첫 번째 숫자: "))
        operator = input("연산자 (+, -, *, /): ")
        num2 = float(input("두 번째 숫자: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            print("올바른 연산자를 입력하세요!")
            return

        print(f"결과: {result}")

    except ValueError:
        print("숫자를 입력하세요!")
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다!")
```

##### 주요 포인트
✅ try 블록에는 예외가 발생할 수 있는 코드
✅ except 블록에는 예외 처리 코드
✅ 여러 예외를 각각 처리 가능

---

### Session 3: 여러 예외 처리 (25분)

#### 이론 (10분)

##### 다중 except 블록 ★★★★★
```python
try:
    # 위험한 코드
    operation()
except ValueError:
    # ValueError 처리
    handle_value_error()
except TypeError:
    # TypeError 처리
    handle_type_error()
except Exception as e:
    # 그 외 모든 예외
    handle_other_errors(e)
```

---

##### 여러 예외를 한 번에 처리 ★★★★
```python
try:
    risky_code()
except (ValueError, TypeError) as e:
    print(f"ValueError 또는 TypeError 발생: {e}")
```

---

##### 예외 계층 구조 ★★★★
```
BaseException
├── Exception
│   ├── ValueError
│   ├── TypeError
│   ├── ZeroDivisionError
│   ├── FileNotFoundError
│   └── ...
├── KeyboardInterrupt
└── SystemExit
```

**주의:** `Exception`은 대부분의 예외를 잡지만, `KeyboardInterrupt`(Ctrl+C)는 잡지 않음!

---

#### 실습 (10분)
**문제:** 파일 처리 프로그램을 만들어보세요.

**요구사항:**
1. 파일명 입력받기
2. 파일 읽기
3. 정수 리스트로 변환
4. 예외 처리:
   - FileNotFoundError
   - ValueError (정수 변환 실패)
   - PermissionError (권한 없음)

**실습 파일:** [session3_multiple_exceptions.py](session3_multiple_exceptions.py)

---

#### 해설 (5분)

##### 모범 답안
```python
def read_numbers_from_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            numbers = [int(x) for x in content.split()]
            return numbers

    except FileNotFoundError:
        print(f"'{filename}' 파일을 찾을 수 없습니다.")
    except ValueError:
        print("파일에 숫자가 아닌 값이 포함되어 있습니다.")
    except PermissionError:
        print(f"'{filename}' 파일에 접근 권한이 없습니다.")
    except Exception as e:
        print(f"예상치 못한 오류: {e}")

    return None
```

##### 주요 포인트
✅ 구체적인 예외를 먼저 처리
✅ `Exception`은 마지막에 (catch-all)
✅ 각 예외에 맞는 처리 제공

---

### Session 4: finally와 else (25분)

#### 이론 (10분)

##### finally 블록 ★★★★★
**항상 실행되는 코드**

```python
try:
    file = open("data.txt", 'r')
    data = file.read()
except FileNotFoundError:
    print("파일이 없습니다")
finally:
    # 예외 발생 여부와 무관하게 실행
    print("정리 작업 수행")
    if 'file' in locals():
        file.close()
```

**언제 사용하나?**
- 파일 닫기
- 데이터베이스 연결 종료
- 리소스 해제

---

##### else 블록 ★★★★
**예외가 발생하지 않았을 때만 실행**

```python
try:
    number = int(input("숫자 입력: "))
except ValueError:
    print("숫자가 아닙니다!")
else:
    # 예외가 없었을 때만 실행
    print(f"입력한 숫자: {number}")
    result = number * 2
    print(f"2배: {result}")
finally:
    print("프로그램 종료")
```

---

##### 전체 구조 ★★★★★
```python
try:
    # 예외가 발생할 수 있는 코드
    risky_operation()
except SomeException:
    # 예외 처리
    handle_exception()
else:
    # 예외가 없을 때만 실행
    success_operation()
finally:
    # 항상 실행
    cleanup()
```

**실행 순서:**
1. `try` 블록 실행
2. 예외 발생 → `except` 블록 실행
3. 예외 없음 → `else` 블록 실행
4. 항상 `finally` 블록 실행

---

#### 실습 (10분)
**문제:** 파일 처리 프로그램을 개선해보세요.

**요구사항:**
1. 파일에서 숫자 읽기
2. 숫자 합계 계산
3. else: 성공 메시지
4. finally: 파일 닫기 확인

**실습 파일:** [session4_finally_else.py](session4_finally_else.py)

---

#### 해설 (5분)

##### 모범 답안
```python
def process_file(filename):
    file = None
    try:
        file = open(filename, 'r')
        numbers = [int(line.strip()) for line in file]
        total = sum(numbers)

    except FileNotFoundError:
        print(f"'{filename}' 파일을 찾을 수 없습니다.")
    except ValueError:
        print("숫자가 아닌 값이 포함되어 있습니다.")
    else:
        print(f"✓ 처리 성공!")
        print(f"  합계: {total}")
    finally:
        if file:
            file.close()
            print("파일이 닫혔습니다.")
```

##### 주요 포인트
✅ `finally`는 항상 실행 (리소스 정리)
✅ `else`는 예외 없을 때만 실행
✅ `with` 문을 사용하면 `finally` 불필요 (자동 정리)

---

### Session 5: raise로 예외 발생시키기 (25분)

#### 이론 (10분)

##### raise 기본 ★★★★★
**명시적으로 예외 발생**

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("잔액이 부족합니다!")
    return balance - amount

try:
    new_balance = withdraw(10000, 50000)
except ValueError as e:
    print(f"오류: {e}")
```

---

##### 예외 재발생 ★★★★
```python
def process_data(data):
    try:
        # 처리
        result = risky_operation(data)
    except Exception as e:
        print(f"로그: {e}")
        raise  # 예외를 상위로 전달
```

---

##### 검증 패턴 ★★★★★
```python
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("나이는 정수여야 합니다!")
    if age < 0 or age > 150:
        raise ValueError("나이는 0~150 사이여야 합니다!")
    return age
```

---

#### 실습 (10분)
**문제:** 은행 계좌 클래스를 만들어보세요.

**요구사항:**
1. BankAccount 클래스
2. deposit(): 입금 (음수 불가)
3. withdraw(): 출금 (잔액 초과 불가)
4. raise로 예외 발생

**실습 파일:** [session5_raise.py](session5_raise.py)

---

#### 해설 (5분)

##### 모범 답안
```python
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("입금액은 0보다 커야 합니다!")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("출금액은 0보다 커야 합니다!")
        if amount > self.balance:
            raise ValueError("잔액이 부족합니다!")
        self.balance -= amount
```

##### 주요 포인트
✅ `raise`로 조건 검증
✅ 적절한 예외 타입 선택
✅ 명확한 오류 메시지 제공

---

### Session 6: 사용자 정의 예외 (25분)

#### 이론 (10분)

##### 사용자 정의 예외 생성 ★★★★★
```python
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
```

---

##### 예외 계층 구조 만들기 ★★★★
```python
class ApplicationError(Exception):
    """애플리케이션 기본 예외"""
    pass

class DatabaseError(ApplicationError):
    """데이터베이스 오류"""
    pass

class ValidationError(ApplicationError):
    """검증 오류"""
    pass
```

---

##### 실무 활용 ★★★★★
```python
class UserRegistrationError(Exception):
    """사용자 등록 오류"""
    pass

def register_user(username, email, age):
    if age < 19:
        raise UserRegistrationError("19세 미만은 가입할 수 없습니다")

    if "@" not in email:
        raise UserRegistrationError("올바른 이메일 형식이 아닙니다")

    # 등록 처리
    print(f"✓ {username} 등록 완료")
```

---

#### 실습 (10분)
**문제:** 쇼핑몰 주문 시스템을 만들어보세요.

**요구사항:**
1. OutOfStockError 예외
2. InvalidQuantityError 예외
3. order() 함수에서 예외 발생

**실습 파일:** [session6_custom_exceptions.py](session6_custom_exceptions.py)

---

#### 해설 (5분)

##### 모범 답안
```python
class OutOfStockError(Exception):
    """재고 부족 예외"""
    def __init__(self, product, available):
        self.product = product
        self.available = available
        super().__init__(f"'{product}' 재고 부족 (재고: {available}개)")

class InvalidQuantityError(Exception):
    """유효하지 않은 수량 예외"""
    pass

def order(product, quantity, stock):
    if quantity <= 0:
        raise InvalidQuantityError("수량은 1 이상이어야 합니다")

    if quantity > stock:
        raise OutOfStockError(product, stock)

    print(f"✓ '{product}' {quantity}개 주문 완료")
```

##### 주요 포인트
✅ `Exception` 상속
✅ 의미 있는 예외 이름
✅ 추가 정보를 예외 객체에 포함

---

### Session 7: 예외 처리 실무 패턴 (25분)

#### 이론 (10분)

##### EAFP vs LBYL ★★★★★

**LBYL (Look Before You Leap)** - Java 스타일
```python
# ❌ Python답지 않음
if 'key' in my_dict:
    value = my_dict['key']
else:
    value = None
```

**EAFP (Easier to Ask for Forgiveness than Permission)** - Python 스타일
```python
# ✅ Pythonic!
try:
    value = my_dict['key']
except KeyError:
    value = None
```

---

##### 컨텍스트 매니저 활용 ★★★★★
```python
# ❌ 수동으로 정리
file = open("data.txt")
try:
    data = file.read()
finally:
    file.close()

# ✅ with 문 사용
with open("data.txt") as file:
    data = file.read()
# 자동으로 파일 닫힘!
```

---

##### 로깅과 함께 사용 ★★★★★
```python
import logging

def process_transaction(amount):
    try:
        # 처리
        result = perform_transaction(amount)
    except ValueError as e:
        logging.error(f"거래 실패: {e}")
        raise
    else:
        logging.info(f"거래 성공: {amount}")
        return result
```

---

#### 실습 (10분)
**문제:** 데이터 처리 파이프라인을 만들어보세요.

**요구사항:**
1. 파일 읽기 → 파싱 → 검증 → 저장
2. 각 단계에서 예외 처리
3. 로깅 추가

**실습 파일:** [session7_best_practices.py](session7_best_practices.py)

---

#### 해설 (5분)

##### 주요 포인트
✅ EAFP 패턴 사용 (Pythonic)
✅ with 문으로 리소스 관리
✅ 적절한 예외만 잡기 (catch-all 피하기)
✅ 예외를 무시하지 않기

##### 모범 사례
```python
# ✅ 좋은 예
try:
    result = process_data(data)
except SpecificError as e:
    logger.error(f"처리 실패: {e}")
    # 복구 시도 또는 재발생
    raise

# ❌ 나쁜 예
try:
    result = process_data(data)
except:  # 모든 예외를 잡음 (위험!)
    pass  # 무시 (버그 숨김!)
```

---

### Session 8: 디버깅 팁 (25분)

#### 이론 (10분)

##### traceback 활용 ★★★★★
```python
import traceback

try:
    risky_operation()
except Exception as e:
    print("오류 발생!")
    traceback.print_exc()  # 전체 스택 트레이스 출력
```

---

##### assert 문 ★★★★
```python
def divide(a, b):
    assert b != 0, "divisor는 0이 아니어야 합니다"
    return a / b

# 개발 중에만 활성화 (python -O로 비활성화)
```

---

##### pdb 디버거 ★★★★
```python
import pdb

def complex_function(data):
    result = process_step1(data)
    pdb.set_trace()  # 여기서 일시 중지
    result = process_step2(result)
    return result
```

---

#### 실습 (10분)
**문제:** 버그가 있는 코드를 디버깅해보세요.

**실습 파일:** [session8_debugging.py](session8_debugging.py)

---

#### 해설 (5분)

##### 디버깅 체크리스트
✅ 오류 메시지를 자세히 읽기
✅ 스택 트레이스 확인
✅ print 디버깅
✅ assert로 가정 검증
✅ 단위 테스트 작성

---

## 📖 후반부: 실전 프로젝트 (2시간)

### 프로젝트 선택 가이드

| 프로젝트 | 난이도 | 주요 기술 | 추천 대상 |
|----------|--------|-----------|-----------|
| 1. 업무 자동화 도구 | ⭐⭐⭐ | pandas, openpyxl | Excel 자동화에 관심 있는 분 |
| 2. 파일 정리 프로그램 | ⭐⭐ | os, shutil, pathlib | 파일 관리 자동화에 관심 있는 분 |
| 3. 데이터 분석 리포트 | ⭐⭐⭐⭐ | pandas, matplotlib | 데이터 분석에 관심 있는 분 |
| 4. 재고 관리 시스템 | ⭐⭐⭐⭐ | SQLite, OOP | 시스템 개발에 관심 있는 분 |

---

## 🚀 프로젝트 1: 업무 자동화 도구

### 프로젝트 개요
**여러 Excel 파일의 데이터를 하나로 병합하고 분석 리포트를 생성하는 도구**

### 요구사항
1. **데이터 병합**
   - 여러 Excel 파일 읽기
   - 데이터 통합
   - 중복 제거

2. **데이터 검증**
   - 필수 컬럼 확인
   - 데이터 타입 검증
   - 이상치 탐지

3. **리포트 생성**
   - 통계 계산
   - Excel 리포트 저장
   - 오류 로그 기록

4. **예외 처리**
   - 파일 없음
   - 잘못된 데이터 형식
   - 권한 오류

### 실습 파일
[project1_excel_automation.py](project1_excel_automation.py)

---

## 🚀 프로젝트 2: 파일 정리 프로그램

### 프로젝트 개요
**다운로드 폴더의 파일을 확장자별로 자동 분류하는 프로그램**

### 요구사항
1. **파일 스캔**
   - 대상 폴더의 모든 파일 탐색
   - 확장자 분류

2. **자동 정리**
   - 확장자별 폴더 생성
   - 파일 이동
   - 중복 파일 처리

3. **로깅**
   - 이동한 파일 기록
   - 오류 로그

4. **예외 처리**
   - 파일 접근 권한
   - 중복 파일명
   - 디스크 공간 부족

### 실습 파일
[project2_file_organizer.py](project2_file_organizer.py)

---

## 🚀 프로젝트 3: 데이터 분석 리포트 생성기

### 프로젝트 개요
**CSV 데이터를 분석하고 시각화 리포트를 생성하는 도구**

### 요구사항
1. **데이터 로드**
   - CSV 파일 읽기
   - 데이터 전처리

2. **통계 분석**
   - 기술 통계량
   - 그룹별 분석
   - 상관관계 분석

3. **시각화**
   - 차트 생성 (텍스트 기반)
   - 리포트 출력

4. **예외 처리**
   - 데이터 형식 오류
   - 결측치 처리

### 실습 파일
[project3_data_report.py](project3_data_report.py)

---

## 🚀 프로젝트 4: 재고 관리 시스템

### 프로젝트 개요
**상품 재고를 관리하는 콘솔 기반 시스템**

### 요구사항
1. **상품 관리**
   - 상품 추가/수정/삭제
   - 재고 조회

2. **재고 관리**
   - 입고 처리
   - 출고 처리
   - 재고 경고 (부족 시)

3. **데이터 저장**
   - SQLite 데이터베이스
   - 자동 백업

4. **예외 처리**
   - 재고 부족
   - 중복 상품
   - DB 연결 오류

### 실습 파일
[project4_inventory_system.py](project4_inventory_system.py)

---

## 💡 핵심 정리

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

---

### 예외 처리 체크리스트
✅ 구체적인 예외 먼저 처리
✅ `Exception`을 마지막에 (최소한으로)
✅ 예외 무시하지 않기 (`pass` 금지)
✅ 적절한 로깅
✅ 리소스는 항상 정리 (`with` 문 사용)
✅ 사용자 정의 예외로 의미 명확하게

---

## 📎 실습 파일 목록

### 전반부: 예외 처리
1. [session1_exception_intro.py](session1_exception_intro.py) - 예외 소개
2. [session2_try_except.py](session2_try_except.py) - try-except 기본
3. [session3_multiple_exceptions.py](session3_multiple_exceptions.py) - 여러 예외 처리
4. [session4_finally_else.py](session4_finally_else.py) - finally와 else
5. [session5_raise.py](session5_raise.py) - raise로 예외 발생
6. [session6_custom_exceptions.py](session6_custom_exceptions.py) - 사용자 정의 예외
7. [session7_best_practices.py](session7_best_practices.py) - 실무 패턴
8. [session8_debugging.py](session8_debugging.py) - 디버깅 팁

### 후반부: 실전 프로젝트
1. [project1_excel_automation.py](project1_excel_automation.py) - 업무 자동화 도구
2. [project2_file_organizer.py](project2_file_organizer.py) - 파일 정리 프로그램
3. [project3_data_report.py](project3_data_report.py) - 데이터 분석 리포트
4. [project4_inventory_system.py](project4_inventory_system.py) - 재고 관리 시스템

---

**축하합니다!** 🎉

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

**Happy Coding!** 🐍✨
