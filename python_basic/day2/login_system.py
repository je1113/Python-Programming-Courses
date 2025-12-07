"""
파일명: login_system.py
목적: 로그인 시스템 (논리 연산자 실습)
"""

# 사용자 데이터베이스 (딕셔너리)
users = {
    "admin": {
        "password": "1234",
        "is_active": True,
        "failed_attempts": 0
    },
    "user1": {
        "password": "pass123",
        "is_active": True,
        "failed_attempts": 2
    },
    "user2": {
        "password": "hello",
        "is_active": False,
        "failed_attempts": 0
    },
    "user3": {
        "password": "test",
        "is_active": True,
        "failed_attempts": 5
    }
}

print("===== 로그인 시스템 =====")

# 사용자 입력
username = input("아이디: ")
password = input("비밀번호: ")

print("-" * 23)

# 로그인 검증
if username in users:
    user = users[username]

    # 로그인 성공 조건 체크
    password_correct = user["password"] == password
    account_active = user["is_active"]
    attempts_ok = user["failed_attempts"] < 5

    # 모든 조건이 참이어야 성공
    if password_correct and account_active and attempts_ok:
        print("로그인 성공!")
        print(f"{username}님, 환영합니다.")

        # 추가 정보
        if username == "admin":
            print("\n[관리자 권한]")
            print("- 사용자 관리")
            print("- 시스템 설정")

    else:
        # 실패 사유 출력
        print("로그인 실패!")

        if not password_correct:
            print("사유: 비밀번호가 일치하지 않습니다")
            user["failed_attempts"] += 1
            remaining = 5 - user["failed_attempts"]
            if remaining > 0:
                print(f"남은 시도 횟수: {remaining}회")
            else:
                print("계정이 잠겼습니다. 관리자에게 문의하세요.")

        elif not account_active:
            print("사유: 계정이 비활성화되었습니다")
            print("관리자에게 문의하세요")

        elif not attempts_ok:
            print("사유: 로그인 시도 횟수 초과")
            print("계정이 잠겼습니다. 관리자에게 문의하세요.")

else:
    print("로그인 실패!")
    print("사유: 존재하지 않는 아이디입니다")

print("=" * 23)

# 추가: 로그인 통계
print("\n===== 시스템 통계 =====")
total_users = len(users)
active_users = sum(1 for user in users.values() if user["is_active"])
locked_users = sum(1 for user in users.values() if user["failed_attempts"] >= 5)

print(f"전체 사용자: {total_users}명")
print(f"활성 계정: {active_users}명")
print(f"잠긴 계정: {locked_users}명")

# 추가: 비밀번호 강도 체크 (입력한 비밀번호)
print("\n===== 비밀번호 강도 =====")
has_number = any(c.isdigit() for c in password)
has_letter = any(c.isalpha() for c in password)
is_long_enough = len(password) >= 8

print(f"길이 (8자 이상): {'✓' if is_long_enough else '✗'}")
print(f"숫자 포함: {'✓' if has_number else '✗'}")
print(f"문자 포함: {'✓' if has_letter else '✗'}")

if is_long_enough and has_number and has_letter:
    print("강도: 강함 🔒")
elif (is_long_enough and has_number) or (is_long_enough and has_letter):
    print("강도: 보통 🔓")
else:
    print("강도: 약함 ⚠️")

# 추가: 로그인 이력 (가상)
if username in users:
    print("\n===== 최근 로그인 이력 =====")
    print("2025-12-05 14:30:25 - 성공")
    print("2025-12-04 09:15:42 - 성공")
    print("2025-12-03 18:45:10 - 실패")
