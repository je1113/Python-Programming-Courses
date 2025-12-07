"""
세션 3: if-elif-else 문 - 해설
난이도: ★★★★★
"""

# ============================================
# 문제 1: 성적 등급 계산 (기초) - 해설
# ============================================
print("=" * 50)
print("문제 1: 성적 등급 계산")
print("=" * 50)

score = 85

# ✅ 모범 답안
print(f"점수: {score}점")

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

print(f"등급: {grade}")

# 📌 주요 포인트:
# 1. 높은 점수부터 순차적으로 검사
# 2. elif는 이전 조건이 거짓일 때만 실행
# 3. 조건 순서가 중요! (90부터 시작)

# ⚠️ 자주 하는 실수:
# if score >= 60:  # ❌ 먼저 검사하면 85도 D가 됨
#     grade = "D"
# elif score >= 80:
#     grade = "B"

# 💡 팁:
# - 범위 지정: if 90 <= score <= 100:
# - 딕셔너리 활용: grades = {90: "A", 80: "B", ...}

print()


# ============================================
# 문제 2: 계절 판단 (월 기준) - 해설
# ============================================
print("=" * 50)
print("문제 2: 계절 판단")
print("=" * 50)

month = 8

# ✅ 모범 답안
if month in [12, 1, 2]:
    season = "겨울"
elif month in [3, 4, 5]:
    season = "봄"
elif month in [6, 7, 8]:
    season = "여름"
elif month in [9, 10, 11]:
    season = "가을"
else:
    season = "잘못된 월"

print(f"{month}월은 {season}입니다.")

# 📌 주요 포인트:
# 1. in 연산자로 여러 값 동시 확인
# 2. 리스트로 그룹화
# 3. else로 예외 처리 (13월 등)

# ⚠️ 자주 하는 실수:
# if month == 6 or 7 or 8:  # ❌ 항상 True
# if month == 6, 7, 8:  # ❌ 튜플이 됨

# 💡 팁:
# - 범위 사용: if 3 <= month <= 5:
# - 딕셔너리: seasons = {12: "겨울", 1: "겨울", ...}

print()


# ============================================
# 문제 3: 배송비 계산 (금액별 차등) - 해설
# ============================================
print("=" * 50)
print("문제 3: 배송비 계산")
print("=" * 50)

order_amount = 35000

# ✅ 모범 답안
print(f"주문 금액: {order_amount:,}원")

if order_amount >= 50000:
    shipping = 0
    print("무료 배송!")
elif order_amount >= 30000:
    shipping = 2500
    print(f"배송비: {shipping:,}원")
else:
    shipping = 3500
    print(f"배송비: {shipping:,}원")

total = order_amount + shipping
print(f"총 결제 금액: {total:,}원")

# 📌 주요 포인트:
# 1. 높은 금액부터 검사 (50000 → 30000)
# 2. 각 구간의 배송비 차등 적용
# 3. 최종 금액 계산 필수

# ⚠️ 자주 하는 실수:
# if order_amount >= 30000:  # ❌ 먼저 검사하면 50000도 2500원
#     shipping = 2500

# 💡 팁:
# - 상수화: FREE_SHIPPING = 50000, BASIC_SHIPPING = 30000
# - 제주도 추가 배송비 고려

print()


# ============================================
# 문제 4: BMI 계산 및 판정 (건강) - 해설
# ============================================
print("=" * 50)
print("문제 4: BMI 계산 및 판정")
print("=" * 50)

height_cm = 170
weight = 65
height_m = height_cm / 100

# ✅ 모범 답안
bmi = weight / (height_m ** 2)

print(f"신장: {height_cm}cm, 체중: {weight}kg")
print(f"BMI: {bmi:.2f}")

if bmi >= 25:
    result = "과체중"
elif bmi >= 18.5:
    result = "정상"
else:
    result = "저체중"

print(f"판정: {result}")

# 📌 주요 포인트:
# 1. BMI 공식: 체중(kg) / 신장(m)²
# 2. cm를 m로 변환 (/100)
# 3. ** 연산자로 제곱
# 4. :.2f로 소수점 2자리까지 표시

# ⚠️ 자주 하는 실수:
# bmi = weight / height_cm ** 2  # ❌ cm 그대로 사용
# bmi = weight / height_m * 2  # ❌ * 대신 **
# if bmi >= 18.5:  # ❌ 높은 값부터 검사해야 함
#     result = "정상"
# elif bmi >= 25:
#     result = "과체중"

# 💡 팁:
# - 더 세분화: 비만(30 이상), 고도비만(35 이상)
# - 입력 검증: height > 0 and weight > 0

print()


# ============================================
# 문제 5: 주차 요금 계산 (시간별) - 해설
# ============================================
print("=" * 50)
print("문제 5: 주차 요금 계산")
print("=" * 50)

hours = 2

# ✅ 모범 답안
print(f"주차 시간: {hours}시간")

if hours <= 1:
    fee = 2000
elif hours <= 3:
    fee = 5000
else:
    fee = 10000

print(f"주차 요금: {fee:,}원")

# 📌 주요 포인트:
# 1. <= 사용으로 경계값 포함
# 2. 1시간 이하, 3시간 이하 순차 검사
# 3. else로 3시간 초과 처리

# ⚠️ 자주 하는 실수:
# if hours < 1:  # ❌ 1시간이 누락됨
# if hours > 3:  # ❌ 순서가 잘못됨 (먼저 검사하면 안됨)

# 💡 팁:
# - 실무: 30분 단위 계산
# - 일일 최대 요금 설정
# - 정기권 할인 적용

print()


# ============================================
# 문제 6: 영화 관람 등급 (나이별) - 해설
# ============================================
print("=" * 50)
print("문제 6: 영화 관람 등급")
print("=" * 50)

age = 17

# ✅ 모범 답안
print(f"나이: {age}세")

if age >= 19:
    print("관람 가능: 청소년 관람불가까지 가능합니다.")
elif age >= 15:
    print("관람 가능: 15세 이상 관람가까지 가능합니다.")
elif age >= 12:
    print("관람 가능: 12세 이상 관람가까지 가능합니다.")
else:
    print("관람 가능: 전체 관람가만 가능합니다.")

# 📌 주요 포인트:
# 1. 높은 나이부터 검사 (19 → 15 → 12)
# 2. 각 등급은 하위 등급 포함
# 3. 실무: 보호자 동반 조건 추가

# ⚠️ 자주 하는 실수:
# if age > 19:  # ❌ 19세가 누락됨
# if age >= 12:  # ❌ 먼저 검사하면 모든 나이가 12세 이상됨

# 💡 팁:
# - 국가별 등급 체계 다름
# - 실제로는 생년월일로 계산

print()


# ============================================
# 문제 7: 할인율 적용 (회원 등급별) - 해설
# ============================================
print("=" * 50)
print("문제 7: 할인율 적용")
print("=" * 50)

price = 100000
membership = "Gold"

# ✅ 모범 답안
print(f"상품 가격: {price:,}원")
print(f"회원 등급: {membership}")

if membership == "VIP":
    discount_rate = 0.20
    print("할인율: 20%")
elif membership == "Gold":
    discount_rate = 0.15
    print("할인율: 15%")
elif membership == "Silver":
    discount_rate = 0.10
    print("할인율: 10%")
else:
    discount_rate = 0
    print("할인율: 없음")

discount_amount = price * discount_rate
final_price = price - discount_amount

print(f"할인 금액: {discount_amount:,.0f}원")
print(f"최종 가격: {final_price:,.0f}원")

# 📌 주요 포인트:
# 1. 문자열 비교로 등급 확인
# 2. 할인율을 변수에 저장
# 3. 할인 금액과 최종 가격 별도 계산

# ⚠️ 자주 하는 실수:
# if membership == "gold":  # ❌ 대소문자 구분
# discount_amount = price * 0.15  # ❌ 하드코딩 (변수 사용 권장)
# final_price = price * 0.85  # ⚠️ 가능하지만 할인 금액 표시 안됨

# 💡 팁:
# - 딕셔너리 활용:
#   rates = {"VIP": 0.20, "Gold": 0.15, "Silver": 0.10}
#   discount_rate = rates.get(membership, 0)
# - 대소문자 무시: membership.upper()

print()


# ============================================
# 문제 8: 시험 결과 종합 판정 - 해설
# ============================================
print("=" * 50)
print("문제 8: 시험 결과 종합 판정")
print("=" * 50)

score = 92

# ✅ 모범 답안
print(f"점수: {score}점")

if score >= 90:
    grade = "A"
    message = "매우 우수합니다!"
elif score >= 80:
    grade = "B"
    message = "우수합니다!"
elif score >= 70:
    grade = "C"
    message = "보통입니다."
elif score >= 60:
    grade = "D"
    message = "노력이 필요합니다."
else:
    grade = "F"
    message = "재시험을 보세요."

print(f"등급: {grade}")
print(f"평가: {message}")

# 📌 주요 포인트:
# 1. 각 조건마다 여러 변수 설정 가능
# 2. 등급과 메시지를 함께 관리
# 3. 사용자 친화적인 피드백 제공

# ⚠️ 자주 하는 실수:
# message = "매우 우수합니다!"  # ❌ 들여쓰기 밖에 있으면 항상 실행
# if score >= 90:
#     grade = "A"

# 💡 팁:
# - 튜플로 묶기:
#   if score >= 90:
#       grade, message = "A", "매우 우수합니다!"
# - 함수로 분리:
#   def get_grade(score):
#       ...

print()


# ============================================
# 🎯 핵심 정리
# ============================================
print("=" * 50)
print("🎯 세션 3 핵심 정리")
print("=" * 50)

print("""
1. if-elif-else 기본 구조
   if 조건1:
       코드1
   elif 조건2:
       코드2
   elif 조건3:
       코드3
   else:
       코드4

2. 순차 검사 원리
   - 위에서부터 순차적으로 확인
   - 참인 조건을 만나면 해당 블록만 실행 후 종료
   - 나머지 elif, else는 건너뜀

3. 조건 순서의 중요성
   ✅ 높은 값부터: if score >= 90, elif score >= 80, ...
   ❌ 낮은 값부터: if score >= 60 (모든 점수가 걸림)

4. in 연산자 활용
   if month in [12, 1, 2]:  # 여러 값 동시 확인
   if grade in ["A", "B"]:  # 문자열도 가능

5. 실무 활용 사례
   - 등급 시스템 (성적, 회원 등급)
   - 요금 계산 (배송비, 주차 요금)
   - 분류 작업 (계절, 연령대)

6. 자주 하는 실수
   ❌ 조건 순서 잘못 (낮은 값부터 검사)
   ❌ else if 사용 (elif 사용해야 함)
   ❌ 범위 중복 (조건이 겹침)

7. 최적화 팁
   - 가장 자주 발생하는 조건을 위에 배치
   - 딕셔너리로 대체 가능한지 검토
   - 너무 많은 elif는 함수나 클래스로 분리

8. 코드 개선 예시
   # 기본
   if grade == "A":
       return 4.5
   elif grade == "B":
       return 3.5

   # 딕셔너리 활용
   grades = {"A": 4.5, "B": 3.5, "C": 2.5}
   return grades.get(grade, 0)
""")

print("=" * 50)
print("✅ 해설 완료!")
print("=" * 50)
