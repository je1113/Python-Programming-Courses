"""
파일명: text_file.py
목적: 텍스트 파일 읽기/쓰기 실습
"""

print("=" * 70)
print("텍스트 파일 처리 실습".center(70))
print("=" * 70)

# 1. 로그 파일 생성
print("\n[1] 로그 파일 생성")
print("-" * 70)

log_data = """[2024-01-15 09:00:00] INFO: 시스템 시작
[2024-01-15 09:05:12] INFO: 사용자 로그인 - user123
[2024-01-15 09:10:33] WARNING: 메모리 사용량 80% 도달
[2024-01-15 09:15:45] ERROR: 데이터베이스 연결 실패
[2024-01-15 09:20:01] INFO: 재시도 성공
[2024-01-15 09:25:18] ERROR: 파일을 찾을 수 없음 - data.csv
[2024-01-15 09:30:22] WARNING: 디스크 공간 부족 (10% 남음)
[2024-01-15 09:35:40] INFO: 백업 시작
[2024-01-15 09:40:55] INFO: 백업 완료
[2024-01-15 09:45:10] ERROR: API 요청 실패 - timeout
"""

# 파일 쓰기
with open("app.log", "w", encoding="utf-8") as f:
    f.write(log_data)

print("✓ app.log 파일 생성 완료")

# 2. 파일 읽기 - 전체 읽기
print("\n[2] 파일 전체 읽기")
print("-" * 70)

with open("app.log", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 3. 파일 읽기 - 한 줄씩 읽기
print("\n[3] 한 줄씩 읽기")
print("-" * 70)

with open("app.log", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(f"{i:2}. {line.strip()}")

# 4. 에러 로그만 필터링
print("\n[4] 에러 로그 필터링")
print("-" * 70)

error_logs = []

with open("app.log", "r", encoding="utf-8") as f:
    for line in f:
        if "ERROR" in line:
            error_logs.append(line.strip())

print(f"에러 로그: {len(error_logs)}건\n")
for i, log in enumerate(error_logs, 1):
    print(f"{i}. {log}")

# 5. 에러 로그를 별도 파일로 저장
print("\n[5] 에러 로그 저장")
print("-" * 70)

with open("errors.log", "w", encoding="utf-8") as f:
    f.write("===== ERROR LOGS =====\n")
    f.write(f"Total: {len(error_logs)} errors\n\n")
    for log in error_logs:
        f.write(log + "\n")

print("✓ errors.log 파일 생성 완료")

# 6. 로그 통계 계산
print("\n[6] 로그 통계")
print("-" * 70)

stats = {"INFO": 0, "WARNING": 0, "ERROR": 0}

with open("app.log", "r", encoding="utf-8") as f:
    for line in f:
        for level in stats.keys():
            if level in line:
                stats[level] += 1

print(f"{'레벨':<10} {'개수':<10} {'비율':<10}")
print("-" * 30)

total = sum(stats.values())
for level, count in stats.items():
    ratio = (count / total * 100) if total > 0 else 0
    print(f"{level:<10} {count:<10} {ratio:>5.1f}%")

# 7. 파일에 추가하기 (append)
print("\n[7] 로그 추가")
print("-" * 70)

new_logs = [
    "[2024-01-15 09:50:00] INFO: 새로운 작업 시작\n",
    "[2024-01-15 09:55:15] INFO: 작업 완료\n"
]

with open("app.log", "a", encoding="utf-8") as f:
    f.writelines(new_logs)

print(f"✓ {len(new_logs)}개의 로그 추가 완료")

# 8. 설정 파일 읽기
print("\n[8] 설정 파일 처리")
print("-" * 70)

# 설정 파일 생성
config_data = """# 애플리케이션 설정
database_host=localhost
database_port=5432
database_name=myapp
log_level=INFO
max_connections=100
"""

with open("config.txt", "w", encoding="utf-8") as f:
    f.write(config_data)

# 설정 파일 읽기 및 파싱
config = {}

with open("config.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        # 주석과 빈 줄 건너뛰기
        if not line or line.startswith("#"):
            continue

        if "=" in line:
            key, value = line.split("=", 1)
            config[key.strip()] = value.strip()

print("설정 값:")
for key, value in config.items():
    print(f"  {key}: {value}")

# 9. 여러 줄 데이터 처리
print("\n[9] 학생 성적 파일")
print("-" * 70)

# 성적 데이터 파일 생성
grades_data = """김철수 85 90 88
이영희 92 95 91
박민수 78 82 80
정지훈 88 85 90
최민지 95 93 96
"""

with open("grades.txt", "w", encoding="utf-8") as f:
    f.write(grades_data)

# 성적 파일 읽고 분석
print(f"{'이름':<10} {'국어':<6} {'영어':<6} {'수학':<6} {'평균':<8}")
print("-" * 40)

with open("grades.txt", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) == 4:
            name = parts[0]
            korean = int(parts[1])
            english = int(parts[2])
            math = int(parts[3])
            avg = (korean + english + math) / 3

            print(f"{name:<10} {korean:<6} {english:<6} {math:<6} {avg:<8.1f}")

# 10. 파일 존재 확인 및 안전한 처리
print("\n[10] 파일 존재 확인")
print("-" * 70)

import os

files_to_check = ["app.log", "errors.log", "nonexistent.txt", "config.txt"]

print(f"{'파일명':<20} {'존재 여부':<15} {'크기':<10}")
print("-" * 45)

for filename in files_to_check:
    exists = os.path.exists(filename)
    if exists:
        size = os.path.getsize(filename)
        status = "✓ 존재"
        size_str = f"{size} bytes"
    else:
        status = "✗ 없음"
        size_str = "-"

    print(f"{filename:<20} {status:<15} {size_str:<10}")

# 11. 대용량 파일 처리 (한 줄씩)
print("\n[11] 대용량 파일 처리 예제")
print("-" * 70)

# 큰 로그 파일 생성 (시뮬레이션)
with open("large.log", "w", encoding="utf-8") as f:
    for i in range(1000):
        f.write(f"[LOG-{i:04d}] 작업 처리 중...\n")

print("✓ 1000줄 로그 파일 생성")

# 메모리 효율적으로 처리
count = 0
with open("large.log", "r", encoding="utf-8") as f:
    for line in f:
        count += 1
        # 실제로는 각 줄 처리...

print(f"✓ {count}줄 처리 완료 (메모리 효율적)")

# 12. 파일 내용 수정
print("\n[12] 파일 내용 수정")
print("-" * 70)

# 원본 읽기
with open("config.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 수정
modified_lines = []
for line in lines:
    if line.startswith("log_level"):
        modified_lines.append("log_level=DEBUG\n")
    else:
        modified_lines.append(line)

# 저장
with open("config.txt", "w", encoding="utf-8") as f:
    f.writelines(modified_lines)

print("✓ config.txt 수정 완료 (log_level → DEBUG)")

# 13. 결과 리포트 생성
print("\n[13] 결과 리포트 생성")
print("-" * 70)

report = f"""
{'='*50}
{'로그 분석 리포트'.center(50)}
{'='*50}

[파일 정보]
- 로그 파일: app.log
- 분석 일시: 2024-01-15 10:00:00

[통계]
- 전체 로그: {sum(stats.values())}건
- INFO: {stats['INFO']}건
- WARNING: {stats['WARNING']}건
- ERROR: {stats['ERROR']}건

[에러 목록]
"""

for i, log in enumerate(error_logs, 1):
    report += f"{i}. {log}\n"

report += f"\n{'='*50}\n"

# 리포트 저장
with open("report.txt", "w", encoding="utf-8") as f:
    f.write(report)

print("✓ report.txt 생성 완료")
print("\n리포트 내용:")
print(report)

# 14. 정리
print("\n[14] 생성된 파일 목록")
print("-" * 70)

created_files = ["app.log", "errors.log", "config.txt", "grades.txt",
                 "large.log", "report.txt"]

print("생성된 파일:")
for i, filename in enumerate(created_files, 1):
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        print(f"  {i}. {filename} ({size:,} bytes)")

print("\n" + "=" * 70)
print("텍스트 파일 처리 완료".center(70))
print("=" * 70)

print("\n💡 Tip: 생성된 파일들을 직접 열어서 확인해보세요!")
