"""
파일명: break_continue.py
목적: 로그인 시스템 (break와 continue 실습)
"""

# 올바른 비밀번호
correct_password = "1234"
max_attempts = 3

print("===== 로그인 =====")

# 로그인 시도
for attempt in range(max_attempts):
    password = input("비밀번호: ").strip()

    # 빈 입력 처리
    if not password:
        print("빈 입력입니다. 다시 입력하세요.\n")
        continue  # 다음 반복으로

    # 비밀번호 확인
    if password == correct_password:
        print("로그인 성공!")
        print("시스템에 접속합니다...")
        break  # 반복 종료
    else:
        remaining = max_attempts - attempt - 1
        if remaining > 0:
            print(f"틀렸습니다. (남은 횟수: {remaining})\n")
        else:
            print("틀렸습니다.")

else:
    # break 없이 for문이 끝난 경우 (3회 모두 실패)
    print("\n계정이 잠겼습니다.")
    print("관리자에게 문의하세요.")

print("=" * 18)

# 추가 기능: 사용자 이름도 입력받기
print("\n===== 고급 로그인 시스템 =====")

# 사용자 데이터
users = {
    "admin": {"password": "admin123", "name": "관리자"},
    "user1": {"password": "pass123", "name": "김철수"},
    "user2": {"password": "hello", "name": "이영희"}
}

# 사용자 이름 입력
username = input("아이디: ").strip()

if username in users:
    user_data = users[username]

    # 비밀번호 시도
    for attempt in range(max_attempts):
        password = input("비밀번호: ").strip()

        # 빈 입력
        if not password:
            print("비밀번호를 입력하세요.\n")
            continue

        # 확인
        if password == user_data["password"]:
            print(f"\n로그인 성공!")
            print(f"{user_data['name']}님, 환영합니다!")

            # 관리자 권한
            if username == "admin":
                print("\n[관리자 권한]")
                print("- 사용자 관리")
                print("- 시스템 설정")

            break
        else:
            remaining = max_attempts - attempt - 1
            if remaining > 0:
                print(f"비밀번호가 틀렸습니다. (남은 횟수: {remaining})\n")

    else:
        print("\n로그인 실패! 계정이 잠겼습니다.")

else:
    print("존재하지 않는 아이디입니다.")

# 추가 기능: 숫자 맞추기 게임
print("\n===== 숫자 맞추기 게임 =====")
import random

answer = random.randint(1, 100)
max_tries = 7

print("1부터 100 사이의 숫자를 맞춰보세요!")
print(f"기회는 {max_tries}번입니다.\n")

for attempt in range(1, max_tries + 1):
    guess = input(f"시도 {attempt}: ")

    # 숫자 검증
    if not guess.isdigit():
        print("숫자만 입력하세요!\n")
        continue

    guess = int(guess)

    # 범위 검증
    if not 1 <= guess <= 100:
        print("1~100 사이의 숫자를 입력하세요!\n")
        continue

    # 정답 확인
    if guess == answer:
        print(f"\n정답입니다! 🎉")
        print(f"{attempt}번 만에 맞추셨습니다!")
        break
    elif guess < answer:
        print("UP! (더 큰 수)")
    else:
        print("DOWN! (더 작은 수)")

    print()

else:
    print(f"\n게임 오버! 정답은 {answer}였습니다.")

# 추가 기능: 목록에서 검색
print("\n===== 상품 검색 =====")
products = [
    "노트북", "키보드", "마우스", "모니터",
    "헤드셋", "웹캠", "스피커", "마이크"
]

search_keyword = input("검색어: ").strip()

print(f"\n'{search_keyword}' 검색 결과:")
found = False

for product in products:
    if search_keyword in product:
        print(f"- {product}")
        found = True

if not found:
    print("검색 결과가 없습니다.")
