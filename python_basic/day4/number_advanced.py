"""
파일명: number_advanced.py
목적: 통계 계산기 (숫자형 자료형 심화 실습)
"""

import math

# 데이터 입력
numbers = [85, 92, 78, 95, 88, 76, 90, 82, 87, 94]

print("===== 통계 계산기 =====")
print(f"데이터: {numbers}")
print("-" * 30)

# 기본 통계
total = sum(numbers)
count = len(numbers)
average = total / count
maximum = max(numbers)
minimum = min(numbers)

print(f"개수: {count}개")
print(f"합계: {total}")
print(f"평균: {average:.2f}")
print(f"최대값: {maximum}")
print(f"최소값: {minimum}")
print(f"범위: {maximum - minimum}")

# 중앙값 (Median)
sorted_numbers = sorted(numbers)
n = len(sorted_numbers)

if n % 2 == 0:
    # 짝수 개: 중간 두 값의 평균
    median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
else:
    # 홀수 개: 중간 값
    median = sorted_numbers[n//2]

print(f"중앙값: {median}")

# 표준편차 (Standard Deviation)
variance = sum((x - average) ** 2 for x in numbers) / count
std_dev = math.sqrt(variance)

print(f"분산: {variance:.2f}")
print(f"표준편차: {std_dev:.2f}")

print("-" * 30)

# 추가 통계
print("\n===== 추가 통계 =====")

# 사분위수
q1 = sorted_numbers[n//4]
q3 = sorted_numbers[3*n//4]
iqr = q3 - q1

print(f"1사분위수 (Q1): {q1}")
print(f"3사분위수 (Q3): {q3}")
print(f"사분위범위 (IQR): {iqr}")

# 이상치 탐지 (Outliers)
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = [x for x in numbers if x < lower_bound or x > upper_bound]

print(f"\n이상치 범위: {lower_bound:.1f} ~ {upper_bound:.1f}")
if outliers:
    print(f"이상치: {outliers}")
else:
    print("이상치 없음")

# 도수 분포
print("\n===== 도수 분포 =====")
bins = [(70, 79), (80, 89), (90, 100)]

for low, high in bins:
    count = len([x for x in numbers if low <= x <= high])
    bar = "█" * count
    print(f"{low}~{high}: {bar} ({count}개)")

# 추가 기능: 백분위수
print("\n===== 백분위수 =====")
percentiles = [25, 50, 75, 90, 95]

for p in percentiles:
    index = int(n * p / 100)
    if index >= n:
        index = n - 1
    value = sorted_numbers[index]
    print(f"{p}번째 백분위수: {value}")

# 추가 기능: 각 값의 표준점수 (Z-score)
print("\n===== 표준점수 (Z-score) =====")
print("값   | Z-score | 해석")
print("-" * 30)

for num in numbers[:5]:  # 처음 5개만
    z_score = (num - average) / std_dev
    if abs(z_score) < 1:
        interpretation = "평균 부근"
    elif abs(z_score) < 2:
        interpretation = "평균에서 약간 벗어남"
    else:
        interpretation = "평균에서 많이 벗어남"

    print(f"{num:3} | {z_score:+7.2f} | {interpretation}")

# 추가 기능: 수학 함수 활용
print("\n===== 수학 함수 =====")

numbers_with_decimal = [3.7, 2.3, 5.8, 4.2, 6.9]

print("값   | ceil | floor | round")
print("-" * 30)

for num in numbers_with_decimal:
    print(f"{num} | {math.ceil(num):4} | {math.floor(num):5} | {round(num):5}")

# 추가 기능: 기하평균, 조화평균
print("\n===== 다양한 평균 =====")

# 산술평균
arithmetic_mean = sum(numbers) / len(numbers)

# 기하평균 (모든 값 곱한 후 n제곱근)
geometric_mean = math.prod(numbers) ** (1/len(numbers))

# 조화평균 (역수의 산술평균의 역수)
harmonic_mean = len(numbers) / sum(1/x for x in numbers)

print(f"산술평균: {arithmetic_mean:.2f}")
print(f"기하평균: {geometric_mean:.2f}")
print(f"조화평균: {harmonic_mean:.2f}")

# 추가 기능: 누적 합계
print("\n===== 누적 합계 =====")
cumsum = 0
for i, num in enumerate(numbers, 1):
    cumsum += num
    print(f"{i}번째까지 합계: {cumsum}")
