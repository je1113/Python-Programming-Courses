# 파이썬 3일차 강의 교안

## 강의 정보
- **강의 시간**: 4시간 (240분)
- **세션 구성**: 이론(10분) + 실습(10분) + 해설(5분) = 25분/세트
- **총 세션**: 9개
- **주제**: 조건문(if)과 반복문(while)

---

## 📋 목차

1. [세션 1: if 문 기초](#세션-1-if-문-기초-) (25분)
2. [세션 2: if-else 문](#세션-2-if-else-문-) (25분)
3. [세션 3: if-elif-else 문](#세션-3-if-elif-else-문-) (25분)
4. [세션 4: 중첩 if 문](#세션-4-중첩-if-문-) (25분)
5. [세션 5: while 문 기초](#세션-5-while-문-기초-) (25분)
6. [세션 6: while 문 활용](#세션-6-while-문-활용-) (25분)
7. [세션 7: 무한 루프와 break](#세션-7-무한-루프와-break-) (25분)
8. [세션 8: continue 문](#세션-8-continue-문-) (25분)
9. [세션 9: 연습 퀴즈 종합](#세션-9-연습-퀴즈-종합-) (25분)

---

## 세션 1: if 문 기초 ★★★★★

### 📖 이론 (10분)

#### 개념 설명
`if` 문은 특정 조건이 참(True)일 때만 코드를 실행하는 조건문입니다.

**기본 문법:**
```python
if 조건식:
    실행할 코드
```

#### 주요 개념
- **조건식**: 결과가 True 또는 False인 표현식
- **들여쓰기**: Python에서 코드 블록을 구분하는 필수 요소 (4칸 공백 권장)
- **비교 연산자**: `>`, `<`, `>=`, `<=`, `==`, `!=`

#### 실무 활용 사례
- 사용자 권한 확인 (관리자인지 체크)
- 데이터 유효성 검증 (나이가 18세 이상인지)
- 알림 발송 조건 (재고가 10개 이하일 때)

#### 코드 예시
```python
# 예시 1: 성인 확인
age = 20
if age >= 18:
    print("성인입니다.")

# 예시 2: 재고 경고
stock = 5
if stock < 10:
    print("재고 부족! 발주가 필요합니다.")

# 예시 3: 로그인 성공
is_logged_in = True
if is_logged_in:
    print("환영합니다!")
```

---

### 💻 실습 (10분)

**[실습 파일: session1_if_basic_practice.py](./session1_if_basic_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session1_if_basic_solution.py](./session1_if_basic_solution.py)**

---

## 세션 2: if-else 문 ★★★★★

### 📖 이론 (10분)

#### 개념 설명
`if-else` 문은 조건이 참일 때와 거짓일 때 각각 다른 코드를 실행합니다.

**기본 문법:**
```python
if 조건식:
    조건이 참일 때 실행
else:
    조건이 거짓일 때 실행
```

#### 실무 활용 사례
- 로그인 성공/실패 처리
- 결제 가능/불가능 판단
- 파일 존재 여부 확인

#### 코드 예시
```python
# 예시 1: 로그인 검증
password = "1234"
if password == "1234":
    print("로그인 성공!")
else:
    print("비밀번호가 틀렸습니다.")

# 예시 2: 잔액 확인
balance = 5000
price = 7000
if balance >= price:
    print("결제 완료")
else:
    print("잔액이 부족합니다.")

# 예시 3: 짝수/홀수 판별
number = 7
if number % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
```

---

### 💻 실습 (10분)

**[실습 파일: session2_if_else_practice.py](./session2_if_else_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session2_if_else_solution.py](./session2_if_else_solution.py)**

---

## 세션 3: if-elif-else 문 ★★★★★

### 📖 이론 (10분)

#### 개념 설명
`if-elif-else` 문은 여러 조건을 순차적으로 검사하여 해당하는 코드를 실행합니다.

**기본 문법:**
```python
if 조건1:
    조건1이 참일 때
elif 조건2:
    조건2가 참일 때
elif 조건3:
    조건3이 참일 때
else:
    모든 조건이 거짓일 때
```

#### 주요 개념
- **elif**: else if의 줄임말
- **순차 검사**: 위에서부터 조건을 확인하고, 참인 조건을 만나면 해당 블록만 실행 후 종료
- **else 생략 가능**: 필수가 아님

#### 실무 활용 사례
- 등급 시스템 (VIP, Gold, Silver, Bronze)
- 성적 처리 (A, B, C, D, F)
- 배송비 계산 (금액별 차등)

#### 코드 예시
```python
# 예시 1: 성적 등급
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"당신의 등급은 {grade}입니다.")

# 예시 2: 배송비 계산
order_amount = 35000
if order_amount >= 50000:
    shipping = 0
    print("무료 배송!")
elif order_amount >= 30000:
    shipping = 2500
    print(f"배송비: {shipping}원")
else:
    shipping = 3500
    print(f"배송비: {shipping}원")

# 예시 3: 계절 판단
month = 8
if month in [12, 1, 2]:
    print("겨울입니다.")
elif month in [3, 4, 5]:
    print("봄입니다.")
elif month in [6, 7, 8]:
    print("여름입니다.")
else:
    print("가을입니다.")
```

---

### 💻 실습 (10분)

**[실습 파일: session3_if_elif_else_practice.py](./session3_if_elif_else_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session3_if_elif_else_solution.py](./session3_if_elif_else_solution.py)**

---

## 세션 4: 중첩 if 문 ★★★★

### 📖 이론 (10분)

#### 개념 설명
중첩 if 문은 if 문 안에 또 다른 if 문을 포함하는 구조입니다. 복잡한 조건을 단계별로 검사할 때 사용합니다.

**기본 문법:**
```python
if 조건1:
    if 조건2:
        조건1과 조건2가 모두 참일 때
    else:
        조건1은 참, 조건2는 거짓일 때
else:
    조건1이 거짓일 때
```

#### 실무 활용 사례
- 다중 권한 체크 (로그인 + 관리자 권한)
- 할인 조건 검증 (회원 등급 + 구매 금액)
- 입력 유효성 다단계 검증

#### 코드 예시
```python
# 예시 1: 영화 관람 등급
age = 25
has_parent = False

if age >= 19:
    print("성인 영화 관람 가능합니다.")
else:
    if age >= 15:
        if has_parent:
            print("보호자 동반으로 관람 가능합니다.")
        else:
            print("보호자 동반이 필요합니다.")
    else:
        print("관람 불가능합니다.")

# 예시 2: 할인 적용
is_member = True
purchase_amount = 100000

if is_member:
    if purchase_amount >= 100000:
        discount = 0.2  # 20% 할인
        print("VIP 할인 20% 적용!")
    elif purchase_amount >= 50000:
        discount = 0.1  # 10% 할인
        print("회원 할인 10% 적용!")
    else:
        discount = 0.05  # 5% 할인
        print("기본 회원 할인 5% 적용!")
else:
    discount = 0
    print("회원 가입 시 할인 혜택이 있습니다!")

final_price = purchase_amount * (1 - discount)
print(f"최종 금액: {final_price:,.0f}원")
```

---

### 💻 실습 (10분)

**[실습 파일: session4_nested_if_practice.py](./session4_nested_if_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session4_nested_if_solution.py](./session4_nested_if_solution.py)**

---

## 세션 5: while 문 기초 ★★★★★

### 📖 이론 (10분)

#### 개념 설명
`while` 문은 조건이 참인 동안 코드를 반복 실행하는 반복문입니다.

**기본 문법:**
```python
while 조건식:
    반복할 코드
```

#### 주요 개념
- **반복 조건**: 조건이 True인 동안 계속 반복
- **무한 루프 주의**: 조건이 항상 True면 무한 반복
- **카운터 변수**: 반복 횟수를 제어하는 변수

#### 실무 활용 사례
- 사용자 입력 재요청 (올바른 값 입력까지)
- 게임 루프 (게임 종료까지)
- 데이터 처리 (모든 데이터 처리 완료까지)

#### 코드 예시
```python
# 예시 1: 1부터 5까지 출력
count = 1
while count <= 5:
    print(count)
    count += 1

# 예시 2: 합계 계산
total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print(f"1부터 10까지의 합: {total}")

# 예시 3: 비밀번호 입력 (최대 3번)
password = "python"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("비밀번호를 입력하세요: ")
    if user_input == password:
        print("로그인 성공!")
        break
    else:
        attempts += 1
        print(f"틀렸습니다. 남은 기회: {max_attempts - attempts}번")
```

---

### 💻 실습 (10분)

**[실습 파일: session5_while_basic_practice.py](./session5_while_basic_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session5_while_basic_solution.py](./session5_while_basic_solution.py)**

---

## 세션 6: while 문 활용 ★★★★

### 📖 이론 (10분)

#### 개념 설명
while 문을 활용하여 실무에서 자주 사용하는 패턴들을 학습합니다.

#### 주요 패턴
1. **누적 합계**: 값을 계속 더하기
2. **조건부 종료**: 특정 조건에서 탈출
3. **플래그 변수**: 상태를 저장하는 변수 활용

#### 실무 활용 사례
- 장바구니 시스템
- 메뉴 선택 프로그램
- ATM 기계 시뮬레이션

#### 코드 예시
```python
# 예시 1: 간단한 메뉴 시스템
running = True
while running:
    print("\n=== 메뉴 ===")
    print("1. 조회")
    print("2. 등록")
    print("3. 종료")

    choice = input("선택: ")

    if choice == "1":
        print("조회 기능")
    elif choice == "2":
        print("등록 기능")
    elif choice == "3":
        print("프로그램을 종료합니다.")
        running = False
    else:
        print("잘못된 선택입니다.")

# 예시 2: 잔액 관리
balance = 10000
while True:
    print(f"\n현재 잔액: {balance}원")
    print("1. 입금  2. 출금  3. 종료")
    choice = input("선택: ")

    if choice == "1":
        amount = int(input("입금액: "))
        balance += amount
    elif choice == "2":
        amount = int(input("출금액: "))
        if amount <= balance:
            balance -= amount
        else:
            print("잔액이 부족합니다!")
    elif choice == "3":
        break
```

---

### 💻 실습 (10분)

**[실습 파일: session6_while_advanced_practice.py](./session6_while_advanced_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session6_while_advanced_solution.py](./session6_while_advanced_solution.py)**

---

## 세션 7: 무한 루프와 break ★★★★

### 📖 이론 (10분)

#### 개념 설명
- **무한 루프**: `while True:`로 만드는 끝없는 반복
- **break**: 반복문을 즉시 종료하는 명령어

**기본 문법:**
```python
while True:
    코드
    if 종료_조건:
        break
```

#### 실무 활용 사례
- 서버 프로그램 (계속 실행, 종료 명령 시 중단)
- 게임 메인 루프
- 사용자 대화형 프로그램

#### 코드 예시
```python
# 예시 1: 계산기 프로그램
while True:
    print("\n=== 간단 계산기 ===")
    num1 = input("첫 번째 숫자 (종료: q): ")

    if num1 == 'q':
        print("계산기를 종료합니다.")
        break

    num2 = input("두 번째 숫자: ")
    operator = input("연산자 (+, -, *, /): ")

    num1 = float(num1)
    num2 = float(num2)

    if operator == '+':
        print(f"결과: {num1 + num2}")
    elif operator == '-':
        print(f"결과: {num1 - num2}")
    elif operator == '*':
        print(f"결과: {num1 * num2}")
    elif operator == '/':
        if num2 != 0:
            print(f"결과: {num1 / num2}")
        else:
            print("0으로 나눌 수 없습니다!")

# 예시 2: 숫자 맞추기 게임
import random
answer = random.randint(1, 100)
attempts = 0

while True:
    attempts += 1
    guess = int(input("숫자를 맞춰보세요 (1-100): "))

    if guess == answer:
        print(f"정답! {attempts}번 만에 맞추셨습니다!")
        break
    elif guess < answer:
        print("더 큰 숫자입니다!")
    else:
        print("더 작은 숫자입니다!")
```

---

### 💻 실습 (10분)

**[실습 파일: session7_break_practice.py](./session7_break_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session7_break_solution.py](./session7_break_solution.py)**

---

## 세션 8: continue 문 ★★★

### 📖 이론 (10분)

#### 개념 설명
`continue`는 현재 반복을 건너뛰고 다음 반복으로 즉시 이동하는 명령어입니다.

**기본 문법:**
```python
while 조건:
    if 건너뛸_조건:
        continue
    실행할_코드
```

#### break vs continue
- **break**: 반복문 완전 종료
- **continue**: 현재 반복만 건너뛰고 계속

#### 실무 활용 사례
- 특정 데이터 필터링 (잘못된 데이터 제외)
- 조건부 처리 (특정 조건은 무시)
- 로그 파싱 (오류 라인 건너뛰기)

#### 코드 예시
```python
# 예시 1: 홀수만 출력
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:  # 짝수면 건너뛰기
        continue
    print(count)  # 홀수만 출력

# 예시 2: 유효한 점수만 처리
scores = [85, -1, 92, 0, 78, -5, 88]
index = 0

while index < len(scores):
    score = scores[index]
    index += 1

    if score < 0:  # 음수 점수는 무시
        print(f"잘못된 점수 {score} - 건너뜀")
        continue

    print(f"점수: {score}")

# 예시 3: 5의 배수 제외하고 합계
total = 0
num = 1

while num <= 20:
    if num % 5 == 0:  # 5의 배수는 제외
        num += 1
        continue
    total += num
    num += 1

print(f"5의 배수를 제외한 합: {total}")
```

---

### 💻 실습 (10분)

**[실습 파일: session8_continue_practice.py](./session8_continue_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session8_continue_solution.py](./session8_continue_solution.py)**

---

## 세션 9: 연습 퀴즈 종합 ★★★★★

### 📖 이론 (10분)

#### 복습 내용
1. **조건문**: if, if-else, if-elif-else, 중첩 if
2. **반복문**: while, 무한 루프
3. **제어문**: break, continue
4. **실무 패턴**: 메뉴 시스템, 유효성 검증, 누적 계산

#### 통합 예제
```python
# 쇼핑몰 주문 시스템
print("=== 쇼핑몰 주문 시스템 ===")

total_price = 0
order_count = 0

while True:
    print("\n1. 상품 추가")
    print("2. 주문 내역")
    print("3. 결제")
    print("4. 종료")

    choice = input("선택: ")

    if choice == "1":
        price = int(input("상품 가격: "))

        if price < 0:
            print("잘못된 가격입니다!")
            continue

        total_price += price
        order_count += 1
        print(f"상품이 추가되었습니다. (현재 {order_count}개)")

    elif choice == "2":
        print(f"\n주문 상품 수: {order_count}개")
        print(f"총 금액: {total_price:,}원")

        if total_price >= 50000:
            print("배송비: 무료")
        else:
            print("배송비: 3,000원")

    elif choice == "3":
        if order_count == 0:
            print("주문한 상품이 없습니다!")
            continue

        print(f"\n최종 금액: {total_price:,}원")

        if total_price >= 50000:
            shipping = 0
        else:
            shipping = 3000

        final = total_price + shipping
        print(f"배송비: {shipping:,}원")
        print(f"결제 금액: {final:,}원")
        print("결제가 완료되었습니다!")
        break

    elif choice == "4":
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 선택입니다!")
```

---

### 💻 실습 (10분)

**[실습 파일: session9_comprehensive_practice.py](./session9_comprehensive_practice.py)**

---

### ✅ 해설 (5분)

**[해설 파일: session9_comprehensive_solution.py](./session9_comprehensive_solution.py)**

---

## 📚 오늘의 핵심 정리

### 조건문 (if)
```python
# 단일 조건
if 조건:
    코드

# 양자택일
if 조건:
    코드
else:
    코드

# 다중 조건
if 조건1:
    코드
elif 조건2:
    코드
else:
    코드
```

### 반복문 (while)
```python
# 기본 while
while 조건:
    코드

# 무한 루프
while True:
    코드
    if 종료조건:
        break

# continue 사용
while 조건:
    if 건너뛸조건:
        continue
    코드
```

### 주의사항
1. **들여쓰기**: Python은 들여쓰기로 코드 블록 구분 (4칸 공백)
2. **무한 루프**: while True 사용 시 반드시 break 조건 필요
3. **비교 연산자**: `==` (같다), `=` (대입) 구분
4. **논리 연산자**: `and`, `or`, `not` 활용

---

## 🎯 다음 강의 예고

**4일차: for 문과 자료구조 기초**
- for 문 기본
- range() 함수
- 리스트 순회
- 문자열 처리
- 실전 프로젝트

---

## ❓ FAQ

**Q1. if 문에서 조건을 여러 개 검사하려면?**
- `and`, `or` 논리 연산자 사용
- 예: `if age >= 18 and has_license:`

**Q2. while과 for의 차이는?**
- while: 조건이 참인 동안 반복
- for: 정해진 횟수/항목만큼 반복 (4일차에 학습)

**Q3. break와 continue의 차이는?**
- break: 반복문 완전 종료
- continue: 현재 반복만 건너뛰고 계속

**Q4. 무한 루프에서 빠져나올 수 없을 때?**
- Ctrl + C로 프로그램 강제 종료

---

**강의 준비 완료! 화이팅!**
