# 파이썬 4일차 강의 교안

## 강의 정보
- **강의 시간**: 4시간 (240분)
- **세션 구성**: 이론(10분) + 실습(10분) + 해설(5분) = 25분/세트
- **총 세션**: 9개
- **주제**: for 반복문과 문자열 처리

---

## 📋 목차

1. [세션 1: for 문 기초](#세션-1-for-문-기초-) (25분)
2. [세션 2: range() 함수](#세션-2-range-함수-) (25분)
3. [세션 3: 리스트 컴프리헨션](#세션-3-리스트-컴프리헨션-) (25분)
4. [세션 4: break와 continue](#세션-4-break와-continue-) (25분)
5. [세션 5: 중첩 반복문](#세션-5-중첩-반복문-) (25분)
6. [세션 6: enumerate와 zip](#세션-6-enumerate와-zip-) (25분)
7. [세션 7: 문자열 메서드](#세션-7-문자열-메서드-) (25분)
8. [세션 8: 문자열 슬라이싱](#세션-8-문자열-슬라이싱-) (25분)
9. [세션 9: 종합 연습](#세션-9-종합-연습-) (25분)

---

## 세션 1: for 문 기초 ★★★★★

### 📖 이론 (10분)

#### 개념 설명
`for` 문은 시퀀스(리스트, 문자열 등)의 각 요소를 하나씩 순회하는 반복문입니다.

**기본 문법**
```python
for 변수 in 시퀀스:
    실행할 코드
```

#### 주요 개념
- **순회**: 리스트, 문자열, 딕셔너리 등을 반복
- **변수**: 각 요소를 저장하는 임시 변수
- **들여쓰기**: 4칸 공백 필수

#### 실무 활용 사례
- 데이터 일괄 처리 (파일 여러 개 처리)
- 가격 계산 (장바구니 총액)
- 리스트 변환 (이름을 대문자로)

#### 코드 예시
```python
# 예시 1: 리스트 순회
fruits = ["사과", "바나나", "포도"]
for fruit in fruits:
    print(fruit)
# 출력: 사과, 바나나, 포도

# 예시 2: 문자열 순회
text = "Python"
for char in text:
    print(char)
# 출력: P, y, t, h, o, n

# 예시 3: 딕셔너리 순회
user = {"name": "김철수", "age": 28, "city": "서울"}

# 키-값 순회
for key, value in user.items():
    print(f"{key}: {value}")
# 출력:
# name: 김철수
# age: 28
# city: 서울

# 실무 패턴: 장바구니 총액
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

---

### 💻 실습 (10분)

**[실습 파일: session1_for_basic_practice.py](./session1_for_basic_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session1_for_basic_solution.py](./session1_for_basic_solution.py)**

---

## 세션 2: range() 함수 ★★★★★

### 📖 이론 (10분)

#### 개념 설명
`range()`는 숫자 시퀀스를 생성하는 함수입니다. for 문과 함께 사용하여 정해진 횟수만큼 반복합니다.

**기본 문법**
```python
range(stop)           # 0부터 stop-1까지
range(start, stop)    # start부터 stop-1까지
range(start, stop, step)  # step만큼 증가
```

#### 주요 개념
- **range(5)**: 0, 1, 2, 3, 4
- **range(1, 6)**: 1, 2, 3, 4, 5
- **range(0, 10, 2)**: 0, 2, 4, 6, 8

#### 실무 활용 사례
- 횟수 반복 (5번 실행)
- 파일 생성 (report_1.txt ~ report_10.txt)
- 구구단 출력

#### 코드 예시
```python
# 예시 1: 기본 range
for i in range(5):
    print(i)
# 출력: 0, 1, 2, 3, 4

for i in range(1, 6):
    print(i)
# 출력: 1, 2, 3, 4, 5

# 예시 2: step 활용
# 짝수만
for i in range(0, 11, 2):
    print(i)
# 출력: 0, 2, 4, 6, 8, 10

# 역순
for i in range(10, 0, -1):
    print(i)
# 출력: 10, 9, 8, ..., 1

# 예시 3: 구구단
dan = 5
for i in range(1, 10):
    print(f"{dan} × {i} = {dan * i}")
# 출력:
# 5 × 1 = 5
# 5 × 2 = 10
# ...
# 5 × 9 = 45

# 실무 패턴: 파일 생성
for i in range(1, 11):
    filename = f"report_{i:02d}.txt"
    print(f"{filename} 생성")
# 출력: report_01.txt, report_02.txt, ...
```

---

### 💻 실습 (10분)

**[실습 파일: session2_range_practice.py](./session2_range_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session2_range_solution.py](./session2_range_solution.py)**

---

## 세션 3: 리스트 컴프리헨션 ★★★★★

### 📖 이론 (10분)

#### 개념 설명
리스트를 생성하는 간결한 문법입니다. for 문을 한 줄로 작성할 수 있습니다.

**기본 문법**
```python
[표현식 for 변수 in 시퀀스]
[표현식 for 변수 in 시퀀스 if 조건]
```

#### 주요 개념
- **간결함**: 3줄 → 1줄
- **가독성**: 단순한 변환에 적합
- **조건**: if로 필터링 가능

#### 실무 활용 사례
- 데이터 변환 (이름 대문자화)
- 필터링 (60점 이상만)
- 파일명 생성

#### 코드 예시
```python
# 예시 1: 기본 사용
# 일반 for 문
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# 리스트 컴프리헨션
squares = [i ** 2 for i in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# 예시 2: 조건 포함
# 짝수만
evens = [i for i in range(1, 11) if i % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# 60점 이상만
scores = [85, 92, 58, 76, 95, 45, 88]
pass_scores = [score for score in scores if score >= 60]
print(pass_scores)  # [85, 92, 76, 95, 88]

# 예시 3: 변환
# 대문자 변환
names = ["kim", "lee", "park"]
upper_names = [name.upper() for name in names]
print(upper_names)  # ["KIM", "LEE", "PARK"]

# 가격에 세금 추가
prices = [10000, 25000, 15000]
prices_with_tax = [int(price * 1.1) for price in prices]
print(prices_with_tax)  # [11000, 27500, 16500]

# 실무 패턴: 파일명 생성
dates = ["2025-12-01", "2025-12-02", "2025-12-03"]
filenames = [f"report_{date}.xlsx" for date in dates]
print(filenames)
# ['report_2025-12-01.xlsx', 'report_2025-12-02.xlsx', ...]
```

---

### 💻 실습 (10분)

**[실습 파일: session3_comprehension_practice.py](./session3_comprehension_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session3_comprehension_solution.py](./session3_comprehension_solution.py)**

---

## 세션 4: break와 continue ★★★★

### 📖 이론 (10분)

#### 개념 설명
반복문의 흐름을 제어하는 명령어입니다.

- **break**: 반복문 즉시 종료
- **continue**: 현재 반복 건너뛰고 다음으로

#### 주요 개념
- **break**: 조건 만족 시 반복 중단
- **continue**: 특정 항목 건너뛰기
- **for-else**: break 없이 정상 종료 시 실행 (Python 특징)

#### 실무 활용 사례
- 검색 후 중단 (찾으면 종료)
- 입력 검증 (유효할 때까지)
- 데이터 정제 (빈 값 건너뛰기)

#### 코드 예시
```python
# 예시 1: break (즉시 종료)
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
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

# 예시 2: continue (건너뛰기)
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
print(valid_scores)  # [85, 0, 92, 78, 95]

# 예시 3: for-else (Python 특징!)
numbers = [1, 3, 5, 7, 9]
target = 4

for num in numbers:
    if num == target:
        print("찾음!")
        break
else:
    print("못 찾음!")  # break 없이 끝나면 실행

# 실무 패턴: 로그인 시도 (3회 제한)
password = "1234"
max_attempts = 3

for attempt in range(max_attempts):
    user_input = input(f"비밀번호 ({attempt + 1}/{max_attempts}): ")

    if user_input == password:
        print("로그인 성공!")
        break
    else:
        print("틀렸습니다.")
else:
    print("계정이 잠겼습니다.")
```

---

### 💻 실습 (10분)

**[실습 파일: session4_break_continue_practice.py](./session4_break_continue_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session4_break_continue_solution.py](./session4_break_continue_solution.py)**

---

## 세션 5: 중첩 반복문 ★★★★

### 📖 이론 (10분)

#### 개념 설명
반복문 안에 또 다른 반복문을 사용하는 것입니다. 2차원 데이터 처리나 조합 생성에 사용합니다.

**기본 구조**
```python
for i in range(외부):
    for j in range(내부):
        실행할 코드
```

#### 주요 개념
- **2중 반복**: 구구단, 좌석 배치
- **조합**: 메뉴 조합, 경우의 수
- **2차원 데이터**: 표, 행렬

#### 실무 활용 사례
- 구구단 전체 출력
- 좌석 배치도
- 메뉴 조합
- 엑셀 시트 처리

#### 코드 예시
```python
# 예시 1: 구구단 전체
for dan in range(2, 10):
    print(f"\n[{dan}단]")
    for i in range(1, 10):
        print(f"{dan} × {i} = {dan * i}")

# 예시 2: 좌석 배치
rows = 5
cols = 8

print("좌석 배치도:")
for row in range(1, rows + 1):
    for col in range(1, cols + 1):
        seat = f"{chr(64 + row)}{col}"
        print(seat, end=" ")
    print()  # 줄바꿈

# 출력:
# A1 A2 A3 A4 A5 A6 A7 A8
# B1 B2 B3 B4 B5 B6 B7 B8
# ...

# 예시 3: 메뉴 조합
mains = ["햄버거", "피자", "파스타"]
drinks = ["콜라", "사이다"]

print("세트 메뉴:")
for main in mains:
    for drink in drinks:
        print(f"{main} + {drink}")

# 출력:
# 햄버거 + 콜라
# 햄버거 + 사이다
# 피자 + 콜라
# ...

# 실무 패턴: 성적표 (2차원 데이터)
scores = [
    [85, 90, 88],  # 1번 학생
    [92, 88, 95],  # 2번 학생
    [78, 85, 80]   # 3번 학생
]

subjects = ["국어", "영어", "수학"]

for i, student_scores in enumerate(scores, 1):
    print(f"\n{i}번 학생:")
    for j, score in enumerate(student_scores):
        print(f"  {subjects[j]}: {score}점")
    avg = sum(student_scores) / len(student_scores)
    print(f"  평균: {avg:.1f}점")
```

---

### 💻 실습 (10분)

**[실습 파일: session5_nested_loop_practice.py](./session5_nested_loop_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session5_nested_loop_solution.py](./session5_nested_loop_solution.py)**

---

## 세션 6: enumerate와 zip ★★★★

### 📖 이론 (10분)

#### 개념 설명
반복문을 더 편리하게 만드는 내장 함수들입니다.

- **enumerate()**: 인덱스와 값을 함께 반환
- **zip()**: 여러 시퀀스를 동시에 순회

#### 주요 개념
- **enumerate**: (인덱스, 값) 튜플 반환
- **zip**: 짧은 시퀀스 기준으로 종료
- **활용**: 순번 출력, 병렬 처리

#### 실무 활용 사례
- 순번 있는 목록 (1. 사과, 2. 바나나)
- 두 리스트 동시 처리 (이름-점수)
- 딕셔너리 생성

#### 코드 예시
```python
# 예시 1: enumerate (인덱스 + 값)
fruits = ["사과", "바나나", "포도"]

# 일반 방법
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# enumerate 사용 (더 깔끔)
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# 1부터 시작
for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")
# 출력:
# 1. 사과
# 2. 바나나
# 3. 포도

# 예시 2: zip (여러 시퀀스 동시 순회)
names = ["김철수", "이영희", "박민수"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}점")
# 출력:
# 김철수: 85점
# 이영희: 92점
# 박민수: 78점

# 딕셔너리 생성
result = dict(zip(names, scores))
print(result)
# {'김철수': 85, '이영희': 92, '박민수': 78}

# 예시 3: 여러 리스트 결합
korean = [85, 90, 88]
english = [92, 88, 95]
math = [78, 85, 80]

for i, (k, e, m) in enumerate(zip(korean, english, math), 1):
    print(f"{i}번 학생: 국어 {k}, 영어 {e}, 수학 {m}")
    total = k + e + m
    avg = total / 3
    print(f"  총점: {total}, 평균: {avg:.1f}")

# 실무 패턴: CSV 데이터 처리
headers = ["이름", "나이", "도시"]
row1 = ["김철수", "28", "서울"]
row2 = ["이영희", "25", "부산"]

for header, value in zip(headers, row1):
    print(f"{header}: {value}")
```

---

### 💻 실습 (10분)

**[실습 파일: session6_enum_zip_practice.py](./session6_enum_zip_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session6_enum_zip_solution.py](./session6_enum_zip_solution.py)**

---

## 세션 7: 문자열 메서드 ★★★★★

### 📖 이론 (10분)

#### 개념 설명
문자열을 처리하는 다양한 내장 메서드입니다. 실무에서 가장 자주 사용합니다.

#### 주요 개념
- **대소문자**: upper(), lower(), capitalize()
- **공백**: strip(), lstrip(), rstrip()
- **분리/결합**: split(), join()
- **검색/치환**: find(), replace(), count()

#### 실무 활용 사례
- 이메일 정규화 (소문자 변환)
- CSV 데이터 정제 (공백 제거)
- 파일 확장자 변경

#### 코드 예시
```python
# 예시 1: 대소문자 변환
text = "Hello Python"

print(text.upper())  # "HELLO PYTHON"
print(text.lower())  # "hello python"
print(text.title())  # "Hello Python" (각 단어 첫 글자 대문자)

# 이메일 정규화
email = "USER@EXAMPLE.COM"
email = email.lower()
print(email)  # "user@example.com"

# 예시 2: 공백 제거
text = "  Hello Python  "

print(text.strip())   # "Hello Python"
print(text.lstrip())  # "Hello Python  "
print(text.rstrip())  # "  Hello Python"

# CSV 데이터 정제
data = "  김철수  ,  28  ,  서울  "
cleaned = [item.strip() for item in data.split(",")]
print(cleaned)  # ["김철수", "28", "서울"]

# 예시 3: 분리와 결합
# split() - 분리
text = "사과,바나나,포도"
fruits = text.split(",")
print(fruits)  # ['사과', '바나나', '포도']

text = "Hello Python Programming"
words = text.split()  # 공백으로 분리
print(words)  # ['Hello', 'Python', 'Programming']

# join() - 결합
fruits = ["사과", "바나나", "포도"]
text = ", ".join(fruits)
print(text)  # "사과, 바나나, 포도"

# 실무 패턴: 파일 확장자 변경
filename = "report.txt"
new_filename = filename.replace(".txt", ".pdf")
print(new_filename)  # "report.pdf"

# 단어 개수 세기
text = "banana"
print(text.count("a"))  # 3

# 시작/끝 확인
filename = "report.pdf"
print(filename.endswith(".pdf"))  # True
print(filename.startswith("report"))  # True
```

---

### 💻 실습 (10분)

**[실습 파일: session7_string_methods_practice.py](./session7_string_methods_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session7_string_methods_solution.py](./session7_string_methods_solution.py)**

---

## 세션 8: 문자열 슬라이싱 ★★★★★

### 📖 이론 (10분)

#### 개념 설명
문자열의 일부분을 추출하는 방법입니다. 리스트에도 동일하게 적용됩니다.

**기본 문법**
```python
문자열[시작:끝]       # 시작부터 끝-1까지
문자열[시작:끝:step]  # step만큼 건너뛰며
```

#### 주요 개념
- **인덱싱**: `text[0]` (첫 문자)
- **슬라이싱**: `text[0:3]` (처음 3글자)
- **역순**: `text[::-1]` (거꾸로)

#### 실무 활용 사례
- 날짜 추출 (2025-12-06 → 년, 월, 일)
- 파일명 처리 (확장자 제거)
- 개인정보 마스킹

#### 코드 예시
```python
# 예시 1: 기본 슬라이싱
text = "Python Programming"

print(text[0:6])    # "Python"
print(text[:6])     # "Python" (처음부터)
print(text[7:])     # "Programming" (끝까지)
print(text[:])      # 전체 복사

# 음수 인덱스
print(text[-11:])   # "Programming" (뒤에서 11번째부터)

# 예시 2: step 활용
text = "Python"

print(text[::2])    # "Pto" (2칸씩)
print(text[::-1])   # "nohtyP" (역순)

# 회문 확인
word = "level"
if word == word[::-1]:
    print("회문입니다")

# 예시 3: 실무 활용
# 날짜 추출
date = "2025-12-06"
year = date[:4]
month = date[5:7]
day = date[8:10]
print(f"{year}년 {month}월 {day}일")

# 주민번호 마스킹
ssn = "123456-1234567"
masked = ssn[:8] + "*" * 6
print(masked)  # "123456-1******"

# 파일명과 확장자 분리
filename = "report.pdf"
name = filename[:filename.rfind(".")]
ext = filename[filename.rfind(".") + 1:]
print(f"파일명: {name}, 확장자: {ext}")
# 파일명: report, 확장자: pdf

# 실무 패턴: 전화번호 포맷
phone = "01012345678"
formatted = f"{phone[:3]}-{phone[3:7]}-{phone[7:]}"
print(formatted)  # "010-1234-5678"
```

---

### 💻 실습 (10분)

**[실습 파일: session8_slicing_practice.py](./session8_slicing_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session8_slicing_solution.py](./session8_slicing_solution.py)**

---

## 세션 9: 종합 연습 ★★★★★

### 📖 이론 (10분)

#### 복습 내용
오늘 배운 모든 내용을 종합하여 실무 프로그램을 만들어봅니다.

**핵심 개념 정리**
1. **for 문**: 리스트, 문자열 순회
2. **range()**: 정해진 횟수 반복
3. **리스트 컴프리헨션**: 간결한 리스트 생성
4. **break/continue**: 흐름 제어
5. **enumerate/zip**: 편리한 반복
6. **문자열 메서드**: 실무 데이터 처리
7. **슬라이싱**: 부분 추출

#### 통합 예제
```python
# 학생 관리 시스템
students = [
    {"name": "김철수", "scores": [85, 90, 88]},
    {"name": "이영희", "scores": [92, 88, 95]},
    {"name": "박민수", "scores": [78, 85, 80]}
]

subjects = ["국어", "영어", "수학"]

print("===== 학생 성적 관리 시스템 =====\n")

# 1. 전체 성적 출력
for i, student in enumerate(students, 1):
    print(f"[{i}. {student['name']}]")

    for subject, score in zip(subjects, student['scores']):
        print(f"  {subject}: {score}점")

    total = sum(student['scores'])
    avg = total / len(student['scores'])
    print(f"  총점: {total}점, 평균: {avg:.1f}점\n")

# 2. 과목별 평균
print("===== 과목별 평균 =====")
for i, subject in enumerate(subjects):
    scores = [s['scores'][i] for s in students]
    avg = sum(scores) / len(scores)
    print(f"{subject}: {avg:.1f}점")

# 3. 우수 학생 (평균 85점 이상)
print("\n===== 우수 학생 =====")
for student in students:
    avg = sum(student['scores']) / len(student['scores'])
    if avg >= 85:
        print(f"{student['name']}: {avg:.1f}점")
```

---

### 💻 실습 (10분)

**[실습 파일: session9_final_practice.py](./session9_final_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session9_final_solution.py](./session9_final_solution.py)**

---

## 📚 오늘의 핵심 정리

### 1. for 반복문
```python
# 리스트 순회
for item in items:
    print(item)

# range 활용
for i in range(10):
    print(i)

# enumerate (인덱스 + 값)
for i, item in enumerate(items, 1):
    print(f"{i}. {item}")

# zip (여러 리스트)
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

### 2. 리스트 컴프리헨션
```python
# 기본
squares = [i**2 for i in range(1, 6)]

# 조건
evens = [i for i in range(10) if i % 2 == 0]

# 변환
upper_names = [name.upper() for name in names]
```

### 3. 흐름 제어
```python
# break - 즉시 종료
for i in range(10):
    if i == 5:
        break

# continue - 건너뛰기
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

### 4. 문자열 처리
```python
# 메서드
text.upper()      # 대문자
text.strip()      # 공백 제거
text.split(",")   # 분리
"-".join(words)   # 결합

# 슬라이싱
text[0:3]    # 처음 3글자
text[::-1]   # 역순
```

---

## 🎯 다음 강의 예고

**5일차에서는:**
- 함수 정의와 사용
- 매개변수와 반환값
- 람다 함수
- 모듈과 패키지

---

## ❓ FAQ

**Q1. for vs while 차이는?**
- for: 정해진 횟수/항목 반복
- while: 조건이 참인 동안 반복

**Q2. 리스트 컴프리헨션은 언제 사용?**
- 간단한 변환/필터링
- 복잡하면 일반 for 문 사용

**Q3. enumerate는 왜 사용하나요?**
- 인덱스와 값을 동시에 필요할 때
- `range(len())`보다 깔끔

**Q4. 슬라이싱 [1:5]는 몇 개?**
- 4개 (1, 2, 3, 4)
- 끝 인덱스는 포함 안 됨

---

**강의 준비 완료! 화이팅!**
