"""
파일명: final_quiz.py
목적: 종합 실습 퀴즈 - 직원 관리 시스템 (Day 1~4 통합)

사용된 개념:
- 변수 및 데이터 타입 (Day 1)
- 형변환 (Day 2)
- 사용자 입력 (Day 2)
- f-string 포맷팅 (Day 2)
- 연산자 (Day 2)
- for 문 (Day 4)
- range() (Day 4)
- break/continue (Day 4)
- 리스트 처리 (Day 4)
- 문자열 메서드 (Day 4)
- 문자열 슬라이싱 (Day 4)
"""

import math

# 직원 데이터베이스
employees = [
    {
        "id": "E001",
        "name": "김철수",
        "age": 28,
        "email": "  KIM@company.com  ",
        "phone": "010-1234-5678",
        "salary": 3500000,
        "department": "개발",
        "position": "사원"
    },
    {
        "id": "E002",
        "name": "이영희",
        "age": 32,
        "email": "LEE@company.com",
        "phone": "01098765432",
        "salary": 4200000,
        "department": "기획",
        "position": "대리"
    },
    {
        "id": "E003",
        "name": "박민수",
        "age": 45,
        "email": "park@COMPANY.COM  ",
        "phone": "010 5555 6666",
        "salary": 6500000,
        "department": "개발",
        "position": "부장"
    },
    {
        "id": "E004",
        "name": "정지훈",
        "age": 26,
        "email": "jung@company.com",
        "phone": "010.7777.8888",
        "salary": 3200000,
        "department": "마케팅",
        "position": "사원"
    },
    {
        "id": "E005",
        "name": "최민지",
        "age": 35,
        "email": "CHOI@COMPANY.COM",
        "phone": "010-9999-0000",
        "salary": 5000000,
        "department": "기획",
        "position": "과장"
    }
]

print("=" * 50)
print("직원 관리 시스템".center(50))
print("=" * 50)

# 1단계: 데이터 정제 (문자열 메서드)
print("\n[1단계] 데이터 정제 중...")

for emp in employees:
    # 이메일 정제: 공백 제거, 소문자 변환
    emp["email"] = emp["email"].strip().lower()

    # 전화번호 정제: 하이픈 형식으로 통일
    phone = emp["phone"].replace("-", "").replace(" ", "").replace(".", "")
    emp["phone"] = f"{phone[:3]}-{phone[3:7]}-{phone[7:]}"

print("✓ 데이터 정제 완료!")

# 2단계: 전체 직원 목록 출력 (for 문, f-string)
print("\n" + "=" * 50)
print("[2단계] 전체 직원 목록")
print("=" * 50)

print(f"{'ID':<6} {'이름':<8} {'나이':>4} {'부서':<10} {'직급':<6} {'연봉':>12}")
print("-" * 50)

for emp in employees:
    print(f"{emp['id']:<6} {emp['name']:<8} {emp['age']:>4} {emp['department']:<10} "
          f"{emp['position']:<6} {emp['salary']:>12,}원")

# 3단계: 부서별 통계 (리스트 처리, 딕셔너리)
print("\n" + "=" * 50)
print("[3단계] 부서별 통계")
print("=" * 50)

departments = {}

for emp in employees:
    dept = emp["department"]

    if dept not in departments:
        departments[dept] = {
            "count": 0,
            "total_salary": 0,
            "employees": []
        }

    departments[dept]["count"] += 1
    departments[dept]["total_salary"] += emp["salary"]
    departments[dept]["employees"].append(emp["name"])

for dept, info in departments.items():
    avg_salary = info["total_salary"] / info["count"]
    print(f"\n부서: {dept}")
    print(f"  인원: {info['count']}명")
    print(f"  평균 연봉: {avg_salary:,.0f}원")
    print(f"  직원: {', '.join(info['employees'])}")

# 4단계: 연봉 순위 (정렬, enumerate)
print("\n" + "=" * 50)
print("[4단계] 연봉 순위 (상위 3명)")
print("=" * 50)

sorted_employees = sorted(employees, key=lambda x: x["salary"], reverse=True)

for i, emp in enumerate(sorted_employees[:3], 1):
    print(f"{i}위: {emp['name']} ({emp['department']} {emp['position']}) - {emp['salary']:,}원")

# 5단계: 연봉 인상 시뮬레이션 (연산자, 조건문)
print("\n" + "=" * 50)
print("[5단계] 연봉 인상 시뮬레이션")
print("=" * 50)

print("인상 기준:")
print("- 사원: 10%")
print("- 대리: 8%")
print("- 과장: 6%")
print("- 부장: 5%")
print()

total_before = 0
total_after = 0

print(f"{'이름':<8} {'현재 연봉':>12} {'인상률':>6} {'인상 후':>12} {'인상액':>12}")
print("-" * 50)

for emp in employees:
    position = emp["position"]
    current_salary = emp["salary"]

    # 직급별 인상률 결정 (조건부 표현식)
    rate = (0.10 if position == "사원" else
            0.08 if position == "대리" else
            0.06 if position == "과장" else
            0.05 if position == "부장" else 0)

    new_salary = current_salary * (1 + rate)
    increase = new_salary - current_salary

    total_before += current_salary
    total_after += new_salary

    print(f"{emp['name']:<8} {current_salary:>12,}원 {rate*100:>5.0f}% "
          f"{new_salary:>12,.0f}원 {increase:>12,.0f}원")

print("-" * 50)
print(f"{'합계':<8} {total_before:>12,}원         {total_after:>12,.0f}원 "
      f"{total_after - total_before:>12,.0f}원")

# 6단계: 나이 통계 (수학 함수)
print("\n" + "=" * 50)
print("[6단계] 나이 통계")
print("=" * 50)

ages = [emp["age"] for emp in employees]

avg_age = sum(ages) / len(ages)
max_age = max(ages)
min_age = min(ages)

# 표준편차
variance = sum((age - avg_age) ** 2 for age in ages) / len(ages)
std_dev = math.sqrt(variance)

print(f"평균 나이: {avg_age:.1f}세")
print(f"최고 나이: {max_age}세")
print(f"최저 나이: {min_age}세")
print(f"표준편차: {std_dev:.2f}")

# 연령대별 분포
print("\n연령대별 분포:")
age_groups = {"20대": 0, "30대": 0, "40대": 0, "50대": 0}

for age in ages:
    if 20 <= age < 30:
        age_groups["20대"] += 1
    elif 30 <= age < 40:
        age_groups["30대"] += 1
    elif 40 <= age < 50:
        age_groups["40대"] += 1
    elif 50 <= age < 60:
        age_groups["50대"] += 1

for group, count in age_groups.items():
    bar = "■" * count
    print(f"{group}: {bar} ({count}명)")

# 7단계: 직원 검색 (문자열 메서드, break)
print("\n" + "=" * 50)
print("[7단계] 직원 검색")
print("=" * 50)

search_name = input("검색할 이름: ").strip()

found = False
for emp in employees:
    if search_name in emp["name"]:
        print(f"\n검색 결과:")
        print(f"ID: {emp['id']}")
        print(f"이름: {emp['name']}")
        print(f"나이: {emp['age']}세")
        print(f"이메일: {emp['email']}")
        print(f"전화번호: {emp['phone']}")
        print(f"부서: {emp['department']}")
        print(f"직급: {emp['position']}")
        print(f"연봉: {emp['salary']:,}원")
        found = True
        break

if not found:
    print("해당 직원을 찾을 수 없습니다.")

# 8단계: 개인정보 마스킹 (문자열 슬라이싱)
print("\n" + "=" * 50)
print("[8단계] 개인정보 보호 (마스킹)")
print("=" * 50)

print(f"{'이름':<8} {'이메일':<25} {'전화번호':<15}")
print("-" * 50)

for emp in employees:
    # 이메일 마스킹 (@ 앞 2자만 보임)
    email = emp["email"]
    at_pos = email.find("@")
    if at_pos > 2:
        masked_email = email[:2] + "*" * (at_pos - 2) + email[at_pos:]
    else:
        masked_email = "*" * at_pos + email[at_pos:]

    # 전화번호 마스킹 (중간 4자리)
    phone = emp["phone"]
    masked_phone = phone[:4] + "****" + phone[8:]

    print(f"{emp['name']:<8} {masked_email:<25} {masked_phone:<15}")

# 9단계: 연봉 구간별 분석 (range, 리스트 컴프리헨션)
print("\n" + "=" * 50)
print("[9단계] 연봉 구간별 분석")
print("=" * 50)

salary_ranges = [
    (3000000, 3999999),
    (4000000, 4999999),
    (5000000, 5999999),
    (6000000, 6999999)
]

for low, high in salary_ranges:
    count = len([emp for emp in employees if low <= emp["salary"] <= high])
    bar = "█" * count
    print(f"{low//1000000:,}~{high//1000000:,}백만원: {bar} ({count}명)")

# 10단계: 성과 평가 시뮬레이션 (복합 조건, continue)
print("\n" + "=" * 50)
print("[10단계] 성과 평가 (랜덤 시뮬레이션)")
print("=" * 50)

import random

print(f"{'이름':<8} {'점수':>4} {'등급':<4} {'평가'}")
print("-" * 40)

for emp in employees:
    # 랜덤 점수 (60~100)
    score = random.randint(60, 100)

    # 등급 산정
    if score >= 90:
        grade = "S"
        comment = "우수"
    elif score >= 80:
        grade = "A"
        comment = "양호"
    elif score >= 70:
        grade = "B"
        comment = "보통"
    else:
        grade = "C"
        comment = "노력 필요"

    print(f"{emp['name']:<8} {score:>4}점 {grade:<4} {comment}")

# 종료
print("\n" + "=" * 50)
print("시스템 종료".center(50))
print("=" * 50)
