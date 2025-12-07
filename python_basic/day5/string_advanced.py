"""
파일명: string_advanced.py
목적: 고객 데이터 정제 및 분석 시스템 (문자열 메서드 심화 실습)
"""

# 더러운 고객 데이터
customers = [
    {
        "name": "  kim CHUL-soo  ",
        "email": "  KIM@GMAIL.COM  ",
        "phone": "01012345678",
        "address": "서울특별시 강남구 테헤란로 123"
    },
    {
        "name": "LEE young hee",
        "email": "lee@NAVER.com",
        "phone": "010 9876 5432",
        "address": "부산광역시 해운대구 센텀로 456"
    },
    {
        "name": "park min su  ",
        "email": "  PARK@daum.NET  ",
        "phone": "010-5555-6666",
        "address": "대구광역시 중구 동성로 789"
    },
    {
        "name": "  CHOI ji hun",
        "email": "choi@GOOGLE.com  ",
        "phone": "010.7777.8888",
        "address": "인천광역시 남동구 논현로 321"
    }
]

print("=" * 60)
print("고객 데이터 정제 시스템".center(60))
print("=" * 60)

# 1단계: 데이터 정제
print("\n[1단계] 데이터 정제")
print("-" * 60)

for customer in customers:
    # 이름 정제: 공백 제거 + Title Case
    customer["name"] = customer["name"].strip().title()

    # 이메일 정제: 공백 제거 + 소문자
    customer["email"] = customer["email"].strip().lower()

    # 전화번호 정제: 하이픈 형식으로 통일
    phone = customer["phone"].replace("-", "").replace(" ", "").replace(".", "")
    customer["phone"] = f"{phone[:3]}-{phone[3:7]}-{phone[7:]}"

    # 주소에서 도시명 추출
    address_parts = customer["address"].split()
    customer["city"] = address_parts[0] if address_parts else "알 수 없음"

print("✓ 데이터 정제 완료!")

# 2단계: 정제된 데이터 출력
print("\n[2단계] 정제된 고객 데이터")
print("-" * 60)

for i, customer in enumerate(customers, 1):
    print(f"\n고객 {i}:")
    print(f"  이름: {customer['name']}")
    print(f"  이메일: {customer['email']}")
    print(f"  전화번호: {customer['phone']}")
    print(f"  도시: {customer['city']}")

# 3단계: 이메일 도메인 분석
print("\n[3단계] 이메일 도메인 분석")
print("-" * 60)

# 도메인별 집계
domain_count = {}

for customer in customers:
    email = customer["email"]
    # @ 기준으로 분리
    if "@" in email:
        domain = email.split("@")[1]

        if domain in domain_count:
            domain_count[domain] += 1
        else:
            domain_count[domain] = 1

print("도메인별 고객 수:")
for domain, count in sorted(domain_count.items()):
    print(f"  {domain}: {count}명")

# 4단계: 도시별 고객 분포
print("\n[4단계] 도시별 고객 분포")
print("-" * 60)

city_count = {}

for customer in customers:
    city = customer["city"]
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1

print("도시별 고객 수:")
for city, count in sorted(city_count.items()):
    print(f"  {city}: {count}명")

# 5단계: 이름 검색 기능
print("\n[5단계] 고객 검색")
print("-" * 60)

search_keyword = input("검색할 이름 (일부만 입력 가능): ").strip()

print(f"\n'{search_keyword}' 검색 결과:")
found = False

for customer in customers:
    # 대소문자 구분 없이 검색
    if search_keyword.lower() in customer["name"].lower():
        print(f"  - {customer['name']} ({customer['email']})")
        found = True

if not found:
    print("  검색 결과가 없습니다.")

# 6단계: 전화번호 마스킹 (개인정보 보호)
print("\n[6단계] 개인정보 보호 (전화번호 마스킹)")
print("-" * 60)

print(f"{'이름':<20} {'마스킹된 전화번호':<20}")
print("-" * 40)

for customer in customers:
    phone = customer["phone"]
    # 중간 4자리 마스킹
    masked_phone = phone[:4] + "****" + phone[8:]
    print(f"{customer['name']:<20} {masked_phone:<20}")

# 7단계: 이메일 검증
print("\n[7단계] 이메일 유효성 검사")
print("-" * 60)

test_emails = [
    "valid@example.com",
    "invalid-email",
    "no-at-sign.com",
    "  test@test.com  ",
    "@nouser.com",
    "user@"
]

print(f"{'이메일':<25} {'유효성':<10}")
print("-" * 35)

for email in test_emails:
    email = email.strip()

    # 간단한 검증
    is_valid = (
        email and
        "@" in email and
        email.count("@") == 1 and
        "." in email.split("@")[1] and
        not email.startswith("@") and
        not email.endswith("@")
    )

    status = "✓ 유효" if is_valid else "✗ 무효"
    print(f"{email:<25} {status:<10}")

# 8단계: 이름 이니셜 생성
print("\n[8단계] 고객 이니셜 생성")
print("-" * 60)

for customer in customers:
    name = customer["name"]
    # 공백으로 분리
    parts = name.split()

    # 각 단어의 첫 글자
    initials = "".join(word[0].upper() for word in parts if word)

    print(f"{name:<20} → {initials}")

# 9단계: 문자열 포맷팅 활용
print("\n[9단계] 고객 명함 생성")
print("-" * 60)

for i, customer in enumerate(customers, 1):
    print(f"\n╔{'═' * 38}╗")
    print(f"║ {customer['name'].center(36)} ║")
    print(f"║ {'─' * 36} ║")
    print(f"║ 📧 {customer['email']:<32} ║")
    print(f"║ 📱 {customer['phone']:<32} ║")
    print(f"║ 🏠 {customer['city']:<32} ║")
    print(f"╚{'═' * 38}╝")

# 10단계: 통계 요약
print("\n[10단계] 데이터 통계 요약")
print("=" * 60)

total_customers = len(customers)
total_domains = len(domain_count)
total_cities = len(city_count)

# 가장 많은 도메인
most_common_domain = max(domain_count, key=domain_count.get)
# 가장 많은 도시
most_common_city = max(city_count, key=city_count.get)

print(f"총 고객 수: {total_customers}명")
print(f"사용 중인 이메일 도메인: {total_domains}개")
print(f"고객 분포 도시: {total_cities}개")
print(f"가장 많은 도메인: {most_common_domain} ({domain_count[most_common_domain]}명)")
print(f"가장 많은 도시: {most_common_city} ({city_count[most_common_city]}명)")

print("\n" + "=" * 60)
print("시스템 종료".center(60))
print("=" * 60)
