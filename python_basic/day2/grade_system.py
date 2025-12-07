"""
파일명: grade_system.py
목적: 성적 등급 시스템 (비교 연산자 실습)
"""

print("===== 성적 관리 시스템 =====")

# 학생 정보 입력
student_name = input("학생 이름: ")
score_input = input("점수: ")

# 점수를 숫자로 변환
score = int(score_input)

# 점수 유효성 검증
if 0 <= score <= 100:
    # 학점 판정
    if score >= 90:
        grade = "A"
        grade_desc = "최우수"
    elif score >= 80:
        grade = "B"
        grade_desc = "우수"
    elif score >= 70:
        grade = "C"
        grade_desc = "보통"
    elif score >= 60:
        grade = "D"
        grade_desc = "미흡"
    else:
        grade = "F"
        grade_desc = "불합격"

    # 합격 여부 (60점 이상)
    pass_status = "합격" if score >= 60 else "불합격"

    # 결과 출력
    print("-" * 25)
    print(f"학생명: {student_name}")
    print(f"점수: {score}점")
    print(f"학점: {grade}")
    print(f"평가: {grade_desc}")
    print(f"합격 여부: {pass_status}")
    print("=" * 25)

    # 추가 정보
    if score >= 95:
        print("\n장학금 대상자입니다! 🎉")
    elif score >= 85:
        print("\n우수 학생입니다!")

    # 다음 등급까지 필요한 점수
    if grade == "B":
        points_needed = 90 - score
        print(f"\nA 학점까지 {points_needed}점 부족합니다")
    elif grade == "C":
        points_needed = 80 - score
        print(f"\nB 학점까지 {points_needed}점 부족합니다")
    elif grade == "D":
        points_needed = 70 - score
        print(f"\nC 학점까지 {points_needed}점 부족합니다")
    elif grade == "F":
        points_needed = 60 - score
        print(f"\n합격까지 {points_needed}점 부족합니다")

else:
    print("-" * 25)
    print("오류: 0~100 사이의 점수를 입력하세요!")
    print("=" * 25)

# 추가: 여러 학생 성적 비교
print("\n===== 전체 학생 비교 =====")

# 다른 학생들의 점수 (예시)
class_scores = [85, 92, 78, 95, 88, 76, 90, 82]

if 0 <= score <= 100:
    # 평균 계산
    class_average = sum(class_scores) / len(class_scores)

    # 현재 학생 점수 추가
    all_scores = class_scores + [score]

    # 순위 계산
    all_scores_sorted = sorted(all_scores, reverse=True)
    rank = all_scores_sorted.index(score) + 1

    print(f"학급 평균: {class_average:.2f}점")
    print(f"{student_name}의 순위: {rank}등 / {len(all_scores)}명")

    # 평균과 비교
    diff = score - class_average
    if diff > 0:
        print(f"평균보다 {diff:.2f}점 높습니다")
    elif diff < 0:
        print(f"평균보다 {abs(diff):.2f}점 낮습니다")
    else:
        print("평균과 동일합니다")

    # 상위 퍼센트
    percent = (rank / len(all_scores)) * 100
    print(f"상위 {percent:.1f}%")
