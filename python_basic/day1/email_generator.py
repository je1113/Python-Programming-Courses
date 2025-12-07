"""
파일명: email_generator.py
목적: 신입사원 이메일 계정 자동 생성 (문자열 자료형 실습)
"""

# 신입사원 정보
name = "Kim Python"
department = "Sales"
join_year = 2025

# 이메일 생성
# 1. 이름에서 공백 제거 → 소문자
name_for_email = name.replace(" ", "").lower()
# "Kim Python" → "kimpython"

# 2. 부서명 소문자
department_lower = department.lower()
# "Sales" → "sales"

# 3. 이메일 조합
email = f"{name_for_email}.{department_lower}@company.com"
# "kimpython.sales@company.com"

# 임시 비밀번호 생성
password = f"{department.upper()}{join_year}!!!"
# "SALES2025!!!"

# 결과 출력
print("=" * 28)
print("  신입사원 계정 정보")
print("=" * 28)
print(f"이름: {name}")
print(f"부서: {department}")
print(f"입사년도: {join_year}")
print("-" * 28)
print(f"이메일: {email}")
print(f"임시 비밀번호: {password}")
print("-" * 28)
print(f"{name}님, 환영합니다!")
print("첫 로그인 시 비밀번호를 변경해주세요.")
print("=" * 28)

# 추가 예시: 여러 신입사원 처리
print("\n" + "=" * 40)
print("추가 신입사원 계정 생성")
print("=" * 40)

# 두 번째 신입사원
name2 = "Lee Java"
department2 = "Marketing"
join_year2 = 2025

name_for_email2 = name2.replace(" ", "").lower()
department_lower2 = department2.lower()
email2 = f"{name_for_email2}.{department_lower2}@company.com"
password2 = f"{department2.upper()}{join_year2}!!!"

print("\n[신입사원 2]")
print("=" * 28)
print("  신입사원 계정 정보")
print("=" * 28)
print(f"이름: {name2}")
print(f"부서: {department2}")
print(f"입사년도: {join_year2}")
print("-" * 28)
print(f"이메일: {email2}")
print(f"임시 비밀번호: {password2}")
print("-" * 28)

# 유용한 문자열 메서드 연습
print("\n" + "=" * 40)
print("문자열 메서드 연습")
print("=" * 40)

sample_email = "USER@EXAMPLE.COM"
print(f"원본: {sample_email}")
print(f"소문자: {sample_email.lower()}")
print(f"대문자: {sample_email.upper()}")

sample_text = "  공백이 많은 텍스트  "
print(f"\n원본: '{sample_text}'")
print(f"공백 제거: '{sample_text.strip()}'")

sample_name = "김-파-이-썬"
print(f"\n원본: {sample_name}")
print(f"하이픈 제거: {sample_name.replace('-', '')}")
