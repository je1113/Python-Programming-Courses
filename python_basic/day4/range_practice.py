"""
파일명: range_practice.py
목적: 구구단 출력 프로그램 (range() 활용 실습)
"""

print("===== 구구단 =====")

# 사용자 입력
while True:
    dan_input = input("원하는 단 (2~9): ")

    if not dan_input.isdigit():
        print("숫자만 입력하세요!")
        continue

    dan = int(dan_input)

    if 2 <= dan <= 9:
        break
    else:
        print("2~9 사이의 숫자를 입력하세요!")

# 구구단 출력
print("-" * 17)
total = 0

for i in range(1, 10):
    result = dan * i
    print(f"{dan} × {i} = {result}")
    total += result

print("-" * 17)
print(f"합계: {total}")

# 짝수 결과만 출력
print("-" * 17)
print("짝수 결과:")

for i in range(1, 10):
    result = dan * i
    if result % 2 == 0:
        print(f"{dan} × {i} = {result}")

print("=" * 17)

# 추가 기능: 전체 구구단 (2단~9단)
print("\n===== 전체 구구단 =====")

for dan in range(2, 10):
    print(f"\n[{dan}단]")
    for i in range(1, 10):
        print(f"{dan} × {i} = {dan * i}")

# 추가 기능: 구구단 표 형식
print("\n===== 구구단 표 =====")
print("    ", end="")
for i in range(1, 10):
    print(f"{i:4}", end="")
print()
print("-" * 40)

for dan in range(2, 10):
    print(f"{dan}단:", end="")
    for i in range(1, 10):
        print(f"{dan*i:4}", end="")
    print()

# 추가 기능: 역순 구구단
print("\n===== 역순 구구단 =====")
print(f"[{dan}단 역순]")
for i in range(9, 0, -1):
    print(f"{dan} × {i} = {dan * i}")

# 추가 기능: 짝수단만
print("\n===== 짝수단만 =====")
for dan in range(2, 10, 2):
    print(f"[{dan}단]", end=" ")
    for i in range(1, 10):
        print(f"{dan*i}", end=" ")
    print()

# 추가 기능: 특정 범위
print("\n===== 5 × (1~5) =====")
for i in range(1, 6):
    print(f"5 × {i} = {5 * i}")
