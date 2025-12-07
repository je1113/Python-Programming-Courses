"""
파일명: regex_basic.py
목적: 로그 파일 분석기 (정규표현식 기초 실습)
"""

import re

# 샘플 로그 데이터
logs = [
    "[2024-01-15 14:23:45] INFO: User login successful - user@example.com from 192.168.1.100",
    "[2024-01-15 14:25:12] ERROR: Connection timeout - DB server unreachable",
    "[2024-01-15 14:27:33] WARNING: High memory usage detected - 85%",
    "[2024-01-15 14:30:01] INFO: Order created - ID: ORD-12345, Amount: 50000원",
    "[2024-01-15 14:32:18] ERROR: Payment failed - Card number: 1234-5678-9012-3456",
    "[2024-01-15 14:35:42] INFO: User registered - Phone: 010-1234-5678, Email: newuser@test.com",
    "[2024-01-15 14:38:05] ERROR: File not found - /var/log/app.log",
    "[2024-01-15 14:40:22] WARNING: API rate limit approaching - 90% of quota used",
    "[2024-01-15 14:42:51] INFO: Backup completed - 192.168.1.200",
    "[2024-01-15 14:45:13] ERROR: Invalid email format - user.example.com"
]

print("=" * 70)
print("로그 파일 분석기".center(70))
print("=" * 70)

# 1단계: 날짜/시간 추출
print("\n[1단계] 날짜/시간 추출")
print("-" * 70)

# 패턴: [YYYY-MM-DD HH:MM:SS]
datetime_pattern = r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]'

print(f"{'로그':<60} {'시간':<20}")
print("-" * 70)

for log in logs[:3]:  # 처음 3개만
    match = re.search(datetime_pattern, log)
    if match:
        datetime = match.group(1)
        # 로그 축약
        log_short = log[:50] + "..." if len(log) > 50 else log
        print(f"{log_short:<60} {datetime:<20}")

# 2단계: 로그 레벨 추출
print("\n[2단계] 로그 레벨 추출 및 집계")
print("-" * 70)

# 패턴: INFO, ERROR, WARNING
level_pattern = r'\] (INFO|ERROR|WARNING):'

level_count = {"INFO": 0, "ERROR": 0, "WARNING": 0}

for log in logs:
    match = re.search(level_pattern, log)
    if match:
        level = match.group(1)
        level_count[level] += 1

print("로그 레벨별 발생 횟수:")
for level, count in level_count.items():
    bar = "█" * count
    print(f"  {level:<8}: {bar} ({count}건)")

# 3단계: IP 주소 추출
print("\n[3단계] IP 주소 추출")
print("-" * 70)

# 패턴: XXX.XXX.XXX.XXX
ip_pattern = r'\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\b'

print("발견된 IP 주소:")
ip_addresses = []

for log in logs:
    matches = re.findall(ip_pattern, log)
    for ip in matches:
        if ip not in ip_addresses:
            ip_addresses.append(ip)
            print(f"  - {ip}")

# 4단계: 에러 메시지 필터링
print("\n[4단계] 에러 로그만 필터링")
print("-" * 70)

error_pattern = r'ERROR:(.+)'

print("에러 로그 목록:")
for i, log in enumerate(logs, 1):
    if "ERROR" in log:
        match = re.search(error_pattern, log)
        if match:
            error_msg = match.group(1).strip()
            print(f"  {i}. {error_msg}")

# 5단계: 이메일 추출
print("\n[5단계] 이메일 주소 추출")
print("-" * 70)

# 패턴: 문자+@+문자+.+문자
email_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'

print("발견된 이메일 주소:")
for log in logs:
    emails = re.findall(email_pattern, log)
    for email in emails:
        print(f"  - {email}")

# 6단계: 전화번호 추출
print("\n[6단계] 전화번호 추출")
print("-" * 70)

# 패턴: XXX-XXXX-XXXX
phone_pattern = r'\b\d{3}-\d{4}-\d{4}\b'

print("발견된 전화번호:")
for log in logs:
    phones = re.findall(phone_pattern, log)
    for phone in phones:
        print(f"  - {phone}")

# 7단계: 개인정보 마스킹
print("\n[7단계] 개인정보 마스킹")
print("-" * 70)

print("마스킹 전 → 마스킹 후:")
print()

for log in logs:
    masked_log = log

    # 이메일 마스킹
    masked_log = re.sub(
        r'\b([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})\b',
        r'***@\2',
        masked_log
    )

    # 전화번호 마스킹
    masked_log = re.sub(
        r'\b(\d{3})-(\d{4})-(\d{4})\b',
        r'\1-****-\3',
        masked_log
    )

    # 카드번호 마스킹
    masked_log = re.sub(
        r'\b(\d{4})-(\d{4})-(\d{4})-(\d{4})\b',
        r'\1-****-****-\4',
        masked_log
    )

    # IP 주소 마스킹 (마지막 옥텟만)
    masked_log = re.sub(
        r'\b(\d{1,3}\.\d{1,3}\.\d{1,3})\.(\d{1,3})\b',
        r'\1.***',
        masked_log
    )

    if masked_log != log:
        print(f"원본: {log}")
        print(f"마스킹: {masked_log}")
        print()

# 8단계: 날짜별 로그 분류
print("\n[8단계] 날짜별 로그 분류")
print("-" * 70)

# 날짜만 추출
date_pattern = r'\[(\d{4}-\d{2}-\d{2})'

date_logs = {}

for log in logs:
    match = re.search(date_pattern, log)
    if match:
        date = match.group(1)
        if date not in date_logs:
            date_logs[date] = []
        date_logs[date].append(log)

for date, log_list in date_logs.items():
    print(f"\n날짜: {date} ({len(log_list)}건)")

# 9단계: 시간대별 분석
print("\n[9단계] 시간대별 로그 분포")
print("-" * 70)

# 시간만 추출 (HH:MM)
time_pattern = r'\[.+ (\d{2}):\d{2}:\d{2}\]'

hour_count = {}

for log in logs:
    match = re.search(time_pattern, log)
    if match:
        hour = match.group(1)
        if hour in hour_count:
            hour_count[hour] += 1
        else:
            hour_count[hour] = 1

print("시간대별 로그 발생 빈도:")
for hour in sorted(hour_count.keys()):
    count = hour_count[hour]
    bar = "▓" * count
    print(f"  {hour}시: {bar} ({count}건)")

# 10단계: 특정 패턴 검색
print("\n[10단계] 사용자 정의 패턴 검색")
print("-" * 70)

# 주문 ID 추출 (ORD-XXXXX)
order_pattern = r'ORD-\d+'

print("주문 ID 검색:")
for log in logs:
    matches = re.findall(order_pattern, log)
    if matches:
        for order_id in matches:
            print(f"  - {order_id}")

# 금액 추출
amount_pattern = r'(\d+)원'

print("\n금액 정보:")
for log in logs:
    matches = re.findall(amount_pattern, log)
    if matches:
        for amount in matches:
            print(f"  - {int(amount):,}원")

# 11단계: 로그 검증
print("\n[11단계] 로그 형식 검증")
print("-" * 70)

# 올바른 로그 형식: [날짜 시간] 레벨: 메시지
valid_log_pattern = r'^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] (INFO|ERROR|WARNING):.+'

valid_count = 0
invalid_count = 0

for i, log in enumerate(logs, 1):
    if re.match(valid_log_pattern, log):
        valid_count += 1
    else:
        invalid_count += 1
        print(f"  잘못된 형식 (줄 {i}): {log[:50]}...")

print(f"\n유효한 로그: {valid_count}건")
print(f"잘못된 로그: {invalid_count}건")

# 12단계: 고급 패턴 - 그룹 추출
print("\n[12단계] 구조화된 로그 파싱")
print("-" * 70)

# 로그를 구조화
full_pattern = r'\[(.+?)\] (\w+): (.+)'

print(f"{'시간':<20} {'레벨':<10} {'메시지':<40}")
print("-" * 70)

for log in logs[:5]:  # 처음 5개만
    match = re.match(full_pattern, log)
    if match:
        timestamp = match.group(1)
        level = match.group(2)
        message = match.group(3)

        # 메시지 축약
        message_short = message[:37] + "..." if len(message) > 40 else message

        print(f"{timestamp:<20} {level:<10} {message_short:<40}")

# 통계 요약
print("\n" + "=" * 70)
print("분석 결과 요약".center(70))
print("=" * 70)

print(f"총 로그 수: {len(logs)}건")
print(f"에러 로그: {level_count['ERROR']}건")
print(f"경고 로그: {level_count['WARNING']}건")
print(f"정보 로그: {level_count['INFO']}건")
print(f"발견된 IP 주소: {len(ip_addresses)}개")

print("\n" + "=" * 70)
print("분석 완료".center(70))
print("=" * 70)
