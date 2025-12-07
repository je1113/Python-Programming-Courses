"""
파일명: list_processing.py
목적: 학생 성적 처리 시스템 (for 문과 리스트 실습)
"""

# 학생 리스트
students = [
    {"name": "김철수", "score": 85},
    {"name": "이영희", "score": 45},
    {"name": "박민수", "score": 92},
    {"name": "정지훈", "score": 58},
    {"name": "최민지", "score": 78},
    {"name": "강호동", "score": 95},
    {"name": "유재석", "score": 42}
]

print("===== 전체 학생 =====")

# 모든 학생 출력
for student in students:
    print(f"{student['name']}: {student['score']}점")

print("-" * 20)

# 합격자 리스트 (60점 이상)
pass_students = [s for s in students if s["score"] >= 60]
print(f"합격자 ({len(pass_students)}명):")
for student in pass_students:
    print(f"- {student['name']}: {student['score']}점")

print("-" * 20)

# 불합격자 리스트
fail_students = [s for s in students if s["score"] < 60]
print(f"불합격자 ({len(fail_students)}명):")
for student in fail_students:
    print(f"- {student['name']}: {student['score']}점")

print("-" * 20)

# 점수 보정 (50점 미만 → 50점으로)
print("점수 보정 후:")
corrected = False

for student in students:
    if student["score"] < 50:
        old_score = student["score"]
        student["score"] = 50
        print(f"{student['name']}: {old_score}점 → {student['score']}점")
        corrected = True

if not corrected:
    print("보정 대상 없음")

print("=" * 20)

# 추가 기능: 통계
print("\n===== 성적 통계 =====")
total_score = sum(s["score"] for s in students)
avg_score = total_score / len(students)
max_student = max(students, key=lambda x: x["score"])
min_student = min(students, key=lambda x: x["score"])

print(f"전체 평균: {avg_score:.2f}점")
print(f"최고 점수: {max_student['name']} ({max_student['score']}점)")
print(f"최저 점수: {min_student['name']} ({min_student['score']}점)")

# 추가 기능: 등급 분포
print("\n===== 등급 분포 =====")
grade_count = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

for student in students:
    score = student["score"]
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    grade_count[grade] += 1

for grade, count in grade_count.items():
    print(f"{grade} 학점: {count}명")

# 추가 기능: 상위 3명
print("\n===== 상위 3명 =====")
top_students = sorted(students, key=lambda x: x["score"], reverse=True)[:3]

for i, student in enumerate(top_students, 1):
    print(f"{i}등: {student['name']} ({student['score']}점)")

# 추가 기능: 점수 구간별 인원
print("\n===== 점수 구간별 인원 =====")
ranges = [(90, 100), (80, 89), (70, 79), (60, 69), (0, 59)]

for low, high in ranges:
    count = len([s for s in students if low <= s["score"] <= high])
    print(f"{low}~{high}점: {count}명")
