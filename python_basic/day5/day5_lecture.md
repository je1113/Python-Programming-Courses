# 파이썬 5일차 강의 교안

## 강의 정보
- **강의 시간**: 4시간 (240분)
- **세션 구성**: 이론(10분) + 실습(10분) + 해설(5분) = 25분/세트
- **총 세션**: 9개
- **주제**: 리스트와 함수 - 데이터 관리와 코드 재사용

---

## 📋 목차

1. [세션 1: 문자열 메서드 심화](#세션-1-문자열-메서드-심화-) (25분)
2. [세션 2: 리스트 기초](#세션-2-리스트-기초-) (25분)
3. [세션 3: 리스트 메서드](#세션-3-리스트-메서드-) (25분)
4. [세션 4: 리스트 슬라이싱](#세션-4-리스트-슬라이싱-) (25분)
5. [세션 5: 리스트 컴프리헨션 심화](#세션-5-리스트-컴프리헨션-심화-) (25분)
6. [세션 6: 함수 정의](#세션-6-함수-정의-) (25분)
7. [세션 7: 매개변수와 반환값](#세션-7-매개변수와-반환값-) (25분)
8. [세션 8: 함수 고급](#세션-8-함수-고급-) (25분)
9. [세션 9: 종합 프로젝트](#세션-9-종합-프로젝트-) (25분)

---

## 세션 1: 문자열 메서드 심화 ★★★★

### 📖 이론 (10분)

#### 개념 설명
문자열의 고급 메서드와 포맷팅 기법을 학습합니다.

#### 주요 개념
- **검색**: find(), index(), count()
- **검증**: startswith(), endswith(), isdigit(), isalpha()
- **포맷**: format(), f-string 고급 활용

#### 실무 활용 사례
- 이메일 검증
- 파일 확장자 확인
- 데이터 유효성 검사

#### 코드 예시
```python
# 예시 1: 검색과 개수
text = "Python Programming"

print(text.find("Pro"))  # 7 (위치)
print(text.find("Java"))  # -1 (없음)
print(text.count("o"))  # 2 (개수)

# 실무: 로그 파일 분석
log = "ERROR: Connection timeout"
if "ERROR" in log:
    error_pos = log.find("ERROR")
    print(f"에러 발견 (위치: {error_pos})")

# 예시 2: 검증 메서드
# 파일 확장자 확인
filename = "report.pdf"
if filename.endswith((".pdf", ".docx")):
    print("문서 파일")

# 이메일 검증
email = "user@example.com"
if "@" in email and "." in email.split("@")[1]:
    print("유효한 이메일")

# 숫자 확인
user_input = "12345"
if user_input.isdigit():
    number = int(user_input)
    print(f"숫자: {number}")

# 예시 3: format() 메서드
name = "김철수"
age = 28
city = "서울"

# format() 방식
message = "이름: {}, 나이: {}, 도시: {}".format(name, age, city)
print(message)

# 인덱스 지정
message = "이름: {0}, 나이: {1}, {0}님 환영합니다!".format(name, age)

# 키워드 인수
message = "이름: {name}, 나이: {age}".format(name=name, age=age)

# f-string (가장 권장)
message = f"이름: {name}, 나이: {age}, 도시: {city}"
```

---

### 💻 실습 (10분)

**[실습 파일: session1_string_advanced_practice.py](./session1_string_advanced_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session1_string_advanced_solution.py](./session1_string_advanced_solution.py)**

---

## 세션 2: 리스트 기초 ★★★★★

### 📖 이론 (10분)

#### 개념 설명
리스트는 여러 값을 순서대로 저장하는 가변 자료형입니다. Python에서 가장 많이 사용하는 자료구조입니다.

#### 주요 개념
- **생성**: `[값1, 값2, ...]`
- **인덱싱**: `list[0]` (0부터 시작)
- **수정 가능**: 값 추가, 삭제, 변경

#### 실무 활용 사례
- 장바구니 관리
- 게시판 글 목록
- 센서 데이터 수집

#### 코드 예시
```python
# 예시 1: 리스트 생성과 접근
fruits = ["사과", "바나나", "포도"]
print(fruits[0])  # "사과"
print(fruits[-1])  # "포도" (마지막)

# 길이
print(len(fruits))  # 3

# 포함 여부
if "사과" in fruits:
    print("사과 있음")

# 예시 2: 리스트 수정
numbers = [1, 2, 3, 4, 5]

# 값 변경
numbers[0] = 10
print(numbers)  # [10, 2, 3, 4, 5]

# 여러 타입 혼합 가능
mixed = [1, "hello", 3.14, True, [1, 2, 3]]
print(mixed)

# 예시 3: 실무 패턴
# 장바구니
cart = []
cart.append({"name": "키보드", "price": 45000})
cart.append({"name": "마우스", "price": 25000})

total = sum(item["price"] for item in cart)
print(f"총액: {total:,}원")

# 센서 데이터
temperatures = []
for i in range(5):
    temp = 20 + i * 0.5  # 시뮬레이션
    temperatures.append(temp)

avg_temp = sum(temperatures) / len(temperatures)
print(f"평균 온도: {avg_temp:.1f}°C")
```

---

### 💻 실습 (10분)

**[실습 파일: session2_list_basic_practice.py](./session2_list_basic_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session2_list_basic_solution.py](./session2_list_basic_solution.py)**

---

## 세션 3: 리스트 메서드 ★★★★★

### 📖 이론 (10분)

#### 개념 설명
리스트를 조작하는 다양한 내장 메서드입니다.

#### 주요 개념
- **추가**: append(), extend(), insert()
- **제거**: remove(), pop(), clear()
- **정렬**: sort(), reverse()
- **검색**: index(), count()

#### 실무 활용 사례
- 할 일 목록 관리
- 데이터 정렬
- 중복 제거

#### 코드 예시
```python
# 예시 1: 추가 메서드
fruits = ["사과", "바나나"]

# 끝에 추가
fruits.append("포도")
print(fruits)  # ["사과", "바나나", "포도"]

# 여러 개 추가
fruits.extend(["딸기", "수박"])
print(fruits)  # ["사과", "바나나", "포도", "딸기", "수박"]

# 특정 위치에 삽입
fruits.insert(1, "오렌지")
print(fruits)  # ["사과", "오렌지", "바나나", ...]

# 예시 2: 제거 메서드
numbers = [1, 2, 3, 4, 5, 3]

# 값으로 제거 (첫 번째만)
numbers.remove(3)
print(numbers)  # [1, 2, 4, 5, 3]

# 인덱스로 제거 및 반환
last = numbers.pop()
print(last)  # 3
print(numbers)  # [1, 2, 4, 5]

first = numbers.pop(0)
print(first)  # 1

# 전체 삭제
numbers.clear()
print(numbers)  # []

# 예시 3: 정렬과 검색
scores = [85, 92, 78, 95, 88]

# 정렬 (원본 변경)
scores.sort()
print(scores)  # [78, 85, 88, 92, 95]

# 역순 정렬
scores.sort(reverse=True)
print(scores)  # [95, 92, 88, 85, 78]

# 뒤집기
scores.reverse()
print(scores)  # [78, 85, 88, 92, 95]

# 검색
print(scores.index(92))  # 3 (위치)
print(scores.count(85))  # 1 (개수)

# 실무 패턴: 할 일 목록
todo_list = []

# 할 일 추가
todo_list.append("이메일 확인")
todo_list.append("회의 참석")
todo_list.append("보고서 작성")

# 할 일 완료 (제거)
todo_list.remove("이메일 확인")

# 우선순위 높은 할 일 추가
todo_list.insert(0, "긴급 업무")

print("남은 할 일:", todo_list)
```

---

### 💻 실습 (10분)

**[실습 파일: session3_list_methods_practice.py](./session3_list_methods_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session3_list_methods_solution.py](./session3_list_methods_solution.py)**

---

## 세션 4: 리스트 슬라이싱 ★★★★★

### 📖 이론 (10분)

#### 개념 설명
리스트의 일부분을 추출하거나 수정하는 방법입니다.

**기본 문법**
```python
list[시작:끝]         # 시작부터 끝-1까지
list[시작:끝:step]    # step만큼 건너뛰며
```

#### 주요 개념
- **추출**: `list[1:4]` (1, 2, 3번 인덱스)
- **복사**: `list[:]` (전체 복사)
- **역순**: `list[::-1]`

#### 실무 활용 사례
- 페이징 처리 (1-10번 게시물)
- 최근 N개 데이터
- 데이터 샘플링

#### 코드 예시
```python
# 예시 1: 기본 슬라이싱
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])    # [2, 3, 4]
print(numbers[:5])     # [0, 1, 2, 3, 4] (처음부터)
print(numbers[5:])     # [5, 6, 7, 8, 9] (끝까지)
print(numbers[:])      # 전체 복사

# 음수 인덱스
print(numbers[-3:])    # [7, 8, 9] (뒤에서 3개)
print(numbers[:-3])    # [0, 1, 2, 3, 4, 5, 6]

# 예시 2: step 활용
print(numbers[::2])    # [0, 2, 4, 6, 8] (짝수 인덱스)
print(numbers[1::2])   # [1, 3, 5, 7, 9] (홀수 인덱스)
print(numbers[::-1])   # [9, 8, 7, ..., 0] (역순)

# 예시 3: 실무 패턴
# 페이징 처리
posts = [f"게시물 {i}" for i in range(1, 101)]
page = 1
posts_per_page = 10

start = (page - 1) * posts_per_page
end = start + posts_per_page
current_page = posts[start:end]
print(current_page)  # 게시물 1~10

# 최근 5개
logs = ["log1", "log2", "log3", "log4", "log5", "log6", "log7"]
recent = logs[-5:]
print(recent)  # ['log3', 'log4', 'log5', 'log6', 'log7']

# Top 3
scores = [85, 92, 78, 95, 88, 91]
scores.sort(reverse=True)
top3 = scores[:3]
print(f"Top 3: {top3}")  # [95, 92, 91]

# 리스트 수정
numbers = [0, 1, 2, 3, 4, 5]
numbers[1:4] = [10, 20, 30]
print(numbers)  # [0, 10, 20, 30, 4, 5]
```

---

### 💻 실습 (10분)

**[실습 파일: session4_list_slicing_practice.py](./session4_list_slicing_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session4_list_slicing_solution.py](./session4_list_slicing_solution.py)**

---

## 세션 5: 리스트 컴프리헨션 심화 ★★★★★

### 📖 이론 (10분)

#### 개념 설명
리스트 컴프리헨션의 고급 기법을 학습합니다.

#### 주요 개념
- **중첩 리스트**: 2차원 리스트 생성
- **다중 조건**: if-else 조합
- **중첩 컴프리헨션**: 리스트 평탄화

#### 실무 활용 사례
- 행렬 생성
- 데이터 변환
- 필터링과 변환 동시 수행

#### 코드 예시
```python
# 예시 1: 조건부 변환
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 짝수는 2배, 홀수는 그대로
result = [n * 2 if n % 2 == 0 else n for n in numbers]
print(result)  # [1, 4, 3, 8, 5, 12, 7, 16, 9, 20]

# 60점 미만은 60점으로 보정
scores = [85, 45, 92, 58, 76]
adjusted = [score if score >= 60 else 60 for score in scores]
print(adjusted)  # [85, 60, 92, 60, 76]

# 예시 2: 중첩 리스트 컴프리헨션
# 구구단표 생성
gugudan = [[d * i for i in range(1, 10)] for d in range(2, 10)]
print(gugudan[0])  # [2, 4, 6, ..., 18] (2단)

# 2차원 리스트 평탄화
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 예시 3: 실무 패턴
# 딕셔너리 → 리스트
users = [
    {"name": "김철수", "age": 28},
    {"name": "이영희", "age": 25},
    {"name": "박민수", "age": 30}
]

names = [user["name"] for user in users]
print(names)  # ['김철수', '이영희', '박민수']

# 조건부 필터링 + 변환
adults = [user["name"] for user in users if user["age"] >= 30]
print(adults)  # ['박민수']

# 파일명 생성
dates = ["2025-12-01", "2025-12-02", "2025-12-03"]
filenames = [f"report_{date.replace('-', '')}.xlsx" for date in dates]
print(filenames)
# ['report_20251201.xlsx', 'report_20251202.xlsx', ...]
```

---

### 💻 실습 (10분)

**[실습 파일: session5_comprehension_advanced_practice.py](./session5_comprehension_advanced_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session5_comprehension_advanced_solution.py](./session5_comprehension_advanced_solution.py)**

---

## 세션 6: 함수 정의 ★★★★★

### 📖 이론 (10분)

#### 개념 설명
함수는 특정 작업을 수행하는 코드 블록입니다. 코드 재사용과 모듈화의 핵심입니다.

**기본 문법**
```python
def 함수명(매개변수):
    실행할 코드
    return 반환값
```

#### 주요 개념
- **def**: 함수 정의 키워드
- **매개변수**: 함수에 전달하는 값
- **return**: 결과 반환
- **호출**: `함수명(인수)`

#### 실무 활용 사례
- 반복되는 계산 (할인가, 부가세)
- 데이터 검증
- 포맷팅

#### 코드 예시
```python
# 예시 1: 기본 함수
def greet(name):
    print(f"안녕하세요, {name}님!")

greet("김철수")  # "안녕하세요, 김철수님!"
greet("이영희")  # "안녕하세요, 이영희님!"

# 예시 2: 반환값이 있는 함수
def add(a, b):
    return a + b

result = add(10, 20)
print(result)  # 30

# 다중 반환
def get_user_info():
    name = "김철수"
    age = 28
    return name, age  # 튜플로 반환

name, age = get_user_info()
print(f"{name}, {age}세")

# 예시 3: 실무 패턴
# 할인가 계산
def calculate_discount(price, rate=0.1):
    """
    할인가를 계산합니다.

    Args:
        price: 원가
        rate: 할인율 (기본값 0.1 = 10%)

    Returns:
        할인가
    """
    discount = price * rate
    return price - discount

final_price = calculate_discount(10000)
print(f"할인가: {final_price:,}원")  # 9,000원

final_price = calculate_discount(10000, 0.2)
print(f"할인가: {final_price:,}원")  # 8,000원

# 이메일 검증
def is_valid_email(email):
    if "@" not in email:
        return False
    if "." not in email.split("@")[1]:
        return False
    return True

print(is_valid_email("user@example.com"))  # True
print(is_valid_email("invalid.email"))  # False
```

---

### 💻 실습 (10분)

**[실습 파일: session6_function_basic_practice.py](./session6_function_basic_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session6_function_basic_solution.py](./session6_function_basic_solution.py)**

---

## 세션 7: 매개변수와 반환값 ★★★★★

### 📖 이론 (10분)

#### 개념 설명
함수의 매개변수와 반환값을 다양하게 활용하는 방법입니다.

#### 주요 개념
- **기본값**: 매개변수에 기본값 설정
- **가변 인수**: `*args`, `**kwargs`
- **키워드 인수**: 이름으로 전달

#### 실무 활용 사례
- 유연한 함수 설계
- API 함수 작성
- 설정 값 관리

#### 코드 예시
```python
# 예시 1: 기본값 매개변수
def create_user(name, age, city="서울"):
    return {
        "name": name,
        "age": age,
        "city": city
    }

user1 = create_user("김철수", 28)
print(user1)  # {'name': '김철수', 'age': 28, 'city': '서울'}

user2 = create_user("이영희", 25, "부산")
print(user2)  # {'name': '이영희', 'age': 25, 'city': '부산'}

# 예시 2: 가변 인수 (*args)
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# 리스트 언패킹
scores = [85, 92, 78]
print(sum_all(*scores))  # 255

# **kwargs (키워드 인수)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="김철수", age=28, city="서울")
# name: 김철수
# age: 28
# city: 서울

# 예시 3: 실무 패턴
# 다양한 할인 규칙
def calculate_price(price, discount=0, tax=0.1, shipping=3000):
    """
    최종 가격 계산

    Args:
        price: 상품 가격
        discount: 할인액 (기본 0원)
        tax: 세율 (기본 10%)
        shipping: 배송비 (기본 3,000원)
    """
    discounted = price - discount
    with_tax = discounted * (1 + tax)
    total = with_tax + shipping
    return int(total)

# 기본
print(calculate_price(10000))  # 14,000

# 할인 적용
print(calculate_price(10000, discount=2000))  # 11,800

# 무료 배송
print(calculate_price(10000, shipping=0))  # 11,000

# 키워드 인수로 명확하게
print(calculate_price(price=10000, discount=2000, shipping=0))
```

---

### 💻 실습 (10분)

**[실습 파일: session7_parameters_practice.py](./session7_parameters_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session7_parameters_solution.py](./session7_parameters_solution.py)**

---

## 세션 8: 함수 고급 ★★★★

### 📖 이론 (10분)

#### 개념 설명
람다 함수, 내장 함수, 함수 활용 패턴을 학습합니다.

#### 주요 개념
- **람다**: 한 줄 익명 함수
- **map/filter**: 리스트 변환/필터링
- **sorted**: 정렬 키 함수

#### 실무 활용 사례
- 간단한 변환 함수
- 데이터 정렬
- 콜백 함수

#### 코드 예시
```python
# 예시 1: 람다 함수
# 일반 함수
def add(a, b):
    return a + b

# 람다 (한 줄)
add_lambda = lambda a, b: a + b
print(add_lambda(10, 20))  # 30

# 즉시 사용
result = (lambda x: x ** 2)(5)
print(result)  # 25

# 예시 2: map과 filter
numbers = [1, 2, 3, 4, 5]

# map (변환)
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# filter (필터링)
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# 리스트 컴프리헨션이 더 깔끔 (권장)
squares = [x ** 2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]

# 예시 3: sorted with key
students = [
    {"name": "김철수", "score": 85},
    {"name": "이영희", "score": 92},
    {"name": "박민수", "score": 78}
]

# 점수 기준 정렬
sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)
for student in sorted_students:
    print(f"{student['name']}: {student['score']}점")
# 이영희: 92점
# 김철수: 85점
# 박민수: 78점

# 문자열 길이 정렬
words = ["apple", "banana", "kiwi", "strawberry"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # ['kiwi', 'apple', 'banana', 'strawberry']

# 실무 패턴: 데이터 변환 파이프라인
prices = [10000, 25000, 15000, 8000, 35000]

# 30000원 이상 → 20% 할인
discounted = [
    int(p * 0.8) if p >= 30000 else p
    for p in prices
]
print(discounted)  # [10000, 25000, 15000, 8000, 28000]
```

---

### 💻 실습 (10분)

**[실습 파일: session8_function_advanced_practice.py](./session8_function_advanced_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session8_function_advanced_solution.py](./session8_function_advanced_solution.py)**

---

## 세션 9: 종합 프로젝트 ★★★★★

### 📖 이론 (10분)

#### 복습 내용
오늘 배운 리스트와 함수를 종합하여 실무 프로그램을 만듭니다.

**핵심 개념 정리**
1. **리스트**: 데이터 컬렉션 관리
2. **리스트 메서드**: 추가, 제거, 정렬
3. **리스트 컴프리헨션**: 간결한 데이터 처리
4. **함수**: 코드 재사용
5. **매개변수**: 유연한 함수 설계

#### 통합 예제
```python
# 도서 관리 시스템
books = []

def add_book(title, author, year):
    """도서 추가"""
    book = {
        "title": title,
        "author": author,
        "year": year
    }
    books.append(book)
    print(f"'{title}' 추가됨")

def search_by_author(author):
    """작가로 검색"""
    results = [b for b in books if b["author"] == author]
    return results

def get_books_by_year(year):
    """연도별 도서"""
    return [b for b in books if b["year"] >= year]

def display_books(book_list):
    """도서 출력"""
    for i, book in enumerate(book_list, 1):
        print(f"{i}. {book['title']} - {book['author']} ({book['year']})")

# 사용 예시
add_book("파이썬 기초", "김철수", 2023)
add_book("자료구조", "이영희", 2024)
add_book("알고리즘", "김철수", 2025)

print("\n=== 전체 도서 ===")
display_books(books)

print("\n=== 김철수 작가의 도서 ===")
kim_books = search_by_author("김철수")
display_books(kim_books)

print("\n=== 2024년 이후 출간 ===")
recent_books = get_books_by_year(2024)
display_books(recent_books)
```

---

### 💻 실습 (10분)

**[실습 파일: session9_final_project_practice.py](./session9_final_project_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session9_final_project_solution.py](./session9_final_project_solution.py)**

---

## 📚 오늘의 핵심 정리

### 1. 리스트
```python
# 생성과 접근
fruits = ["사과", "바나나", "포도"]
print(fruits[0])

# 메서드
fruits.append("딸기")      # 추가
fruits.remove("바나나")    # 제거
fruits.sort()             # 정렬

# 슬라이싱
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])   # [1, 2, 3]
print(numbers[::-1])  # 역순

# 컴프리헨션
squares = [x**2 for x in range(1, 6)]
evens = [x for x in range(10) if x % 2 == 0]
```

### 2. 함수
```python
# 기본 함수
def greet(name):
    return f"안녕하세요, {name}님!"

# 기본값 매개변수
def create_user(name, city="서울"):
    return {"name": name, "city": city}

# 가변 인수
def sum_all(*numbers):
    return sum(numbers)

# 람다
add = lambda a, b: a + b
```

### Java vs Python
```python
# Java - ArrayList
# import java.util.ArrayList;
# ArrayList<String> fruits = new ArrayList<>();
# fruits.add("사과");

# Python - 리스트
fruits = []
fruits.append("사과")

# Java - 함수 (메서드)
# public int add(int a, int b) {
#     return a + b;
# }

# Python - 함수
def add(a, b):
    return a + b
```

---

## 🎯 다음 강의 예고

**6일차에서는:**
- 모듈과 패키지
- 파일 입출력
- CSV, JSON 처리
- 예외 처리

---

## ❓ FAQ

**Q1. 리스트 vs 튜플?**
- 리스트: 수정 가능 (대부분 사용)
- 튜플: 수정 불가 (고정 데이터)

**Q2. 함수는 언제 만드나요?**
- 같은 코드가 3번 이상 반복되면
- 복잡한 로직을 명확하게 표현하고 싶을 때

**Q3. 람다는 언제 사용?**
- 간단한 함수 (한 줄)
- 복잡하면 일반 함수 사용 권장

**Q4. 리스트 컴프리헨션 vs for 문?**
- 간단한 변환: 컴프리헨션
- 복잡한 로직: for 문

---

**강의 준비 완료! 화이팅!**
