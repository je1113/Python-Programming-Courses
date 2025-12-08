# 파이썬 1일차 강의 교안

## 강의 정보
- **강의 시간**: 4시간 (240분)
- **세션 구성**: 이론(10분) + 실습(10분) + 해설(5분) = 25분/세트
- **총 세션**: 9개
- **주제**: Python 기초 - 환경 구축부터 기본 자료형까지

---

## 📋 목차

1. [세션 1: 왜 파이썬인가?](#세션-1-왜-파이썬인가-) (25분)
2. [세션 2: 파이썬 특징과 활용](#세션-2-파이썬-특징과-활용-) (25분)
3. [세션 3: 개발 환경 구축](#세션-3-개발-환경-구축-) (25분)
4. [세션 4: 주석 작성법](#세션-4-주석-작성법-) (25분)
5. [세션 5: print() 함수](#세션-5-print-함수-) (25분)
6. [세션 6: 변수와 변수명 규칙](#세션-6-변수와-변수명-규칙-) (25분)
7. [세션 7: 숫자형 자료형](#세션-7-숫자형-자료형-) (25분)
8. [세션 8: 문자열 자료형](#세션-8-문자열-자료형-) (25분)
9. [세션 9: 불린 자료형](#세션-9-불린-자료형-) (25분)

---

## 세션 1: 왜 파이썬인가? ★★★★★

### 📖 이론 (10분)

#### 개념 설명
프로그래밍은 컴퓨터에게 내리는 명령어의 집합입니다. 파이썬은 가장 배우기 쉽고 강력한 프로그래밍 언어입니다.

**왜 파이썬인가?**
- **쉬운 문법**: 영어 문장처럼 읽힘
- **빠른 개발**: 같은 기능을 Java보다 5배 빠르게 구현
- **만능 언어**: 웹, AI, 데이터 분석, 자동화 모두 가능
- **방대한 생태계**: 50만개 이상의 무료 라이브러리

#### 주요 개념
- **프로그래밍**: 반복 작업을 자동화하여 시간 절약
- **실무 효과**: 30분 작업 → 3초로 단축
- **시장 가치**: Python 개발자 평균 연봉 신입 4,500만원

#### 실무 활용 사례
- 엑셀 파일 100개를 1초만에 합치기
- 웹사이트에서 데이터 자동 수집
- 1000개 파일 이름 일괄 변경

#### 코드 예시
```python
# 예시 1: Hello World (Java와 비교)
# Java: 5줄 필요
# public class HelloWorld {
#     public static void main(String[] args) {
#         System.out.println("Hello, World!");
#     }
# }

# Python: 1줄로 끝!
print("Hello, World!")

# 예시 2: 엑셀 100개 합치기 (실제로 가능)
import pandas as pd
import glob

files = glob.glob("*.xlsx")
result = pd.concat([pd.read_excel(f) for f in files])
result.to_excel("통합본.xlsx", index=False)
# 실행 시간: 1초 / 수동: 30분+

# 예시 3: 파일명 일괄 변경
import os

files = os.listdir("./photos")
for i, file in enumerate(files, 1):
    old_name = f"./photos/{file}"
    new_name = f"./photos/여행사진_{i}.jpg"
    os.rename(old_name, new_name)
# 1000개 파일: 2초 / 수동: 1시간+
```

---

### 💻 실습 (10분)

**[실습 파일: session1_why_python_practice.py](./session1_why_python_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session1_why_python_solution.py](./session1_why_python_solution.py)**

---

## 세션 2: 파이썬 특징과 활용 ★★★★

### 📖 이론 (10분)

#### 개념 설명
파이썬은 **인터프리터 언어**이자 **동적 타입 언어**입니다. 코드를 수정하면 즉시 실행 결과를 확인할 수 있습니다.

**주요 특징**
1. **인터프리터 언어**: 한 줄씩 바로 실행 (수정 후 1초 만에 확인)
2. **동적 타입**: 변수 타입을 자동으로 판단
3. **들여쓰기 문법**: 코드가 자동으로 깔끔해짐

#### Java vs Python 비교

**변수 선언**
```python
# Java - 타입 명시 필수
# String name = "김파이썬";
# int age = 28;
# double height = 175.5;

# Python - 타입 자동 판단
name = "김파이썬"  # 알아서 문자열
age = 28          # 알아서 정수
height = 175.5    # 알아서 실수
```

**조건문**
```python
# Java - 중괄호 사용
# if (age >= 18) {
#     System.out.println("성인입니다");
# }

# Python - 들여쓰기 사용
if age >= 18:
    print("성인입니다")
```

#### 실무 활용 분야
1. **데이터 분석**: Netflix 추천 시스템, NASA 우주 데이터 분석
2. **웹 개발**: Instagram, Spotify, YouTube, Dropbox
3. **AI/머신러닝**: Google AI, Tesla 자율주행, ChatGPT
4. **자동화**: 가격 모니터링, 뉴스 수집, 정기 리포트

#### 코드 예시
```python
# 예시 1: 동적 타입
number = 123      # 정수
number = "123"    # 문자열로 변경 가능 (Java는 불가)
print(type(number))  # <class 'str'>

# 예시 2: 데이터 분석 (간단한 예시)
import pandas as pd

# 엑셀 읽기 → 분석 → 그래프
sales = pd.read_excel("월별매출.xlsx")
monthly_total = sales.groupby("월")["매출"].sum()
print(monthly_total)

# 예시 3: 웹 크롤링 (간단한 예시)
import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.naver.com")
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.select('.news_title')
for title in titles:
    print(title.text)
```

---

### 💻 실습 (10분)

**[실습 파일: session2_python_features_practice.py](./session2_python_features_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session2_python_features_solution.py](./session2_python_features_solution.py)**

---

## 세션 3: 개발 환경 구축 ★★★★★

### 📖 이론 (10분)

#### 개념 설명
Python 개발을 위해서는 **Python 인터프리터**와 **코드 편집기(VS Code)**가 필요합니다.

**필수 도구**
1. **Python**: 코드를 실행하는 엔진
2. **VS Code**: 코드를 편하게 작성하는 도구
3. **가상환경**: 프로젝트별로 독립된 Python 환경

#### 주요 개념
- **인터프리터**: 파이썬 코드를 읽고 실행하는 프로그램
- **VS Code**: 무료, 가볍고 빠름, 전 세계 개발자 70% 사용
- **가상환경**: 프로젝트마다 다른 라이브러리 버전 사용 가능

#### 실무 활용 사례
- 프로젝트A는 pandas 1.0 필요
- 프로젝트B는 pandas 2.0 필요
- 가상환경으로 각각 독립적으로 관리

#### 설치 및 설정
```bash
# 예시 1: Python 설치 확인
python --version
# Python 3.12.x

# 예시 2: 가상환경 생성
python -m venv venv

# Windows 활성화
venv\Scripts\activate

# Mac/Linux 활성화
source venv/bin/activate

# 예시 3: 첫 프로그램 실행
# hello.py 파일 생성 후
print("환경 설정 완료!")
print("파이썬 학습 시작!")
```

---

### 💻 실습 (10분)

**[실습 파일: session3_setup_practice.py](./session3_setup_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session3_setup_solution.py](./session3_setup_solution.py)**

---

## 세션 4: 주석 작성법 ★★★★

### 📖 이론 (10분)

#### 개념 설명
주석은 코드에 대한 설명을 작성하는 방법입니다. 프로그램 실행에는 영향을 주지 않습니다.

**주석 문법**
- `#`: 한 줄 주석
- `"""` 또는 `'''`: 여러 줄 주석

#### 주요 개념
- **목적**: 코드의 의도와 이유를 설명
- **원칙**: "무엇"보다 "왜"를 설명
- **효과**: 3개월 후의 나와 팀원을 위한 배려

#### 실무 활용 사례
- 복잡한 로직 설명
- TODO 목록 작성
- 함수/클래스 설명 (Docstring)

#### 코드 예시
```python
# 예시 1: 한 줄 주석
MAX_RETRY = 5  # 서버 정책상 최대 5회까지만 재시도 허용

# 예시 2: 여러 줄 주석
"""
파일명: data_processor.py
작성자: 김파이썬
작성일: 2025-12-06
기능: 엑셀 데이터 자동 처리 프로그램
"""

# 예시 3: 좋은 주석 vs 나쁜 주석
# ❌ 나쁜 주석 (당연한 것 설명)
x = 5  # x에 5를 할당

# ✅ 좋은 주석 (의도/이유 설명)
TIMEOUT = 30  # API 응답 대기 시간 (30초 이상 시 타임아웃)

# TODO: 에러 처리 로직 추가 필요
result = calculate_total(data)
```

---

### 💻 실습 (10분)

**[실습 파일: session4_comments_practice.py](./session4_comments_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session4_comments_solution.py](./session4_comments_solution.py)**

---

## 세션 5: print() 함수 ★★★★★

### 📖 이론 (10분)

#### 개념 설명
`print()` 함수는 화면에 텍스트를 출력하는 함수입니다. 가장 기본적이고 자주 사용하는 함수입니다.

**기본 문법**
```python
print(값1, 값2, ...)
```

#### 주요 개념
- **여러 값 출력**: 쉼표로 구분
- **sep**: 구분자 지정 (기본값: 공백)
- **end**: 끝 문자 지정 (기본값: 줄바꿈)

#### 실무 활용 사례
- 디버깅: 변수 값 확인
- 로그 출력: 프로그램 실행 상태 기록
- 사용자 안내: 프로그램 진행 상황 표시

#### 코드 예시
```python
# 예시 1: 기본 출력
print("Hello, World!")
print(100)
print(3.14)
print("이름:", "김파이썬")
print("나이:", 28, "세")

# 예시 2: sep과 end 옵션
print("2025", "12", "06", sep="-")  # 2025-12-06
print("안녕하세요", end=" ")
print("반갑습니다")  # 안녕하세요 반갑습니다

# 예시 3: 여러 줄 출력
print("""
====================================
            명  함
====================================
이름: 김파이썬
직책: 데이터 분석가
====================================
""")
```

---

### 💻 실습 (10분)

**[실습 파일: session5_print_practice.py](./session5_print_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session5_print_solution.py](./session5_print_solution.py)**

---

## 세션 6: 변수와 변수명 규칙 ★★★★★

### 📖 이론 (10분)

#### 개념 설명
변수는 데이터를 저장하는 이름 붙인 공간입니다. 값을 재사용하고 코드를 효율적으로 만듭니다.

**기본 문법**
```python
변수명 = 값
```

#### 주요 개념
- **동적 타입**: 타입 선언 불필요 (자동 추론)
- **변수명 규칙**: 문자/숫자/언더스코어, 숫자로 시작 불가
- **네이밍 스타일**: snake_case (Python 권장)

#### 실무 활용 사례
- 설정 값 관리: API_KEY, MAX_RETRY
- 계산 결과 저장: total_price, average_score
- 상태 관리: is_logged_in, has_permission

#### 코드 예시
```python
# 예시 1: 변수 사용 (Java vs Python)
# Java: String name = "김파이썬";
# Python:
name = "김파이썬"  # 타입 자동 추론
age = 28
height = 175.5

print(f"{name}님, 환영합니다!")
print(f"{name}님의 나이는 {age}세입니다.")

# 예시 2: 변수명 규칙
# ✅ 가능한 변수명
user_name = "김파이썬"  # snake_case (권장)
userName = "김파이썬"   # camelCase
name1 = "김파이썬"
_name = "김파이썬"

# ❌ 불가능한 변수명
# 1name = "김파이썬"      # 숫자로 시작
# user-name = "김파이썬"  # 하이픈
# for = 10               # 예약어

# 예시 3: 상수 (대문자 + 언더스코어)
MAX_RETRY = 5
PI = 3.14159
API_KEY = "your-api-key-here"
```

---

### 💻 실습 (10분)

**[실습 파일: session6_variables_practice.py](./session6_variables_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session6_variables_solution.py](./session6_variables_solution.py)**

---

## 세션 7: 숫자형 자료형 ★★★★★

### 📖 이론 (10분)

#### 개념 설명
파이썬의 숫자형은 **정수(int)**와 **실수(float)** 두 가지가 있습니다.

**기본 문법**
```python
정수 = 10
실수 = 3.14
```

#### 주요 개념
- **int**: 소수점 없는 숫자, 크기 제한 없음
- **float**: 소수점 있는 숫자
- **연산자**: +, -, *, /, //, %, **

#### 실무 활용 사례
- 가격 계산: 총액, 할인가, 부가세
- 통계 계산: 평균, 합계, 최대/최소
- 페이지 계산: 전체 페이지 수

#### 코드 예시
```python
# 예시 1: 정수와 실수
age = 28
price = 45000
pi = 3.14159
rate = 0.15  # 15%

# 큰 숫자 (언더스코어 사용 가능)
salary = 1_000_000  # 백만

# 예시 2: 기본 연산
print(10 + 3)   # 13 (덧셈)
print(10 - 3)   # 7  (뺄셈)
print(10 * 3)   # 30 (곱셈)
print(10 / 3)   # 3.333... (나눗셈 - 항상 float!)
print(10 // 3)  # 3  (몫)
print(10 % 3)   # 1  (나머지)
print(10 ** 3)  # 1000 (거듭제곱)

# 예시 3: 가격 계산
price = 10000
quantity = 3
discount_rate = 0.2  # 20% 할인

total = price * quantity
discount = total * discount_rate
final_price = total - discount

print(f"총액: {total:,}원")
print(f"할인: {discount:,}원")
print(f"최종 금액: {final_price:,}원")
```

---

### 💻 실습 (10분)

**[실습 파일: session7_numbers_practice.py](./session7_numbers_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session7_numbers_solution.py](./session7_numbers_solution.py)**

---

## 세션 8: 문자열 자료형 ★★★★★

### 📖 이론 (10분)

#### 개념 설명
문자열(str)은 텍스트 데이터를 다루는 자료형입니다. 작은따옴표(' ') 또는 큰따옴표(" ")로 표현합니다.

**기본 문법**
```python
text = "Hello Python"
text = '안녕하세요'
```

#### 주요 개념
- **f-string**: 변수를 문자열에 삽입 (가장 권장)
- **연산**: + (연결), * (반복)
- **메서드**: upper(), lower(), strip(), split() 등

#### 실무 활용 사례
- 사용자 정보 출력: 이름, 이메일, 메시지
- 데이터 정제: 공백 제거, 대소문자 변환
- 파일명 생성: 날짜별 파일명, 순번 추가

#### 코드 예시
```python
# 예시 1: 문자열 생성과 연산
name = "김파이썬"
greeting = "안녕하세요"

# 연결
full_greeting = greeting + ", " + name + "님!"
print(full_greeting)  # 안녕하세요, 김파이썬님!

# 반복
print("=" * 20)  # ====================

# 길이
print(len(name))  # 4

# 예시 2: f-string (가장 권장!)
name = "김파이썬"
age = 28
height = 175.5

print(f"이름: {name}, 나이: {age}")
print(f"키: {height:.1f}cm")  # 소수점 1자리

# 표현식 가능
price = 10000
quantity = 3
print(f"총액: {price * quantity:,}원")  # 30,000원

# 예시 3: 문자열 메서드
text = "Hello Python"

print(text.upper())  # HELLO PYTHON (대문자)
print(text.lower())  # hello python (소문자)
print(text.replace("Python", "World"))  # Hello World

email = "  user@example.com  "
print(email.strip())  # "user@example.com" (공백 제거)

csv_data = "사과,바나나,포도"
fruits = csv_data.split(",")
print(fruits)  # ['사과', '바나나', '포도']
```

---

### 💻 실습 (10분)

**[실습 파일: session8_strings_practice.py](./session8_strings_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session8_strings_solution.py](./session8_strings_solution.py)**

---

## 세션 9: 불린 자료형 ★★★★

### 📖 이론 (10분)

#### 개념 설명
불린(bool)은 참(True) 또는 거짓(False) 두 가지 값만 가지는 자료형입니다. 조건문의 핵심입니다.

**기본 문법**
```python
is_active = True
is_married = False
```

#### 주요 개념
- **비교 연산자**: >, <, >=, <=, ==, !=
- **논리 연산자**: and, or, not
- **Truthy/Falsy**: 다른 값도 True/False로 평가됨

#### 실무 활용 사례
- 권한 확인: is_admin, has_permission
- 상태 관리: is_logged_in, is_active
- 조건 검사: age >= 18, score >= 60

#### 코드 예시
```python
# 예시 1: 비교 연산자
print(10 > 5)     # True
print(10 == 10)   # True
print(10 != 5)    # True

age = 25
print(age >= 18)  # True

# 문자열 비교
print("apple" == "apple")  # True
print("Apple" == "apple")  # False (대소문자 구분)

# 예시 2: 논리 연산자
age = 25
has_license = True

# and: 모두 참이어야 참
can_drive = (age >= 18) and has_license
print(can_drive)  # True

# or: 하나라도 참이면 참
is_vip = (age >= 65) or (has_license and age >= 18)
print(is_vip)  # True

# not: 반대로
is_minor = not (age >= 18)
print(is_minor)  # False

# 예시 3: Truthy와 Falsy
# Falsy 값 (거짓으로 평가)
print(bool(0))       # False
print(bool(""))      # False (빈 문자열)
print(bool(None))    # False

# Truthy 값 (참으로 평가)
print(bool(1))       # True
print(bool("Hi"))    # True
print(bool([1, 2]))  # True (비어있지 않은 리스트)
```

---

### 💻 실습 (10분)

**[실습 파일: session9_boolean_practice.py](./session9_boolean_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session9_boolean_solution.py](./session9_boolean_solution.py)**

---

## 📚 오늘의 핵심 정리

### 1. 프로그래밍 기초
- Python = 가장 배우기 쉽고 강력한 언어
- 30분 작업 → 3초로 단축 가능

### 2. 개발 환경
```bash
python --version              # 설치 확인
python -m venv venv           # 가상환경 생성
venv\Scripts\activate         # 활성화 (Windows)
```

### 3. 기본 문법
```python
# 주석
# 한 줄 주석
"""여러 줄 주석"""

# 출력
print("Hello")
print(f"이름: {name}")

# 변수
name = "김파이썬"
age = 28
```

### 4. 자료형
```python
# 숫자형
age = 28                    # int (정수)
height = 175.5              # float (실수)

# 문자열
name = "김파이썬"            # str
email = "user@example.com"

# 불린
is_student = True           # bool
is_active = False

# 타입 확인
print(type(age))            # <class 'int'>
```

### Java vs Python 비교
```python
# Java (5줄)
# public class HelloWorld {
#     public static void main(String[] args) {
#         System.out.println("Hello, World!");
#     }
# }

# Python (1줄)
print("Hello, World!")

# Java - 타입 명시
# String name = "김파이썬";
# int age = 28;

# Python - 타입 자동 추론
name = "김파이썬"
age = 28
```

---

## 🎯 다음 강의 예고

**2일차에서는:**
- 컬렉션 자료형 (리스트, 튜플, 딕셔너리, 집합)
- 자료형 변환과 input() 함수
- 연산자 완전 정복
- 조건 표현식 (삼항 연산자)

---

## ❓ FAQ

**Q1. Python 2 vs Python 3 차이는?**
- Python 2는 2020년 지원 종료
- 반드시 Python 3 사용 (현재 3.12 버전)

**Q2. PyCharm vs VS Code?**
- VS Code: 가볍고 빠름, 다양한 언어 지원 (권장)
- PyCharm: Python 전용, 무거움

**Q3. 가상환경은 꼭 필요한가요?**
- 프로젝트별 라이브러리 버전 관리를 위해 필수
- 협업 시 "내 컴퓨터에서는 되는데요?" 문제 방지

**Q4. 어떤 자료형을 사용해야 하나요?**
- 숫자 계산 → int, float
- 텍스트 처리 → str
- 참/거짓 판단 → bool
- 여러 값 저장 → list (2일차 학습)

---

**강의 준비 완료! 화이팅!**
