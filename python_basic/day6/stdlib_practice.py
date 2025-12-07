"""
파일명: stdlib_practice.py
목적: 표준 라이브러리 활용 프로그램
"""

import random
import math
from datetime import datetime, date, timedelta
import os
import sys

print("=" * 70)
print("표준 라이브러리 활용 프로그램".center(70))
print("=" * 70)

# 1. 로또 번호 생성기 (random)
print("\n[1] 로또 번호 생성기")
print("-" * 70)

def generate_lotto():
    """로또 번호 생성 (1~45 중 6개)"""
    return sorted(random.sample(range(1, 46), 6))

print("로또 번호 5세트 생성:\n")

for i in range(5):
    lotto_numbers = generate_lotto()
    print(f"  [{i+1}] {lotto_numbers}")

# 자동/수동 혼합
manual_numbers = [3, 7, 15]
remaining = [n for n in range(1, 46) if n not in manual_numbers]
auto_numbers = sorted(random.sample(remaining, 6 - len(manual_numbers)))
mixed_lotto = sorted(manual_numbers + auto_numbers)

print(f"\n수동 선택: {manual_numbers}")
print(f"혼합 번호: {mixed_lotto}")

# 2. D-Day 계산기 (datetime)
print("\n[2] D-Day 계산기")
print("-" * 70)

today = date.today()

# 주요 이벤트 D-Day
events = [
    ("크리스마스", date(today.year, 12, 25)),
    ("새해", date(today.year + 1, 1, 1)),
    ("설날", date(2024, 2, 10)),  # 예시
]

print(f"오늘: {today}\n")
print(f"{'이벤트':<15} {'날짜':<15} {'D-Day':<10}")
print("-" * 45)

for event_name, event_date in events:
    d_day = (event_date - today).days

    if d_day > 0:
        d_day_str = f"D-{d_day}"
    elif d_day == 0:
        d_day_str = "D-Day!"
    else:
        d_day_str = f"D+{abs(d_day)}"

    print(f"{event_name:<15} {event_date:<15} {d_day_str:<10}")

# 3. 근무 시간 계산
print("\n[3] 근무 시간 계산")
print("-" * 70)

work_start = datetime(2024, 1, 15, 9, 0, 0)
work_end = datetime(2024, 1, 15, 18, 30, 0)

work_duration = work_end - work_start
hours = work_duration.seconds // 3600
minutes = (work_duration.seconds % 3600) // 60

print(f"출근 시간: {work_start.strftime('%H:%M')}")
print(f"퇴근 시간: {work_end.strftime('%H:%M')}")
print(f"근무 시간: {hours}시간 {minutes}분")

# 주간 근무 시간
daily_hours = 9.5
weekly_hours = daily_hours * 5
monthly_hours = weekly_hours * 4

print(f"\n주간 근무 시간: {weekly_hours}시간")
print(f"월간 근무 시간: {monthly_hours}시간 (약)")

# 4. 원의 넓이/둘레 계산 (math)
print("\n[4] 원의 넓이/둘레 계산")
print("-" * 70)

radii = [5, 10, 15, 20, 25]

print(f"{'반지름':<10} {'넓이':<15} {'둘레':<15}")
print("-" * 40)

for r in radii:
    area = math.pi * r ** 2
    circumference = 2 * math.pi * r
    print(f"{r:<10} {area:<15.2f} {circumference:<15.2f}")

# 5. 삼각형 계산
print("\n[5] 직각삼각형 빗변 계산 (피타고라스)")
print("-" * 70)

triangles = [(3, 4), (5, 12), (8, 15), (7, 24)]

print(f"{'밑변':<10} {'높이':<10} {'빗변':<15}")
print("-" * 35)

for base, height in triangles:
    hypotenuse = math.sqrt(base**2 + height**2)
    print(f"{base:<10} {height:<10} {hypotenuse:<15.2f}")

# 6. 파일 목록 조회 (os)
print("\n[6] 파일 목록 조회")
print("-" * 70)

current_dir = os.getcwd()
print(f"현재 디렉토리: {current_dir}\n")

# 파일 분류
files = os.listdir(".")
py_files = [f for f in files if f.endswith('.py')]
dirs = [f for f in files if os.path.isdir(f)]

print(f"Python 파일 ({len(py_files)}개):")
for i, file in enumerate(py_files[:5], 1):
    size = os.path.getsize(file) if os.path.isfile(file) else 0
    print(f"  {i}. {file} ({size:,} bytes)")

if len(py_files) > 5:
    print(f"  ... 외 {len(py_files) - 5}개")

print(f"\n디렉토리 ({len(dirs)}개):")
for i, directory in enumerate(dirs[:5], 1):
    print(f"  {i}. {directory}/")

# 7. 시스템 정보 출력 (sys)
print("\n[7] 시스템 정보")
print("-" * 70)

print(f"Python 버전:")
print(f"  {sys.version}")

print(f"\n플랫폼: {sys.platform}")

print(f"\n실행 정보:")
print(f"  실행 파일: {sys.executable}")
print(f"  스크립트: {sys.argv[0]}")

print(f"\n메모리 정보:")
print(f"  최대 정수: {sys.maxsize:,}")

# 8. 랜덤 비밀번호 생성기
print("\n[8] 랜덤 비밀번호 생성기")
print("-" * 70)

import string

def generate_password(length=12):
    """안전한 비밀번호 생성"""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

print("생성된 비밀번호 (5개):\n")

for i in range(5):
    pwd = generate_password(16)
    print(f"  [{i+1}] {pwd}")

# 9. 주사위 시뮬레이터
print("\n[9] 주사위 시뮬레이터")
print("-" * 70)

def roll_dice(count=1):
    """주사위 굴리기"""
    return [random.randint(1, 6) for _ in range(count)]

print("주사위 2개를 10번 굴린 결과:\n")

results = {i: 0 for i in range(2, 13)}  # 2~12

for i in range(10):
    dice = roll_dice(2)
    total = sum(dice)
    results[total] += 1
    print(f"  {i+1}회: {dice} = {total}")

print("\n합계별 빈도:")
for total, count in sorted(results.items()):
    bar = "■" * count
    print(f"  {total:2}: {bar} ({count}회)")

# 10. 날짜 범위 생성
print("\n[10] 날짜 범위 생성")
print("-" * 70)

start_date = date.today()
end_date = start_date + timedelta(days=7)

print(f"기간: {start_date} ~ {end_date}\n")

print(f"{'날짜':<15} {'요일':<10}")
print("-" * 25)

current_date = start_date
weekdays = ["월", "화", "수", "목", "금", "토", "일"]

while current_date <= end_date:
    weekday = weekdays[current_date.weekday()]
    print(f"{current_date:<15} {weekday:<10}")
    current_date += timedelta(days=1)

# 11. 수학 함수 종합
print("\n[11] 수학 함수 종합")
print("-" * 70)

numbers = [2.3, 5.7, -3.14, 8.9, -1.5]

print(f"{'숫자':<10} {'절대값':<10} {'올림':<10} {'내림':<10} {'반올림':<10}")
print("-" * 50)

for num in numbers:
    abs_val = abs(num)
    ceil_val = math.ceil(num)
    floor_val = math.floor(num)
    round_val = round(num)

    print(f"{num:<10.2f} {abs_val:<10.2f} {ceil_val:<10} {floor_val:<10} {round_val:<10}")

# 12. 종합 예제: 시험 일정 관리
print("\n[12] 종합 예제: 시험 일정 관리")
print("-" * 70)

# 시험 과목과 날짜
exams = {
    "수학": date(2024, 3, 15),
    "영어": date(2024, 3, 18),
    "과학": date(2024, 3, 22),
    "국어": date(2024, 3, 25)
}

today = date.today()

print(f"오늘: {today}\n")
print(f"{'과목':<10} {'시험일':<15} {'D-Day':<10} {'준비 시간':<15}")
print("-" * 50)

for subject, exam_date in sorted(exams.items(), key=lambda x: x[1]):
    d_day = (exam_date - today).days

    if d_day > 0:
        d_day_str = f"D-{d_day}"
        prep_time = f"{d_day}일 남음"
    elif d_day == 0:
        d_day_str = "오늘!"
        prep_time = "시험 당일"
    else:
        d_day_str = "종료"
        prep_time = "시험 끝"

    print(f"{subject:<10} {exam_date:<15} {d_day_str:<10} {prep_time:<15}")

print("\n" + "=" * 70)
print("표준 라이브러리 실습 완료".center(70))
print("=" * 70)
