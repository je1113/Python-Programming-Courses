"""
파일명: business_card.py
목적: 명함 정보를 화면에 출력 (print 함수 실습)
"""

# 명함 너비 설정
width = 36

# 상단 구분선
print("=" * width)

# 제목 (가운데 정렬)
print(f"{'명  함':^{width}}")

# 구분선
print("=" * width)

# 개인 정보
print("이름: 김파이썬")
print("직책: 데이터 분석가")
print("회사: 파이썬 주식회사")

# 중간 구분선
print("-" * width)

# 연락처 정보
print("연락처: 010-1234-5678")
print("이메일: python@example.com")
print("주소: 서울시 강남구 테헤란로 123")

# 하단 구분선
print("=" * width)

# 더 나은 방법: 변수 사용
print("\n" + "=" * 50)
print("변수를 사용한 버전:")
print("=" * 50)

name = "김파이썬"
position = "데이터 분석가"
company = "파이썬 주식회사"
phone = "010-1234-5678"
email = "python@example.com"
address = "서울시 강남구 테헤란로 123"

print("=" * width)
print(f"{'명  함':^{width}}")
print("=" * width)
print(f"이름: {name}")
print(f"직책: {position}")
print(f"회사: {company}")
print("-" * width)
print(f"연락처: {phone}")
print(f"이메일: {email}")
print(f"주소: {address}")
print("=" * width)
