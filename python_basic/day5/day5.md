# Day 5: 리스트와 함수 - 코드 재사용과 데이터 관리

## 📋 강의 개요

**학습 목표:**
- 문자열 고급 처리 기법 습득
- 리스트를 활용한 데이터 컬렉션 관리
- 함수를 통한 코드 재사용과 모듈화
- 실무에서 자주 사용하는 패턴 익히기

**소요 시간:** 4시간 (240분)

**세션 구성:** 9개 세션 × 25분 (이론 10분 + 실습 10분 + 해설 5분)

---

## 💡 Day 5를 배워야 하는 이유

### 1. 리스트 - 데이터 컬렉션의 핵심

**실무 활용 사례:**
- 엑셀 데이터 처리 (행/열 단위 작업)
- 게시판 글 목록, 댓글 목록 관리
- 쇼핑몰 장바구니, 주문 내역
- 센서 데이터, 로그 데이터 수집

**통계로 보는 리스트의 중요성:**
- Python 개발자 90% 이상이 매일 리스트 사용
- 데이터 분석 라이브러리(Pandas)의 기반 자료구조
- 알고리즘 코딩 테스트의 70% 이상이 리스트 활용

### 2. 함수 - 코드 재사용의 시작

**함수가 필요한 이유:**
```python
# ❌ 함수 없이 (코드 중복, 유지보수 어려움)
# 할인가 계산 1
price1 = 10000
if price1 >= 50000:
    discount1 = price1 * 0.2
elif price1 >= 30000:
    discount1 = price1 * 0.1
else:
    discount1 = 0
final1 = price1 - discount1

# 할인가 계산 2 (똑같은 코드 반복!)
price2 = 35000
if price2 >= 50000:
    discount2 = price2 * 0.2
elif price2 >= 30000:
    discount2 = price2 * 0.1
else:
    discount2 = 0
final2 = price2 - discount2

# ✅ 함수 사용 (재사용 가능, 유지보수 쉬움)
def calculate_discount(price):
    if price >= 50000:
        discount = price * 0.2
    elif price >= 30000:
        discount = price * 0.1
    else:
        discount = 0
    return price - discount

final1 = calculate_discount(10000)
final2 = calculate_discount(35000)
final3 = calculate_discount(60000)  # 새로운 계산도 쉽게!
```

**함수의 장점:**
- 코드 중복 제거 (DRY 원칙: Don't Repeat Yourself)
- 유지보수 용이 (할인율 변경 시 한 곳만 수정)
- 테스트 가능 (함수 단위 검증)
- 가독성 향상 (복잡한 로직을 의미있는 이름으로 추상화)

---

## 세션 1: 문자열 메서드 심화 (25분)
**중요도:** ★★★★☆

### 📚 이론 (10분)

#### 1.1 고급 문자열 메서드

**실무에서 자주 사용하는 메서드:**

```python
text = "Python Programming"

# 1. 검색 메서드
print(text.find("Pro"))        # 7 (첫 번째 위치)
print(text.find("Java"))       # -1 (없으면 -1)
print(text.index("Pro"))       # 7 (없으면 에러 발생!)

# 2. 개수 세기
print(text.count("o"))         # 2

# 3. 시작/끝 확인
print(text.startswith("Py"))   # True
print(text.endswith("ing"))    # True

# 4. 대소문자 변환
print(text.upper())            # PYTHON PROGRAMMING
print(text.lower())            # python programming
print(text.title())            # Python Programming
print(text.swapcase())         # pYTHON pROGRAMMING

# 5. 공백 제거
text = "  hello  "
print(text.strip())            # "hello"
print(text.lstrip())           # "hello  "
print(text.rstrip())           # "  hello"

# 6. 문자열 분리/결합
csv = "apple,banana,cherry"
fruits = csv.split(",")        # ['apple', 'banana', 'cherry']
result = " | ".join(fruits)    # "apple | banana | cherry"

# 7. 치환
text = "I like Java"
print(text.replace("Java", "Python"))  # "I like Python"

# 8. 정렬
print("Python".center(20, "-"))    # "-------Python-------"
print("Python".ljust(10))          # "Python    "
print("Python".rjust(10))          # "    Python"
print("42".zfill(5))               # "00042"
```

#### 1.2 format() 메서드

```python
# 1. 위치 인덱스
print("이름: {0}, 나이: {1}".format("김철수", 28))

# 2. 키워드 인자
print("이름: {name}, 나이: {age}".format(name="김철수", age=28))

# 3. 숫자 포맷팅
print("금액: {0:,}원".format(1000000))        # 1,000,000
print("비율: {0:.2f}%".format(85.5678))       # 85.57%
print("진행: {0:>5.1f}%".format(42.3))        # " 42.3%"
```

📌 **format() vs f-string**

Python 3.6 이전에는 `format()`을 주로 사용했지만, 현재는 **f-string이 표준**입니다.

```python
name = "김철수"
age = 28

# 예전 방식
print("이름: {}, 나이: {}".format(name, age))

# 현대적 방식 (권장)
print(f"이름: {name}, 나이: {age}")
```

#### 1.3 문자열 검증 메서드

```python
# 문자 타입 확인
print("123".isdigit())         # True (숫자)
print("abc".isalpha())         # True (문자)
print("abc123".isalnum())      # True (문자+숫자)
print("   ".isspace())         # True (공백)

# 대소문자 확인
print("ABC".isupper())         # True
print("abc".islower())         # True
print("Hello World".istitle()) # True
```

**실무 활용:**
```python
# 사용자 입력 검증
user_input = input("나이: ")
if user_input.isdigit():
    age = int(user_input)
    print(f"입력한 나이: {age}")
else:
    print("숫자만 입력하세요!")

# 파일 확장자 확인
filename = "report.pdf"
if filename.lower().endswith(('.pdf', '.docx', '.xlsx')):
    print("문서 파일입니다.")
```

#### 1.4 Java와 비교

```java
// Java
String text = "  hello  ";
text = text.trim();                    // 공백 제거
text = text.toUpperCase();             // 대문자
boolean starts = text.startsWith("H"); // 시작 확인
String[] parts = text.split(",");      // 분리
String joined = String.join("|", parts); // 결합
```

```python
# Python - 더 간결하고 직관적
text = "  hello  "
text = text.strip().upper()
starts = text.startswith("H")
parts = text.split(",")
joined = "|".join(parts)
```

💡 **Tip:** Python의 문자열 메서드는 **원본을 변경하지 않고** 새 문자열을 반환합니다. (불변성)

### 🔨 실습 (10분)

[실습 파일: string_advanced.py](./string_advanced.py)

**과제:** 고객 데이터 정제 및 분석 시스템

더러운 고객 데이터(이메일, 전화번호, 주소 등)를 정제하고 분석하는 프로그램을 작성하세요.

**요구사항:**
1. 이메일 주소 정제 (공백 제거, 소문자 변환, 도메인 추출)
2. 전화번호 형식 통일 (010-XXXX-XXXX)
3. 주소에서 도시명 추출
4. 고객명 정규화 (Title Case)
5. 도메인별 고객 수 집계

### 💬 해설 (5분)

**핵심 포인트:**
1. `strip()`, `lower()`로 기본 정제
2. `split()`과 `join()`으로 데이터 분리/결합
3. `replace()`로 형식 통일
4. `find()`, `startswith()`, `endswith()`로 패턴 검색

**자주 하는 실수:**
```python
# ❌ 원본 변경 기대
text = "  hello  "
text.strip()  # 아무 효과 없음!
print(text)   # "  hello  " (그대로)

# ✅ 반환값 저장
text = "  hello  "
text = text.strip()  # 반환값을 다시 저장
print(text)          # "hello"
```

**실무 팁:**
- 사용자 입력은 항상 `strip()` 먼저!
- 대소문자 구분 없는 비교는 `lower()` 사용
- 여러 조건 검사는 튜플 활용: `filename.endswith(('.pdf', '.docx'))`

---

## 세션 2: 정규표현식 기초 (25분) ⭐ 선택사항
**중요도:** ★★★☆☆

### 📚 이론 (10분)

#### 2.1 정규표현식이란?

📌 **정규표현식 (Regular Expression, Regex)**

문자열에서 **패턴을 검색, 추출, 치환**하기 위한 강력한 도구입니다.

**왜 필요한가?**
- 이메일 주소 검증: `user@example.com`
- 전화번호 추출: `010-1234-5678`
- 날짜 형식 확인: `2024-01-15`
- 로그 파싱: `[ERROR] Connection timeout`

#### 2.2 기본 패턴

```python
import re

text = "전화번호: 010-1234-5678, 이메일: user@example.com"

# 1. 검색 (search)
match = re.search(r'\d{3}-\d{4}-\d{4}', text)
if match:
    print(match.group())  # "010-1234-5678"

# 2. 모두 찾기 (findall)
emails = re.findall(r'\w+@\w+\.\w+', text)
print(emails)  # ['user@example.com']

# 3. 치환 (sub)
masked = re.sub(r'\d{4}-\d{4}', '****-****', text)
print(masked)  # "전화번호: 010-****-****, ..."

# 4. 분리 (split)
parts = re.split(r'[,\s]+', "apple, banana  cherry")
print(parts)  # ['apple', 'banana', 'cherry']
```

#### 2.3 자주 사용하는 패턴

| 패턴 | 의미 | 예시 |
|------|------|------|
| `\d` | 숫자 | `[0-9]` |
| `\w` | 문자+숫자+_ | `[a-zA-Z0-9_]` |
| `\s` | 공백 | 스페이스, 탭, 개행 |
| `.` | 임의의 문자 | 아무 문자 |
| `*` | 0회 이상 반복 | `a*` = "", "a", "aa" |
| `+` | 1회 이상 반복 | `a+` = "a", "aa" |
| `?` | 0~1회 | `a?` = "", "a" |
| `{n}` | 정확히 n회 | `\d{3}` = "123" |
| `{n,m}` | n~m회 | `\d{2,4}` = "12", "123" |
| `^` | 시작 | `^Hello` |
| `$` | 끝 | `world$` |
| `[]` | 문자 집합 | `[abc]` = a, b, c 중 하나 |
| `[^]` | 부정 | `[^0-9]` = 숫자가 아닌 것 |

#### 2.4 실무 예제

```python
import re

# 이메일 검증
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

print(is_valid_email("user@example.com"))  # True
print(is_valid_email("invalid-email"))     # False

# 전화번호 추출
text = "연락처: 010-1234-5678, 02-9876-5432"
phones = re.findall(r'\d{2,3}-\d{3,4}-\d{4}', text)
print(phones)  # ['010-1234-5678', '02-9876-5432']

# 날짜 형식 변환 (YYYY-MM-DD → MM/DD/YYYY)
date = "2024-01-15"
new_date = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', date)
print(new_date)  # "01/15/2024"
```

⚠️ **주의사항:**
- 정규표현식은 강력하지만 **과도하게 복잡하면 가독성 저하**
- 간단한 경우 문자열 메서드 사용 권장
- 정규표현식 디버깅 사이트 활용: [regex101.com](https://regex101.com)

### 🔨 실습 (10분)

[실습 파일: regex_basic.py](./regex_basic.py)

**과제:** 로그 파일 분석기

로그 데이터에서 정규표현식을 사용하여 필요한 정보를 추출하세요.

**요구사항:**
1. 날짜/시간 추출
2. 로그 레벨 추출 (INFO, ERROR, WARNING)
3. IP 주소 추출
4. 에러 메시지만 필터링
5. 개인정보(이메일, 전화번호) 마스킹

### 💬 해설 (5분)

**핵심 포인트:**
1. `re.search()` - 첫 번째 매칭
2. `re.findall()` - 모든 매칭
3. `re.sub()` - 치환
4. 그룹 `()` 사용으로 부분 추출

**자주 하는 실수:**
```python
# ❌ raw string 미사용 (이스케이프 문제)
pattern = "\d+"  # 잘못된 이스케이프

# ✅ raw string 사용
pattern = r"\d+"  # 올바름
```

**실무 팁:**
- 정규표현식은 **컴파일 후 재사용**하면 성능 향상
```python
pattern = re.compile(r'\d{3}-\d{4}')
for text in texts:
    pattern.findall(text)
```

---

## 세션 3: 리스트 생성과 접근 (25분)
**중요도:** ★★★★★

### 📚 이론 (10분)

#### 3.1 리스트란?

📌 **리스트 (List)**

**여러 개의 값을 하나의 변수에 저장**하는 자료구조입니다.

**왜 필요한가?**
```python
# ❌ 리스트 없이 (변수가 너무 많음)
student1 = "김철수"
student2 = "이영희"
student3 = "박민수"
# ... 100명이면?

# ✅ 리스트 사용 (효율적 관리)
students = ["김철수", "이영희", "박민수"]
```

#### 3.2 리스트 생성

```python
# 1. 대괄호 사용
numbers = [1, 2, 3, 4, 5]
names = ["김철수", "이영희", "박민수"]
mixed = [1, "hello", 3.14, True]  # 다양한 타입 가능

# 2. 빈 리스트
empty = []
empty = list()

# 3. range()로 생성
numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]
evens = list(range(0, 11, 2))  # [0, 2, 4, 6, 8, 10]

# 4. 반복으로 생성
zeros = [0] * 5  # [0, 0, 0, 0, 0]
grid = [[0] * 3 for _ in range(3)]  # 2차원 리스트
```

#### 3.3 리스트 접근

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# 1. 인덱싱 (0부터 시작!)
print(fruits[0])    # "apple" (첫 번째)
print(fruits[2])    # "cherry" (세 번째)
print(fruits[-1])   # "elderberry" (마지막)
print(fruits[-2])   # "date" (뒤에서 두 번째)

# 2. 슬라이싱
print(fruits[1:3])      # ['banana', 'cherry']
print(fruits[:2])       # ['apple', 'banana']
print(fruits[2:])       # ['cherry', 'date', 'elderberry']
print(fruits[::2])      # ['apple', 'cherry', 'elderberry'] (2칸씩)
print(fruits[::-1])     # 역순

# 3. 길이
print(len(fruits))  # 5

# 4. 포함 여부
print("apple" in fruits)  # True
print("grape" in fruits)  # False
```

#### 3.4 리스트 수정 (Mutable)

```python
numbers = [1, 2, 3, 4, 5]

# 요소 변경
numbers[0] = 10
print(numbers)  # [10, 2, 3, 4, 5]

# 슬라이스 변경
numbers[1:3] = [20, 30]
print(numbers)  # [10, 20, 30, 4, 5]
```

💡 **문자열 vs 리스트**

```python
# 문자열 - Immutable (변경 불가)
text = "hello"
# text[0] = "H"  # ❌ 에러!
text = "H" + text[1:]  # ✅ 새로운 문자열 생성

# 리스트 - Mutable (변경 가능)
chars = ['h', 'e', 'l', 'l', 'o']
chars[0] = 'H'  # ✅ 직접 변경 가능
print(chars)    # ['H', 'e', 'l', 'l', 'o']
```

#### 3.5 Java와 비교

```java
// Java - 배열 (크기 고정)
int[] numbers = {1, 2, 3, 4, 5};
String[] names = new String[3];
names[0] = "김철수";

// Java - ArrayList (크기 가변)
ArrayList<String> students = new ArrayList<>();
students.add("김철수");
students.add("이영희");
```

```python
# Python - 리스트 (크기 자동 조절)
students = ["김철수", "이영희"]
students.append("박민수")  # 자동으로 확장
```

### 🔨 실습 (10분)

[실습 파일: list_basic.py](./list_basic.py)

**과제:** 월별 매출 데이터 관리

12개월 매출 데이터를 리스트로 관리하고 다양한 분석을 수행하세요.

**요구사항:**
1. 12개월 매출 데이터 리스트 생성
2. 특정 월 매출 조회
3. 상반기/하반기 매출 계산
4. 최고/최저 매출 월 찾기
5. 매출 역순 출력

### 💬 해설 (5분)

**핵심 포인트:**
1. 인덱스는 **0부터 시작**
2. 음수 인덱스는 뒤에서부터
3. 슬라이싱 `[start:end]`는 start 포함, end 미포함
4. `in` 연산자로 포함 여부 확인

**자주 하는 실수:**
```python
# ❌ 인덱스 범위 초과
numbers = [1, 2, 3]
print(numbers[3])  # IndexError!

# ✅ 범위 확인
if len(numbers) > 3:
    print(numbers[3])
```

**실무 팁:**
- 마지막 요소는 `list[-1]`이 편리
- 리스트 복사는 `new_list = old_list[:]` 또는 `copy()`

---

## 세션 4: 리스트 메서드 (25분)
**중요도:** ★★★★★

### 📚 이론 (10분)

#### 4.1 요소 추가

```python
fruits = ["apple", "banana"]

# 1. append() - 끝에 추가
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']

# 2. insert() - 특정 위치에 추가
fruits.insert(1, "orange")  # 인덱스 1에 삽입
print(fruits)  # ['apple', 'orange', 'banana', 'cherry']

# 3. extend() - 다른 리스트 추가
fruits.extend(["date", "elderberry"])
print(fruits)  # ['apple', 'orange', 'banana', 'cherry', 'date', 'elderberry']

# extend vs append 차이
numbers = [1, 2, 3]
numbers.extend([4, 5])  # [1, 2, 3, 4, 5]

numbers = [1, 2, 3]
numbers.append([4, 5])  # [1, 2, 3, [4, 5]] - 리스트 자체가 추가됨!
```

#### 4.2 요소 제거

```python
fruits = ["apple", "banana", "cherry", "banana", "date"]

# 1. remove() - 값으로 제거 (첫 번째만)
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry', 'banana', 'date']

# 2. pop() - 인덱스로 제거 및 반환
last = fruits.pop()      # 마지막 요소 제거 및 반환
print(last)              # 'date'
second = fruits.pop(1)   # 인덱스 1 제거 및 반환
print(second)            # 'cherry'

# 3. clear() - 전체 삭제
fruits.clear()
print(fruits)  # []

# 4. del 문 - 인덱스/슬라이스 삭제
numbers = [1, 2, 3, 4, 5]
del numbers[0]       # [2, 3, 4, 5]
del numbers[1:3]     # [2, 5]
```

#### 4.3 검색 및 정렬

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# 1. index() - 값의 인덱스 찾기
pos = numbers.index(4)
print(pos)  # 2

# 2. count() - 값의 개수
count = numbers.count(1)
print(count)  # 2

# 3. sort() - 정렬 (원본 변경)
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

numbers.sort(reverse=True)  # 내림차순
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

# 4. sorted() - 정렬 (새 리스트 반환)
original = [3, 1, 4]
sorted_list = sorted(original)
print(original)     # [3, 1, 4] (원본 유지)
print(sorted_list)  # [1, 3, 4]

# 5. reverse() - 역순 (원본 변경)
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]
```

#### 4.4 복사

```python
# ❌ 잘못된 복사 (참조만 복사)
original = [1, 2, 3]
reference = original
reference[0] = 10
print(original)  # [10, 2, 3] - 원본도 변경됨!

# ✅ 올바른 복사 (얕은 복사)
original = [1, 2, 3]
copy1 = original[:]
copy2 = original.copy()
copy3 = list(original)

copy1[0] = 10
print(original)  # [1, 2, 3] - 원본 유지
print(copy1)     # [10, 2, 3]
```

⚠️ **2차원 리스트는 깊은 복사 필요:**
```python
import copy

# 얕은 복사 문제
original = [[1, 2], [3, 4]]
shallow = original[:]
shallow[0][0] = 10
print(original)  # [[10, 2], [3, 4]] - 원본도 변경!

# 깊은 복사
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 10
print(original)  # [[1, 2], [3, 4]] - 원본 유지
```

#### 4.5 유용한 함수

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# 최대/최소/합계
print(max(numbers))    # 9
print(min(numbers))    # 1
print(sum(numbers))    # 31

# 평균
avg = sum(numbers) / len(numbers)
print(avg)  # 3.875

# 모두 참/거짓
conditions = [True, True, False]
print(all(conditions))  # False (하나라도 False면)
print(any(conditions))  # True (하나라도 True면)
```

### 🔨 실습 (10분)

[실습 파일: list_methods.py](./list_methods.py)

**과제:** 할 일 관리 프로그램 (To-Do List)

리스트 메서드를 활용하여 할 일을 추가, 완료, 삭제하는 프로그램을 작성하세요.

**요구사항:**
1. 할 일 추가 (append)
2. 특정 위치에 긴급 업무 삽입 (insert)
3. 완료된 일 제거 (remove, pop)
4. 할 일 목록 정렬 (sort)
5. 중요도별 통계 (count)

### 💬 해설 (5분)

**핵심 포인트:**
1. `append()` vs `extend()` vs `insert()` 차이
2. `remove()` vs `pop()` 차이
3. `sort()` (원본 변경) vs `sorted()` (새 리스트)
4. 리스트 복사 시 주의사항

**자주 하는 실수:**
```python
# ❌ remove() 없는 값 제거
fruits = ["apple", "banana"]
fruits.remove("cherry")  # ValueError!

# ✅ 존재 확인 후 제거
if "cherry" in fruits:
    fruits.remove("cherry")
```

**실무 팁:**
- `pop()`은 스택(Stack) 구현에 유용
- 큰 리스트에서 `insert(0, x)`는 느림 → `deque` 사용 고려

---

## 세션 5: 리스트 슬라이싱 (25분)
**중요도:** ★★★★☆

### 📚 이론 (10분)

#### 5.1 슬라이싱 심화

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 기본: [start:end:step]
print(numbers[2:7])      # [2, 3, 4, 5, 6]
print(numbers[::2])      # [0, 2, 4, 6, 8] (짝수 인덱스)
print(numbers[1::2])     # [1, 3, 5, 7, 9] (홀수 인덱스)
print(numbers[::-1])     # 역순
print(numbers[::-2])     # [9, 7, 5, 3, 1] (역순 2칸씩)

# 음수 인덱스
print(numbers[-3:])      # [7, 8, 9] (마지막 3개)
print(numbers[:-3])      # [0, 1, 2, 3, 4, 5, 6] (뒤 3개 제외)
print(numbers[-5:-2])    # [5, 6, 7]
```

#### 5.2 슬라이싱으로 수정

```python
numbers = [0, 1, 2, 3, 4, 5]

# 부분 교체
numbers[1:3] = [10, 20]
print(numbers)  # [0, 10, 20, 3, 4, 5]

# 크기가 다른 교체
numbers[1:3] = [100, 200, 300]
print(numbers)  # [0, 100, 200, 300, 3, 4, 5]

# 삭제
numbers[1:3] = []
print(numbers)  # [0, 300, 3, 4, 5]

# 짝수 인덱스만 변경
numbers = [0, 1, 2, 3, 4, 5]
numbers[::2] = [10, 20, 30]
print(numbers)  # [10, 1, 20, 3, 30, 5]
```

#### 5.3 실무 활용 패턴

```python
# 1. 페이지네이션
items = list(range(100))
page = 2
page_size = 10
start = (page - 1) * page_size
end = start + page_size
page_items = items[start:end]
print(page_items)  # [10, 11, 12, ..., 19]

# 2. 배치 처리
data = list(range(100))
batch_size = 20

for i in range(0, len(data), batch_size):
    batch = data[i:i+batch_size]
    print(f"배치 {i//batch_size + 1}: {len(batch)}개")
    # 배치 처리 로직...

# 3. 슬라이딩 윈도우
temperatures = [20, 22, 25, 27, 26, 24, 23, 21]
window_size = 3

for i in range(len(temperatures) - window_size + 1):
    window = temperatures[i:i+window_size]
    avg = sum(window) / len(window)
    print(f"{i}~{i+window_size-1}일: 평균 {avg:.1f}°C")
```

#### 5.4 2차원 리스트 슬라이싱

```python
# 2차원 리스트
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 행 추출
print(matrix[0])     # [1, 2, 3] (첫 행)
print(matrix[1:3])   # [[4, 5, 6], [7, 8, 9]] (2~3행)

# 열 추출 (리스트 컴프리헨션 필요)
col = [row[1] for row in matrix]
print(col)  # [2, 5, 8] (두 번째 열)

# 부분 행렬
sub = [row[1:3] for row in matrix[0:2]]
print(sub)  # [[2, 3], [5, 6]]
```

### 🔨 실습 (10분)

[실습 파일: list_slicing.py](./list_slicing.py)

**과제:** 데이터 분석 및 리포트 생성

시계열 데이터를 슬라이싱하여 다양한 분석을 수행하세요.

**요구사항:**
1. 주간/월간 데이터 추출
2. 최근 N일 데이터 분석
3. 이동 평균 계산 (슬라이딩 윈도우)
4. 데이터 샘플링 (N개씩 건너뛰기)
5. 페이지 단위로 데이터 출력

### 💬 해설 (5분)

**핵심 포인트:**
1. `[start:end]` - end는 포함 안 됨
2. `[::-1]` - 역순
3. 음수 인덱스로 뒤에서부터 접근
4. 슬라이싱은 항상 새 리스트 생성

**자주 하는 실수:**
```python
# ❌ step에서 start > end (빈 리스트)
numbers = [0, 1, 2, 3, 4]
print(numbers[4:1])   # [] (빈 리스트)

# ✅ 역순 step 사용
print(numbers[4:1:-1])  # [4, 3, 2]
```

**실무 팁:**
- 마지막 N개: `list[-N:]`
- 처음 N개: `list[:N]`
- N개 제외한 나머지: `list[N:]` 또는 `list[:-N]`

---

## 세션 6: 리스트 컴프리헨션 (25분)
**중요도:** ★★★★★

### 📚 이론 (10분)

#### 6.1 리스트 컴프리헨션이란?

📌 **리스트 컴프리헨션 (List Comprehension)**

**리스트를 간결하게 생성**하는 Python의 강력한 기능입니다.

```python
# ❌ 기존 방식 (5줄)
squares = []
for i in range(10):
    squares.append(i ** 2)

# ✅ 리스트 컴프리헨션 (1줄)
squares = [i ** 2 for i in range(10)]
```

**왜 사용하는가?**
- 코드가 **짧고 명확**
- **빠름** (내부 최적화)
- **Pythonic** (Python답게 코드 작성)

#### 6.2 기본 문법

```python
# 형식: [표현식 for 변수 in 반복가능객체]

# 1. 숫자 리스트
numbers = [i for i in range(10)]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2. 제곱 리스트
squares = [i ** 2 for i in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 3. 문자열 처리
fruits = ["apple", "banana", "cherry"]
upper_fruits = [fruit.upper() for fruit in fruits]
# ['APPLE', 'BANANA', 'CHERRY']

# 4. 연산 적용
prices = [1000, 2000, 3000]
discounted = [price * 0.9 for price in prices]
# [900.0, 1800.0, 2700.0]
```

#### 6.3 조건문 포함

```python
# 형식: [표현식 for 변수 in 반복가능객체 if 조건]

# 1. 짝수만
evens = [i for i in range(10) if i % 2 == 0]
# [0, 2, 4, 6, 8]

# 2. 양수만
numbers = [-2, -1, 0, 1, 2]
positives = [n for n in numbers if n > 0]
# [1, 2]

# 3. 특정 길이 이상 문자열
words = ["a", "ab", "abc", "abcd"]
long_words = [word for word in words if len(word) >= 3]
# ['abc', 'abcd']

# 4. 조건부 표현식 (if-else)
# 형식: [참일때값 if 조건 else 거짓일때값 for 변수 in 반복가능객체]
numbers = [1, 2, 3, 4, 5]
labels = ["짝수" if n % 2 == 0 else "홀수" for n in numbers]
# ['홀수', '짝수', '홀수', '짝수', '홀수']
```

#### 6.4 중첩 컴프리헨션

```python
# 1. 2차원 리스트 생성
matrix = [[i * j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# 2. 평탄화 (Flatten)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. 조합 생성
colors = ["red", "blue"]
sizes = ["S", "M", "L"]
products = [f"{color}-{size}" for color in colors for size in sizes]
# ['red-S', 'red-M', 'red-L', 'blue-S', 'blue-M', 'blue-L']
```

#### 6.5 실무 활용

```python
# 1. 데이터 추출
employees = [
    {"name": "김철수", "age": 28},
    {"name": "이영희", "age": 32},
    {"name": "박민수", "age": 25}
]

names = [emp["name"] for emp in employees]
# ['김철수', '이영희', '박민수']

adults = [emp for emp in employees if emp["age"] >= 30]
# [{'name': '이영희', 'age': 32}]

# 2. 파일명 필터링
files = ["report.pdf", "data.csv", "image.png", "doc.pdf"]
pdf_files = [f for f in files if f.endswith(".pdf")]
# ['report.pdf', 'doc.pdf']

# 3. 좌표 생성
coords = [(x, y) for x in range(3) for y in range(3)]
# [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
```

#### 6.6 Java와 비교

```java
// Java - Stream API (Java 8+)
List<Integer> numbers = IntStream.range(0, 10)
    .map(i -> i * i)
    .boxed()
    .collect(Collectors.toList());

List<Integer> evens = numbers.stream()
    .filter(n -> n % 2 == 0)
    .collect(Collectors.toList());
```

```python
# Python - 훨씬 간결
numbers = [i * i for i in range(10)]
evens = [n for n in numbers if n % 2 == 0]
```

⚠️ **과도한 사용 주의:**
```python
# ❌ 너무 복잡 (가독성 저하)
result = [[x*y for x in range(10) if x % 2 == 0]
          for y in range(10) if y % 3 == 0]

# ✅ 일반 for문이 더 명확
result = []
for y in range(10):
    if y % 3 == 0:
        row = []
        for x in range(10):
            if x % 2 == 0:
                row.append(x * y)
        result.append(row)
```

### 🔨 실습 (10분)

[실습 파일: list_comprehension.py](./list_comprehension.py)

**과제:** 데이터 변환 및 필터링

리스트 컴프리헨션을 사용하여 다양한 데이터 변환 작업을 수행하세요.

**요구사항:**
1. 온도 데이터 섭씨 → 화씨 변환
2. 제품 중 재고 있는 것만 필터링
3. 학생 중 합격자 명단 추출
4. 구구단 2~9단 2차원 리스트 생성
5. 파일 경로에서 파일명만 추출

### 💬 해설 (5분)

**핵심 포인트:**
1. 기본: `[표현식 for 변수 in 반복가능객체]`
2. 조건: `[표현식 for 변수 in 반복가능객체 if 조건]`
3. if-else: `[참값 if 조건 else 거짓값 for 변수 in 반복가능객체]`
4. 중첩: 바깥쪽 for가 먼저, 안쪽 for가 나중

**자주 하는 실수:**
```python
# ❌ if-else 위치 틀림
[i for i in range(10) if i % 2 == 0 else i * 2]  # 문법 에러!

# ✅ 올바른 위치
[i if i % 2 == 0 else i * 2 for i in range(10)]
```

**실무 팁:**
- 단순한 변환/필터링만 사용
- 3줄 이상 복잡하면 일반 for문 사용
- 성능: 리스트 컴프리헨션 > for + append

---

## 세션 7: 함수 정의 (25분)
**중요도:** ★★★★★

### 📚 이론 (10분)

#### 7.1 함수란?

📌 **함수 (Function)**

**특정 작업을 수행하는 코드 블록**에 이름을 붙인 것입니다.

**왜 필요한가?**
- 코드 **재사용**
- **유지보수** 용이
- 코드 **가독성** 향상
- **테스트** 가능

```python
# ❌ 함수 없이 (중복 많음)
print("안녕하세요, 김철수님!")
print("안녕하세요, 이영희님!")
print("안녕하세요, 박민수님!")

# ✅ 함수 사용 (재사용)
def greet(name):
    print(f"안녕하세요, {name}님!")

greet("김철수")
greet("이영희")
greet("박민수")
```

#### 7.2 함수 정의

```python
# 기본 문법
def 함수이름():
    # 실행할 코드
    pass

# 예제 1: 간단한 함수
def hello():
    print("Hello, World!")

hello()  # 함수 호출

# 예제 2: 여러 줄 함수
def print_menu():
    print("=" * 30)
    print("1. 조회")
    print("2. 추가")
    print("3. 삭제")
    print("=" * 30)

print_menu()
```

#### 7.3 매개변수 (Parameters)

```python
# 1. 매개변수 1개
def greet(name):
    print(f"안녕하세요, {name}님!")

greet("김철수")

# 2. 매개변수 여러 개
def introduce(name, age):
    print(f"이름: {name}")
    print(f"나이: {age}세")

introduce("김철수", 28)

# 3. 기본값 (Default Value)
def greet(name, message="안녕하세요"):
    print(f"{message}, {name}님!")

greet("김철수")              # "안녕하세요, 김철수님!"
greet("이영희", "환영합니다")  # "환영합니다, 이영희님!"
```

#### 7.4 반환값 (Return)

```python
# 1. 값 반환
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8

# 2. 여러 값 반환 (튜플)
def get_name_age():
    return "김철수", 28

name, age = get_name_age()
print(name, age)  # 김철수 28

# 3. 조건부 반환
def abs_value(num):
    if num >= 0:
        return num
    else:
        return -num

print(abs_value(-5))  # 5
print(abs_value(3))   # 3

# 4. return 없음 (None 반환)
def print_hello():
    print("Hello")
    # return 없음

result = print_hello()  # "Hello" 출력
print(result)           # None
```

#### 7.5 독스트링 (Docstring)

```python
def calculate_discount(price, rate):
    """
    할인가를 계산합니다.

    Args:
        price: 원가
        rate: 할인율 (0~1 사이)

    Returns:
        할인 적용 후 가격

    Examples:
        >>> calculate_discount(10000, 0.2)
        8000.0
    """
    return price * (1 - rate)

# 독스트링 확인
print(calculate_discount.__doc__)
help(calculate_discount)
```

#### 7.6 Java와 비교

```java
// Java
public class Calculator {
    // 반환 타입 명시 필수
    public static int add(int a, int b) {
        return a + b;
    }

    // void = 반환값 없음
    public static void printHello() {
        System.out.println("Hello");
    }
}

Calculator.add(3, 5);
```

```python
# Python - 타입 명시 불필요 (동적 타입)
def add(a, b):
    return a + b

def print_hello():
    print("Hello")

add(3, 5)
print_hello()
```

💡 **Python 타입 힌트 (Type Hints):**
```python
# Python 3.5+ 타입 힌트 (선택사항)
def add(a: int, b: int) -> int:
    return a + b

# 실행에는 영향 없음, IDE/도구가 활용
result = add(3, 5)       # OK
result = add("a", "b")   # 경고는 나오지만 실행됨
```

### 🔨 실습 (10분)

[실습 파일: function_basic.py](./function_basic.py)

**과제:** 유틸리티 함수 모음

다양한 유틸리티 함수를 작성하세요.

**요구사항:**
1. 인사말 출력 함수
2. 사각형 넓이 계산 함수
3. 섭씨 → 화씨 변환 함수
4. 학점 계산 함수 (점수 → A, B, C, D, F)
5. 비밀번호 강도 검사 함수

### 💬 해설 (5분)

**핵심 포인트:**
1. `def 함수명(매개변수):`로 정의
2. `return`으로 값 반환
3. 기본값으로 선택적 매개변수 구현
4. 독스트링으로 함수 설명

**자주 하는 실수:**
```python
# ❌ return 후 코드 (실행 안 됨)
def add(a, b):
    return a + b
    print("완료")  # 실행되지 않음!

# ✅ return 전에 실행
def add(a, b):
    print("계산 중...")
    return a + b
```

**실무 팁:**
- 함수는 **한 가지 일**만 하도록
- 함수명은 **동사**로 시작 (calculate, get, is, print)
- 너무 긴 함수는 분리

---

## 세션 8: 함수 매개변수와 반환값 (25분)
**중요도:** ★★★★★

### 📚 이론 (10분)

#### 8.1 다양한 매개변수

```python
# 1. 위치 인자 (Positional Arguments)
def introduce(name, age, city):
    print(f"{name}, {age}세, {city} 거주")

introduce("김철수", 28, "서울")  # 순서대로

# 2. 키워드 인자 (Keyword Arguments)
introduce(city="부산", name="이영희", age=32)  # 순서 바뀌어도 OK

# 3. 기본값 매개변수
def greet(name, message="안녕하세요"):
    print(f"{message}, {name}님!")

greet("김철수")                    # "안녕하세요, 김철수님!"
greet("이영희", "환영합니다")       # "환영합니다, 이영희님!"

# ⚠️ 기본값 매개변수는 마지막에!
# def wrong(a=1, b):  # ❌ SyntaxError
def correct(b, a=1):  # ✅ OK
    pass
```

#### 8.2 가변 인자

```python
# 1. *args - 위치 인자들을 튜플로
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# 2. **kwargs - 키워드 인자들을 딕셔너리로
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="김철수", age=28, city="서울")
# name: 김철수
# age: 28
# city: 서울

# 3. 혼합 사용
def func(a, b, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

func(1, 2, 3, 4, 5, x=10, y=20)
# a=1, b=2
# args=(3, 4, 5)
# kwargs={'x': 10, 'y': 20}
```

#### 8.3 반환값 패턴

```python
# 1. 단일 값
def square(x):
    return x ** 2

# 2. 여러 값 (튜플 언패킹)
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide(10, 3)
print(q, r)  # 3 1

# 3. 리스트/딕셔너리 반환
def get_stats(numbers):
    return {
        "min": min(numbers),
        "max": max(numbers),
        "avg": sum(numbers) / len(numbers)
    }

stats = get_stats([1, 2, 3, 4, 5])
print(stats)  # {'min': 1, 'max': 5, 'avg': 3.0}

# 4. 조건부 반환 (Early Return)
def find_user(user_id):
    if user_id < 0:
        return None  # 조기 반환

    # 유저 검색 로직...
    return {"id": user_id, "name": "김철수"}

# 5. 반환값 없음 (None)
def log_message(msg):
    print(f"[LOG] {msg}")
    # return 없음 → None 반환

result = log_message("테스트")
print(result)  # None
```

#### 8.4 함수의 스코프 (Scope)

```python
# 전역 변수
global_var = 100

def test_scope():
    # 지역 변수
    local_var = 10
    print(global_var)  # 100 (전역 변수 읽기 가능)
    print(local_var)   # 10

test_scope()
# print(local_var)  # ❌ NameError (함수 밖에서 접근 불가)

# global 키워드
count = 0

def increment():
    global count  # 전역 변수 수정 선언
    count += 1

increment()
print(count)  # 1

# ⚠️ global 사용보다 반환값 활용 권장
def increment_better(count):
    return count + 1

count = 0
count = increment_better(count)
print(count)  # 1
```

#### 8.5 람다 함수 (Lambda)

```python
# 일반 함수
def add(a, b):
    return a + b

# 람다 함수 (익명 함수)
add_lambda = lambda a, b: a + b

print(add(3, 5))        # 8
print(add_lambda(3, 5)) # 8

# 주로 일회성 함수에 사용
numbers = [1, 2, 3, 4, 5]

# map() - 각 요소에 함수 적용
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# filter() - 조건 만족하는 요소만
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# sorted() - 정렬 기준
students = [
    {"name": "김철수", "score": 85},
    {"name": "이영희", "score": 92},
    {"name": "박민수", "score": 78}
]
sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
print(sorted_students)
```

💡 **람다 vs 일반 함수:**
- 람다: 간단한 일회성 작업
- 일반 함수: 복잡한 로직, 재사용

### 🔨 실습 (10분)

[실습 파일: function_params.py](./function_params.py)

**과제:** 계산기 함수 모음

다양한 매개변수 패턴을 사용하는 계산 함수들을 작성하세요.

**요구사항:**
1. 여러 숫자의 평균 계산 (*args)
2. 학생 정보 출력 (**kwargs)
3. 할인가 계산 (기본값 매개변수)
4. 통계 정보 반환 (딕셔너리)
5. 리스트 필터링 (람다 활용)

### 💬 해설 (5분)

**핵심 포인트:**
1. `*args` - 가변 위치 인자 (튜플)
2. `**kwargs` - 가변 키워드 인자 (딕셔너리)
3. 여러 값 반환 - 튜플 언패킹
4. 람다 - 간단한 익명 함수

**자주 하는 실수:**
```python
# ❌ 가변 인자 위치 틀림
def wrong(*args, required):  # 에러!
    pass

# ✅ 필수 인자가 먼저
def correct(required, *args):
    pass
```

**실무 팁:**
- 매개변수 3개 이상이면 키워드 인자 사용 고려
- `*args`, `**kwargs`는 필요할 때만 (과용 금지)
- 함수는 한 가지 타입 반환하도록 (일관성)

---

## 세션 9: 함수 활용 종합 (25분)
**중요도:** ★★★★★

### 📚 이론 (10분)

#### 9.1 함수 설계 원칙

**1. 단일 책임 원칙 (Single Responsibility)**
```python
# ❌ 한 함수가 너무 많은 일
def process_user(data):
    # 검증
    if not data.get("email"):
        return False
    # 저장
    save_to_db(data)
    # 이메일 전송
    send_email(data["email"])
    # 로그
    log(f"User {data['email']} created")
    return True

# ✅ 책임 분리
def validate_user(data):
    return bool(data.get("email"))

def create_user(data):
    if not validate_user(data):
        return False
    save_to_db(data)
    send_welcome_email(data["email"])
    log_user_creation(data["email"])
    return True
```

**2. 순수 함수 (Pure Function)**
```python
# ✅ 순수 함수 - 같은 입력 → 같은 출력, 부작용 없음
def calculate_total(price, quantity):
    return price * quantity

# ❌ 비순수 함수 - 외부 상태 변경
total = 0
def add_to_total(amount):
    global total
    total += amount  # 부작용!
```

**3. 명확한 이름**
```python
# ❌ 모호한 이름
def process(data):
    pass

def do_it(x, y):
    pass

# ✅ 명확한 이름
def calculate_discount(price):
    pass

def send_notification_email(user):
    pass
```

#### 9.2 실무 패턴

**1. 검증 함수**
```python
def validate_email(email):
    """이메일 유효성 검사"""
    if not email:
        return False, "이메일을 입력하세요"
    if "@" not in email:
        return False, "올바른 이메일 형식이 아닙니다"
    return True, "OK"

is_valid, message = validate_email("user@example.com")
if not is_valid:
    print(message)
```

**2. 데이터 변환 함수**
```python
def normalize_phone(phone):
    """전화번호 정규화: 010-1234-5678"""
    # 숫자만 추출
    digits = ''.join(c for c in phone if c.isdigit())

    if len(digits) != 11:
        return None

    return f"{digits[:3]}-{digits[3:7]}-{digits[7:]}"

print(normalize_phone("01012345678"))     # "010-1234-5678"
print(normalize_phone("010 1234 5678"))   # "010-1234-5678"
```

**3. 집계 함수**
```python
def calculate_statistics(numbers):
    """통계 계산"""
    if not numbers:
        return None

    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "avg": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }

stats = calculate_statistics([1, 2, 3, 4, 5])
print(f"평균: {stats['avg']}")
```

**4. 필터링 함수**
```python
def filter_active_users(users):
    """활성 사용자만 필터링"""
    return [user for user in users if user.get("active", False)]

def filter_by_age(users, min_age, max_age):
    """나이 범위로 필터링"""
    return [
        user for user in users
        if min_age <= user.get("age", 0) <= max_age
    ]
```

#### 9.3 함수 조합

```python
# 여러 함수를 조합하여 복잡한 작업 수행

def clean_text(text):
    """텍스트 정제"""
    return text.strip().lower()

def remove_special_chars(text):
    """특수문자 제거"""
    return ''.join(c for c in text if c.isalnum() or c.isspace())

def normalize_spaces(text):
    """공백 정규화"""
    return ' '.join(text.split())

def process_text(text):
    """텍스트 전처리 파이프라인"""
    text = clean_text(text)
    text = remove_special_chars(text)
    text = normalize_spaces(text)
    return text

result = process_text("  Hello,  World!!!  ")
print(result)  # "hello world"
```

#### 9.4 에러 처리

```python
def divide_safe(a, b):
    """안전한 나눗셈"""
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except TypeError:
        return None

print(divide_safe(10, 2))   # 5.0
print(divide_safe(10, 0))   # None
print(divide_safe(10, "a")) # None

# 또는 예외 발생
def divide(a, b):
    """나눗셈 (에러 발생 가능)"""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다")
    return a / b
```

#### 9.5 함수 문서화

```python
def calculate_bmi(weight, height):
    """
    BMI(체질량지수)를 계산합니다.

    Args:
        weight (float): 체중 (kg)
        height (float): 키 (m)

    Returns:
        dict: BMI 값과 판정 결과
            {
                'bmi': float,
                'category': str
            }

    Raises:
        ValueError: 체중 또는 키가 0 이하인 경우

    Examples:
        >>> result = calculate_bmi(70, 1.75)
        >>> print(result['bmi'])
        22.86
        >>> print(result['category'])
        '정상'
    """
    if weight <= 0 or height <= 0:
        raise ValueError("체중과 키는 0보다 커야 합니다")

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "저체중"
    elif bmi < 23:
        category = "정상"
    elif bmi < 25:
        category = "과체중"
    else:
        category = "비만"

    return {
        "bmi": round(bmi, 2),
        "category": category
    }
```

### 🔨 실습 (10분)

[실습 파일: function_practice.py](./function_practice.py)

**과제:** 직원 관리 시스템

함수를 활용하여 직원 데이터를 관리하는 시스템을 작성하세요.

**요구사항:**
1. 직원 추가 함수 (검증 포함)
2. 직원 검색 함수 (이름, 부서별)
3. 연봉 통계 계산 함수
4. 승진 처리 함수
5. 직원 목록 정렬 함수 (다양한 기준)

**함수 설계 원칙 적용:**
- 단일 책임
- 명확한 함수명
- 적절한 매개변수와 반환값
- 독스트링 작성

### 💬 해설 (5분)

**핵심 포인트:**
1. 각 함수는 한 가지 역할만
2. 검증, 변환, 집계 함수 분리
3. 함수 조합으로 복잡한 작업 구현
4. 독스트링으로 문서화

**자주 하는 실수:**
```python
# ❌ 함수 내부에서 print (재사용 어려움)
def calculate_total(items):
    total = sum(item['price'] for item in items)
    print(f"합계: {total}")  # 출력까지 담당
    return total

# ✅ 반환만 담당 (호출자가 출력 결정)
def calculate_total(items):
    return sum(item['price'] for item in items)

total = calculate_total(items)
print(f"합계: {total}")  # 호출 측에서 출력
```

**실무 팁:**
- 함수는 10~20줄 이내로 유지
- 매개변수는 3개 이하 권장
- 복잡한 조건은 별도 함수로 분리
- 함수명만 보고도 기능 파악 가능하게

---

## 🎯 Day 5 마무리

### 학습 내용 요약

1. **문자열 메서드 심화** ★★★★☆
   - find, replace, format, strip, split, join
   - 문자열 검증 메서드 (isdigit, isalpha 등)

2. **정규표현식 기초** ★★★☆☆ (선택)
   - 패턴 매칭 및 추출
   - re.search, findall, sub

3. **리스트 생성과 접근** ★★★★★
   - 인덱싱, 슬라이싱
   - Mutable vs Immutable

4. **리스트 메서드** ★★★★★
   - append, insert, extend, remove, pop
   - sort, reverse, count, index

5. **리스트 슬라이싱** ★★★★☆
   - 고급 슬라이싱 패턴
   - 실무 활용 (페이지네이션, 배치 처리)

6. **리스트 컴프리헨션** ★★★★★
   - 간결한 리스트 생성
   - 조건문 포함
   - 중첩 컴프리헨션

7. **함수 정의** ★★★★★
   - def, return
   - 매개변수, 기본값
   - 독스트링

8. **함수 매개변수와 반환값** ★★★★★
   - *args, **kwargs
   - 여러 값 반환
   - 람다 함수

9. **함수 활용 종합** ★★★★★
   - 함수 설계 원칙
   - 실무 패턴
   - 함수 조합

### 실무 활용 포인트

**리스트를 사용하는 경우:**
- 순서가 있는 데이터 컬렉션
- 중복 허용
- 동적으로 크기 변경
- 예: 주문 목록, 로그 데이터, 센서 값

**함수를 사용하는 경우:**
- 반복되는 코드
- 복잡한 로직 분리
- 테스트 가능한 단위
- 예: 계산, 검증, 데이터 변환

### 다음 단계 (Day 6 예고)

- 딕셔너리와 세트
- 튜플과 자료구조 비교
- 파일 입출력
- 예외 처리
- 모듈과 패키지

### 추가 학습 자료

**온라인 리소스:**
- Python 공식 문서: https://docs.python.org/ko/3/
- Real Python 튜토리얼: https://realpython.com
- LeetCode (리스트 문제): https://leetcode.com

**연습 문제:**
1. 리스트 컴프리헨션으로 피보나치 수열 생성
2. 함수로 간단한 계산기 구현
3. 문자열 처리 함수로 CSV 파서 작성

**과제:**
- 전화번호부 프로그램 (리스트 + 함수 활용)
- 성적 처리 시스템 (통계 함수 작성)
- 로그 분석기 (정규표현식 + 함수)

---

**수고하셨습니다! 🎉**

오늘 배운 리스트와 함수는 Python 프로그래밍의 핵심입니다.
실습 파일을 반복해서 연습하고, 자신만의 프로그램을 만들어보세요!
