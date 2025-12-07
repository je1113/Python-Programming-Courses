"""
세션 6: while 문 활용 - 해설
난이도: ★★★★
"""

# ============================================
# 문제 1: 간단한 메뉴 시스템 (기초) - 해설
# ============================================
print("=" * 50)
print("문제 1: 간단한 메뉴 시스템")
print("=" * 50)

test_choices = ["1", "2", "4", "3"]
test_index = 0

# ✅ 모범 답안
running = True
while running:
    print("\n=== 메뉴 ===")
    print("1. 조회")
    print("2. 등록")
    print("3. 종료")

    choice = test_choices[test_index]
    test_index += 1
    print(f"선택: {choice}")

    if choice == "1":
        print("조회 기능 실행")
    elif choice == "2":
        print("등록 기능 실행")
    elif choice == "3":
        print("프로그램을 종료합니다.")
        running = False
    else:
        print("잘못된 선택입니다.")

# 📌 주요 포인트:
# 1. running 플래그 변수로 루프 제어
# 2. while running: 패턴 (가독성 좋음)
# 3. running = False로 종료
# 4. 잘못된 입력 처리 (else)

# ⚠️ 자주 하는 실수:
# while True:  # ⚠️ 가능하지만 break 사용해야 함
# if choice == 3:  # ❌ 문자열과 정수 비교
# running = True  # ❌ False로 설정해야 종료

# 💡 팁:
# - while True + break 패턴도 일반적
# - 함수로 분리하여 각 기능 구현
# - 딕셔너리로 메뉴 관리

print()


# ============================================
# 문제 2: ATM 기계 (입출금) - 해설
# ============================================
print("=" * 50)
print("문제 2: ATM 기계")
print("=" * 50)

balance = 10000
test_atm_choices = ["1", "3", "2", "4"]
test_amounts = [5000, 3000]
test_index = 0
amount_index = 0

# ✅ 모범 답안
while True:
    print(f"\n=== ATM ===")
    print(f"현재 잔액: {balance:,}원")
    print("1. 입금  2. 출금  3. 잔액조회  4. 종료")

    choice = test_atm_choices[test_index]
    test_index += 1
    print(f"선택: {choice}")

    if choice == "1":
        # amount = int(input("입금액: "))
        amount = test_amounts[amount_index]
        amount_index += 1
        print(f"입금액: {amount}")

        balance += amount
        print(f"{amount:,}원이 입금되었습니다.")

    elif choice == "2":
        # amount = int(input("출금액: "))
        amount = test_amounts[amount_index]
        amount_index += 1
        print(f"출금액: {amount}")

        if balance >= amount:
            balance -= amount
            print(f"{amount:,}원이 출금되었습니다.")
        else:
            print("잔액이 부족합니다!")

    elif choice == "3":
        print(f"현재 잔액: {balance:,}원")

    elif choice == "4":
        print("이용해 주셔서 감사합니다.")
        break

    else:
        print("잘못된 선택입니다.")

# 📌 주요 포인트:
# 1. while True + break 패턴
# 2. 출금 시 잔액 확인 필수
# 3. 잔액 변화 즉시 반영
# 4. 천 단위 구분 기호 사용

# ⚠️ 자주 하는 실수:
# balance = amount  # ❌ += 또는 -= 사용해야 함
# if balance > amount:  # ❌ >= 사용해야 함 (같을 때도 출금 가능)

# 💡 팁:
# - 거래 내역 저장 (리스트)
# - 일일 출금 한도 설정
# - 수수료 계산 추가

print()


# ============================================
# 문제 3: 장바구니 시스템 - 해설
# ============================================
print("=" * 50)
print("문제 3: 장바구니 시스템")
print("=" * 50)

total_price = 0
item_count = 0

test_cart_choices = ["1", "1", "2", "3"]
test_prices = [15000, 8000]
test_index = 0
price_index = 0

# ✅ 모범 답안
while True:
    print("\n=== 장바구니 ===")
    print("1. 상품 추가  2. 장바구니 보기  3. 결제  4. 초기화  5. 나가기")

    choice = test_cart_choices[test_index]
    test_index += 1
    print(f"선택: {choice}")

    if choice == "1":
        # price = int(input("상품 가격: "))
        price = test_prices[price_index]
        price_index += 1
        print(f"상품 가격: {price}")

        total_price += price
        item_count += 1
        print("상품이 추가되었습니다.")

    elif choice == "2":
        print(f"\n상품 개수: {item_count}개")
        print(f"총 금액: {total_price:,}원")

    elif choice == "3":
        if item_count == 0:
            print("장바구니가 비어있습니다!")
        else:
            print(f"\n결제 금액: {total_price:,}원")
            print("결제가 완료되었습니다!")
            break

    elif choice == "4":
        total_price = 0
        item_count = 0
        print("장바구니가 초기화되었습니다.")

    elif choice == "5":
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 선택입니다.")

# 📌 주요 포인트:
# 1. total_price와 item_count 별도 관리
# 2. 장바구니 비어있을 때 결제 방지
# 3. 초기화 기능으로 재사용 가능

# ⚠️ 자주 하는 실수:
# if item_count:  # ⚠️ 가능하지만 명확성 떨어짐
# total_price = 0  # ❌ 초기화 기능 외에는 사용 금지

# 💡 팁:
# - 상품명과 가격을 튜플/딕셔너리로 저장
# - 할인 쿠폰 적용 기능
# - 배송비 계산 추가

print()


# ============================================
# 문제 4: 평균 점수 계산기 - 해설
# ============================================
print("=" * 50)
print("문제 4: 평균 점수 계산기")
print("=" * 50)

total = 0
count = 0
test_scores = [85, 90, 78, 0]
test_index = 0

# ✅ 모범 답안
while True:
    # score = int(input("점수 입력 (종료: 0): "))
    score = test_scores[test_index]
    test_index += 1
    print(f"점수 입력 (종료: 0): {score}")

    if score == 0:
        break

    total += score
    count += 1

print("\n=== 결과 ===")
print(f"학생 수: {count}명")
print(f"총점: {total}점")

if count > 0:
    average = total / count
    print(f"평균: {average:.2f}점")
else:
    print("입력된 점수가 없습니다.")

# 📌 주요 포인트:
# 1. 0 입력 시 break로 종료
# 2. total과 count 누적
# 3. 0으로 나누기 방지 (count > 0 확인)
# 4. :.2f로 소수점 2자리까지 표시

# ⚠️ 자주 하는 실수:
# average = total / count  # ❌ count가 0일 수 있음
# if score == 0:  # ❌ break 전에 total += score 실행됨
#     total += score

# 💡 팁:
# - 최고점, 최저점 추가 계산
# - 점수 리스트로 저장하여 나중에 조회
# - 유효한 점수 범위 검증 (0-100)

print()


# ============================================
# 문제 5: 숫자 맞추기 게임 (기회 제한) - 해설
# ============================================
print("=" * 50)
print("문제 5: 숫자 맞추기 게임")
print("=" * 50)

answer = 27
attempts = 0
max_attempts = 7
test_guesses = [25, 30, 27]
test_index = 0

# ✅ 모범 답안
while attempts < max_attempts:
    # guess = int(input("숫자를 맞춰보세요 (1-50): "))
    guess = test_guesses[test_index]
    test_index += 1
    print(f"숫자를 맞춰보세요 (1-50): {guess}")

    attempts += 1

    if guess == answer:
        print(f"정답! {attempts}번 만에 맞추셨습니다!")
        break
    elif guess < answer:
        print("더 큰 수입니다.")
    else:
        print("더 작은 수입니다.")

if attempts >= max_attempts and guess != answer:
    print(f"실패! 정답은 {answer}였습니다.")

# 📌 주요 포인트:
# 1. attempts로 시도 횟수 카운트
# 2. 맞추면 break로 즉시 종료
# 3. 힌트 제공 (더 크다/작다)
# 4. 기회 소진 시 정답 공개

# ⚠️ 자주 하는 실수:
# if attempts == max_attempts:  # ❌ >= 사용해야 함
# if guess != answer:  # ❌ 루프 안에 있으면 매번 실행

# 💡 팁:
# - import random으로 정답 무작위 생성
# - 범위 좁혀가며 힌트 (1-50 → 20-50)
# - 난이도 선택 (쉬움/보통/어려움)

print()


# ============================================
# 문제 6: 구구단 전체 출력 (중첩 while) - 해설
# ============================================
print("=" * 50)
print("문제 6: 구구단 전체 출력")
print("=" * 50)

dan = 2

# ✅ 모범 답안
while dan <= 9:
    print(f"\n=== {dan}단 ===")

    num = 1
    while num <= 9:
        result = dan * num
        print(f"{dan} x {num} = {result}")
        num += 1

    dan += 1

# 📌 주요 포인트:
# 1. 외부 while: 단 (2~9)
# 2. 내부 while: 곱할 수 (1~9)
# 3. 내부 while 끝날 때마다 dan 증가
# 4. num은 매번 1로 초기화

# ⚠️ 자주 하는 실수:
# num = 1  # ❌ 외부 루프에 있으면 초기화 안됨
# while dan <= 9:
#     while num <= 9:

# dan += 1  # ❌ 내부 while 안에 있으면 매번 증가
#     while num <= 9:
#         dan += 1

# 💡 팁:
# - for 문이 더 간결: for dan in range(2, 10):
# - 원하는 단만 선택하여 출력
# - 가로 형태로 출력 (2 x 1 = 2  2 x 2 = 4  ...)

print()


# ============================================
# 🎯 핵심 정리
# ============================================
print("=" * 50)
print("🎯 세션 6 핵심 정리")
print("=" * 50)

print("""
1. while 문 활용 패턴

   # 패턴 1: 플래그 변수
   running = True
   while running:
       if 종료조건:
           running = False

   # 패턴 2: while True + break
   while True:
       if 종료조건:
           break

   # 패턴 3: 카운터 기반
   count = 0
   while count < max_count:
       count += 1

2. 메뉴 시스템 구조
   while True:
       # 메뉴 출력
       # 선택 입력
       # if-elif-else로 처리
       # 종료 조건에서 break

3. 플래그 변수 vs break
   - 플래그: 종료 이유 명확, 여러 곳에서 종료 가능
   - break: 간결, 즉시 종료

4. 누적 계산 패턴
   total = 0
   count = 0
   while 조건:
       total += value
       count += 1
   average = total / count  # 0으로 나누기 주의!

5. 중첩 while 문
   외부_카운터 = 초기값
   while 외부_조건:
       내부_카운터 = 초기값  # 매번 초기화!
       while 내부_조건:
           내부_카운터 += 1
       외부_카운터 += 1

6. 입력 검증 패턴
   while True:
       value = input()
       if 유효한_입력:
           break
       else:
           print("다시 입력하세요")

7. 실무 활용 사례
   - ATM/키오스크 시스템
   - 게임 메인 루프
   - 데이터 입력 및 검증
   - 메뉴 기반 프로그램

8. 자주 하는 실수
   ❌ 무한 루프 (종료 조건 없음)
   ❌ 0으로 나누기 (평균 계산 시)
   ❌ 중첩 while에서 내부 카운터 초기화 안함
   ❌ 플래그 변수 업데이트 빠뜨림

9. 최적화 팁
   - 불필요한 중첩 피하기
   - 조건 순서 최적화 (자주 발생하는 조건 위로)
   - 함수로 분리하여 재사용
   - 상수는 변수로 관리 (MAX_ATTEMPTS 등)

10. 디버깅 팁
    - print로 각 단계 확인
    - 카운터 값 추적
    - 조건식 단순화
    - 작은 부분부터 테스트

11. for vs while 선택
    ✅ for: 횟수/범위가 명확할 때
    ✅ while: 조건에 따라 반복, 무한 루프 필요

12. 실전 코드 예시
    # 입금/출금 검증 패턴
    while True:
        amount = int(input("금액: "))
        if amount <= 0:
            print("양수를 입력하세요")
        elif amount > balance:
            print("잔액 부족")
        else:
            balance -= amount
            break
""")

print("=" * 50)
print("✅ 해설 완료!")
print("=" * 50)
