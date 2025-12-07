"""
세션 7: 무한 루프와 break - 해설
난이도: ★★★★
"""

# ============================================
# 문제 1: 간단한 계산기 (기초) - 해설
# ============================================
print("=" * 50)
print("문제 1: 간단한 계산기")
print("=" * 50)

test_calc = [
    ("10", "5", "+"),
    ("20", "4", "/"),
    ("q", "", "")
]
test_index = 0

# ✅ 모범 답안
while True:
    print("\n=== 계산기 ===")

    num1, num2, op = test_calc[test_index]
    test_index += 1
    print(f"첫 번째 숫자 (종료: q): {num1}")

    if num1 == 'q':
        print("계산기를 종료합니다.")
        break

    print(f"두 번째 숫자: {num2}")
    print(f"연산자 (+, -, *, /): {op}")

    num1 = float(num1)
    num2 = float(num2)

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("0으로 나눌 수 없습니다!")
            continue
    else:
        print("잘못된 연산자입니다.")
        continue

    print(f"결과: {result}")

# 📌 주요 포인트:
# 1. while True로 무한 루프
# 2. 'q' 입력 시 break로 즉시 종료
# 3. 0으로 나누기 방지
# 4. 잘못된 입력 시 continue로 재시작

# ⚠️ 자주 하는 실수:
# if num1 == "q":  # ❌ break 전에 num2 입력받으면 오류
#     num2 = input()
#     break
# result = num1 / num2  # ❌ 0 검사 없이 나누기

# 💡 팁:
# - try-except로 예외 처리
# - 연산자를 함수로 분리
# - 이전 결과를 다음 계산에 사용

print()


# ============================================
# 문제 2: 비밀번호 설정 (유효성 검증) - 해설
# ============================================
print("=" * 50)
print("문제 2: 비밀번호 설정")
print("=" * 50)

test_passwords = ["abc", "1234", "python1234"]
test_index = 0

# ✅ 모범 답안
while True:
    password = test_passwords[test_index]
    test_index += 1
    print(f"비밀번호 설정: {password}")

    if len(password) >= 8:
        print("비밀번호가 설정되었습니다.")
        break
    else:
        print("8자 이상 입력하세요.")

# 📌 주요 포인트:
# 1. while True로 조건 만족까지 반복
# 2. len() 함수로 길이 확인
# 3. 조건 만족 시 break
# 4. 불만족 시 다시 루프

# ⚠️ 자주 하는 실수:
# if len(password) < 8:  # ⚠️ 가능하지만 로직 복잡
#     print("8자 이상")
# else:
#     break

# 💡 팁:
# - 추가 조건: 숫자 포함, 특수문자 포함
# - any() 함수: any(c.isdigit() for c in password)
# - 정규표현식으로 복잡한 패턴 검증

print()


# ============================================
# 문제 3: 숫자 맞추기 게임 (무제한) - 해설
# ============================================
print("=" * 50)
print("문제 3: 숫자 맞추기 게임")
print("=" * 50)

answer = 42
attempts = 0
test_guesses = [50, 40, 42]
test_index = 0

# ✅ 모범 답안
while True:
    guess = test_guesses[test_index]
    test_index += 1
    print(f"숫자를 맞춰보세요: {guess}")

    attempts += 1

    if guess == answer:
        print(f"정답! {attempts}번 만에 맞추셨습니다!")
        break
    elif guess < answer:
        print("더 큰 숫자입니다.")
    else:
        print("더 작은 숫자입니다.")

# 📌 주요 포인트:
# 1. 정답 맞출 때까지 무한 반복
# 2. 맞추면 break
# 3. 시도 횟수 카운트
# 4. 힌트 제공으로 사용성 향상

# ⚠️ 자주 하는 실수:
# attempts += 1  # ❌ break 후에 있으면 실행 안됨
# if guess == answer:
#     break

# 💡 팁:
# - import random으로 정답 랜덤화
# - 범위 힌트: "20-50 사이입니다"
# - 최소 시도 횟수 기록 (베스트 스코어)

print()


# ============================================
# 문제 4: 소수 찾기 (특정 개수만큼) - 해설
# ============================================
print("=" * 50)
print("문제 4: 소수 찾기")
print("=" * 50)

found_count = 0
num = 2

# ✅ 모범 답안
while True:
    # 소수 판별
    is_prime = True

    if num > 2:
        i = 2
        while i < num:
            if num % i == 0:
                is_prime = False
                break
            i += 1

    if is_prime:
        found_count += 1
        print(f"소수 {found_count}: {num}")

        if found_count == 5:
            print("5개의 소수를 찾았습니다!")
            break

    num += 1

# 📌 주요 포인트:
# 1. 무한 루프로 계속 검사
# 2. 소수 판별 알고리즘
# 3. 5개 찾으면 break
# 4. 중첩 while과 break 활용

# ⚠️ 자주 하는 실수:
# if found_count >= 5:  # ❌ 루프 밖에 있으면 실행 안됨
# while True:
#     ...
# if found_count >= 5:
#     break

# 💡 팁:
# - 최적화: i * i <= num까지만 검사
# - 2 제외하고 홀수만 검사
# - 에라토스테네스의 체 알고리즘

print()


# ============================================
# 문제 5: 목표 금액 달성 (저축) - 해설
# ============================================
print("=" * 50)
print("문제 5: 목표 금액 달성")
print("=" * 50)

target = 100000
total = 0
month = 0
test_savings = [30000, 25000, 20000, 25000]
test_index = 0

# ✅ 모범 답안
print(f"목표 금액: {target:,}원\n")

while True:
    month += 1
    saving = test_savings[test_index]
    test_index += 1
    print(f"{month}개월차 저축액: {saving}")

    total += saving

    if total >= target:
        print(f"현재 총액: {total:,}원")
        print(f"목표 달성! {month}개월이 걸렸습니다!")
        break
    else:
        remaining = target - total
        print(f"현재 총액: {total:,}원 (목표까지 {remaining:,}원)\n")

# 📌 주요 포인트:
# 1. 목표 달성까지 계속 저축
# 2. 매월 누적 금액 계산
# 3. 목표 달성 시 break
# 4. 진행 상황 표시

# ⚠️ 자주 하는 실수:
# if total == target:  # ❌ 딱 맞지 않으면 무한 루프
# total = saving  # ❌ += 사용해야 누적됨

# 💡 팁:
# - 이자 계산 추가
# - 월별 저축액 리스트로 저장
# - 그래프로 시각화

print()


# ============================================
# 문제 6: 완벽한 제곱수 찾기 - 해설
# ============================================
print("=" * 50)
print("문제 6: 완벽한 제곱수 찾기")
print("=" * 50)

count = 0
n = 1

# ✅ 모범 답안
while True:
    square = n * n
    count += 1
    print(f"{square} = {n}²")

    if count == 10:
        break

    n += 1

# 대안: while count < 10:
# while count < 10:
#     n += 1
#     square = n * n
#     print(f"{square} = {n}²")
#     count += 1

# 📌 주요 포인트:
# 1. n을 증가시키며 제곱 계산
# 2. 10개 출력하면 break
# 3. 간단한 수학 패턴

# ⚠️ 자주 하는 실수:
# if count >= 10:  # ❌ >= 사용 시 11개 출력될 수 있음
# square = n ** 2  # ⚠️ 가능하지만 * * 권장

# 💡 팁:
# - ** 연산자: n ** 2
# - math.sqrt()로 역계산
# - 입력받은 수까지의 제곱수 출력

print()


# ============================================
# 🎯 핵심 정리
# ============================================
print("=" * 50)
print("🎯 세션 7 핵심 정리")
print("=" * 50)

print("""
1. while True 패턴
   while True:
       # 무한 루프
       if 종료조건:
           break

2. break의 역할
   - 반복문을 즉시 종료
   - 가장 가까운 반복문만 탈출
   - 조건 만족 시 더 이상 반복 불필요할 때 사용

3. 무한 루프 활용 시나리오
   - 조건이 언제 충족될지 모를 때
   - 사용자 입력 계속 받을 때
   - 게임 메인 루프
   - 서버 프로그램

4. break 사용 패턴

   # 패턴 1: 조건 만족 시 종료
   while True:
       if 목표_달성:
           break

   # 패턴 2: 특정 입력 시 종료
   while True:
       user_input = input()
       if user_input == 'q':
           break

   # 패턴 3: 카운터 기반
   count = 0
   while True:
       count += 1
       if count >= 10:
           break

5. 중첩 루프에서 break
   while True:
       while True:
           if 조건:
               break  # 내부 while만 탈출
       if 조건:
           break  # 외부 while 탈출

6. continue vs break
   - break: 반복문 완전 종료
   - continue: 현재 반복만 건너뛰고 계속

7. 무한 루프 방지
   ✅ 반드시 break 조건 있어야 함
   ✅ 조건이 언젠가 True가 되는지 확인
   ⚠️ break 없으면 Ctrl+C로 강제 종료

8. 실무 활용 사례
   - 데이터 처리 (조건 만족까지)
   - 사용자 입력 검증 (올바른 값까지)
   - 게임 루프 (게임 오버까지)
   - 검색 알고리즘 (찾을 때까지)

9. 디버깅 팁
   - break 조건 확인
   - 무한 루프 걸리면 Ctrl+C
   - print로 루프 진행 상황 확인
   - 최대 반복 횟수 제한 추가 (안전장치)

10. 최적화
    # 불필요한 계산 피하기
    while True:
        result = expensive_calculation()
        if result:
            break
        # result 재사용

    # 조건 먼저 확인
    while True:
        if simple_check():  # 빠른 검사 먼저
            break
        complex_operation()  # 무거운 작업 나중

11. 안전한 무한 루프
    # 안전장치 추가
    max_iterations = 1000
    count = 0
    while True:
        count += 1
        if count > max_iterations:
            print("최대 반복 횟수 초과!")
            break
        if 정상_종료_조건:
            break

12. 자주 하는 실수
    ❌ break 조건 없음 (진짜 무한 루프)
    ❌ 도달할 수 없는 break
    ❌ break 후 코드 (실행 안됨)
    ❌ 잘못된 들여쓰기
""")

print("=" * 50)
print("✅ 해설 완료!")
print("=" * 50)
