"""
파일명: ternary_practice.py
목적: 배송비 계산기 (삼항 연산자 실습)
"""

print("===== 배송비 계산기 =====")

# 사용자 입력
order_amount = int(input("주문 금액: "))
is_member = input("회원 여부 (Y/N): ").upper() == "Y"

# 배송비 계산 (삼항 연산자 사용)
# 3만원 이상: 무료, 3만원 미만: 3,000원
delivery_fee = 0 if order_amount >= 30000 else 3000

# 포인트 적립 (삼항 연산자 사용)
# 회원: 5%, 비회원: 0%
point_rate = 0.05 if is_member else 0
points = int(order_amount * point_rate)

# 총 결제 금액
total_amount = order_amount + delivery_fee

# 결과 출력
print("-" * 22)
print(f"주문 금액: {order_amount:,}원")
print(f"배송비: {delivery_fee:,}원")
print("-" * 22)
print(f"총 결제 금액: {total_amount:,}원")
print(f"적립 포인트: {points:,}P")
print("=" * 22)

# 추가 정보 (삼항 연산자 활용)
membership_status = "회원" if is_member else "비회원"
free_shipping_msg = "무료 배송" if delivery_fee == 0 else f"배송비 {delivery_fee:,}원"

print(f"\n[주문 정보]")
print(f"회원 구분: {membership_status}")
print(f"배송: {free_shipping_msg}")

# 추가: 다양한 삼항 연산자 예시
print("\n===== 삼항 연산자 활용 예시 =====")

# 1. 등급 판정
grade = "VIP" if order_amount >= 100000 else "일반"
print(f"고객 등급: {grade}")

# 2. 할인 메시지
discount_msg = "할인 대상" if is_member and order_amount >= 50000 else "할인 없음"
print(f"할인: {discount_msg}")

# 3. 배송 방식
shipping_method = "빠른 배송" if order_amount >= 50000 else "일반 배송"
print(f"배송 방식: {shipping_method}")

# 4. 사은품 제공
gift = "사은품 제공" if order_amount >= 100000 else "사은품 없음"
print(f"사은품: {gift}")

# 5. 무료 배송까지 남은 금액
remaining = 30000 - order_amount if order_amount < 30000 else 0
remaining_msg = f"{remaining:,}원 더 구매 시 무료 배송" if remaining > 0 else "무료 배송 달성!"
print(f"\n{remaining_msg}")

# 추가: 여러 조건 처리
print("\n===== 복합 조건 처리 =====")

# VIP 조건: 회원이면서 10만원 이상 구매
is_vip = True if (is_member and order_amount >= 100000) else False
vip_benefit = "추가 5% 할인" if is_vip else "해당 없음"
print(f"VIP 여부: {'VIP' if is_vip else '일반'}")
print(f"VIP 혜택: {vip_benefit}")

# 긴급 배송 가능 여부: 주문 금액 5만원 이상
express_available = order_amount >= 50000
express_fee = 5000 if express_available else 0
express_msg = f"가능 (추가 {express_fee:,}원)" if express_available else "불가능"
print(f"긴급 배송: {express_msg}")

# 추가: 최종 혜택 요약
print("\n===== 최종 혜택 요약 =====")

# 혜택 계산
total_benefits = 0

# 배송비 절약
if delivery_fee == 0:
    saved_delivery = 3000
    total_benefits += saved_delivery
    print(f"✓ 배송비 절약: {saved_delivery:,}원")

# 포인트 적립
if points > 0:
    total_benefits += points
    print(f"✓ 포인트 적립: {points:,}P")

# VIP 할인
if is_vip:
    vip_discount = int(order_amount * 0.05)
    total_benefits += vip_discount
    print(f"✓ VIP 할인: {vip_discount:,}원")

# 총 혜택
benefit_summary = f"총 {total_benefits:,}원 상당의 혜택" if total_benefits > 0 else "혜택 없음"
print(f"\n{benefit_summary}")

# 추가: 다음 등급까지
print("\n===== 다음 등급 안내 =====")

if order_amount < 50000:
    next_grade = "우수"
    needed = 50000 - order_amount
    print(f"{next_grade} 등급까지 {needed:,}원 남았습니다")
elif order_amount < 100000:
    next_grade = "VIP"
    needed = 100000 - order_amount
    print(f"{next_grade} 등급까지 {needed:,}원 남았습니다")
else:
    print("최고 등급입니다! 🎉")

# 추가: 권장 메시지 (삼항 연산자 활용)
recommendation = (
    f"{30000 - order_amount:,}원 더 구매하시면 무료 배송입니다!"
    if 0 < order_amount < 30000
    else "무료 배송 적용 중입니다!"
    if delivery_fee == 0
    else "쇼핑을 시작해보세요!"
)
print(f"\n💡 {recommendation}")
