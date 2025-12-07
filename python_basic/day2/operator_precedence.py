"""
파일명: operator_precedence.py
목적: 할인 계산기 (연산자 우선순위 실습)
"""

print("===== 할인 계산기 =====")

# 사용자 입력
price = int(input("상품 가격: "))
quantity = int(input("수량: "))
is_member = input("회원 여부 (Y/N): ").upper() == "Y"
has_coupon = input("쿠폰 여부 (Y/N): ").upper() == "Y"

# 상품 금액
product_total = price * quantity

print("-" * 21)
print(f"상품 금액: {product_total:,}원")

# 할인 적용 (순차적으로)
current_price = product_total

# 1. 기본 할인 (10만원 이상 구매 시 5%)
basic_discount = 0
if current_price >= 100000:
    basic_discount = current_price * 0.05
    current_price = current_price - basic_discount

if basic_discount > 0:
    print(f"기본 할인 (5%): -{basic_discount:,.0f}원")
else:
    print("기본 할인 (5%): 해당 없음")

# 2. 회원 할인 (추가 10%)
member_discount = 0
if is_member:
    member_discount = current_price * 0.1
    current_price = current_price - member_discount

if member_discount > 0:
    print(f"회원 할인 (10%): -{member_discount:,.0f}원")
else:
    print("회원 할인 (10%): 해당 없음")

# 3. 쿠폰 할인 (5,000원 차감)
coupon_discount = 0
if has_coupon:
    coupon_discount = 5000
    current_price = current_price - coupon_discount

if coupon_discount > 0:
    print(f"쿠폰 할인: -{coupon_discount:,}원")
else:
    print("쿠폰 할인: 해당 없음")

# 최종 금액
final_price = current_price

# 총 할인액
total_discount = product_total - final_price
discount_rate = (total_discount / product_total) * 100

print("-" * 21)
print(f"최종 금액: {final_price:,.0f}원")
print("=" * 22)

# 할인 요약
print(f"\n[할인 요약]")
print(f"총 할인액: {total_discount:,.0f}원")
print(f"할인율: {discount_rate:.1f}%")
print(f"절약 금액: {total_discount:,.0f}원")

# 추가: 복잡한 연산자 우선순위 예시
print("\n===== 연산자 우선순위 예시 =====")

# 예시 1: 산술 + 비교
result1 = 5 + 3 * 2 > 10
print(f"5 + 3 * 2 > 10 = {result1}")
print("계산: (5 + (3 * 2)) > 10 = 11 > 10 = True")

# 예시 2: 비교 + 논리
age = 25
score = 85
result2 = age >= 18 and score >= 80
print(f"\nage >= 18 and score >= 80 = {result2}")
print(f"계산: ({age} >= 18) and ({score} >= 80) = True and True = True")

# 예시 3: 복합 조건
price_check = product_total >= 100000
member_check = is_member
result3 = price_check and member_check or has_coupon
print(f"\nprice >= 100000 and is_member or has_coupon = {result3}")
print(f"계산: ({price_check} and {member_check}) or {has_coupon}")
print(f"     = {price_check and member_check} or {has_coupon} = {result3}")

# 괄호의 중요성
print("\n===== 괄호의 중요성 =====")
a, b, c = 2, 3, 4

# 괄호 없이
result_no_paren = a + b * c
print(f"a + b * c = {result_no_paren}")
print(f"계산: 2 + (3 * 4) = 2 + 12 = 14")

# 괄호 있음
result_with_paren = (a + b) * c
print(f"\n(a + b) * c = {result_with_paren}")
print(f"계산: (2 + 3) * 4 = 5 * 4 = 20")

# 추가: 할인 적용 순서에 따른 차이
print("\n===== 할인 순서의 중요성 =====")

# 원래 방식: 기본 → 회원 → 쿠폰
method1 = product_total
if method1 >= 100000:
    method1 *= 0.95
if is_member:
    method1 *= 0.9
if has_coupon:
    method1 -= 5000

# 다른 순서: 쿠폰 → 기본 → 회원
method2 = product_total
if has_coupon:
    method2 -= 5000
if method2 >= 100000:
    method2 *= 0.95
if is_member:
    method2 *= 0.9

print(f"방식 1 (기본→회원→쿠폰): {method1:,.0f}원")
print(f"방식 2 (쿠폰→기본→회원): {method2:,.0f}원")
print(f"차이: {abs(method1 - method2):,.0f}원")
