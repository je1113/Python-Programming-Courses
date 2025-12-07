"""
세션 5: while 문 기초 - 해설
난이도: ★★★★★
"""

# ============================================
# 문제 1: 1부터 10까지 출력 (기초) - 해설
# ============================================
print("=" * 50)
print("문제 1: 1부터 10까지 출력")
print("=" * 50)

count = 1

# ✅ 모범 답안
while count <= 10:
    print(count)
    count += 1

# 📌 주요 포인트:
# 1. 초기값 설정: count = 1
# 2. 조건식: count <= 10 (10도 포함)
# 3. 증가: count += 1 (필수! 없으면 무한 루프)

# ⚠️ 자주 하는 실수:
# while count <= 10:  # ❌ count += 1 빠짐 → 무한 루프
#     print(count)
# while count < 10:  # ❌ 10이 출력 안됨

# 💡 팁:
# - count += 1은 count = count + 1과 동일
# - for 문으로 더 간결: for i in range(1, 11):

print()


# ============================================
# 문제 2: 합계 계산 (1부터 100까지) - 해설
# ============================================
print("=" * 50)
print("문제 2: 합계 계산")
print("=" * 50)

num = 1
total = 0

# ✅ 모범 답안
while num <= 100:
    total += num
    num += 1

print(f"1부터 100까지의 합: {total}")

# 📌 주요 포인트:
# 1. total 변수로 누적 합계
# 2. total += num으로 계속 더하기
# 3. num은 카운터, total은 누적기

# ⚠️ 자주 하는 실수:
# total = num  # ❌ += 대신 = 사용하면 덮어씀
# while num < 100:  # ❌ 100이 누락됨

# 💡 팁:
# - 수학 공식: n(n+1)/2 = 100*101/2 = 5050
# - sum(range(1, 101))로 한 줄 해결

print()


# ============================================
# 문제 3: 짝수만 출력 (1부터 20까지) - 해설
# ============================================
print("=" * 50)
print("문제 3: 짝수만 출력")
print("=" * 50)

num = 1

# ✅ 모범 답안 1: if 문 활용
while num <= 20:
    if num % 2 == 0:
        print(num, end=' ')
    num += 1
print()  # 줄바꿈

# 대안 2: 2씩 증가
# num = 2
# while num <= 20:
#     print(num, end=' ')
#     num += 2

# 📌 주요 포인트:
# 1. num % 2 == 0으로 짝수 판별
# 2. end=' '로 가로로 출력
# 3. 또는 2씩 증가시켜서 짝수만 접근

# ⚠️ 자주 하는 실수:
# if num % 2:  # ❌ 홀수일 때 True (짝수는 0이라 False)
# num = 2; num += 1  # ❌ 1씩 증가하면 홀수도 포함

# 💡 팁:
# - 홀수: num % 2 == 1 또는 num % 2 != 0
# - range(2, 21, 2)로 for 문 사용 가능

print()


# ============================================
# 문제 4: 카운트다운 (10부터 1까지) - 해설
# ============================================
print("=" * 50)
print("문제 4: 카운트다운")
print("=" * 50)

count = 10

# ✅ 모범 답안
while count >= 1:
    print(count)
    count -= 1
print("발사!")

# 📌 주요 포인트:
# 1. 초기값 10에서 시작
# 2. count -= 1로 감소
# 3. count >= 1 조건 (1도 포함)
# 4. 루프 종료 후 "발사!" 출력

# ⚠️ 자주 하는 실수:
# count += 1  # ❌ 증가하면 무한 루프
# while count > 1:  # ❌ 1이 출력 안됨
# print("발사!")  # ❌ 들여쓰기하면 매번 출력

# 💡 팁:
# - while count > 0: 도 가능
# - range(10, 0, -1)로 for 문 가능

print()


# ============================================
# 문제 5: 구구단 출력 (5단) - 해설
# ============================================
print("=" * 50)
print("문제 5: 구구단 출력")
print("=" * 50)

print("=== 5단 ===")
num = 1

# ✅ 모범 답안
while num <= 9:
    result = 5 * num
    print(f"5 x {num} = {result}")
    num += 1

# 📌 주요 포인트:
# 1. num을 1부터 9까지 증가
# 2. 5 * num으로 계산
# 3. f-string으로 깔끔하게 출력

# ⚠️ 자주 하는 실수:
# while num < 9:  # ❌ 9가 누락됨
# print(f"5 x {num} = {5 * num}")  # ⚠️ 가능하지만 가독성 떨어짐

# 💡 팁:
# - 중첩 while로 전체 구구단 가능
# - 입력받아서 원하는 단 출력

print()


# ============================================
# 문제 6: 비밀번호 입력 (최대 3번) - 해설
# ============================================
print("=" * 50)
print("문제 6: 비밀번호 입력")
print("=" * 50)

correct_password = "python123"
attempts = 0
max_attempts = 3

# ✅ 모범 답안 (테스트용)
test_inputs = ["abc", "def", "python123"]
test_index = 0

while attempts < max_attempts:
    # user_input = input("비밀번호를 입력하세요: ")
    user_input = test_inputs[test_index]  # 테스트용
    test_index += 1
    print(f"비밀번호를 입력하세요: {user_input}")

    if user_input == correct_password:
        print("로그인 성공!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"틀렸습니다. 남은 기회: {remaining}번")

if attempts >= max_attempts:
    print("계정이 잠겼습니다.")

# 📌 주요 포인트:
# 1. attempts < max_attempts 조건
# 2. 맞으면 break로 루프 탈출
# 3. 틀리면 attempts 증가
# 4. 루프 종료 후 최종 확인 (계정 잠금)

# ⚠️ 자주 하는 실수:
# while attempts <= max_attempts:  # ❌ 4번 시도 가능
# if attempts == max_attempts:  # ❌ 루프 안에 있으면 매번 확인
#     print("계정 잠금")
# break 빠뜨림  # ❌ 성공해도 계속 입력 요청

# 💡 팁:
# - 실무: 계정 잠금 시간 설정, 로그 기록
# - 비밀번호 힌트 제공
# - 대소문자 무시: .lower() 사용

print()


# ============================================
# 문제 7: 잔액 누적 (입금 시뮬레이션) - 해설
# ============================================
print("=" * 50)
print("문제 7: 잔액 누적")
print("=" * 50)

balance = 0
count = 1
deposit_amount = 1000

# ✅ 모범 답안
while count <= 5:
    balance += deposit_amount
    print(f"{count}번째 입금: {deposit_amount:,}원 (잔액: {balance:,}원)")
    count += 1

print(f"최종 잔액: {balance:,}원")

# 📌 주요 포인트:
# 1. balance로 잔액 누적
# 2. count로 입금 횟수 카운트
# 3. 매번 현재 잔액 표시
# 4. :, 로 천 단위 구분

# ⚠️ 자주 하는 실수:
# balance = deposit_amount  # ❌ += 대신 = 사용
# while count < 5:  # ❌ 5번째 입금 누락

# 💡 팁:
# - 입금 금액을 매번 입력받기
# - 출금 기능 추가
# - 거래 내역 리스트로 저장

print()


# ============================================
# 문제 8: 특정 수까지의 곱 (팩토리얼) - 해설
# ============================================
print("=" * 50)
print("문제 8: 팩토리얼")
print("=" * 50)

n = 5
result = 1
num = 1

# ✅ 모범 답안
while num <= n:
    result *= num
    num += 1

print(f"{n}! = {result}")

# 대안: 역순으로 곱하기
# num = n
# while num >= 1:
#     result *= num
#     num -= 1

# 📌 주요 포인트:
# 1. result 초기값 1 (0이면 항상 0)
# 2. result *= num으로 누적 곱
# 3. 1부터 n까지 차례로 곱하기

# ⚠️ 자주 하는 실수:
# result = 0  # ❌ 0으로 초기화하면 계속 0
# result += num  # ❌ + 대신 * 사용해야 함
# while num < n:  # ❌ n이 누락됨

# 💡 팁:
# - 큰 수는 오버플로우 주의 (Python은 자동 처리)
# - math.factorial(n) 내장 함수 사용 가능
# - 재귀 함수로 구현 가능

print()


# ============================================
# 🎯 핵심 정리
# ============================================
print("=" * 50)
print("🎯 세션 5 핵심 정리")
print("=" * 50)

print("""
1. while 문 기본 구조
   while 조건식:
       반복할 코드
       카운터 증가/감소

2. 필수 요소
   - 초기값 설정
   - 조건식 (언젠가 False가 되어야 함)
   - 카운터 변경 (증가/감소)

3. 주요 패턴

   # 카운트업
   count = 1
   while count <= 10:
       print(count)
       count += 1

   # 카운트다운
   count = 10
   while count >= 1:
       print(count)
       count -= 1

   # 누적 합계
   total = 0
   num = 1
   while num <= 100:
       total += num
       num += 1

   # 누적 곱
   result = 1
   num = 1
   while num <= 5:
       result *= num
       num += 1

4. 증감 연산자
   count += 1  # count = count + 1
   count -= 1  # count = count - 1
   count *= 2  # count = count * 2
   count //= 2  # count = count // 2

5. 조건 비교
   while count < 10:   # 10 미포함
   while count <= 10:  # 10 포함
   while count > 0:    # 0 미포함
   while count >= 1:   # 1 포함 (0 미포함)

6. 무한 루프 방지
   ✅ 카운터 증가/감소 필수
   ✅ 조건이 언젠가 False가 되는지 확인
   ❌ 조건이 항상 True면 무한 루프

7. break 활용
   while count < max_attempts:
       if success:
           break  # 즉시 루프 탈출
       count += 1

8. 실무 활용
   - 사용자 입력 재요청
   - 누적 계산 (합계, 평균)
   - 반복 작업 (로그 처리)
   - 조건 충족까지 대기

9. for vs while
   for: 횟수가 정해진 경우 (range 사용)
   while: 조건에 따라 반복 (횟수 미정)

10. 디버깅 팁
    - print로 카운터 값 확인
    - 조건식 제대로 작성했는지 확인
    - 카운터 증가/감소 빠뜨리지 않았는지 확인
    - Ctrl+C로 무한 루프 강제 종료
""")

print("=" * 50)
print("✅ 해설 완료!")
print("=" * 50)
