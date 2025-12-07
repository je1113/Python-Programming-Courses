"""
파일명: order_summary.py
목적: 온라인 쇼핑몰 주문서 출력 (변수와 변수명 규칙 실습)
"""

# 고객 정보
customer_name = "김파이썬"

# 상품 정보
product_name = "무선 키보드"
product_price = 45000  # 단위: 원
quantity = 2           # 단위: 개

# 배송 정보
delivery_fee = 3000    # 단위: 원

# 총 금액 계산
subtotal = product_price * quantity  # 소계
total_price = subtotal + delivery_fee  # 총액

# 주문서 출력
print("====== 주문 내역 ======")
print(f"고객명: {customer_name}")
print(f"상품명: {product_name}")
print(f"단가: {product_price:,}원")
print(f"수량: {quantity}개")
print(f"배송비: {delivery_fee:,}원")
print("-" * 20)
print(f"총 금액: {total_price:,}원")
print("=" * 20)

# 추가: 상세 내역 포함
print("\n" + "=" * 30)
print("상세 주문 내역")
print("=" * 30)
print(f"고객명: {customer_name}")
print(f"상품명: {product_name}")
print(f"단가: {product_price:,}원")
print(f"수량: {quantity}개")
print(f"상품 금액: {subtotal:,}원")
print(f"배송비: {delivery_fee:,}원")
print("-" * 30)
print(f"총 결제 금액: {total_price:,}원")
print("=" * 30)
print(f"\n{customer_name}님, 주문해주셔서 감사합니다!")
print("빠른 시일 내에 배송해드리겠습니다.")
