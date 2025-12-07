"""
파일명: fstring_practice.py
목적: 급여 명세서 생성기 (f-string 포매팅 심화 실습)
"""

print("===== 급여 명세서 입력 =====")

# 사원 정보 입력
employee_name = input("사원명: ")
base_salary = int(input("기본급: "))
bonus = int(input("성과급: "))

# 계산
total_salary = base_salary + bonus
tax_rate = 0.1  # 10%
tax = total_salary * tax_rate
net_salary = total_salary - tax

# 명세서 출력
width = 32

print("=" * width)
print(f"{'급여 명세서':^{width}}")
print("=" * width)
print(f"사원명: {employee_name}")
print("-" * width)
print(f"{'기본급:':>10} {base_salary:>20,}원")
print(f"{'성과급:':>10} {bonus:>20,}원")
print("-" * width)
print(f"{'총 급여:':>10} {total_salary:>20,}원")
print(f"{'세금(10%):':>10} {-tax:>20,.0f}원")
print("-" * width)
print(f"{'실수령액:':>10} {net_salary:>20,.0f}원")
print("=" * width)

# 추가 정보
print(f"\n[상세 정보]")
print(f"세전 급여: {total_salary:>15,}원")
print(f"공제액:   {tax:>15,.0f}원 ({tax_rate:.0%})")
print(f"실수령액: {net_salary:>15,.0f}원")

# 추가: 연봉 정보
yearly_salary = total_salary * 12
yearly_tax = tax * 12
yearly_net = net_salary * 12

print(f"\n[연봉 정보]")
print("-" * 30)
print(f"연봉(세전):  {yearly_salary:>15,}원")
print(f"연간 세금:   {yearly_tax:>15,.0f}원")
print(f"연봉(세후):  {yearly_net:>15,.0f}원")

# 추가: 비교 정보
average_salary = 3000000  # 평균 급여
diff = total_salary - average_salary
diff_percent = (diff / average_salary) * 100

print(f"\n[평균과 비교]")
print(f"업계 평균: {average_salary:,}원")
if diff > 0:
    print(f"평균보다 {diff:,}원 높음 (+{diff_percent:.1f}%)")
elif diff < 0:
    print(f"평균보다 {abs(diff):,}원 낮음 ({diff_percent:.1f}%)")
else:
    print("평균과 동일")

# 추가: 진행률 바 (세금 비율 시각화)
bar_length = 20
filled = int(bar_length * tax_rate)
bar = "█" * filled + "░" * (bar_length - filled)
print(f"\n[세율 시각화]")
print(f"세율: [{bar}] {tax_rate:.0%}")
