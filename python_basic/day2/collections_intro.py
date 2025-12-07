"""
파일명: collections_intro.py
목적: 리스트, 튜플, 딕셔너리 기초 (자료형 심화 실습)
"""

# 학생 정보를 딕셔너리로 저장
student1 = {
    "name": "김철수",
    "korean": 85,
    "english": 90,
    "math": 88
}

student2 = {
    "name": "이영희",
    "korean": 92,
    "english": 88,
    "math": 95
}

student3 = {
    "name": "박민수",
    "korean": 78,
    "english": 85,
    "math": 80
}

# 학생 리스트
students = [student1, student2, student3]

print("===== 학생 성적 관리 =====")

# 각 학생의 총점과 평균 계산
for i, student in enumerate(students, 1):
    name = student["name"]
    korean = student["korean"]
    english = student["english"]
    math = student["math"]

    total = korean + english + math
    average = total / 3

    print(f"\n[학생 {i}]")
    print(f"이름: {name}")
    print(f"국어: {korean}점")
    print(f"영어: {english}점")
    print(f"수학: {math}점")
    print(f"총점: {total}점")
    print(f"평균: {average:.2f}점")
    print("-" * 22)

# 전체 학생의 평균 계산
all_scores = []
for student in students:
    total = student["korean"] + student["english"] + student["math"]
    average = total / 3
    all_scores.append(average)

overall_average = sum(all_scores) / len(all_scores)
print(f"\n전체 평균: {overall_average:.2f}점")

# 가장 높은 점수를 받은 학생 찾기
max_average = max(all_scores)
max_index = all_scores.index(max_average)
best_student = students[max_index]

print(f"최고 득점자: {best_student['name']} (평균 {max_average:.2f}점)")
print("=" * 24)

# 추가: 튜플 사용 예시
print("\n===== 튜플 활용 예시 =====")
# 학생 정보를 튜플로 반환
def get_student_summary(student):
    name = student["name"]
    total = student["korean"] + student["english"] + student["math"]
    average = total / 3
    return (name, total, average)  # 튜플 반환

# 언패킹
name, total, avg = get_student_summary(student1)
print(f"{name}: 총점 {total}, 평균 {avg:.2f}")
