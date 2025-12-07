"""
파일명: type_conversion.py
목적: BMI 계산기 (타입 변환 실습)
"""

print("===== BMI 계산기 =====")

# 사용자 입력 받기
height_cm = input("키를 입력하세요 (cm): ")
weight_kg = input("몸무게를 입력하세요 (kg): ")

# 문자열을 숫자로 변환
height_cm = float(height_cm)
weight_kg = float(weight_kg)

# cm를 m로 변환
height_m = height_cm / 100

# BMI 계산: 몸무게(kg) / (키(m) ** 2)
bmi = weight_kg / (height_m ** 2)

# BMI 판정
if bmi < 18.5:
    status = "저체중"
elif bmi < 23:
    status = "정상"
elif bmi < 25:
    status = "과체중"
else:
    status = "비만"

# 결과 출력
print("-" * 20)
print(f"키: {height_cm:.1f}cm")
print(f"몸무게: {weight_kg:.1f}kg")
print(f"BMI: {bmi:.2f}")
print(f"판정: {status}")
print("=" * 20)

# 추가: 표준 체중 계산
standard_weight = (height_m ** 2) * 22  # BMI 22를 표준으로
weight_diff = weight_kg - standard_weight

print(f"\n표준 체중: {standard_weight:.1f}kg")
if weight_diff > 0:
    print(f"표준 체중보다 {weight_diff:.1f}kg 더 나갑니다")
elif weight_diff < 0:
    print(f"표준 체중보다 {abs(weight_diff):.1f}kg 덜 나갑니다")
else:
    print("표준 체중과 동일합니다")

# 추가: 타입 확인
print(f"\n[타입 확인]")
print(f"height_cm 타입: {type(height_cm)}")
print(f"weight_kg 타입: {type(weight_kg)}")
print(f"bmi 타입: {type(bmi)}")
print(f"status 타입: {type(status)}")
