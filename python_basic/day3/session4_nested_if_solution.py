"""
세션 4: 중첩 if 문 - 해설
난이도: ★★★★
"""

# ============================================
# 문제 1: 로그인 및 권한 확인 (기초) - 해설
# ============================================
print("=" * 50)
print("문제 1: 로그인 및 권한 확인")
print("=" * 50)

is_logged_in = True
is_admin = True

# ✅ 모범 답안
if is_logged_in:
    if is_admin:
        print("관리자 페이지 접근 가능")
    else:
        print("권한이 없습니다.")
else:
    print("먼저 로그인하세요.")

# 대안: and 연산자 사용 (더 간결)
# if not is_logged_in:
#     print("먼저 로그인하세요.")
# elif is_logged_in and is_admin:
#     print("관리자 페이지 접근 가능")
# else:
#     print("권한이 없습니다.")

# 📌 주요 포인트:
# 1. 외부 조건 먼저 검사 (로그인 여부)
# 2. 내부 조건 후 검사 (관리자 여부)
# 3. 단계별 검증으로 보안 강화

# ⚠️ 자주 하는 실수:
# if is_admin:  # ❌ 로그인 확인 없이 관리자 확인
#     if is_logged_in:

# 💡 팁:
# - and 연산자로 간단히: if is_logged_in and is_admin:
# - 함수로 분리: def check_admin_access():

print()


# ============================================
# 문제 2: 영화 관람 등급 (나이 + 보호자) - 해설
# ============================================
print("=" * 50)
print("문제 2: 영화 관람 등급")
print("=" * 50)

age = 13
has_parent = True

# ✅ 모범 답안
print(f"나이: {age}세")

if age >= 15:
    print("관람 가능합니다.")
else:
    if has_parent:
        print("보호자 동반으로 관람 가능합니다.")
    else:
        print("관람 불가능합니다.")

# 📌 주요 포인트:
# 1. 나이 기준 먼저 확인
# 2. 미성년자의 경우 보호자 동반 여부 추가 확인
# 3. 실무: 신분증 확인, 보호자 동의서 등

# ⚠️ 자주 하는 실수:
# if has_parent:  # ❌ 나이 확인 없이 보호자만 확인
# if age >= 15 and has_parent:  # ❌ 성인에게 보호자 요구

# 💡 팁:
# - 등급별 세분화: 12세, 15세, 19세
# - 온라인 예매 시 생년월일 검증

print()


# ============================================
# 문제 3: 할인 적용 (회원 등급 + 금액) - 해설
# ============================================
print("=" * 50)
print("문제 3: 할인 적용")
print("=" * 50)

is_member = True
amount = 120000

# ✅ 모범 답안
print(f"회원 여부: {'회원' if is_member else '비회원'}")
print(f"구매 금액: {amount:,}원")

if is_member:
    if amount >= 100000:
        discount_rate = 0.20
        print("VIP 할인 20% 적용!")
    elif amount >= 50000:
        discount_rate = 0.10
        print("회원 할인 10% 적용!")
    else:
        discount_rate = 0.05
        print("기본 회원 할인 5% 적용!")
else:
    discount_rate = 0
    print("비회원 - 할인 없음")

final_amount = amount * (1 - discount_rate)
print(f"최종 금액: {final_amount:,.0f}원")

# 📌 주요 포인트:
# 1. 회원 여부 먼저 확인
# 2. 회원인 경우 금액별 차등 할인
# 3. 높은 금액부터 순차 검사 (if-elif 순서 중요)

# ⚠️ 자주 하는 실수:
# if amount >= 50000:  # ❌ 회원 확인 없이 금액만 검사
#     discount_rate = 0.10
# elif amount >= 100000:  # ❌ 순서 잘못 (낮은 금액 먼저)
#     discount_rate = 0.20

# 💡 팁:
# - 등급 시스템: VIP, Gold, Silver
# - 쿠폰 중복 적용 여부 확인
# - 최대 할인 한도 설정

print()


# ============================================
# 문제 4: 시험 응시 자격 (출석 + 과제) - 해설
# ============================================
print("=" * 50)
print("문제 4: 시험 응시 자격")
print("=" * 50)

attendance = 85
assignment_submitted = True

# ✅ 모범 답안
print(f"출석률: {attendance}%")
print(f"과제 제출 여부: {'제출함' if assignment_submitted else '미제출'}")

if attendance >= 80:
    if assignment_submitted:
        print("시험 응시 가능합니다.")
    else:
        print("과제를 먼저 제출하세요.")
else:
    print("출석률이 부족합니다.")

# 📌 주요 포인트:
# 1. 출석률이 1차 조건 (필수)
# 2. 출석률 충족 후 과제 제출 여부 확인
# 3. 단계별 안내 메시지 제공

# ⚠️ 자주 하는 실수:
# if assignment_submitted:  # ❌ 출석률 무시
#     if attendance >= 80:
# if attendance >= 80 and assignment_submitted:  # ⚠️ 가능하지만 메시지 구분 어려움

# 💡 팁:
# - 실무: 출석률, 과제, 퀴즈 점수 종합 평가
# - 예외 처리: 공결, 질병 등

print()


# ============================================
# 문제 5: 대출 가능 여부 (나이 + 소득 + 신용) - 해설
# ============================================
print("=" * 50)
print("문제 5: 대출 가능 여부")
print("=" * 50)

age = 25
income = 3500
credit_score = 650

# ✅ 모범 답안
print(f"나이: {age}세")
print(f"연소득: {income:,}만원")
print(f"신용등급: {credit_score}점")

if age >= 20:
    if income >= 3000:
        if credit_score >= 600:
            print("대출 가능합니다!")
        else:
            print("신용등급이 낮습니다.")
    else:
        print("소득이 부족합니다.")
else:
    print("나이 제한으로 대출 불가능합니다.")

# 대안: and 연산자 사용
# if age < 20:
#     print("나이 제한으로 대출 불가능합니다.")
# elif income < 3000:
#     print("소득이 부족합니다.")
# elif credit_score < 600:
#     print("신용등급이 낮습니다.")
# else:
#     print("대출 가능합니다!")

# 📌 주요 포인트:
# 1. 3단계 중첩 if 문
# 2. 각 단계별 실패 메시지 제공
# 3. 모든 조건 충족 시에만 승인

# ⚠️ 자주 하는 실수:
# if age >= 20 and income >= 3000 and credit_score >= 600:  # ⚠️ 가능하지만 단계별 메시지 불가
# if credit_score >= 600:  # ❌ 나이, 소득 확인 없이 신용만 확인

# 💡 팁:
# - 실무: 부채비율(DTI), 담보 가치 등 추가 검토
# - 조건별 가중치 부여
# - 함수로 분리하여 가독성 향상

print()


# ============================================
# 문제 6: 배송 가능 여부 (재고 + 주소) - 해설
# ============================================
print("=" * 50)
print("문제 6: 배송 가능 여부")
print("=" * 50)

stock = 10
region = "서울"

# ✅ 모범 답안
print(f"재고: {stock}개")
print(f"배송 지역: {region}")

if stock > 0:
    if region == "제주":
        print("제주 배송은 3일 소요됩니다.")
    else:
        print("내일 도착 예정입니다.")
else:
    print("품절입니다.")

# 📌 주요 포인트:
# 1. 재고 확인이 우선 (재고 없으면 배송 불가)
# 2. 재고 있으면 지역별 배송 안내
# 3. 사용자에게 명확한 정보 제공

# ⚠️ 자주 하는 실수:
# if region == "제주":  # ❌ 재고 확인 없이 지역만 확인
# if stock >= 0:  # ❌ 0개도 배송 가능하게 됨

# 💡 팁:
# - 지역별 배송비 차등
# - 도서산간 지역 추가 확인
# - 예상 배송일 계산 (영업일 기준)

print()


# ============================================
# 🎯 핵심 정리
# ============================================
print("=" * 50)
print("🎯 세션 4 핵심 정리")
print("=" * 50)

print("""
1. 중첩 if 문 기본 구조
   if 조건1:
       if 조건2:
           조건1, 2 모두 참
       else:
           조건1만 참
   else:
       조건1 거짓

2. 중첩 vs and 연산자
   # 중첩 if (단계별 메시지 가능)
   if age >= 20:
       if income >= 3000:
           print("승인")
       else:
           print("소득 부족")
   else:
       print("나이 미달")

   # and 연산자 (간결하지만 메시지 구분 어려움)
   if age >= 20 and income >= 3000:
       print("승인")

3. 언제 중첩 if 사용?
   ✅ 각 단계별 다른 메시지 필요할 때
   ✅ 조건 검사 순서가 중요할 때
   ✅ 내부 조건이 외부 조건에 종속될 때

4. 언제 and 연산자 사용?
   ✅ 모든 조건을 동시에 검사할 때
   ✅ 실패 이유 구분이 불필요할 때
   ✅ 코드를 간결하게 작성하고 싶을 때

5. 들여쓰기 주의
   - 각 중첩 레벨마다 4칸 추가
   - 너무 깊은 중첩(3단계 이상)은 가독성 저하
   - 함수로 분리 고려

6. 실무 활용
   - 권한 시스템 (로그인 + 역할)
   - 다단계 검증 (나이 + 소득 + 신용)
   - 조건부 할인 (회원 + 금액)
   - 배송 로직 (재고 + 지역)

7. 리팩토링 팁
   # 3단계 이상 중첩 → 함수 분리
   def check_loan_eligibility(age, income, credit):
       if age < 20:
           return False, "나이 미달"
       if income < 3000:
           return False, "소득 부족"
       if credit < 600:
           return False, "신용 부족"
       return True, "승인"

8. 자주 하는 실수
   ❌ 조건 검사 순서 잘못
   ❌ 불필요한 중첩 (and로 간단히 가능한 경우)
   ❌ 들여쓰기 잘못
   ❌ else 블록 누락으로 예외 처리 안됨
""")

print("=" * 50)
print("✅ 해설 완료!")
print("=" * 50)
