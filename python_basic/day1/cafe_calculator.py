"""
파일명: cafe_calculator.py
목적: 카페 주문 금액 계산 및 할인 적용 (숫자형 자료형 실습)
"""

# 메뉴 가격 (단위: 원)
americano_price = 4500
latte_price = 5000
cake_price = 6500

# 주문 수량
americano_qty = 2
latte_qty = 1
cake_qty = 1

# 메뉴별 금액 계산
americano_total = americano_price * americano_qty
latte_total = latte_price * latte_qty
cake_total = cake_price * cake_qty

# 소계 계산
subtotal = americano_total + latte_total + cake_total

# 할인 계산 (10%)
discount_rate = 0.1
discount_amount = subtotal * discount_rate

# 최종 금액
final_price = subtotal - discount_amount

# 결과 출력
print("===== 카페 주문 계산 =====")
print(f"아메리카노 {americano_qty}잔: {americano_total:,}원")
print(f"카페라떼 {latte_qty}잔: {latte_total:,}원")
print(f"케이크 {cake_qty}조각: {cake_total:,}원")
print("-" * 23)
print(f"소계: {subtotal:,}원")
print(f"할인(10%): -{discount_amount:,.0f}원")
print("-" * 23)
print(f"최종 금액: {final_price:,.0f}원")
print("=" * 24)

# 추가 기능: 할인율 변경해보기
print("\n" + "=" * 30)
print("VIP 고객 할인 (20%)")
print("=" * 30)

vip_discount_rate = 0.2
vip_discount_amount = subtotal * vip_discount_rate
vip_final_price = subtotal - vip_discount_amount

print("===== 카페 주문 계산 =====")
print(f"아메리카노 {americano_qty}잔: {americano_total:,}원")
print(f"카페라떼 {latte_qty}잔: {latte_total:,}원")
print(f"케이크 {cake_qty}조각: {cake_total:,}원")
print("-" * 23)
print(f"소계: {subtotal:,}원")
print(f"VIP 할인(20%): -{vip_discount_amount:,.0f}원")
print("-" * 23)
print(f"최종 금액: {vip_final_price:,.0f}원")
print("=" * 24)

# 절약 금액 표시
saved_amount = discount_amount
vip_saved_amount = vip_discount_amount
print(f"\n일반 할인으로 {saved_amount:,.0f}원 절약!")
print(f"VIP 할인으로 {vip_saved_amount:,.0f}원 절약!")
print(f"VIP는 {vip_saved_amount - saved_amount:,.0f}원 더 절약!")
