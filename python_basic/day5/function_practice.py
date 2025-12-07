"""
파일명: function_practice.py
목적: 직원 관리 시스템 (함수 활용 종합 실습)

사용된 개념:
- 함수 정의 및 호출
- 매개변수 (기본값, *args, **kwargs)
- 반환값 (단일, 여러 값, 딕셔너리)
- 리스트 컴프리헨션
- 람다 함수
- 함수 조합
"""

# 직원 데이터베이스
employees = [
    {
        "id": "E001",
        "name": "김철수",
        "department": "개발",
        "position": "사원",
        "salary": 3500000,
        "hire_date": "2022-01-15"
    },
    {
        "id": "E002",
        "name": "이영희",
        "department": "기획",
        "position": "대리",
        "salary": 4200000,
        "hire_date": "2020-05-20"
    },
    {
        "id": "E003",
        "name": "박민수",
        "department": "개발",
        "position": "부장",
        "salary": 6500000,
        "hire_date": "2015-03-10"
    },
    {
        "id": "E004",
        "name": "정지훈",
        "department": "마케팅",
        "position": "사원",
        "salary": 3200000,
        "hire_date": "2023-07-01"
    },
    {
        "id": "E005",
        "name": "최민지",
        "department": "기획",
        "position": "과장",
        "salary": 5000000,
        "hire_date": "2018-11-05"
    }
]

print("=" * 70)
print("직원 관리 시스템".center(70))
print("=" * 70)

# 1. 직원 추가 함수 (검증 포함)
def add_employee(employees_list, **employee_data):
    """
    새 직원을 추가합니다 (유효성 검증 포함)

    Args:
        employees_list: 직원 리스트
        **employee_data: 직원 정보

    Returns:
        (성공 여부, 메시지) 튜플
    """
    # 필수 필드 검증
    required_fields = ["id", "name", "department", "position", "salary"]

    for field in required_fields:
        if field not in employee_data:
            return False, f"필수 필드 누락: {field}"

    # ID 중복 검사
    if any(emp["id"] == employee_data["id"] for emp in employees_list):
        return False, f"중복된 ID: {employee_data['id']}"

    # 연봉 검증
    if employee_data["salary"] <= 0:
        return False, "연봉은 0보다 커야 합니다"

    # 추가
    employees_list.append(employee_data)
    return True, f"{employee_data['name']} 직원이 추가되었습니다"

print("\n[1] 직원 추가 기능")
print("-" * 70)

# 성공 케이스
success, message = add_employee(
    employees,
    id="E006",
    name="강호동",
    department="영업",
    position="대리",
    salary=4000000,
    hire_date="2024-01-01"
)
print(f"✓ {message}" if success else f"✗ {message}")

# 실패 케이스 (중복 ID)
success, message = add_employee(
    employees,
    id="E001",  # 중복!
    name="유재석",
    department="영업",
    position="사원",
    salary=3300000
)
print(f"✓ {message}" if success else f"✗ {message}")

# 2. 직원 검색 함수 (이름으로)
def search_by_name(employees_list, name):
    """
    이름으로 직원을 검색합니다 (부분 일치)

    Args:
        employees_list: 직원 리스트
        name: 검색할 이름 (일부만 입력 가능)

    Returns:
        검색된 직원 리스트
    """
    return [
        emp for emp in employees_list
        if name.lower() in emp["name"].lower()
    ]

print("\n[2] 직원 검색 (이름)")
print("-" * 70)

search_name = "이"
found = search_by_name(employees, search_name)

print(f"'{search_name}' 검색 결과: {len(found)}명\n")

for emp in found:
    print(f"  - {emp['name']} ({emp['department']} {emp['position']})")

# 3. 직원 검색 함수 (부서별)
def search_by_department(employees_list, department):
    """
    부서별 직원을 검색합니다

    Args:
        employees_list: 직원 리스트
        department: 부서명

    Returns:
        해당 부서 직원 리스트
    """
    return [
        emp for emp in employees_list
        if emp["department"] == department
    ]

print("\n[3] 직원 검색 (부서)")
print("-" * 70)

dept = "개발"
dept_employees = search_by_department(employees, dept)

print(f"{dept} 부서 직원: {len(dept_employees)}명\n")

for emp in dept_employees:
    print(f"  - {emp['name']} ({emp['position']}, 연봉: {emp['salary']:,}원)")

# 4. 연봉 통계 계산 함수
def calculate_salary_stats(employees_list):
    """
    연봉 통계를 계산합니다

    Args:
        employees_list: 직원 리스트

    Returns:
        통계 딕셔너리
    """
    if not employees_list:
        return None

    salaries = [emp["salary"] for emp in employees_list]

    return {
        "total": sum(salaries),
        "average": sum(salaries) / len(salaries),
        "max": max(salaries),
        "min": min(salaries),
        "count": len(salaries)
    }

print("\n[4] 연봉 통계")
print("-" * 70)

stats = calculate_salary_stats(employees)

print(f"전체 직원: {stats['count']}명")
print(f"총 연봉: {stats['total']:,}원")
print(f"평균 연봉: {stats['average']:,.0f}원")
print(f"최고 연봉: {stats['max']:,}원")
print(f"최저 연봉: {stats['min']:,}원")

# 부서별 통계
print("\n부서별 평균 연봉:")
departments = set(emp["department"] for emp in employees)

for dept in sorted(departments):
    dept_emps = search_by_department(employees, dept)
    dept_stats = calculate_salary_stats(dept_emps)
    print(f"  {dept}: {dept_stats['average']:,.0f}원 ({dept_stats['count']}명)")

# 5. 승진 처리 함수
def promote_employee(employees_list, employee_id, new_position, salary_increase=0):
    """
    직원을 승진시킵니다

    Args:
        employees_list: 직원 리스트
        employee_id: 직원 ID
        new_position: 새 직급
        salary_increase: 연봉 인상액 (기본값 0)

    Returns:
        (성공 여부, 메시지) 튜플
    """
    # 직원 찾기
    employee = None
    for emp in employees_list:
        if emp["id"] == employee_id:
            employee = emp
            break

    if not employee:
        return False, f"직원을 찾을 수 없습니다: {employee_id}"

    old_position = employee["position"]
    old_salary = employee["salary"]

    # 승진 처리
    employee["position"] = new_position
    employee["salary"] += salary_increase

    message = (
        f"{employee['name']} 승진: {old_position} → {new_position}, "
        f"연봉: {old_salary:,}원 → {employee['salary']:,}원"
    )

    return True, message

print("\n[5] 승진 처리")
print("-" * 70)

# 김철수 승진
success, message = promote_employee(employees, "E001", "대리", 500000)
print(f"✓ {message}" if success else f"✗ {message}")

# 존재하지 않는 직원
success, message = promote_employee(employees, "E999", "과장")
print(f"✓ {message}" if success else f"✗ {message}")

# 6. 직원 목록 정렬 함수
def sort_employees(employees_list, key="name", reverse=False):
    """
    직원 목록을 정렬합니다

    Args:
        employees_list: 직원 리스트
        key: 정렬 기준 ("name", "salary", "hire_date")
        reverse: 역순 정렬 여부

    Returns:
        정렬된 직원 리스트
    """
    return sorted(employees_list, key=lambda emp: emp[key], reverse=reverse)

print("\n[6] 직원 목록 정렬")
print("-" * 70)

# 연봉 높은 순
print("연봉 높은 순:")
sorted_by_salary = sort_employees(employees, key="salary", reverse=True)
for i, emp in enumerate(sorted_by_salary[:3], 1):
    print(f"  {i}. {emp['name']}: {emp['salary']:,}원")

# 이름순
print("\n이름순:")
sorted_by_name = sort_employees(employees, key="name")
for emp in sorted_by_name:
    print(f"  - {emp['name']}")

# 7. 연봉 인상 계산 함수
def calculate_raise(employees_list, rate=0.05):
    """
    전 직원 연봉 인상액을 계산합니다

    Args:
        employees_list: 직원 리스트
        rate: 인상률 (기본값 5%)

    Returns:
        인상 정보 리스트
    """
    results = []

    for emp in employees_list:
        current = emp["salary"]
        increase = int(current * rate)
        new_salary = current + increase

        results.append({
            "name": emp["name"],
            "current": current,
            "increase": increase,
            "new": new_salary
        })

    return results

print("\n[7] 연봉 인상 시뮬레이션 (5%)")
print("-" * 70)

raises = calculate_raise(employees, rate=0.05)

print(f"{'이름':<10} {'현재 연봉':<15} {'인상액':<12} {'인상 후':<15}")
print("-" * 52)

for r in raises:
    print(f"{r['name']:<10} {r['current']:>10,}원  "
          f"{r['increase']:>8,}원  {r['new']:>10,}원")

total_increase = sum(r["increase"] for r in raises)
print("-" * 52)
print(f"{'총 인상액:':<10} {total_increase:>37,}원")

# 8. 필터링 함수들
def filter_by_salary_range(employees_list, min_salary, max_salary):
    """연봉 범위로 필터링"""
    return [
        emp for emp in employees_list
        if min_salary <= emp["salary"] <= max_salary
    ]

def filter_by_position(employees_list, position):
    """직급으로 필터링"""
    return [emp for emp in employees_list if emp["position"] == position]

print("\n[8] 다양한 필터링")
print("-" * 70)

# 연봉 범위 필터링
mid_salary = filter_by_salary_range(employees, 3500000, 5000000)
print(f"연봉 350~500만원: {len(mid_salary)}명")
for emp in mid_salary:
    print(f"  - {emp['name']}: {emp['salary']:,}원")

# 직급 필터링
managers = filter_by_position(employees, "대리")
print(f"\n대리 직급: {len(managers)}명")
for emp in managers:
    print(f"  - {emp['name']} ({emp['department']})")

# 9. 직원 정보 포맷팅 함수
def format_employee_card(employee):
    """
    직원 정보를 카드 형식으로 포맷팅합니다

    Args:
        employee: 직원 딕셔너리

    Returns:
        포맷팅된 문자열
    """
    card = f"""
╔{'═' * 48}╗
║ {employee['name'].center(46)} ║
║ {'─' * 46} ║
║ ID: {employee['id']:<42} ║
║ 부서: {employee['department']:<40} ║
║ 직급: {employee['position']:<40} ║
║ 연봉: {f"{employee['salary']:,}원":<40} ║
╚{'═' * 48}╝
"""
    return card

print("\n[9] 직원 카드 출력")
print("-" * 70)

# 첫 번째 직원 카드 출력
print(format_employee_card(employees[0]))

# 10. 부서별 집계 함수
def get_department_summary(employees_list):
    """
    부서별 요약 정보를 생성합니다

    Args:
        employees_list: 직원 리스트

    Returns:
        부서별 요약 딕셔너리
    """
    summary = {}

    for emp in employees_list:
        dept = emp["department"]

        if dept not in summary:
            summary[dept] = {
                "count": 0,
                "total_salary": 0,
                "employees": []
            }

        summary[dept]["count"] += 1
        summary[dept]["total_salary"] += emp["salary"]
        summary[dept]["employees"].append(emp["name"])

    return summary

print("\n[10] 부서별 요약")
print("-" * 70)

dept_summary = get_department_summary(employees)

for dept, info in sorted(dept_summary.items()):
    avg = info["total_salary"] / info["count"]
    print(f"\n{dept} 부서:")
    print(f"  인원: {info['count']}명")
    print(f"  총 연봉: {info['total_salary']:,}원")
    print(f"  평균 연봉: {avg:,.0f}원")
    print(f"  직원: {', '.join(info['employees'])}")

# 11. 보고서 생성 함수
def generate_report(employees_list):
    """
    종합 보고서를 생성합니다

    Args:
        employees_list: 직원 리스트

    Returns:
        보고서 문자열
    """
    stats = calculate_salary_stats(employees_list)
    dept_summary = get_department_summary(employees_list)

    report = f"""
{'=' * 70}
{'직원 현황 보고서'.center(70)}
{'=' * 70}

[전체 통계]
- 총 직원: {stats['count']}명
- 총 인건비: {stats['total']:,}원
- 평균 연봉: {stats['average']:,.0f}원
- 최고 연봉: {stats['max']:,}원
- 최저 연봉: {stats['min']:,}원

[부서별 현황]
"""

    for dept, info in sorted(dept_summary.items()):
        avg = info["total_salary"] / info["count"]
        report += f"\n{dept} 부서: {info['count']}명, 평균 연봉 {avg:,.0f}원"

    # 상위 연봉자
    top_earners = sort_employees(employees_list, key="salary", reverse=True)[:3]
    report += f"\n\n[상위 연봉자 TOP 3]\n"

    for i, emp in enumerate(top_earners, 1):
        report += f"\n{i}. {emp['name']} ({emp['department']} {emp['position']}) - {emp['salary']:,}원"

    report += f"\n\n{'=' * 70}"

    return report

print("\n[11] 종합 보고서")
print("-" * 70)

report = generate_report(employees)
print(report)

# 12. 직원 삭제 함수
def remove_employee(employees_list, employee_id):
    """
    직원을 삭제합니다

    Args:
        employees_list: 직원 리스트
        employee_id: 삭제할 직원 ID

    Returns:
        (성공 여부, 메시지) 튜플
    """
    for i, emp in enumerate(employees_list):
        if emp["id"] == employee_id:
            removed = employees_list.pop(i)
            return True, f"{removed['name']} 직원이 삭제되었습니다"

    return False, f"직원을 찾을 수 없습니다: {employee_id}"

print("\n[12] 직원 삭제")
print("-" * 70)

# 백업
employees_backup = employees.copy()

# 삭제 시도
success, message = remove_employee(employees, "E006")
print(f"✓ {message}" if success else f"✗ {message}")

# 복원
employees = employees_backup.copy()

# 13. 검증 함수들
def validate_employee_id(employee_id):
    """직원 ID 형식 검증 (E + 3자리 숫자)"""
    if len(employee_id) != 4:
        return False
    if not employee_id.startswith("E"):
        return False
    if not employee_id[1:].isdigit():
        return False
    return True

def validate_salary(salary):
    """연봉 유효성 검증"""
    return isinstance(salary, int) and salary > 0

print("\n[13] 데이터 검증")
print("-" * 70)

test_ids = ["E001", "E999", "A001", "E12", "E1234"]

print(f"{'ID':<10} {'유효성':<10}")
print("-" * 20)

for test_id in test_ids:
    valid = "✓ 유효" if validate_employee_id(test_id) else "✗ 무효"
    print(f"{test_id:<10} {valid:<10}")

# 14. 통합 검색 함수
def search_employees(employees_list, **criteria):
    """
    여러 조건으로 직원을 검색합니다

    Args:
        employees_list: 직원 리스트
        **criteria: 검색 조건 (department, position, min_salary, max_salary 등)

    Returns:
        검색 결과 리스트
    """
    results = employees_list

    if "department" in criteria:
        results = [e for e in results if e["department"] == criteria["department"]]

    if "position" in criteria:
        results = [e for e in results if e["position"] == criteria["position"]]

    if "min_salary" in criteria:
        results = [e for e in results if e["salary"] >= criteria["min_salary"]]

    if "max_salary" in criteria:
        results = [e for e in results if e["salary"] <= criteria["max_salary"]]

    return results

print("\n[14] 통합 검색")
print("-" * 70)

# 개발 부서 + 연봉 400만 이상
results = search_employees(
    employees,
    department="개발",
    min_salary=4000000
)

print(f"조건: 개발 부서 + 연봉 400만 이상")
print(f"결과: {len(results)}명\n")

for emp in results:
    print(f"  - {emp['name']} ({emp['position']}, {emp['salary']:,}원)")

# 마무리
print("\n" + "=" * 70)
print("직원 관리 시스템 종료".center(70))
print("=" * 70)
