"""
파일명: for_basic.py
목적: 상품 재고 관리 시스템 (for 문 기초 실습)
"""

# 상품 리스트 (딕셔너리 리스트)
products = [
    {"name": "키보드", "stock": 15, "price": 45000},
    {"name": "마우스", "stock": 3, "price": 25000},
    {"name": "모니터", "stock": 8, "price": 350000},
    {"name": "헤드셋", "stock": 12, "price": 80000},
    {"name": "웹캠", "stock": 4, "price": 120000}
]

print("===== 재고 현황 =====")

# 총 재고 가치 계산
total_value = 0

# 모든 상품 정보 출력
for product in products:
    name = product["name"]
    stock = product["stock"]
    price = product["price"]
    value = stock * price

    print(f"{name}: {stock}개, 단가 {price:,}원, 재고가치 {value:,}원")
    total_value += value

print("-" * 20)
print(f"총 재고 가치: {total_value:,}원")
print("-" * 20)

# 재고 부족 상품 찾기 (재고 5개 미만)
print("재고 부족 상품:")
low_stock_products = []

for product in products:
    if product["stock"] < 5:
        low_stock_products.append(product)
        print(f"- {product['name']} ({product['stock']}개)")

if not low_stock_products:
    print("없음")

print("=" * 19)

# 추가 기능: 재고 보충 필요 수량
print("\n===== 재고 보충 계획 =====")
target_stock = 10  # 목표 재고

for product in products:
    if product["stock"] < target_stock:
        needed = target_stock - product["stock"]
        cost = needed * product["price"]
        print(f"{product['name']}: {needed}개 필요 (비용: {cost:,}원)")

# 추가 기능: 가장 비싼 상품
print("\n===== 고가 상품 TOP 3 =====")
sorted_products = sorted(products, key=lambda x: x["price"], reverse=True)

for i, product in enumerate(sorted_products[:3], 1):
    print(f"{i}. {product['name']}: {product['price']:,}원")

# 추가 기능: 통계
print("\n===== 재고 통계 =====")
total_items = sum(p["stock"] for p in products)
avg_stock = total_items / len(products)
max_stock_product = max(products, key=lambda x: x["stock"])
min_stock_product = min(products, key=lambda x: x["stock"])

print(f"총 재고 수량: {total_items}개")
print(f"평균 재고: {avg_stock:.1f}개")
print(f"최다 재고: {max_stock_product['name']} ({max_stock_product['stock']}개)")
print(f"최소 재고: {min_stock_product['name']} ({min_stock_product['stock']}개)")
