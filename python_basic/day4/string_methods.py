"""
파일명: string_methods.py
목적: 데이터 정제 프로그램 (문자열 메서드 실습)
"""

# 더러운 데이터 (실제 CSV에서 가져온 것처럼)
raw_data = [
    "  kim@GMAIL.COM  ",
    "PARK@naver.com",
    "  lee@DAUM.net  ",
    "choi@GOOGLE.COM  ",
    "  JUNG@kakao.com"
]

print("===== 이메일 정제 =====")
print("원본 데이터:")
for email in raw_data:
    print(f"'{email}'")

print("\n정제 후:")
cleaned_emails = []

for email in raw_data:
    # 1. 공백 제거
    email = email.strip()
    # 2. 소문자로 통일
    email = email.lower()
    cleaned_emails.append(email)
    print(email)

print("-" * 30)

# 추가 기능: 도메인별 분류
print("\n===== 도메인별 분류 =====")
domains = {}

for email in cleaned_emails:
    # @ 기준으로 분리
    username, domain = email.split("@")

    # 도메인별 카운트
    if domain in domains:
        domains[domain] += 1
    else:
        domains[domain] = 1

for domain, count in domains.items():
    print(f"{domain}: {count}명")

# 추가 기능: 전화번호 형식 통일
print("\n===== 전화번호 정제 =====")
phone_numbers = [
    "010-1234-5678",
    "01012345678",
    "010 1234 5678",
    "010.1234.5678"
]

print("원본:")
for phone in phone_numbers:
    print(phone)

print("\n정제 후 (하이픈 형식):")
for phone in phone_numbers:
    # 모든 구분자 제거
    clean_phone = phone.replace("-", "").replace(" ", "").replace(".", "")

    # 하이픈 형식으로 변환
    formatted = f"{clean_phone[:3]}-{clean_phone[3:7]}-{clean_phone[7:]}"
    print(formatted)

print("-" * 30)

# 추가 기능: 이름 데이터 정제
print("\n===== 이름 데이터 정제 =====")
names = [
    "  김철수  ",
    "LEE YOUNG HEE",
    "park min su",
    "  CHOI JI HUN  "
]

print("원본 → 정제")
for name in names:
    # 공백 제거 및 제목 형식 (Title Case)
    cleaned = name.strip().title()
    print(f"'{name}' → '{cleaned}'")

# 추가 기능: 텍스트 검색
print("\n===== 텍스트 검색 =====")
text = "Python은 배우기 쉽고 강력한 프로그래밍 언어입니다. Python으로 웹, 데이터 분석, AI를 할 수 있습니다."

print(f"원문: {text}\n")

# 검색어
keyword = "Python"
count = text.count(keyword)
print(f"'{keyword}' 등장 횟수: {count}번")

# 첫 번째 위치
first_pos = text.find(keyword)
print(f"첫 번째 위치: {first_pos}번째 문자")

# 시작 여부
starts = text.startswith("Python")
print(f"'Python'으로 시작: {starts}")

# 종료 여부
ends = text.endswith("습니다.")
print(f"'습니다.'로 끝남: {ends}")

print("-" * 30)

# 추가 기능: 문자열 치환
print("\n===== 금지어 필터링 =====")
comment = "이 제품은 정말 쓰레기입니다. 완전 최악이에요."

print(f"원문: {comment}")

# 금지어 목록
banned_words = ["쓰레기", "최악"]

filtered = comment
for word in banned_words:
    filtered = filtered.replace(word, "***")

print(f"필터링: {filtered}")

# 추가 기능: CSV 파싱
print("\n===== CSV 데이터 파싱 =====")
csv_line = "김철수,28,서울,개발자"

print(f"CSV: {csv_line}")

# 콤마로 분리
parts = csv_line.split(",")

print("\n파싱 결과:")
print(f"이름: {parts[0]}")
print(f"나이: {parts[1]}세")
print(f"지역: {parts[2]}")
print(f"직업: {parts[3]}")

# 다시 결합
new_csv = " | ".join(parts)
print(f"\n새 형식: {new_csv}")

# 추가 기능: 파일명 정제
print("\n===== 파일명 정제 =====")
filenames = [
    "문서 (1).txt",
    "보고서_최종_진짜최종.docx",
    "사진 - 복사본.jpg",
    "데이터(수정)(2).xlsx"
]

print("원본 → 정제")
for filename in filenames:
    # 괄호와 내용물 제거, 공백을 언더스코어로
    cleaned = filename

    # 불필요한 패턴 제거
    patterns = [" (1)", "_최종_진짜최종", " - 복사본", "(수정)(2)"]
    for pattern in patterns:
        cleaned = cleaned.replace(pattern, "")

    # 공백을 언더스코어로
    cleaned = cleaned.replace(" ", "_")

    print(f"{filename} → {cleaned}")

# 추가 기능: URL 파싱
print("\n===== URL 파싱 =====")
url = "https://www.example.com/products/12345?color=red&size=large"

print(f"URL: {url}")

# 프로토콜 확인
if url.startswith("https://"):
    print("보안 연결 (HTTPS)")
elif url.startswith("http://"):
    print("일반 연결 (HTTP)")

# 도메인 추출
domain_start = url.find("//") + 2
domain_end = url.find("/", domain_start)
domain = url[domain_start:domain_end]
print(f"도메인: {domain}")

# 쿼리 파라미터
if "?" in url:
    query_start = url.find("?") + 1
    query = url[query_start:]
    print(f"쿼리: {query}")

    # 파라미터 분리
    params = query.split("&")
    print("\n파라미터:")
    for param in params:
        key, value = param.split("=")
        print(f"  {key}: {value}")

# 추가 기능: 태그 제거 (간단한 HTML)
print("\n===== HTML 태그 제거 =====")
html = "<h1>제목</h1><p>이것은 <strong>중요한</strong> 내용입니다.</p>"

print(f"HTML: {html}")

# 간단한 태그 제거 (실제로는 BeautifulSoup 사용 권장)
text_only = html
while "<" in text_only and ">" in text_only:
    start = text_only.find("<")
    end = text_only.find(">", start)
    if end != -1:
        text_only = text_only[:start] + text_only[end+1:]
    else:
        break

print(f"텍스트만: {text_only}")

# 추가 기능: 대소문자 변환 활용
print("\n===== 대소문자 검사 =====")
passwords = ["Password123", "password", "PASSWORD", "Pass123!"]

print("비밀번호 강도 검사:")
for pwd in passwords:
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)

    strength = 0
    if has_upper:
        strength += 1
    if has_lower:
        strength += 1
    if has_digit:
        strength += 1

    if strength == 3:
        level = "강함"
    elif strength == 2:
        level = "보통"
    else:
        level = "약함"

    print(f"{pwd}: {level} (대문자:{has_upper}, 소문자:{has_lower}, 숫자:{has_digit})")

print("=" * 30)
