"""
파일명: user_input.py
목적: 간단한 쇼핑몰 주문 시스템 (input 함수 실습)
"""

print("===== 쇼핑몰 주문 =====")

# 고객 정보 입력
customer_name = input("고객명: ")
product_name = input("상품명: ")
quantity = input("수량: ")
unit_price = input("단가: ")

# 숫자 타입 변환
quantity = int(quantity)
unit_price = int(unit_price)

# 배송비 (고정)
delivery_fee = 3000

# 금액 계산
product_total = unit_price * quantity
final_total = product_total + delivery_fee

# 주문서 출력
print("-" * 20)
print(f"상품명: {product_name}")
print(f"수량: {quantity}개")
print(f"단가: {unit_price:,}원")
print(f"상품 금액: {product_total:,}원")
print(f"배송비: {delivery_fee:,}원")
print("-" * 20)
print(f"총 결제 금액: {final_total:,}원")
print("=" * 20)
print(f"감사합니다, {customer_name}님!")

# 추가 기능: 적립 포인트 (구매 금액의 1%)
points = int(product_total * 0.01)
print(f"적립 예정 포인트: {points:,}P")

# 추가 기능: 배송 예정일 (3일 후)
from datetime import datetime, timedelta

today = datetime.now()
delivery_date = today + timedelta(days=3)

print(f"\n[배송 정보]")
print(f"주문일: {today.strftime('%Y년 %m월 %d일')}")
print(f"배송 예정일: {delivery_date.strftime('%Y년 %m월 %d일')}")

# 추가 기능: 주문 확인 메시지
print(f"\n{customer_name}님의 주문이 접수되었습니다.")
print(f"주문 상품: {product_name} {quantity}개")
print(f"결제 금액: {final_total:,}원")
