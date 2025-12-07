"""
파일명: csv_file.py
목적: CSV 파일 처리 실습
"""

import csv
import os

print("=" * 70)
print("CSV 파일 처리 실습".center(70))
print("=" * 70)

# 1. CSV 파일 생성 (기본)
print("\n[1] CSV 파일 생성")
print("-" * 70)

employees = [
    ["이름", "나이", "부서", "연봉"],
    ["김철수", 28, "개발", 3500],
    ["이영희", 32, "기획", 4200],
    ["박민수", 25, "개발", 3200],
    ["정지훈", 30, "마케팅", 3800],
    ["최민지", 27, "기획", 4000]
]

with open("employees.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(employees)

print("✓ employees.csv 파일 생성 완료")

# 2. CSV 파일 읽기
print("\n[2] CSV 파일 읽기")
print("-" * 70)

with open("employees.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    for i, row in enumerate(reader):
        if i == 0:
            print(f"{'':>3} {row[0]:<10} {row[1]:<6} {row[2]:<10} {row[3]:<10}")
            print("-" * 45)
        else:
            print(f"{i:>3}. {row[0]:<10} {row[1]:<6} {row[2]:<10} {row[3]:<10}")

# 3. DictReader로 읽기 (편리!)
print("\n[3] DictReader로 읽기")
print("-" * 70)

with open("employees.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    print(f"{'이름':<10} {'부서':<10} {'연봉':<12}")
    print("-" * 35)

    for row in reader:
        print(f"{row['이름']:<10} {row['부서']:<10} {int(row['연봉']):>8,}만원")

# 4. 부서별 평균 연봉 계산
print("\n[4] 부서별 평균 연봉")
print("-" * 70)

dept_salaries = {}

with open("employees.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        dept = row['부서']
        salary = int(row['연봉'])

        if dept not in dept_salaries:
            dept_salaries[dept] = []

        dept_salaries[dept].append(salary)

print(f"{'부서':<10} {'평균 연봉':<15} {'인원':<10}")
print("-" * 35)

for dept, salaries in dept_salaries.items():
    avg = sum(salaries) / len(salaries)
    print(f"{dept:<10} {avg:>10,.0f}만원  {len(salaries):>3}명")

# 5. 필터링 및 새 CSV 생성
print("\n[5] 개발 부서 직원만 추출")
print("-" * 70)

dev_employees = []

with open("employees.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        if row['부서'] == "개발":
            dev_employees.append(row)

print(f"개발 부서: {len(dev_employees)}명")

# DictWriter로 저장
with open("dev_team.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["이름", "나이", "부서", "연봉"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(dev_employees)

print("✓ dev_team.csv 생성 완료")

# 6. 판매 데이터 생성
print("\n[6] 판매 데이터 생성 및 분석")
print("-" * 70)

sales_data = [
    ["날짜", "제품", "수량", "단가"],
    ["2024-01-01", "노트북", 3, 1200000],
    ["2024-01-02", "마우스", 50, 30000],
    ["2024-01-02", "키보드", 30, 89000],
    ["2024-01-03", "노트북", 2, 1200000],
    ["2024-01-03", "모니터", 5, 350000],
    ["2024-01-04", "마우스", 40, 30000],
    ["2024-01-05", "노트북", 4, 1200000]
]

with open("sales.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(sales_data)

print("✓ sales.csv 생성 완료")

# 판매 데이터 분석
product_sales = {}
total_revenue = 0

with open("sales.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        product = row['제품']
        quantity = int(row['수량'])
        price = int(row['단가'])
        revenue = quantity * price

        if product not in product_sales:
            product_sales[product] = {'quantity': 0, 'revenue': 0}

        product_sales[product]['quantity'] += quantity
        product_sales[product]['revenue'] += revenue
        total_revenue += revenue

print(f"\n{'제품':<10} {'판매량':<10} {'매출액':<15}")
print("-" * 40)

for product, data in sorted(product_sales.items(), key=lambda x: x[1]['revenue'], reverse=True):
    print(f"{product:<10} {data['quantity']:>6}개  {data['revenue']:>12,}원")

print("-" * 40)
print(f"{'총계':<10} {'':<10} {total_revenue:>12,}원")

# 7. CSV에 데이터 추가
print("\n[7] 직원 데이터 추가")
print("-" * 70)

new_employees = [
    {"이름": "강호동", "나이": 35, "부서": "영업", "연봉": 4500},
    {"이름": "유재석", "나이": 33, "부서": "마케팅", "연봉": 4300}
]

# 기존 데이터 읽기
existing_employees = []
with open("employees.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    existing_employees = list(reader)

# 새 데이터 추가
existing_employees.extend(new_employees)

# 저장
with open("employees.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["이름", "나이", "부서", "연봉"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(existing_employees)

print(f"✓ {len(new_employees)}명의 직원 추가 완료")
print(f"현재 총 인원: {len(existing_employees)}명")

# 8. pandas로 CSV 처리 (더 강력!)
print("\n[8] pandas로 CSV 처리")
print("-" * 70)

try:
    import pandas as pd

    # CSV 읽기
    df = pd.read_csv("employees.csv", encoding="utf-8")

    print("데이터프레임:")
    print(df)

    # 통계
    print("\n연봉 통계:")
    print(df['연봉'].describe())

    # 부서별 그룹화
    print("\n부서별 평균 연봉:")
    dept_avg = df.groupby('부서')['연봉'].mean()
    print(dept_avg)

    # 정렬
    print("\n연봉 높은 순:")
    sorted_df = df.sort_values('연봉', ascending=False)
    print(sorted_df[['이름', '연봉']].head())

    # 필터링
    print("\n30세 이상 직원:")
    filtered = df[df['나이'] >= 30]
    print(filtered[['이름', '나이', '부서']])

    # 새 CSV로 저장
    df.to_csv("employees_processed.csv", index=False, encoding="utf-8-sig")
    print("\n✓ employees_processed.csv 생성 (Excel 호환)")

except ImportError:
    print("⚠️  pandas가 설치되지 않았습니다.")
    print("   설치: pip install pandas")

# 9. 복잡한 CSV 처리
print("\n[9] 성적 데이터 처리")
print("-" * 70)

# 성적 데이터 생성
grades_data = [
    ["학생", "국어", "영어", "수학"],
    ["김철수", 85, 90, 88],
    ["이영희", 92, 95, 91],
    ["박민수", 78, 82, 80],
    ["정지훈", 88, 85, 90],
    ["최민지", 95, 93, 96]
]

with open("grades.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(grades_data)

# 평균 계산 및 등급 추가
results = [["학생", "국어", "영어", "수학", "평균", "등급"]]

with open("grades.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        korean = int(row['국어'])
        english = int(row['영어'])
        math = int(row['수학'])
        avg = (korean + english + math) / 3

        # 등급 계산
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        else:
            grade = "D"

        results.append([row['학생'], korean, english, math, f"{avg:.1f}", grade])

# 결과 저장
with open("grades_result.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(results)

print("✓ grades_result.csv 생성 완료")

# 결과 출력
print(f"\n{'학생':<10} {'국어':<6} {'영어':<6} {'수학':<6} {'평균':<8} {'등급':<6}")
print("-" * 50)

for row in results[1:]:
    print(f"{row[0]:<10} {row[1]:<6} {row[2]:<6} {row[3]:<6} {row[4]:<8} {row[5]:<6}")

# 10. 생성된 파일 목록
print("\n[10] 생성된 CSV 파일")
print("-" * 70)

csv_files = [f for f in os.listdir(".") if f.endswith('.csv')]

print(f"{'파일명':<30} {'크기':<15} {'줄 수':<10}")
print("-" * 55)

for filename in csv_files:
    size = os.path.getsize(filename)

    # 줄 수 세기
    with open(filename, "r", encoding="utf-8") as f:
        line_count = sum(1 for _ in f)

    print(f"{filename:<30} {size:>10} bytes  {line_count:>5}줄")

print("\n" + "=" * 70)
print("CSV 파일 처리 완료".center(70))
print("=" * 70)

print("\n💡 Tip: CSV 파일은 Excel에서 바로 열 수 있습니다!")
print("💡 Tip: pandas를 사용하면 훨씬 편리합니다!")
