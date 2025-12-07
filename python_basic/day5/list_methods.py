"""
파일명: list_methods.py
목적: 할 일 관리 프로그램 (리스트 메서드 실습)
"""

# 할 일 목록
todos = [
    {"task": "보고서 작성", "priority": "높음", "completed": False},
    {"task": "이메일 확인", "priority": "중간", "completed": False},
    {"task": "회의 참석", "priority": "높음", "completed": False},
    {"task": "점심 식사", "priority": "낮음", "completed": False}
]

print("=" * 70)
print("할 일 관리 프로그램 (To-Do List)".center(70))
print("=" * 70)

# 1단계: 현재 할 일 목록 출력
def print_todos():
    """할 일 목록 출력"""
    print(f"\n{'번호':<6} {'할 일':<20} {'우선순위':<10} {'상태':<10}")
    print("-" * 50)

    for i, todo in enumerate(todos, 1):
        task = todo["task"]
        priority = todo["priority"]
        status = "✓ 완료" if todo["completed"] else "○ 미완료"
        print(f"{i:<6} {task:<20} {priority:<10} {status:<10}")

    print("-" * 50)
    print(f"총 {len(todos)}개의 할 일")

print("\n[현재 할 일 목록]")
print_todos()

# 2단계: append() - 할 일 추가
print("\n[2단계] 할 일 추가 (append)")
print("-" * 70)

new_task = {"task": "코드 리뷰", "priority": "중간", "completed": False}
todos.append(new_task)
print(f"추가: '{new_task['task']}'")

print_todos()

# 3단계: insert() - 특정 위치에 긴급 업무 추가
print("\n[3단계] 긴급 업무 삽입 (insert)")
print("-" * 70)

urgent_task = {"task": "긴급 버그 수정", "priority": "높음", "completed": False}
# 맨 앞에 추가 (인덱스 0)
todos.insert(0, urgent_task)
print(f"삽입 (맨 앞): '{urgent_task['task']}'")

print_todos()

# 4단계: extend() - 여러 할 일 한번에 추가
print("\n[4단계] 여러 할 일 추가 (extend)")
print("-" * 70)

additional_tasks = [
    {"task": "운동하기", "priority": "낮음", "completed": False},
    {"task": "독서", "priority": "낮음", "completed": False}
]

todos.extend(additional_tasks)
print(f"{len(additional_tasks)}개의 할 일 추가")

print_todos()

# 5단계: remove() - 완료된 일 제거
print("\n[5단계] 할 일 제거 (remove)")
print("-" * 70)

# 점심 식사 완료
lunch_task = None
for todo in todos:
    if todo["task"] == "점심 식사":
        lunch_task = todo
        break

if lunch_task:
    todos.remove(lunch_task)
    print(f"제거: '{lunch_task['task']}'")

print_todos()

# 6단계: pop() - 마지막 할 일 제거
print("\n[6단계] 마지막 할 일 제거 (pop)")
print("-" * 70)

last_task = todos.pop()
print(f"제거된 할 일: '{last_task['task']}'")

print_todos()

# 7단계: index() - 특정 할 일 찾기
print("\n[7단계] 할 일 검색 (index)")
print("-" * 70)

search_task = "회의 참석"

for i, todo in enumerate(todos):
    if todo["task"] == search_task:
        print(f"'{search_task}'의 위치: {i + 1}번째")
        print(f"우선순위: {todo['priority']}")
        break
else:
    print(f"'{search_task}'를 찾을 수 없습니다.")

# 8단계: count() - 우선순위별 개수
print("\n[8단계] 우선순위별 통계 (count)")
print("-" * 70)

priorities = ["높음", "중간", "낮음"]

print(f"{'우선순위':<10} {'개수':<10} {'그래프':<20}")
print("-" * 40)

for priority in priorities:
    count = sum(1 for todo in todos if todo["priority"] == priority)
    bar = "■" * count
    print(f"{priority:<10} {count:<10} {bar:<20}")

# 9단계: sort() - 우선순위별 정렬
print("\n[9단계] 우선순위별 정렬 (sort)")
print("-" * 70)

# 정렬 기준 정의
priority_order = {"높음": 1, "중간": 2, "낮음": 3}

# 정렬 (원본 변경)
todos.sort(key=lambda x: priority_order[x["priority"]])
print("우선순위 높은 순으로 정렬 완료")

print_todos()

# 10단계: reverse() - 역순 정렬
print("\n[10단계] 역순 정렬 (reverse)")
print("-" * 70)

todos.reverse()
print("리스트를 역순으로 정렬")

print_todos()

# 11단계: copy() - 백업 생성
print("\n[11단계] 할 일 목록 백업 (copy)")
print("-" * 70)

todos_backup = todos.copy()
print(f"백업 생성 완료: {len(todos_backup)}개 항목")

# 백업 확인
print("\n원본과 백업 비교:")
print(f"원본 ID: {id(todos)}")
print(f"백업 ID: {id(todos_backup)}")
print(f"다른 객체: {id(todos) != id(todos_backup)}")

# 12단계: 할 일 완료 처리
print("\n[12단계] 할 일 완료 처리")
print("-" * 70)

complete_task = "이메일 확인"

for todo in todos:
    if todo["task"] == complete_task:
        todo["completed"] = True
        print(f"'{complete_task}' 완료 처리됨")
        break

print_todos()

# 13단계: 완료/미완료 분리
print("\n[13단계] 완료/미완료 분리")
print("-" * 70)

completed_todos = [todo for todo in todos if todo["completed"]]
pending_todos = [todo for todo in todos if not todo["completed"]]

print(f"\n완료된 할 일 ({len(completed_todos)}개):")
for todo in completed_todos:
    print(f"  ✓ {todo['task']}")

print(f"\n미완료 할 일 ({len(pending_todos)}개):")
for todo in pending_todos:
    print(f"  ○ {todo['task']} [{todo['priority']}]")

# 14단계: 우선순위 변경
print("\n[14단계] 우선순위 변경")
print("-" * 70)

change_task = "코드 리뷰"

for todo in todos:
    if todo["task"] == change_task:
        old_priority = todo["priority"]
        todo["priority"] = "높음"
        print(f"'{change_task}' 우선순위 변경: {old_priority} → {todo['priority']}")
        break

print_todos()

# 15단계: 조건부 제거
print("\n[15단계] 완료된 할 일 모두 제거")
print("-" * 70)

# 완료된 할 일 개수 확인
completed_count = sum(1 for todo in todos if todo["completed"])
print(f"완료된 할 일: {completed_count}개")

# 완료되지 않은 것만 남김
todos = [todo for todo in todos if not todo["completed"]]
print(f"완료된 할 일 제거 완료")

print_todos()

# 16단계: 할 일 검색 (부분 일치)
print("\n[16단계] 할 일 검색 (부분 일치)")
print("-" * 70)

keyword = input("검색 키워드: ").strip()

print(f"\n'{keyword}' 검색 결과:")
found_count = 0

for i, todo in enumerate(todos, 1):
    if keyword in todo["task"]:
        print(f"  {i}. {todo['task']} [{todo['priority']}]")
        found_count += 1

if found_count == 0:
    print("  검색 결과가 없습니다.")
else:
    print(f"\n총 {found_count}개 발견")

# 17단계: 통계 요약
print("\n[17단계] 할 일 통계 요약")
print("-" * 70)

total = len(todos)
high_priority = sum(1 for todo in todos if todo["priority"] == "높음")
medium_priority = sum(1 for todo in todos if todo["priority"] == "중간")
low_priority = sum(1 for todo in todos if todo["priority"] == "낮음")
completed = sum(1 for todo in todos if todo["completed"])
pending = total - completed

print(f"총 할 일: {total}개")
print(f"  - 완료: {completed}개 ({completed / total * 100:.0f}%)")
print(f"  - 미완료: {pending}개 ({pending / total * 100:.0f}%)")
print()
print(f"우선순위별:")
print(f"  - 높음: {high_priority}개")
print(f"  - 중간: {medium_priority}개")
print(f"  - 낮음: {low_priority}개")

# 18단계: 정렬된 복사본 생성
print("\n[18단계] 정렬된 복사본 생성 (sorted)")
print("-" * 70)

# 원본은 유지하고 정렬된 새 리스트 생성
sorted_todos = sorted(todos, key=lambda x: x["task"])

print("작업명 알파벳순 정렬:")
for todo in sorted_todos:
    print(f"  - {todo['task']}")

print(f"\n원본 리스트는 유지됨 (첫 번째 항목: {todos[0]['task']})")

# 19단계: 리스트 병합
print("\n[19단계] 백업 목록 병합")
print("-" * 70)

print(f"현재 할 일: {len(todos)}개")
print(f"백업 할 일: {len(todos_backup)}개")

# 중복 제거하며 병합
combined = todos.copy()

for backup_todo in todos_backup:
    # 같은 작업이 없으면 추가
    if not any(todo["task"] == backup_todo["task"] for todo in combined):
        combined.append(backup_todo)

print(f"병합 후: {len(combined)}개")

# 20단계: 최종 요약
print("\n" + "=" * 70)
print("최종 할 일 목록".center(70))
print("=" * 70)

print_todos()

print("\n프로그램 종료")
print("=" * 70)
