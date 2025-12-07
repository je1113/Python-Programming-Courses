# 파이썬 기초 - 4일차 강의 교안

**총 강의 시간:** 4시간 (240분)
**세션 구성:** 이론(10분) + 실습(10분) + 해설(5분) = 25분/세션

---

## 📋 강의 개요
- for 반복문 완전 정복
- 문자열 처리 심화
- 반복 작업 자동화
- 1~4일차 종합 퀴즈

---

## 세션 1: for 문 기초 (★★★★★)

### 📖 이론 (10분)

#### 1.1 for 문이란?

> **📌 개념: for 반복문**
>
> 시퀀스(리스트, 문자열 등)의 각 요소를 하나씩 순회하는 구문
>
> **왜 필요한가?**
> - 같은 작업을 여러 번 반복
> - 데이터를 하나씩 처리
> - 코드 중복 제거

**문제 상황**
```python
# ❌ 반복문 없이
print("1번 학생 출석")
print("2번 학생 출석")
print("3번 학생 출석")
# ... 100번 복사-붙여넣기?

students = ["김철수", "이영희", "박민수"]
print(f"{students[0]}님, 안녕하세요")
print(f"{students[1]}님, 안녕하세요")
print(f"{students[2]}님, 안녕하세요")
# 학생이 추가되면 코드도 추가...
```

**해결: for 문**
```python
# ✅ for 문 사용
for i in range(1, 101):
    print(f"{i}번 학생 출석")

students = ["김철수", "이영희", "박민수", "정지훈", "최민지"]
for student in students:
    print(f"{student}님, 안녕하세요")
```

#### 1.2 기본 문법

```python
# 리스트 순회
fruits = ["사과", "바나나", "포도"]
for fruit in fruits:
    print(fruit)
# 출력:
# 사과
# 바나나
# 포도

# 문자열 순회
text = "Hello"
for char in text:
    print(char)
# 출력: H, e, l, l, o (한 글자씩)

# 딕셔너리 순회
user = {"name": "김철수", "age": 28, "city": "서울"}

# 키만 순회
for key in user:
    print(key)

# 키-값 순회
for key, value in user.items():
    print(f"{key}: {value}")
```

#### 1.3 실무 활용 패턴

**1) 데이터 일괄 처리**
```python
# 여러 파일 처리
files = ["report1.txt", "report2.txt", "report3.txt"]

for file in files:
    print(f"{file} 처리 중...")
    # 실제로는 파일 읽기, 처리, 저장
    print(f"{file} 완료!")
```

**2) 가격 계산**
```python
# 장바구니 총액 계산
cart = [
    {"name": "키보드", "price": 45000},
    {"name": "마우스", "price": 25000},
    {"name": "모니터", "price": 350000}
]

total = 0
for item in cart:
    print(f"{item['name']}: {item['price']:,}원")
    total += item['price']

print(f"총액: {total:,}원")
```

**3) 데이터 변환**
```python
# 이름을 대문자로 변환
names = ["kim", "lee", "park"]
uppercase_names = []

for name in names:
    uppercase_names.append(name.upper())

print(uppercase_names)  # ["KIM", "LEE", "PARK"]

# 더 간단한 방법 (리스트 컴프리헨션)
uppercase_names = [name.upper() for name in names]
```

**4) 조건부 처리**
```python
# 합격자만 출력
scores = [85, 92, 58, 76, 95, 45, 88]

for score in scores:
    if score >= 60:
        print(f"{score}점 - 합격")
    else:
        print(f"{score}점 - 불합격")
```

**Java vs Python: for 문**
```java
// Java - 전통적인 for 문
String[] fruits = {"사과", "바나나", "포도"};

for (int i = 0; i < fruits.length; i++) {
    System.out.println(fruits[i]);
}

// Java - 향상된 for 문 (for-each)
for (String fruit : fruits) {
    System.out.println(fruit);
}
```

```python
# Python - 훨씬 간단!
fruits = ["사과", "바나나", "포도"]

for fruit in fruits:
    print(fruit)
```

### 🔨 실습 (10분)

**👉 [실습 파일: for_basic.py](./for_basic.py)**

**문제:** 상품 재고 관리 시스템

**요구사항:**
1. 상품 리스트 (딕셔너리 리스트)
   - 상품명, 재고, 가격
2. 모든 상품 정보 출력
3. 총 재고 가치 계산
4. 재고 부족 상품 찾기 (재고 5개 미만)

**출력 형식:**
```
===== 재고 현황 =====
키보드: 15개, 단가 45,000원
마우스: 3개, 단가 25,000원
모니터: 8개, 단가 350,000원
--------------------
총 재고 가치: X,XXX,XXX원
--------------------
재고 부족 상품:
- 마우스 (3개)
===================
```

### ✅ 해설 (5분)

**주요 포인트:**
1. **딕셔너리 접근:** `item["key"]`로 값 가져오기
2. **누적 계산:** 변수에 계속 더하기
3. **조건부 출력:** if 문으로 필터링

**초보자가 자주 하는 실수:**
1. **들여쓰기 오류**
   ```python
   for item in items:
   print(item)  # ❌ IndentationError

   for item in items:
       print(item)  # ✅ 4칸 들여쓰기
   ```

2. **변수명 오타**
   ```python
   for fruit in fruits:
       print(frut)  # ❌ NameError
   ```

3. **딕셔너리 키 오류**
   ```python
   for item in cart:
       print(item["nome"])  # ❌ KeyError (name 오타)
   ```

**추가 Tip:**
```python
# enumerate로 인덱스와 함께
fruits = ["사과", "바나나", "포도"]
for i, fruit in enumerate(fruits):
    print(f"{i+1}. {fruit}")
# 1. 사과
# 2. 바나나
# 3. 포도

# zip으로 두 리스트 동시 순회
names = ["김철수", "이영희", "박민수"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}점")
```

---

## 세션 2: range() 함수 활용 (★★★★★)

### 📖 이론 (10분)

#### 2.1 range() 함수란?

> **📌 개념: range()**
>
> 숫자 시퀀스를 생성하는 함수
> - 주로 for 문과 함께 사용
> - 메모리 효율적 (실제로 모든 수를 만들지 않음)

**기본 문법**
```python
# range(stop) - 0부터 stop-1까지
for i in range(5):
    print(i)
# 0, 1, 2, 3, 4

# range(start, stop) - start부터 stop-1까지
for i in range(1, 6):
    print(i)
# 1, 2, 3, 4, 5

# range(start, stop, step) - step만큼 증가
for i in range(0, 10, 2):
    print(i)
# 0, 2, 4, 6, 8

# 역순
for i in range(10, 0, -1):
    print(i)
# 10, 9, 8, ..., 1
```

#### 2.2 실무 활용 패턴

**1) 횟수 반복**
```python
# 5번 반복
for i in range(5):
    print("안녕하세요")

# 파일 여러 개 생성
for i in range(1, 11):
    filename = f"report_{i}.txt"
    print(f"{filename} 생성")
```

**2) 인덱스 접근**
```python
fruits = ["사과", "바나나", "포도", "딸기"]

# 인덱스로 접근
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# 짝수 인덱스만
for i in range(0, len(fruits), 2):
    print(fruits[i])  # 사과, 포도
```

**3) 구구단**
```python
# 2단
for i in range(1, 10):
    print(f"2 × {i} = {2 * i}")
```

**4) 구간 합계**
```python
# 1부터 100까지 합
total = 0
for i in range(1, 101):
    total += i
print(total)  # 5050

# 또는 sum 사용
total = sum(range(1, 101))
```

**5) 카운트다운**
```python
# 10부터 1까지
for i in range(10, 0, -1):
    print(f"{i}초 남았습니다...")
print("발사!")
```

**Java vs Python: 반복 횟수**
```java
// Java
for (int i = 0; i < 10; i++) {
    System.out.println(i);
}
```

```python
# Python
for i in range(10):
    print(i)
```

#### 2.3 range() 고급 활용

```python
# 리스트로 변환
numbers = list(range(1, 6))
print(numbers)  # [1, 2, 3, 4, 5]

# 역순 리스트
reverse = list(range(10, 0, -1))
print(reverse)  # [10, 9, 8, ..., 1]

# 짝수만
evens = list(range(0, 21, 2))
print(evens)  # [0, 2, 4, ..., 20]

# 홀수만
odds = list(range(1, 21, 2))
print(odds)  # [1, 3, 5, ..., 19]
```

### 🔨 실습 (10분)

**👉 [실습 파일: range_practice.py](./range_practice.py)**

**문제:** 구구단 출력 프로그램

**요구사항:**
1. 사용자로부터 단(2~9) 입력받기
2. 해당 단의 구구단 출력
3. 합계 계산
4. 짝수 결과만 출력

**출력 형식:**
```
===== 구구단 =====
원하는 단 (2~9): 5
-----------------
5 × 1 = 5
5 × 2 = 10
5 × 3 = 15
...
5 × 9 = 45
-----------------
합계: 225
-----------------
짝수 결과:
5 × 2 = 10
5 × 4 = 20
5 × 6 = 30
5 × 8 = 40
=================
```

### ✅ 해설 (5분)

**주요 포인트:**
1. **range(1, 10):** 1부터 9까지
2. **조건 확인:** if 문으로 짝수 필터링
3. **누적 합계:** total 변수 사용

**초보자가 자주 하는 실수:**
1. **range 범위 착각**
   ```python
   # 1부터 10까지? NO!
   range(1, 10)  # 1부터 9까지!
   range(1, 11)  # 1부터 10까지
   ```

2. **step 방향 오류**
   ```python
   range(10, 1, 1)   # ❌ 빈 시퀀스 (증가인데 역순)
   range(10, 1, -1)  # ✅ 10부터 2까지
   ```

**추가 Tip:**
```python
# 전체 구구단
for dan in range(2, 10):
    print(f"\n[{dan}단]")
    for i in range(1, 10):
        print(f"{dan} × {i} = {dan * i}")

# 패턴 생성
for i in range(1, 6):
    print("*" * i)
# *
# **
# ***
# ****
# *****
```

---

## 세션 3: for 문과 리스트 (★★★★★)

### 📖 이론 (10분)

#### 3.1 리스트 컴프리헨션

> **📌 개념: 리스트 컴프리헨션**
>
> 리스트를 생성하는 간결한 문법
> - 한 줄로 리스트 생성
> - 가독성과 성능 모두 우수

**기본 문법**
```python
# 일반 for 문
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# 리스트 컴프리헨션
squares = [i ** 2 for i in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

**조건 포함**
```python
# 짝수만
evens = [i for i in range(1, 11) if i % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# 60점 이상 점수만
scores = [85, 92, 58, 76, 95, 45, 88]
pass_scores = [score for score in scores if score >= 60]
print(pass_scores)  # [85, 92, 76, 95, 88]
```

**변환 포함**
```python
# 대문자 변환
names = ["kim", "lee", "park"]
upper_names = [name.upper() for name in names]
print(upper_names)  # ["KIM", "LEE", "PARK"]

# 가격에 세금 추가
prices = [10000, 25000, 15000]
prices_with_tax = [price * 1.1 for price in prices]
print(prices_with_tax)  # [11000.0, 27500.0, 16500.0]
```

#### 3.2 리스트 수정

```python
# 모든 요소에 2 곱하기
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    numbers[i] *= 2
print(numbers)  # [2, 4, 6, 8, 10]

# 조건부 수정
scores = [85, 92, 58, 76, 95]
for i in range(len(scores)):
    if scores[i] < 60:
        scores[i] = 60  # 최소 점수 보정
print(scores)  # [85, 92, 60, 76, 95]
```

#### 3.3 실무 활용

**1) 데이터 필터링**
```python
# 재고 부족 상품 찾기
products = [
    {"name": "키보드", "stock": 15},
    {"name": "마우스", "stock": 3},
    {"name": "모니터", "stock": 8}
]

low_stock = [p for p in products if p["stock"] < 5]
for product in low_stock:
    print(f"{product['name']} 재고 부족!")
```

**2) 파일명 일괄 생성**
```python
# 날짜별 보고서 파일명
dates = ["2025-12-01", "2025-12-02", "2025-12-03"]
filenames = [f"report_{date}.xlsx" for date in dates]
print(filenames)
# ["report_2025-12-01.xlsx", "report_2025-12-02.xlsx", ...]
```

**3) 데이터 집계**
```python
# 부서별 인원수
employees = [
    {"name": "김철수", "dept": "영업"},
    {"name": "이영희", "dept": "개발"},
    {"name": "박민수", "dept": "영업"},
    {"name": "정지훈", "dept": "개발"}
]

sales_count = len([e for e in employees if e["dept"] == "영업"])
dev_count = len([e for e in employees if e["dept"] == "개발"])

print(f"영업: {sales_count}명, 개발: {dev_count}명")
```

**Java vs Python: 리스트 변환**
```java
// Java - Stream 사용 (Java 8+)
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
List<Integer> squares = numbers.stream()
    .map(n -> n * n)
    .collect(Collectors.toList());
```

```python
# Python - 리스트 컴프리헨션
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
```

### 🔨 실습 (10분)

**👉 [실습 파일: list_processing.py](./list_processing.py)**

**문제:** 학생 성적 처리 시스템

**요구사항:**
1. 학생 리스트 (이름, 점수)
2. 모든 학생 출력
3. 합격자 리스트 (60점 이상)
4. 불합격자 리스트
5. 점수 보정 (50점 미만 → 50점으로)

**출력 형식:**
```
===== 전체 학생 =====
김철수: 85점
이영희: 45점
박민수: 92점
정지훈: 58점
--------------------
합격자 (4명):
- 김철수: 85점
- 박민수: 92점
...
--------------------
불합격자 (2명):
- 이영희: 45점
- 정지훈: 58점
--------------------
점수 보정 후:
이영희: 45점 → 50점
====================
```

### ✅ 해설 (5분)

**주요 포인트:**
1. **리스트 컴프리헨션:** 조건으로 필터링
2. **len():** 개수 세기
3. **조건부 출력:** 보정 대상만 표시

**초보자가 자주 하는 실수:**
1. **원본 리스트 수정**
   ```python
   # 반복 중 리스트 수정 주의!
   numbers = [1, 2, 3, 4, 5]
   for num in numbers:
       numbers.remove(num)  # ❌ 예상과 다르게 동작!
   ```

2. **리스트 컴프리헨션 과용**
   ```python
   # ❌ 복잡하면 일반 for 문 사용
   result = [x * 2 if x > 0 else x / 2 if x < 0 else 0 for x in nums]

   # ✅ 가독성 우선
   result = []
   for x in nums:
       if x > 0:
           result.append(x * 2)
       elif x < 0:
           result.append(x / 2)
       else:
           result.append(0)
   ```

**추가 Tip:**
```python
# 중첩 리스트 컴프리헨션
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 딕셔너리 컴프리헨션
names = ["김철수", "이영희", "박민수"]
name_dict = {i: name for i, name in enumerate(names)}
print(name_dict)  # {0: "김철수", 1: "이영희", 2: "박민수"}
```

---

## 세션 4: break와 continue 심화 (★★★★)

### 📖 이론 (10분)

#### 4.1 break와 continue

> **📌 개념**
>
> - **break:** 반복문 즉시 종료
> - **continue:** 현재 반복 건너뛰고 다음으로

**break 예시**
```python
# 특정 조건에서 중단
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    if num > 5:
        break  # 5 초과 시 중단
    print(num)
# 출력: 1, 2, 3, 4, 5

# 검색 후 중단
students = ["김철수", "이영희", "박민수", "정지훈"]
target = "박민수"

for student in students:
    if student == target:
        print(f"{target} 찾음!")
        break
```

**continue 예시**
```python
# 특정 조건 건너뛰기
for i in range(1, 11):
    if i % 2 == 0:
        continue  # 짝수는 건너뛰기
    print(i)
# 출력: 1, 3, 5, 7, 9

# 오류 데이터 건너뛰기
scores = [85, -1, 92, 0, 78, -5, 95]
valid_scores = []
for score in scores:
    if score < 0:
        continue  # 음수는 무시
    valid_scores.append(score)
```

#### 4.2 실무 활용 패턴

**1) 검색 최적화**
```python
# 대량 데이터에서 찾기
users = [
    {"id": 1, "name": "김철수"},
    {"id": 2, "name": "이영희"},
    # ... 수천 개
]

target_id = 2
for user in users:
    if user["id"] == target_id:
        print(f"찾음: {user['name']}")
        break  # 찾았으면 중단 (효율적!)
```

**2) 입력 검증**
```python
# 유효한 입력 받을 때까지
while True:
    age = input("나이 (1-120): ")

    if not age.isdigit():
        print("숫자만 입력하세요")
        continue

    age = int(age)
    if 1 <= age <= 120:
        break  # 유효하면 종료
    else:
        print("1~120 사이로 입력하세요")

print(f"입력된 나이: {age}")
```

**3) 데이터 정제**
```python
# 빈 문자열, 공백 제거
texts = ["  hello  ", "", "world", "   ", "python"]
cleaned = []

for text in texts:
    text = text.strip()
    if not text:  # 빈 문자열
        continue
    cleaned.append(text)

print(cleaned)  # ["hello", "world", "python"]
```

**4) 조건부 처리**
```python
# 주말 제외 처리
days = ["월", "화", "수", "목", "금", "토", "일"]
for day in days:
    if day in ["토", "일"]:
        continue  # 주말 건너뛰기
    print(f"{day}요일 근무")
```

**Java vs Python: break/continue**
```java
// Java
for (int i = 0; i < 10; i++) {
    if (i == 5) break;
    if (i % 2 == 0) continue;
    System.out.println(i);
}
```

```python
# Python - 동일
for i in range(10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)
```

#### 4.3 else 절 (Python 특징!)

> **📌 Python만의 특징: for-else**
>
> break 없이 정상 종료 시 else 실행

```python
# 목록에서 찾기
numbers = [1, 3, 5, 7, 9]
target = 4

for num in numbers:
    if num == target:
        print("찾음!")
        break
else:
    print("못 찾음!")  # break 없이 끝나면 실행

# 소수 판별
number = 17
for i in range(2, number):
    if number % i == 0:
        print(f"{number}는 소수가 아님")
        break
else:
    print(f"{number}는 소수")
```

### 🔨 실습 (10분)

**👉 [실습 파일: break_continue.py](./break_continue.py)**

**문제:** 로그인 시스템 (3회 제한)

**요구사항:**
1. 최대 3회 시도 가능
2. 올바른 비밀번호 입력 시 즉시 종료
3. 3회 실패 시 계정 잠금
4. 빈 입력은 무시 (continue)

**출력 형식:**
```
===== 로그인 =====
비밀번호:
빈 입력입니다. 다시 입력하세요.

비밀번호: 1111
틀렸습니다. (남은 횟수: 2)

비밀번호: 1234
로그인 성공!
==================

또는

비밀번호: (3회 실패)
계정이 잠겼습니다.
```

### ✅ 해설 (5분)

**주요 포인트:**
1. **반복 횟수 제한:** range(3)
2. **즉시 종료:** break
3. **건너뛰기:** continue

**초보자가 자주 하는 실수:**
1. **무한 루프**
   ```python
   while True:
       print("멈추지 않음!")
       # break가 없으면 무한 반복!
   ```

2. **잘못된 위치의 break**
   ```python
   for i in range(10):
       if i == 5:
           break
   print("종료")  # for 밖 - 항상 실행

   for i in range(10):
       if i == 5:
           break
       print("종료")  # for 안 - i가 5일 때만 실행 안 됨
   ```

**추가 Tip:**
```python
# 중첩 반복문에서 break
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # 내부 for만 중단
        print(f"({i}, {j})")

# 모두 중단하려면 flag 사용
found = False
for i in range(3):
    for j in range(3):
        if i == j == 1:
            found = True
            break
    if found:
        break
```

---

## 세션 5: 중첩 반복문 (★★★★)

### 📖 이론 (10분)

#### 5.1 중첩 반복문이란?

> **📌 개념: 중첩 반복문**
>
> 반복문 안에 또 다른 반복문
> - 2차원 데이터 처리
> - 조합 생성
> - 패턴 출력

**기본 구조**
```python
# 2중 반복
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()  # 줄바꿈

# 출력:
# (0, 0) (0, 1) (0, 2)
# (1, 0) (1, 1) (1, 2)
# (2, 0) (2, 1) (2, 2)
```

#### 5.2 실무 활용 패턴

**1) 구구단 전체**
```python
print("===== 구구단 전체 =====")
for dan in range(2, 10):
    print(f"\n[{dan}단]")
    for i in range(1, 10):
        print(f"{dan} × {i} = {dan * i}")
```

**2) 좌석 배치**
```python
rows = 5
cols = 10

print("좌석 배치도:")
for row in range(1, rows + 1):
    for col in range(1, cols + 1):
        seat = f"{row:02d}-{col:02d}"
        print(seat, end=" ")
    print()

# 출력:
# 01-01 01-02 01-03 ... 01-10
# 02-01 02-02 02-03 ... 02-10
# ...
```

**3) 메뉴 조합**
```python
main_dishes = ["햄버거", "피자", "파스타"]
drinks = ["콜라", "사이다", "주스"]

print("세트 메뉴:")
for main in main_dishes:
    for drink in drinks:
        print(f"{main} + {drink}")

# 햄버거 + 콜라
# 햄버거 + 사이다
# ...
```

**4) 2차원 리스트**
```python
# 성적표
scores = [
    [85, 90, 88],  # 1번 학생
    [92, 88, 95],  # 2번 학생
    [78, 85, 80]   # 3번 학생
]

for i, student_scores in enumerate(scores, 1):
    print(f"\n{i}번 학생:")
    subjects = ["국어", "영어", "수학"]
    for j, score in enumerate(student_scores):
        print(f"  {subjects[j]}: {score}점")
```

**5) 패턴 생성**
```python
# 별 삼각형
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# 출력:
# *
# **
# ***
# ****
# *****

# 역삼각형
for i in range(5, 0, -1):
    print("*" * i)
```

**Java vs Python: 중첩 반복문**
```java
// Java
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        System.out.println("(" + i + ", " + j + ")");
    }
}
```

```python
# Python
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
```

### 🔨 실습 (10분)

**👉 [실습 파일: nested_loop.py](./nested_loop.py)**

**문제:** 영화관 좌석 예약 시스템

**요구사항:**
1. 5행 8열 좌석 생성
2. 전체 좌석 출력 (A1, A2, ...)
3. 예약된 좌석 표시
4. 예약 가능 좌석 개수

**출력 형식:**
```
===== 좌석 현황 =====
  1  2  3  4  5  6  7  8
A O  O  X  O  O  O  O  O
B O  O  O  X  X  O  O  O
C O  O  O  O  O  O  O  O
D X  O  O  O  O  O  X  O
E O  O  O  O  O  O  O  O
---------------------
총 좌석: 40석
예약석: 6석
잔여석: 34석
=====================
```

### ✅ 해설 (5분)

**주요 포인트:**
1. **행 문자:** chr(65 + i) → A, B, C...
2. **2차원 구조:** 행과 열
3. **조건부 표시:** 예약 여부 확인

**초보자가 자주 하는 실수:**
1. **인덱스 혼동**
   ```python
   # i와 j 헷갈림
   for i in range(rows):
       for j in range(cols):
           print(matrix[j][i])  # ❌ 잘못됨
           print(matrix[i][j])  # ✅ 올바름
   ```

2. **줄바꿈 위치**
   ```python
   # 잘못된 위치
   for i in range(3):
       print()  # ❌ 먼저 줄바꿈
       for j in range(3):
           print("*", end="")

   # 올바른 위치
   for i in range(3):
       for j in range(3):
           print("*", end="")
       print()  # ✅ 나중에 줄바꿈
   ```

**추가 Tip:**
```python
# 대각선 패턴
for i in range(5):
    for j in range(5):
        if i == j:
            print("*", end=" ")
        else:
            print("O", end=" ")
    print()

# 출력:
# * O O O O
# O * O O O
# O O * O O
# O O O * O
# O O O O *
```

---

## 세션 6: 숫자형 자료형 심화 (★★★★)

### 📖 이론 (10분)

#### 6.1 숫자 처리 함수

```python
# 절대값
print(abs(-10))  # 10

# 반올림
print(round(3.7))      # 4
print(round(3.14159, 2))  # 3.14

# 최대/최소
numbers = [5, 2, 8, 1, 9]
print(max(numbers))  # 9
print(min(numbers))  # 1

# 합계
print(sum(numbers))  # 25

# 거듭제곱
print(pow(2, 3))  # 8
print(2 ** 3)     # 8 (동일)
```

#### 6.2 math 모듈

```python
import math

# 올림/내림/버림
print(math.ceil(3.1))   # 4 (올림)
print(math.floor(3.9))  # 3 (내림)
print(math.trunc(3.9))  # 3 (버림)

# 제곱근
print(math.sqrt(16))  # 4.0

# 상수
print(math.pi)  # 3.141592653589793
print(math.e)   # 2.718281828459045

# 삼각함수
print(math.sin(math.pi / 2))  # 1.0
print(math.cos(0))  # 1.0
```

#### 6.3 실무 활용

**1) 가격 계산**
```python
# 부가세 포함 가격
price = 10000
vat = price * 0.1
total = price + vat

# 반올림
total = round(total)
print(f"총액: {total:,}원")
```

**2) 할인율 계산**
```python
original = 50000
discounted = 40000

discount_rate = (original - discounted) / original * 100
print(f"할인율: {discount_rate:.1f}%")
```

**3) 페이지 계산**
```python
import math

total_items = 47
items_per_page = 10

# 올림으로 페이지 수 계산
total_pages = math.ceil(total_items / items_per_page)
print(f"총 페이지: {total_pages}")  # 5
```

### 🔨 실습 (10분)

**👉 [실습 파일: number_advanced.py](./number_advanced.py)**

**문제:** 통계 계산기

**요구사항:**
1. 숫자 리스트 입력
2. 평균, 최대, 최소, 합계 계산
3. 표준편차 계산
4. 중앙값 계산

---

## 세션 7: 문자열 메서드 (★★★★★)

### 📖 이론 (10분)

#### 7.1 대소문자 변환

```python
text = "Hello Python"

# 대문자로
print(text.upper())  # "HELLO PYTHON"

# 소문자로
print(text.lower())  # "hello python"

# 첫 글자만 대문자
print(text.capitalize())  # "Hello python"

# 각 단어 첫 글자 대문자
print(text.title())  # "Hello Python"

# 대소문자 반전
print(text.swapcase())  # "hELLO pYTHON"
```

**실무 활용:**
```python
# 이메일 정규화
email = "USER@EXAMPLE.COM"
email = email.lower()
print(email)  # "user@example.com"

# 이름 정규화
name = "KIM CHULSOO"
name = name.title()
print(name)  # "Kim Chulsoo"
```

#### 7.2 공백 제거

```python
text = "  Hello  Python  "

# 양쪽 공백 제거
print(text.strip())  # "Hello  Python"

# 왼쪽 공백 제거
print(text.lstrip())  # "Hello  Python  "

# 오른쪽 공백 제거
print(text.rstrip())  # "  Hello  Python"

# 특정 문자 제거
text = "***Hello***"
print(text.strip("*"))  # "Hello"
```

**실무 활용:**
```python
# 사용자 입력 정제
user_input = input("이름: ").strip()

# CSV 데이터 처리
data = "  김철수  ,  28  ,  서울  "
cleaned = [item.strip() for item in data.split(",")]
print(cleaned)  # ["김철수", "28", "서울"]
```

#### 7.3 분리와 결합

**split() - 분리**
```python
# 공백으로 분리
text = "Hello Python Programming"
words = text.split()
print(words)  # ["Hello", "Python", "Programming"]

# 특정 구분자로 분리
text = "사과,바나나,포도"
fruits = text.split(",")
print(fruits)  # ["사과", "바나나", "포도"]

# 최대 분리 횟수
text = "a-b-c-d"
parts = text.split("-", 2)
print(parts)  # ["a", "b", "c-d"]
```

**join() - 결합**
```python
# 리스트를 문자열로
words = ["Hello", "Python", "Programming"]
text = " ".join(words)
print(text)  # "Hello Python Programming"

# 쉼표로 결합
fruits = ["사과", "바나나", "포도"]
text = ", ".join(fruits)
print(text)  # "사과, 바나나, 포도"

# 줄바꿈으로 결합
lines = ["첫째 줄", "둘째 줄", "셋째 줄"]
text = "\n".join(lines)
print(text)
```

**실무 활용:**
```python
# URL 생성
parts = ["https:", "", "www.example.com", "api", "users", "123"]
url = "/".join(parts)
print(url)  # "https://www.example.com/api/users/123"

# SQL 쿼리 생성
columns = ["name", "age", "email"]
query = f"SELECT {', '.join(columns)} FROM users"
print(query)
```

#### 7.4 검색과 치환

**find() / index()**
```python
text = "Hello Python"

# find: 없으면 -1
print(text.find("Python"))  # 6
print(text.find("Java"))    # -1

# index: 없으면 오류
print(text.index("Python"))  # 6
# print(text.index("Java"))  # ValueError

# 시작 위치 지정
print(text.find("o", 5))  # 9 (두 번째 o)
```

**replace() - 치환**
```python
text = "Hello Python Python"

# 모두 치환
print(text.replace("Python", "Java"))
# "Hello Java Java"

# 최대 횟수 지정
print(text.replace("Python", "Java", 1))
# "Hello Java Python"
```

**count() - 개수**
```python
text = "banana"
print(text.count("a"))  # 3
print(text.count("na"))  # 2
```

**실무 활용:**
```python
# 파일 확장자 변경
filename = "report.txt"
new_filename = filename.replace(".txt", ".pdf")
print(new_filename)  # "report.pdf"

# 민감 정보 마스킹
email = "user@example.com"
masked = email.replace(email.split("@")[0], "****")
print(masked)  # "****@example.com"
```

#### 7.5 확인 메서드

```python
# 시작/끝 확인
filename = "report.pdf"
print(filename.startswith("report"))  # True
print(filename.endswith(".pdf"))      # True

# 포함 확인
text = "Hello Python"
print("Python" in text)  # True

# 문자 타입 확인
print("123".isdigit())    # True (숫자)
print("abc".isalpha())    # True (문자)
print("abc123".isalnum()) # True (문자+숫자)
print("   ".isspace())    # True (공백)
```

**실무 활용:**
```python
# 파일 타입 확인
allowed_extensions = [".jpg", ".png", ".gif"]
filename = "photo.jpg"

if any(filename.endswith(ext) for ext in allowed_extensions):
    print("이미지 파일")

# 입력 검증
password = input("비밀번호: ")
if len(password) >= 8 and any(c.isdigit() for c in password):
    print("유효한 비밀번호")
```

### 🔨 실습 (10분)

**👉 [실습 파일: string_methods.py](./string_methods.py)**

**문제:** 데이터 정제 프로그램

**요구사항:**
1. CSV 형식 데이터 (공백 포함)
2. 데이터 정제
   - 공백 제거
   - 소문자 변환
   - 특수문자 제거
3. 결과 출력

---

## 세션 8: 문자열 슬라이싱 (★★★★★)

### 📖 이론 (10분)

#### 8.1 슬라이싱 기본

```python
text = "Python Programming"

# [시작:끝]
print(text[0:6])    # "Python"
print(text[7:18])   # "Programming"

# 생략
print(text[:6])     # "Python" (처음부터)
print(text[7:])     # "Programming" (끝까지)
print(text[:])      # 전체 복사

# 음수 인덱스
print(text[-11:])   # "Programming" (뒤에서 11번째부터)
print(text[:-12])   # "Python" (뒤에서 12번째 전까지)
```

#### 8.2 step 활용

```python
text = "Python"

# [시작:끝:step]
print(text[::2])    # "Pto" (2칸씩)
print(text[::3])    # "Ph" (3칸씩)

# 역순
print(text[::-1])   # "nohtyP"
print(text[::-2])   # "nhy" (역순으로 2칸씩)
```

#### 8.3 실무 활용

**1) 부분 문자열 추출**
```python
# 날짜 추출
date = "2025-12-06"
year = date[:4]
month = date[5:7]
day = date[8:10]
print(f"{year}년 {month}월 {day}일")

# 전화번호 분리
phone = "010-1234-5678"
parts = phone.split("-")
print(f"국번: {parts[0]}, 앞자리: {parts[1]}, 뒷자리: {parts[2]}")
```

**2) 마스킹**
```python
# 주민번호 마스킹
ssn = "123456-1234567"
masked = ssn[:8] + "*" * 6
print(masked)  # "123456-1******"

# 카드번호 마스킹
card = "1234-5678-9012-3456"
parts = card.split("-")
masked_card = f"{parts[0]}-****-****-{parts[3]}"
print(masked_card)  # "1234-****-****-3456"
```

**3) 파일 경로 처리**
```python
path = "/home/user/documents/report.pdf"

# 파일명 추출
filename = path.split("/")[-1]
print(filename)  # "report.pdf"

# 확장자 추출
extension = filename.split(".")[-1]
print(extension)  # "pdf"

# 확장자 제외
name_only = filename[:filename.rfind(".")]
print(name_only)  # "report"
```

### 🔨 실습 (10분)

**👉 [실습 파일: string_slicing.py](./string_slicing.py)**

**문제:** 개인정보 처리

**요구사항:**
1. 주민번호 마스킹
2. 이메일 마스킹
3. 전화번호 포맷 변경
4. URL 파싱

---

## 세션 9: 중간 점검 퀴즈 (★★★★★)

### 📖 종합 문제 (30분)

**👉 [실습 파일: final_quiz.py](./final_quiz.py)**

**문제:** 직원 관리 시스템

**요구사항:**
1. 직원 데이터 (이름, 부서, 급여, 입사일)
2. 전체 직원 목록 출력
3. 부서별 평균 급여 계산
4. 입사 5년 이상 직원 찾기
5. 이름 검색 기능
6. 급여 인상 (10%)
7. 데이터 CSV 형식으로 출력

**출력 형식:**
```
===== 직원 관리 시스템 =====

[1. 전체 직원 목록]
김철수 (개발팀) - 5,000,000원 (2020-01-15)
이영희 (영업팀) - 4,500,000원 (2021-03-20)
...

[2. 부서별 평균 급여]
개발팀: 5,200,000원
영업팀: 4,300,000원
...

[3. 근속 5년 이상]
김철수: 5년 11개월
박민수: 7년 2개월

[4. 이름 검색]
검색어: 김
- 김철수 (개발팀)
- 김지훈 (기획팀)

[5. 급여 인상 후]
김철수: 5,000,000 → 5,500,000 (+500,000)
...

[6. CSV 출력]
이름,부서,급여,입사일
김철수,개발팀,5500000,2020-01-15
...

===========================
```

### ✅ 종합 평가 (10분)

**평가 기준:**
- [ ] for 문 활용
- [ ] 리스트/딕셔너리 처리
- [ ] 문자열 메서드 활용
- [ ] 조건문 활용
- [ ] 계산 및 포맷팅
- [ ] 코드 가독성

---

## 🎓 총 정리 및 복습 (15분)

### 오늘 배운 내용 요약

#### 1. for 반복문
```python
# 리스트 순회
for item in items:
    print(item)

# range 활용
for i in range(10):
    print(i)

# enumerate
for i, item in enumerate(items):
    print(f"{i}: {item}")
```

#### 2. break와 continue
```python
# break: 중단
for i in range(10):
    if i == 5:
        break

# continue: 건너뛰기
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

#### 3. 문자열 메서드
```python
text = "  Hello Python  "

text.upper()      # 대문자
text.lower()      # 소문자
text.strip()      # 공백 제거
text.split()      # 분리
"-".join(words)   # 결합
text.replace("Python", "Java")  # 치환
```

#### 4. 슬라이싱
```python
text = "Python"
text[0:3]    # "Pyt"
text[:3]     # "Pyt"
text[3:]     # "hon"
text[::-1]   # "nohtyP" (역순)
```

### 실습 파일 목록

1. **[for_basic.py](./for_basic.py)** - for 문 기초
2. **[range_practice.py](./range_practice.py)** - range() 활용
3. **[list_processing.py](./list_processing.py)** - 리스트 처리
4. **[break_continue.py](./break_continue.py)** - break/continue
5. **[nested_loop.py](./nested_loop.py)** - 중첩 반복문
6. **[number_advanced.py](./number_advanced.py)** - 숫자 처리
7. **[string_methods.py](./string_methods.py)** - 문자열 메서드
8. **[string_slicing.py](./string_slicing.py)** - 문자열 슬라이싱
9. **[final_quiz.py](./final_quiz.py)** - 종합 퀴즈

### 다음 시간 예고

**5일차에서는:**
- 함수 정의와 활용
- 모듈과 패키지
- 파일 입출력
- 예외 처리
- 최종 프로젝트!

---

## 📚 과제 (선택 사항)

**미니 프로젝트: 성적 처리 프로그램**

**요구사항:**
1. 학생 정보 입력 (이름, 3과목 점수)
2. 총점, 평균 계산
3. 학점 부여
4. 전체 통계 (평균, 최고점, 최저점)
5. 결과를 파일로 저장

---

## 🎯 강사용 체크리스트

- [ ] for 문 기본 개념 이해
- [ ] range() 활용법 숙지
- [ ] break/continue 차이 이해
- [ ] 중첩 반복문 패턴 연습
- [ ] 문자열 메서드 주요 기능 암기
- [ ] 슬라이싱 문법 완벽 이해
- [ ] 종합 퀴즈 완료

---

**강의 종료!** 🎉

4일차까지 수고하셨습니다! 이제 본격적인 프로그래밍이 가능합니다!
