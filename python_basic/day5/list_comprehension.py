"""
파일명: list_comprehension.py
목적: 데이터 변환 및 필터링 (리스트 컴프리헨션 실습)
"""

print("=" * 70)
print("리스트 컴프리헨션 실습".center(70))
print("=" * 70)

# 1단계: 온도 데이터 변환 (섭씨 → 화씨)
print("\n[1단계] 온도 변환 (섭씨 → 화씨)")
print("-" * 70)

celsius_temps = [0, 10, 20, 25, 30, 35, 40]

# 공식: F = C × 9/5 + 32
fahrenheit_temps = [(c * 9/5) + 32 for c in celsius_temps]

print(f"{'섭씨(°C)':<15} {'화씨(°F)':<15}")
print("-" * 30)

for c, f in zip(celsius_temps, fahrenheit_temps):
    print(f"{c:>10}°C  {f:>10.1f}°F")

# 2단계: 제품 재고 필터링
print("\n[2단계] 재고 있는 제품 필터링")
print("-" * 70)

products = [
    {"name": "노트북", "stock": 5, "price": 1200000},
    {"name": "마우스", "stock": 0, "price": 25000},
    {"name": "키보드", "stock": 3, "price": 89000},
    {"name": "모니터", "stock": 0, "price": 350000},
    {"name": "헤드셋", "stock": 7, "price": 120000}
]

# 재고가 있는 제품만
in_stock = [p for p in products if p["stock"] > 0]

print(f"총 {len(products)}개 제품 중 재고 있음: {len(in_stock)}개\n")

for product in in_stock:
    print(f"  - {product['name']}: {product['stock']}개 (가격: {product['price']:,}원)")

# 3단계: 학생 합격자 추출
print("\n[3단계] 합격자 명단 추출")
print("-" * 70)

students = [
    {"name": "김철수", "score": 85, "attendance": 95},
    {"name": "이영희", "score": 92, "attendance": 88},
    {"name": "박민수", "score": 58, "attendance": 75},
    {"name": "정지훈", "score": 78, "attendance": 92},
    {"name": "최민지", "score": 95, "attendance": 98}
]

# 합격 조건: 점수 >= 80 AND 출석률 >= 90
passed = [s for s in students if s["score"] >= 80 and s["attendance"] >= 90]

print(f"합격 조건: 점수 80점 이상 + 출석률 90% 이상")
print(f"합격자: {len(passed)}명\n")

for student in passed:
    print(f"  ✓ {student['name']}: 점수 {student['score']}점, 출석률 {student['attendance']}%")

# 불합격자
failed = [s for s in students if not (s["score"] >= 80 and s["attendance"] >= 90)]

print(f"\n불합격자: {len(failed)}명\n")

for student in failed:
    print(f"  ✗ {student['name']}: 점수 {student['score']}점, 출석률 {student['attendance']}%")

# 4단계: 구구단 2차원 리스트
print("\n[4단계] 구구단 표 생성 (2~9단)")
print("-" * 70)

# 2차원 리스트 컴프리헨션
gugudan = [[dan * i for i in range(1, 10)] for dan in range(2, 10)]

print("    ", end="")
for i in range(1, 10):
    print(f"{i:4}", end="")
print()
print("-" * 40)

for dan in range(2, 10):
    print(f"{dan}단:", end="")
    for result in gugudan[dan - 2]:
        print(f"{result:4}", end="")
    print()

# 5단계: 파일 경로에서 파일명 추출
print("\n[5단계] 파일 경로에서 파일명 추출")
print("-" * 70)

file_paths = [
    "/home/user/documents/report.pdf",
    "/var/log/system/app.log",
    "/usr/local/bin/python3.9",
    "/home/user/pictures/vacation.jpg"
]

# 경로에서 마지막 부분(파일명)만 추출
filenames = [path.split("/")[-1] for path in file_paths]

print(f"{'전체 경로':<40} {'파일명':<20}")
print("-" * 60)

for path, filename in zip(file_paths, filenames):
    print(f"{path:<40} {filename:<20}")

# 6단계: 제곱수 리스트
print("\n[6단계] 제곱수 리스트 생성")
print("-" * 70)

squares = [i ** 2 for i in range(1, 11)]

print("1~10의 제곱수:")
print(squares)

# 짝수의 제곱만
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]

print("\n짝수의 제곱수:")
print(even_squares)

# 7단계: 문자열 리스트 변환
print("\n[7단계] 문자열 대소문자 변환")
print("-" * 70)

words = ["Hello", "WORLD", "Python", "PROGRAMMING"]

# 모두 대문자로
upper_words = [word.upper() for word in words]
# 모두 소문자로
lower_words = [word.lower() for word in words]
# 첫 글자만 대문자
title_words = [word.title() for word in words]

print(f"{'원본':<15} {'대문자':<15} {'소문자':<15} {'타이틀':<15}")
print("-" * 60)

for orig, upper, lower, title in zip(words, upper_words, lower_words, title_words):
    print(f"{orig:<15} {upper:<15} {lower:<15} {title:<15}")

# 8단계: 조건부 변환
print("\n[8단계] 조건부 값 변환")
print("-" * 70)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 짝수는 제곱, 홀수는 2배
transformed = [n ** 2 if n % 2 == 0 else n * 2 for n in numbers]

print(f"{'원본':<10} {'변환 후':<15} {'규칙':<20}")
print("-" * 45)

for orig, trans in zip(numbers, transformed):
    rule = "제곱 (짝수)" if orig % 2 == 0 else "2배 (홀수)"
    print(f"{orig:<10} {trans:<15} {rule:<20}")

# 9단계: 중첩 리스트 평탄화
print("\n[9단계] 중첩 리스트 평탄화")
print("-" * 70)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 평탄화 (flatten)
flattened = [num for row in nested_list for num in row]

print(f"중첩 리스트: {nested_list}")
print(f"평탄화: {flattened}")

# 10단계: 좌표 생성
print("\n[10단계] 좌표 조합 생성")
print("-" * 70)

x_coords = [0, 1, 2]
y_coords = [0, 1, 2]

# 모든 조합
coords = [(x, y) for x in x_coords for y in y_coords]

print("생성된 좌표 (9개):")
for coord in coords:
    print(f"  {coord}", end="")
    if (coords.index(coord) + 1) % 3 == 0:
        print()  # 3개마다 줄바꿈

# 11단계: 가격 할인 계산
print("\n[11단계] 할인가 계산")
print("-" * 70)

prices = [10000, 25000, 50000, 75000, 100000]

# 50000원 이상: 20% 할인, 미만: 10% 할인
discounted = [
    int(p * 0.8) if p >= 50000 else int(p * 0.9)
    for p in prices
]

print(f"{'원가':<15} {'할인율':<10} {'할인가':<15} {'할인액':<15}")
print("-" * 55)

for orig, disc in zip(prices, discounted):
    rate = "20%" if orig >= 50000 else "10%"
    saved = orig - disc
    print(f"{orig:>10,}원  {rate:<10} {disc:>10,}원  {saved:>10,}원")

# 12단계: 문자열 길이 필터링
print("\n[12단계] 문자열 길이 필터링")
print("-" * 70)

words = ["a", "ab", "abc", "abcd", "abcde", "abcdef"]

# 길이 3 이상만
long_words = [word for word in words if len(word) >= 3]

print(f"전체 단어: {words}")
print(f"길이 3 이상: {long_words}")

# 단어 길이 리스트
lengths = [len(word) for word in words]
print(f"각 단어 길이: {lengths}")

# 13단계: 딕셔너리에서 값 추출
print("\n[13단계] 딕셔너리 리스트에서 값 추출")
print("-" * 70)

employees = [
    {"name": "김철수", "salary": 3500000, "department": "개발"},
    {"name": "이영희", "salary": 4200000, "department": "기획"},
    {"name": "박민수", "salary": 6500000, "department": "개발"},
    {"name": "정지훈", "salary": 3200000, "department": "마케팅"}
]

# 이름만 추출
names = [emp["name"] for emp in employees]
print(f"직원 이름: {names}")

# 개발 부서 직원만
dev_team = [emp["name"] for emp in employees if emp["department"] == "개발"]
print(f"개발팀: {dev_team}")

# 연봉 400만 이상
high_salary = [
    emp["name"]
    for emp in employees
    if emp["salary"] >= 4000000
]
print(f"연봉 400만 이상: {high_salary}")

# 14단계: 범위 생성
print("\n[14단계] 다양한 범위 생성")
print("-" * 70)

# 1~20 중 3의 배수
multiples_of_3 = [i for i in range(1, 21) if i % 3 == 0]
print(f"1~20 중 3의 배수: {multiples_of_3}")

# 1~100 중 완전제곱수
perfect_squares = [i for i in range(1, 101) if int(i ** 0.5) ** 2 == i]
print(f"1~100 중 완전제곱수: {perfect_squares}")

# 15단계: 문자열 포맷팅
print("\n[15단계] 문자열 포맷팅")
print("-" * 70)

numbers = [1, 2, 3, 4, 5]

# 패딩 추가
padded = [f"{n:03d}" for n in numbers]
print(f"0 패딩: {padded}")

# 접두사 추가
prefixed = [f"item_{n}" for n in numbers]
print(f"접두사: {prefixed}")

# 16단계: 조건부 필터링 + 변환
print("\n[16단계] 조건부 필터링 및 변환")
print("-" * 70)

scores = [45, 78, 92, 65, 88, 54, 95, 71]

# 60점 이상만 선택하고 등급 부여
grades = [
    "A" if s >= 90 else "B" if s >= 80 else "C"
    for s in scores
    if s >= 60
]

print(f"전체 점수: {scores}")
print(f"60점 이상: {[s for s in scores if s >= 60]}")
print(f"등급: {grades}")

# 17단계: 체스판 패턴
print("\n[17단계] 체스판 패턴 생성")
print("-" * 70)

# 8x8 체스판 (True=흰색, False=검은색)
chessboard = [
    [(i + j) % 2 == 0 for j in range(8)]
    for i in range(8)
]

print("체스판 패턴 (□=흰색, ■=검은색):")
for row in chessboard:
    for is_white in row:
        print("□" if is_white else "■", end=" ")
    print()

# 18단계: 데이터 집계
print("\n[18단계] 데이터 집계")
print("-" * 70)

orders = [
    {"item": "사과", "quantity": 10, "price": 1000},
    {"item": "바나나", "quantity": 5, "price": 1500},
    {"item": "사과", "quantity": 3, "price": 1000},
    {"item": "오렌지", "quantity": 7, "price": 2000}
]

# 총 금액 계산
totals = [order["quantity"] * order["price"] for order in orders]
grand_total = sum(totals)

print(f"{'상품':<10} {'수량':<10} {'단가':<12} {'금액':<12}")
print("-" * 44)

for order, total in zip(orders, totals):
    print(f"{order['item']:<10} {order['quantity']:<10} "
          f"{order['price']:>8,}원  {total:>8,}원")

print("-" * 44)
print(f"{'총계':<30} {grand_total:>8,}원")

# 19단계: 중복 제거
print("\n[19단계] 중복 제거")
print("-" * 70)

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]

# 중복 제거 (순서 유지)
unique = []
[unique.append(n) for n in numbers if n not in unique]

print(f"원본: {numbers}")
print(f"중복 제거: {unique}")

# 20단계: 종합 예제 - 성적 처리
print("\n[20단계] 종합 예제 - 성적 처리 시스템")
print("-" * 70)

students = [
    {"name": "김철수", "scores": [85, 90, 88]},
    {"name": "이영희", "scores": [92, 95, 91]},
    {"name": "박민수", "scores": [78, 82, 80]},
    {"name": "정지훈", "scores": [65, 70, 68]}
]

# 평균 계산 및 등급 부여
results = [
    {
        "name": s["name"],
        "avg": sum(s["scores"]) / len(s["scores"]),
        "grade": "A" if sum(s["scores"]) / len(s["scores"]) >= 90 else
                 "B" if sum(s["scores"]) / len(s["scores"]) >= 80 else
                 "C" if sum(s["scores"]) / len(s["scores"]) >= 70 else "D"
    }
    for s in students
]

print(f"{'이름':<10} {'평균':<10} {'등급':<10}")
print("-" * 30)

for result in results:
    print(f"{result['name']:<10} {result['avg']:>6.1f}점  {result['grade']:<10}")

# 우수 학생 (평균 85점 이상)
excellent = [r["name"] for r in results if r["avg"] >= 85]
print(f"\n우수 학생 (평균 85점 이상): {excellent}")

print("\n" + "=" * 70)
print("실습 완료".center(70))
print("=" * 70)
