"""
파일명: list_slicing.py
목적: 데이터 분석 및 리포트 생성 (리스트 슬라이싱 실습)
"""

# 일일 방문자 수 데이터 (30일)
daily_visitors = [
    1200, 1350, 1420, 1580, 1650, 1720, 1890,  # 1주차
    2100, 1950, 1800, 2200, 2500, 2300, 2150,  # 2주차
    2400, 2600, 2550, 2700, 2800, 2650, 2500,  # 3주차
    2900, 3100, 3050, 3200, 3300, 3150, 3000,  # 4주차
    3400, 3500                                  # 5주차 (2일)
]

print("=" * 70)
print("웹사이트 방문자 데이터 분석".center(70))
print("=" * 70)

# 1단계: 주간 데이터 추출
print("\n[1단계] 주간 데이터 분석")
print("-" * 70)

week1 = daily_visitors[0:7]
week2 = daily_visitors[7:14]
week3 = daily_visitors[14:21]
week4 = daily_visitors[21:28]
week5 = daily_visitors[28:]  # 나머지 전부

weeks = [week1, week2, week3, week4, week5]

print(f"{'주차':<10} {'방문자 수':<15} {'일평균':<15} {'증감':<15}")
print("-" * 70)

prev_avg = 0
for i, week in enumerate(weeks, 1):
    total = sum(week)
    avg = total / len(week)

    if i == 1:
        change = "-"
    else:
        diff = avg - prev_avg
        change = f"{diff:+.0f} ({diff/prev_avg*100:+.1f}%)"

    print(f"{i}주차:<10} {total:>10,}명  {avg:>10,.0f}명  {change:<15}")
    prev_avg = avg

# 2단계: 최근 N일 데이터 분석
print("\n[2단계] 최근 N일 데이터 분석")
print("-" * 70)

# 최근 7일
recent_7days = daily_visitors[-7:]
recent_7days_avg = sum(recent_7days) / len(recent_7days)

# 최근 14일
recent_14days = daily_visitors[-14:]
recent_14days_avg = sum(recent_14days) / len(recent_14days)

# 최근 30일
recent_30days = daily_visitors[-30:]
recent_30days_avg = sum(recent_30days) / len(recent_30days)

print(f"최근  7일 평균: {recent_7days_avg:,.0f}명")
print(f"최근 14일 평균: {recent_14days_avg:,.0f}명")
print(f"최근 30일 평균: {recent_30days_avg:,.0f}명")

# 3단계: 이동 평균 계산 (슬라이딩 윈도우)
print("\n[3단계] 7일 이동 평균 계산")
print("-" * 70)

window_size = 7

print(f"{'기간':<20} {'이동 평균':<15}")
print("-" * 35)

for i in range(len(daily_visitors) - window_size + 1):
    window = daily_visitors[i:i+window_size]
    avg = sum(window) / len(window)
    period = f"{i+1}~{i+window_size}일"
    print(f"{period:<20} {avg:>10,.0f}명")

# 4단계: 월초/월중/월말 비교
print("\n[4단계] 월초/월중/월말 비교")
print("-" * 70)

first_10days = daily_visitors[:10]
middle_10days = daily_visitors[10:20]
last_days = daily_visitors[20:]

first_avg = sum(first_10days) / len(first_10days)
middle_avg = sum(middle_10days) / len(middle_10days)
last_avg = sum(last_days) / len(last_days)

print(f"월초 (1~10일):   {first_avg:,.0f}명")
print(f"월중 (11~20일):  {middle_avg:,.0f}명")
print(f"월말 (21일~):    {last_avg:,.0f}명")

# 5단계: 데이터 샘플링 (N개씩 건너뛰기)
print("\n[5단계] 데이터 샘플링")
print("-" * 70)

# 2일마다 샘플링
sample_2days = daily_visitors[::2]
print(f"2일 간격 샘플링 ({len(sample_2days)}개): {sample_2days[:5]}...")

# 3일마다 샘플링
sample_3days = daily_visitors[::3]
print(f"3일 간격 샘플링 ({len(sample_3days)}개): {sample_3days[:5]}...")

# 7일마다 샘플링 (주간 대표값)
sample_7days = daily_visitors[::7]
print(f"7일 간격 샘플링 ({len(sample_7days)}개): {sample_7days}")

# 6단계: 페이지 단위로 데이터 출력
print("\n[6단계] 페이지별 데이터 출력")
print("-" * 70)

page_size = 10
total_pages = (len(daily_visitors) + page_size - 1) // page_size

for page in range(total_pages):
    start = page * page_size
    end = start + page_size
    page_data = daily_visitors[start:end]

    print(f"\n페이지 {page + 1} ({start + 1}~{min(end, len(daily_visitors))}일):")
    print(f"  데이터: {page_data}")
    print(f"  평균: {sum(page_data) / len(page_data):,.0f}명")

# 7단계: 역순 분석
print("\n[7단계] 역순 데이터 분석")
print("-" * 70)

# 최근부터 과거로
reversed_data = daily_visitors[::-1]

print("최근 5일 (역순):")
for i, visitors in enumerate(reversed_data[:5]):
    day = len(daily_visitors) - i
    print(f"  {day}일차: {visitors:,}명")

# 8단계: 특정 범위 추출
print("\n[8단계] 특정 범위 데이터 추출")
print("-" * 70)

# 2주차만 (8~14일)
week2_data = daily_visitors[7:14]
print(f"2주차 데이터 (8~14일): {week2_data}")
print(f"2주차 평균: {sum(week2_data) / len(week2_data):,.0f}명")

# 중간 절반
mid_start = len(daily_visitors) // 4
mid_end = len(daily_visitors) * 3 // 4
middle_half = daily_visitors[mid_start:mid_end]
print(f"\n중간 절반 데이터: {len(middle_half)}일")
print(f"중간 절반 평균: {sum(middle_half) / len(middle_half):,.0f}명")

# 9단계: 평일/주말 패턴 (가정: 1일은 월요일)
print("\n[9단계] 평일/주말 패턴 분석")
print("-" * 70)

# 평일: 월~금 (0, 1, 2, 3, 4)
weekday_data = []
weekend_data = []

for i, visitors in enumerate(daily_visitors):
    day_of_week = i % 7  # 0=월, 1=화, ..., 6=일

    if day_of_week < 5:  # 월~금
        weekday_data.append(visitors)
    else:  # 토~일
        weekend_data.append(visitors)

weekday_avg = sum(weekday_data) / len(weekday_data)
weekend_avg = sum(weekend_data) / len(weekend_data)

print(f"평일 평균: {weekday_avg:,.0f}명 ({len(weekday_data)}일)")
print(f"주말 평균: {weekend_avg:,.0f}명 ({len(weekend_data)}일)")

diff = weekend_avg - weekday_avg
print(f"차이: {diff:+,.0f}명 ({diff/weekday_avg*100:+.1f}%)")

# 10단계: 배치 처리
print("\n[10단계] 배치 처리 (7일 단위)")
print("-" * 70)

batch_size = 7

print(f"{'배치':<10} {'기간':<15} {'총 방문자':<15} {'평균':<15}")
print("-" * 60)

for i in range(0, len(daily_visitors), batch_size):
    batch = daily_visitors[i:i+batch_size]
    batch_num = i // batch_size + 1
    period = f"{i+1}~{min(i+batch_size, len(daily_visitors))}일"
    total = sum(batch)
    avg = total / len(batch)

    print(f"{batch_num}번:<10} {period:<15} {total:>10,}명  {avg:>10,.0f}명")

# 11단계: 성장 구간 찾기
print("\n[11단계] 성장 구간 분석")
print("-" * 70)

# 전반부와 후반부 비교
first_half = daily_visitors[:len(daily_visitors)//2]
second_half = daily_visitors[len(daily_visitors)//2:]

first_half_avg = sum(first_half) / len(first_half)
second_half_avg = sum(second_half) / len(second_half)

print(f"전반부 평균: {first_half_avg:,.0f}명")
print(f"후반부 평균: {second_half_avg:,.0f}명")

growth = second_half_avg - first_half_avg
growth_rate = (growth / first_half_avg) * 100

print(f"성장: {growth:+,.0f}명 ({growth_rate:+.1f}%)")

# 12단계: 상위/하위 N일
print("\n[12단계] 상위/하위 방문일 분석")
print("-" * 70)

# 복사본 정렬 (원본 유지)
sorted_visitors = sorted(daily_visitors, reverse=True)

# 상위 5일
top_5 = sorted_visitors[:5]
# 하위 5일
bottom_5 = sorted_visitors[-5:][::-1]  # 역순으로

print("상위 5일:")
for i, visitors in enumerate(top_5, 1):
    # 원본에서 인덱스 찾기
    day = daily_visitors.index(visitors) + 1
    print(f"  {i}. {day}일차: {visitors:,}명")

print("\n하위 5일:")
for i, visitors in enumerate(bottom_5, 1):
    day = daily_visitors.index(visitors) + 1
    print(f"  {i}. {day}일차: {visitors:,}명")

# 13단계: 슬라이싱으로 데이터 수정 (시뮬레이션)
print("\n[13단계] 데이터 보정 시뮬레이션")
print("-" * 70)

# 원본 복사
corrected_data = daily_visitors.copy()

# 2주차 데이터에 10% 보정 적용 (예시)
week2_start = 7
week2_end = 14

print(f"2주차 데이터 보정 (10% 증가):")
print(f"보정 전: {corrected_data[week2_start:week2_end]}")

# 보정 적용
corrected_data[week2_start:week2_end] = [
    int(v * 1.1) for v in corrected_data[week2_start:week2_end]
]

print(f"보정 후: {corrected_data[week2_start:week2_end]}")

# 14단계: 이상치 탐지
print("\n[14단계] 이상치 탐지")
print("-" * 70)

avg = sum(daily_visitors) / len(daily_visitors)
threshold = avg * 0.5  # 평균의 50% 이상 차이

print(f"전체 평균: {avg:,.0f}명")
print(f"이상치 기준: 평균 ± {threshold:,.0f}명")
print()

outliers = []
for i, visitors in enumerate(daily_visitors):
    if abs(visitors - avg) > threshold:
        outliers.append((i + 1, visitors))

if outliers:
    print("이상치 발견:")
    for day, visitors in outliers:
        diff = visitors - avg
        print(f"  {day}일차: {visitors:,}명 (평균 대비 {diff:+,.0f}명)")
else:
    print("이상치 없음")

# 15단계: 종합 리포트
print("\n" + "=" * 70)
print("종합 분석 리포트".center(70))
print("=" * 70)

total_visitors = sum(daily_visitors)
avg_visitors = total_visitors / len(daily_visitors)
max_visitors = max(daily_visitors)
min_visitors = min(daily_visitors)
max_day = daily_visitors.index(max_visitors) + 1
min_day = daily_visitors.index(min_visitors) + 1

print(f"\n기간: 1~{len(daily_visitors)}일 ({len(daily_visitors)}일간)")
print(f"총 방문자: {total_visitors:,}명")
print(f"일평균: {avg_visitors:,.0f}명")
print(f"최다 방문일: {max_day}일차 ({max_visitors:,}명)")
print(f"최소 방문일: {min_day}일차 ({min_visitors:,}명)")
print(f"방문자 범위: {max_visitors - min_visitors:,}명")

print(f"\n성장 분석:")
print(f"  초기 7일 평균: {sum(daily_visitors[:7])/7:,.0f}명")
print(f"  최근 7일 평균: {sum(daily_visitors[-7:])/7:,.0f}명")
growth = (sum(daily_visitors[-7:])/7) - (sum(daily_visitors[:7])/7)
print(f"  성장: {growth:+,.0f}명 ({growth/(sum(daily_visitors[:7])/7)*100:+.1f}%)")

print("\n" + "=" * 70)
print("분석 완료".center(70))
print("=" * 70)
