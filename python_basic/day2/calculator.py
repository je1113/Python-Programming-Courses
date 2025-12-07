"""
파일명: calculator.py
목적: 다기능 계산기 (산술 연산자 실습)
"""

print("===== 계산기 =====")

# 두 숫자 입력받기
num1 = float(input("첫 번째 숫자: "))
num2 = float(input("두 번째 숫자: "))

# 결과 출력
print("-" * 17)

# 덧셈
result_add = num1 + num2
print(f"{num1} + {num2} = {result_add}")

# 뺄셈
result_sub = num1 - num2
print(f"{num1} - {num2} = {result_sub}")

# 곱셈
result_mul = num1 * num2
print(f"{num1} * {num2} = {result_mul}")

# 나눗셈
result_div = num1 / num2
print(f"{num1} / {num2} = {result_div:.2f}")

# 몫
result_floordiv = int(num1) // int(num2)
print(f"{int(num1)} // {int(num2)} = {result_floordiv} (몫)")

# 나머지
result_mod = int(num1) % int(num2)
print(f"{int(num1)} % {int(num2)} = {result_mod} (나머지)")

# 거듭제곱
result_pow = num1 ** num2
print(f"{num1} ** {num2} = {result_pow}")

print("=" * 17)

# 추가 기능: 고급 연산
print("\n===== 고급 연산 =====")

# 절대값
abs_num1 = abs(num1)
abs_num2 = abs(num2)
print(f"|{num1}| = {abs_num1}")
print(f"|{num2}| = {abs_num2}")

# 반올림
print(f"\nround({result_div}) = {round(result_div)}")
print(f"round({result_div}, 1) = {round(result_div, 1)}")
print(f"round({result_div}, 2) = {round(result_div, 2)}")

# 최대값/최소값
print(f"\nmax({num1}, {num2}) = {max(num1, num2)}")
print(f"min({num1}, {num2}) = {min(num1, num2)}")

# divmod (몫과 나머지 동시에)
quotient, remainder = divmod(int(num1), int(num2))
print(f"\ndivmod({int(num1)}, {int(num2)}) = ({quotient}, {remainder})")

# 추가: 복합 할당 연산자 예시
print("\n===== 복합 할당 연산자 =====")
value = num1
print(f"초기값: {value}")

value += num2
print(f"+= {num2} 후: {value}")

value -= num2
print(f"-= {num2} 후: {value}")

value *= 2
print(f"*= 2 후: {value}")

value /= 2
print(f"/= 2 후: {value}")

# 추가: 0으로 나누기 예외 처리
print("\n===== 안전한 나눗셈 =====")
divisor = float(input("나눌 숫자: "))

if divisor != 0:
    safe_result = num1 / divisor
    print(f"{num1} / {divisor} = {safe_result:.2f}")
else:
    print("오류: 0으로 나눌 수 없습니다!")
