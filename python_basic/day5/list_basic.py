"""
파일명: list_basic.py
목적: 월별 매출 데이터 관리 (리스트 생성과 접근 실습)
"""

# 12개월 매출 데이터 (단위: 만원)
monthly_sales = [1200, 1350, 1420, 1580, 1650, 1720, 1890, 2100, 1950, 1800, 2200, 2500]

# 월 이름
months = ["1월", "2월", "3월", "4월", "5월", "6월",
          "7월", "8월", "9월", "10월", "11월", "12월"]

print("=" * 60)
print("월별 매출 데이터 관리 시스템".center(60))
print("=" * 60)

# 1단계: 전체 매출 데이터 출력
print("\n[1단계] 전체 매출 현황")
print("-" * 60)

print(f"{'월':<6} {'매출액':>10} {'그래프':<30}")
print("-" * 60)

for i in range(len(monthly_sales)):
    month = months[i]
    sales = monthly_sales[i]
    # 100만원 = ▓ 1개
    bar = "▓" * (sales // 100)
    print(f"{month:<6} {sales:>8}만원 {bar:<30}")

print("-" * 60)

# 2단계: 특정 월 매출 조회
print("\n[2단계] 특정 월 매출 조회")
print("-" * 60)

# 인덱싱
print(f"1월 매출: {monthly_sales[0]:,}만원")
print(f"6월 매출: {monthly_sales[5]:,}만원")
print(f"12월 매출: {monthly_sales[11]:,}만원")

# 음수 인덱스
print(f"마지막 달 매출: {monthly_sales[-1]:,}만원")
print(f"마지막에서 두 번째 달 매출: {monthly_sales[-2]:,}만원")

# 3단계: 분기별 매출 계산
print("\n[3단계] 분기별 매출 분석")
print("-" * 60)

# 슬라이싱으로 분기 추출
q1_sales = monthly_sales[0:3]   # 1~3월
q2_sales = monthly_sales[3:6]   # 4~6월
q3_sales = monthly_sales[6:9]   # 7~9월
q4_sales = monthly_sales[9:12]  # 10~12월

q1_total = sum(q1_sales)
q2_total = sum(q2_sales)
q3_total = sum(q3_sales)
q4_total = sum(q4_sales)

print(f"1분기 (1~3월) 매출: {q1_total:,}만원")
print(f"  - 월평균: {q1_total // 3:,}만원")
print(f"  - 구성: {q1_sales}")

print(f"\n2분기 (4~6월) 매출: {q2_total:,}만원")
print(f"  - 월평균: {q2_total // 3:,}만원")
print(f"  - 구성: {q2_sales}")

print(f"\n3분기 (7~9월) 매출: {q3_total:,}만원")
print(f"  - 월평균: {q3_total // 3:,}만원")
print(f"  - 구성: {q3_sales}")

print(f"\n4분기 (10~12월) 매출: {q4_total:,}만원")
print(f"  - 월평균: {q4_total // 3:,}만원")
print(f"  - 구성: {q4_sales}")

# 4단계: 상반기/하반기 비교
print("\n[4단계] 상반기/하반기 비교")
print("-" * 60)

first_half = monthly_sales[:6]   # 처음 6개월
second_half = monthly_sales[6:]  # 나머지 6개월

first_half_total = sum(first_half)
second_half_total = sum(second_half)

print(f"상반기 (1~6월) 매출: {first_half_total:,}만원")
print(f"하반기 (7~12월) 매출: {second_half_total:,}만원")

difference = second_half_total - first_half_total
growth_rate = (difference / first_half_total) * 100

if difference > 0:
    print(f"하반기가 {difference:,}만원 더 많습니다. ({growth_rate:.1f}% 증가)")
else:
    print(f"상반기가 {abs(difference):,}만원 더 많습니다.")

# 5단계: 최고/최저 매출 월 찾기
print("\n[5단계] 최고/최저 매출 분석")
print("-" * 60)

max_sales = max(monthly_sales)
min_sales = min(monthly_sales)

# 인덱스 찾기
max_month_index = monthly_sales.index(max_sales)
min_month_index = monthly_sales.index(min_sales)

max_month = months[max_month_index]
min_month = months[min_month_index]

print(f"최고 매출: {max_month} - {max_sales:,}만원")
print(f"최저 매출: {min_month} - {min_sales:,}만원")
print(f"매출 차이: {max_sales - min_sales:,}만원")

# 6단계: 목표 달성 여부
print("\n[6단계] 월별 목표 달성 현황")
print("-" * 60)

target = 1500  # 목표: 1500만원

print(f"월별 목표: {target:,}만원\n")
print(f"{'월':<6} {'매출':<10} {'목표':<10} {'달성 여부':<10}")
print("-" * 40)

achieved_count = 0

for i in range(len(monthly_sales)):
    month = months[i]
    sales = monthly_sales[i]

    if sales >= target:
        status = "✓ 달성"
        achieved_count += 1
    else:
        status = "✗ 미달"

    print(f"{month:<6} {sales:<8}만원 {target:<8}만원 {status:<10}")

print("-" * 40)
print(f"목표 달성: {achieved_count}개월 / 12개월 ({achieved_count / 12 * 100:.0f}%)")

# 7단계: 매출 역순 출력
print("\n[7단계] 매출 역순 출력 (12월 → 1월)")
print("-" * 60)

print(f"{'월':<6} {'매출':>10}")
print("-" * 20)

# 역순 슬라이싱
for i in range(len(monthly_sales) - 1, -1, -1):
    month = months[i]
    sales = monthly_sales[i]
    print(f"{month:<6} {sales:>8}만원")

# 8단계: 홀수/짝수 월 비교
print("\n[8단계] 홀수월 vs 짝수월 비교")
print("-" * 60)

# 슬라이싱으로 홀수/짝수 월 추출
odd_months_sales = monthly_sales[::2]   # 1, 3, 5, 7, 9, 11월
even_months_sales = monthly_sales[1::2] # 2, 4, 6, 8, 10, 12월

odd_total = sum(odd_months_sales)
even_total = sum(even_months_sales)

print(f"홀수 월 (1, 3, 5, 7, 9, 11월) 매출: {odd_total:,}만원")
print(f"  - 월평균: {odd_total // 6:,}만원")

print(f"\n짝수 월 (2, 4, 6, 8, 10, 12월) 매출: {even_total:,}만원")
print(f"  - 월평균: {even_total // 6:,}만원")

# 9단계: 연간 통계
print("\n[9단계] 연간 매출 통계")
print("-" * 60)

total_sales = sum(monthly_sales)
avg_sales = total_sales / len(monthly_sales)
range_sales = max_sales - min_sales

print(f"총 매출: {total_sales:,}만원")
print(f"평균 매출: {avg_sales:,.0f}만원")
print(f"최고 매출: {max_sales:,}만원 ({max_month})")
print(f"최저 매출: {min_sales:,}만원 ({min_month})")
print(f"매출 범위: {range_sales:,}만원")

# 10단계: 특정 월 범위 조회
print("\n[10단계] 사용자 지정 기간 조회")
print("-" * 60)

# 예시: 여름 시즌 (6~8월)
summer_start = 5  # 6월 (인덱스 5)
summer_end = 8    # 8월 (인덱스 7)

summer_sales = monthly_sales[summer_start:summer_end]
summer_total = sum(summer_sales)

print(f"여름 시즌 (6~8월) 매출: {summer_total:,}만원")
print(f"  - 월평균: {summer_total // 3:,}만원")

# 11단계: 매출 포함 여부 확인
print("\n[11단계] 특정 매출 검색")
print("-" * 60)

search_amount = 1650

if search_amount in monthly_sales:
    index = monthly_sales.index(search_amount)
    month = months[index]
    print(f"{search_amount:,}만원 매출이 있습니다.")
    print(f"  - 월: {month}")
else:
    print(f"{search_amount:,}만원 매출은 없습니다.")

# 12단계: 리스트 길이 및 타입
print("\n[12단계] 데이터 정보")
print("-" * 60)

print(f"데이터 개수: {len(monthly_sales)}개월")
print(f"데이터 타입: {type(monthly_sales)}")
print(f"첫 번째 요소 타입: {type(monthly_sales[0])}")

# 13단계: 매출 성장 추이
print("\n[13단계] 월별 성장률 분석")
print("-" * 60)

print(f"{'월':<6} {'매출':<12} {'전월 대비':<15}")
print("-" * 40)

for i in range(len(monthly_sales)):
    month = months[i]
    sales = monthly_sales[i]

    if i == 0:
        change = "-"
    else:
        prev_sales = monthly_sales[i - 1]
        diff = sales - prev_sales
        rate = (diff / prev_sales) * 100
        change = f"{diff:+,}만원 ({rate:+.1f}%)"

    print(f"{month:<6} {sales:>8}만원 {change:<15}")

# 마무리
print("\n" + "=" * 60)
print("분석 완료".center(60))
print("=" * 60)
