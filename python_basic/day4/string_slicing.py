"""
파일명: string_slicing.py
목적: 개인정보 처리 프로그램 (문자열 슬라이싱 실습)
"""

print("===== 주민등록번호 처리 =====")

# 주민등록번호
ssn = "901225-1234567"

print(f"원본: {ssn}")
print("-" * 30)

# 생년월일 추출
year = ssn[0:2]
month = ssn[2:4]
day = ssn[4:6]

print(f"생년월일: {year}년 {month}월 {day}일")

# 성별 코드
gender_code = ssn[7]
if gender_code in "13":
    gender = "남성"
else:
    gender = "여성"

print(f"성별: {gender}")

# 마스킹 (뒷자리 숨기기)
masked_ssn = ssn[:8] + "*" * 6
print(f"마스킹: {masked_ssn}")

print("=" * 30)

# 추가 기능: 전화번호 처리
print("\n===== 전화번호 처리 =====")
phone = "010-1234-5678"

print(f"원본: {phone}")

# 지역번호/통신사 코드
area_code = phone[0:3]
print(f"통신사: {area_code}")

# 중간번호
middle = phone[4:8]
print(f"중간번호: {middle}")

# 뒷번호
last = phone[9:13]
print(f"뒷번호: {last}")

# 마스킹 (중간 4자리)
masked_phone = phone[:4] + "****" + phone[8:]
print(f"마스킹: {masked_phone}")

print("-" * 30)

# 추가 기능: 이메일 처리
print("\n===== 이메일 처리 =====")
email = "user1234@example.com"

print(f"원본: {email}")

# @ 위치 찾기
at_pos = email.find("@")

# 사용자명과 도메인 분리
username = email[:at_pos]
domain = email[at_pos+1:]

print(f"사용자명: {username}")
print(f"도메인: {domain}")

# 도메인명과 확장자 분리
dot_pos = domain.find(".")
domain_name = domain[:dot_pos]
extension = domain[dot_pos+1:]

print(f"도메인명: {domain_name}")
print(f"확장자: {extension}")

# 사용자명 마스킹 (앞 2자만 보임)
if len(username) > 2:
    masked_email = username[:2] + "*" * (len(username) - 2) + "@" + domain
else:
    masked_email = "*" * len(username) + "@" + domain

print(f"마스킹: {masked_email}")

# 추가 기능: 카드번호 처리
print("\n===== 카드번호 처리 =====")
card = "1234-5678-9012-3456"

print(f"원본: {card}")

# 카드사 코드 (첫 4자리)
issuer = card[0:4]
print(f"카드사 코드: {issuer}")

# 마스킹 (중간 8자리)
masked_card = card[:5] + "****-****" + card[14:]
print(f"마스킹: {masked_card}")

# 마지막 4자리만
last_four = card[-4:]
print(f"끝자리: **** **** **** {last_four}")

print("-" * 30)

# 추가 기능: URL 슬라이싱
print("\n===== URL 파싱 =====")
url = "https://www.example.com/products/12345"

print(f"URL: {url}")

# 프로토콜
protocol = url[:5]  # "https"
print(f"프로토콜: {protocol}")

# 도메인 (// 다음부터 / 전까지)
domain_start = url.find("//") + 2
domain_end = url.find("/", domain_start)
domain = url[domain_start:domain_end]
print(f"도메인: {domain}")

# 경로
path = url[domain_end:]
print(f"경로: {path}")

# 마지막 세그먼트 (상품 ID)
last_slash = url.rfind("/")
product_id = url[last_slash+1:]
print(f"상품 ID: {product_id}")

# 추가 기능: 파일 경로 처리
print("\n===== 파일 경로 처리 =====")
filepath = "/home/user/documents/report.pdf"

print(f"경로: {filepath}")

# 파일명 추출
last_slash = filepath.rfind("/")
filename = filepath[last_slash+1:]
print(f"파일명: {filename}")

# 디렉토리 경로
directory = filepath[:last_slash]
print(f"디렉토리: {directory}")

# 확장자
dot_pos = filename.rfind(".")
name = filename[:dot_pos]
ext = filename[dot_pos+1:]
print(f"이름: {name}")
print(f"확장자: {ext}")

# 추가 기능: 문자열 역순
print("\n===== 문자열 뒤집기 =====")
text = "Python"

print(f"원본: {text}")
print(f"역순: {text[::-1]}")

# 회문(palindrome) 검사
words = ["level", "hello", "radar", "python", "noon"]

print("\n회문 검사:")
for word in words:
    is_palindrome = word == word[::-1]
    result = "회문" if is_palindrome else "회문 아님"
    print(f"{word}: {result}")

# 추가 기능: 부분 문자열 추출
print("\n===== 로그 파싱 =====")
log = "[2024-01-15 14:23:45] ERROR: Connection failed"

print(f"로그: {log}")

# 날짜 추출
date = log[1:11]
print(f"날짜: {date}")

# 시간 추출
time = log[12:20]
print(f"시간: {time}")

# 로그 레벨
level_start = log.find("]") + 2
level_end = log.find(":", level_start)
level = log[level_start:level_end]
print(f"레벨: {level}")

# 메시지
message = log[level_end+2:]
print(f"메시지: {message}")

# 추가 기능: 문자열 간격 슬라이싱
print("\n===== 패턴 추출 =====")
sequence = "ABCDEFGHIJKLMNOP"

print(f"원본: {sequence}")

# 짝수 위치 문자
even_chars = sequence[::2]
print(f"짝수 위치: {even_chars}")

# 홀수 위치 문자
odd_chars = sequence[1::2]
print(f"홀수 위치: {odd_chars}")

# 2칸씩 건너뛰기
every_third = sequence[::3]
print(f"3칸 간격: {every_third}")

# 역순으로 2칸씩
reverse_every_second = sequence[::-2]
print(f"역순 2칸: {reverse_every_second}")

# 추가 기능: 문자열 자르기 응용
print("\n===== 데이터 추출 =====")
data = "NAME:김철수|AGE:28|CITY:서울|JOB:개발자"

print(f"데이터: {data}")

# 각 필드 추출
fields = data.split("|")

for field in fields:
    colon_pos = field.find(":")
    key = field[:colon_pos]
    value = field[colon_pos+1:]
    print(f"{key}: {value}")

# 추가 기능: 고정 길이 데이터 파싱
print("\n===== 고정폭 데이터 파싱 =====")
# 이름(10자) + 나이(3자) + 도시(10자)
fixed_data = "김철수       028서울       "

print(f"원본: '{fixed_data}'")

name = fixed_data[0:10].strip()
age = fixed_data[10:13].strip()
city = fixed_data[13:23].strip()

print(f"이름: {name}")
print(f"나이: {age}")
print(f"도시: {city}")

# 추가 기능: 시간 문자열 처리
print("\n===== 시간 처리 =====")
timestamp = "2024-01-15T14:23:45.123Z"

print(f"타임스탬프: {timestamp}")

year = timestamp[0:4]
month = timestamp[5:7]
day = timestamp[8:10]
hour = timestamp[11:13]
minute = timestamp[14:16]
second = timestamp[17:19]
millisec = timestamp[20:23]

print(f"날짜: {year}-{month}-{day}")
print(f"시간: {hour}:{minute}:{second}")
print(f"밀리초: {millisec}")

# 추가 기능: 사용자 입력 처리
print("\n===== 사용자 입력 처리 =====")
user_input = input("주민등록번호 (YYMMDD-NNNNNNN): ").strip()

if len(user_input) == 14 and user_input[6] == "-":
    birth_year = user_input[0:2]
    birth_month = user_input[2:4]
    birth_day = user_input[4:6]
    gender_code = user_input[7]

    print(f"\n생년월일: {birth_year}년 {birth_month}월 {birth_day}일")

    if gender_code in "13":
        print("성별: 남성")
    elif gender_code in "24":
        print("성별: 여성")
    else:
        print("성별: 확인 불가")

    # 마스킹
    masked = user_input[:8] + "*" * 6
    print(f"마스킹: {masked}")
else:
    print("올바른 형식이 아닙니다!")

print("=" * 30)
