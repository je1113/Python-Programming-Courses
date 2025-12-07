"""
파일명: session2_encapsulation.py
목적: 캡슐화와 정보 은닉 실습
"""

print("=" * 70)
print("캡슐화와 정보 은닉".center(70))
print("=" * 70)

# 1. 기본 개념
print("\n[1] Private 변수 (__variable)")
print("-" * 70)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # public
        self.__balance = balance  # private (__)

    def get_balance(self):
        """잔액 조회 (Getter)"""
        return self.__balance

    def deposit(self, amount):
        """입금"""
        if amount > 0:
            self.__balance += amount
            print(f"{amount:,}원 입금 완료. 잔액: {self.__balance:,}원")
        else:
            print("입금액은 0보다 커야 합니다!")

    def withdraw(self, amount):
        """출금"""
        if amount > self.__balance:
            print("잔액 부족!")
        elif amount <= 0:
            print("출금액은 0보다 커야 합니다!")
        else:
            self.__balance -= amount
            print(f"{amount:,}원 출금 완료. 잔액: {self.__balance:,}원")

# 계좌 생성
account = BankAccount("김철수", 100000)

# ✅ Getter로 조회
print(f"잔액: {account.get_balance():,}원")

# ❌ 직접 접근 시도
try:
    print(account.__balance)  # AttributeError!
except AttributeError as e:
    print(f"✗ 오류: {e}")

# Name Mangling으로는 접근 가능 (비추천!)
print(f"Name Mangling: {account._BankAccount__balance:,}원")

account.deposit(50000)
account.withdraw(30000)

# 2. Protected 변수 (_variable)
print("\n[2] Protected 변수 (_variable)")
print("-" * 70)

class Employee:
    def __init__(self, name, salary):
        self.name = name  # public
        self._salary = salary  # protected (관례상 내부용)

    def _calculate_bonus(self):
        """내부 메서드 (관례상 외부에서 호출 안함)"""
        return self._salary * 0.1

    def get_total_pay(self):
        """공개 메서드"""
        bonus = self._calculate_bonus()
        return self._salary + bonus

emp = Employee("김철수", 3500)

# public 메서드는 자유롭게 호출
print(f"총 급여: {emp.get_total_pay():,}만원")

# protected는 접근 가능하지만 관례상 사용 자제
print(f"기본급(protected): {emp._salary:,}만원")  # 가능하지만 비추천

# 3. 실습: 급여 관리 클래스
print("\n[3] 실습: 직원 급여 관리")
print("-" * 70)

class EmployeeManagement:
    MIN_SALARY = 1000  # 최소 급여 (클래스 변수)

    def __init__(self, name, salary):
        self.name = name
        self.__salary = 0
        self.set_salary(salary)  # Setter를 통한 검증

    def get_salary(self):
        """급여 조회 (Getter)"""
        return self.__salary

    def set_salary(self, amount):
        """급여 설정 (Setter + 검증)"""
        if amount < EmployeeManagement.MIN_SALARY:
            raise ValueError(f"급여는 {EmployeeManagement.MIN_SALARY:,}만원 이상이어야 합니다!")
        self.__salary = amount
        print(f"✓ {self.name}님 급여 설정: {self.__salary:,}만원")

    def give_raise(self, percentage):
        """급여 인상 (검증 포함)"""
        if not 0 <= percentage <= 100:
            raise ValueError("인상률은 0~100% 사이여야 합니다!")

        increase = int(self.__salary * (percentage / 100))
        old_salary = self.__salary
        self.__salary += increase

        print(f"✓ {self.name}님 급여 {percentage}% 인상")
        print(f"  {old_salary:,}만원 → {self.__salary:,}만원 (+{increase:,}만원)")

    def display_info(self):
        """정보 출력"""
        print(f"{self.name}: {self.__salary:,}만원")

# 직원 생성
print()
emp1 = EmployeeManagement("김철수", 3500)
emp2 = EmployeeManagement("이영희", 4200)

print()

# 급여 인상
emp1.give_raise(10)
emp2.give_raise(15)

print()

# 정보 출력
emp1.display_info()
emp2.display_info()

# 잘못된 급여 설정 시도
print()
try:
    emp3 = EmployeeManagement("박민수", 500)  # 최소 급여 미달
except ValueError as e:
    print(f"✗ 오류: {e}")

# 잘못된 인상률
try:
    emp1.give_raise(150)  # 150% 불가
except ValueError as e:
    print(f"✗ 오류: {e}")

# 4. Private 메서드
print("\n[4] Private 메서드")
print("-" * 70)

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = self.__hash_password(password)  # private 메서드 사용

    def __hash_password(self, password):
        """비밀번호 해싱 (private 메서드)"""
        # 실제로는 hashlib 사용하지만 여기서는 간단히
        return "hashed_" + password

    def verify_password(self, password):
        """비밀번호 검증 (public 메서드)"""
        hashed = self.__hash_password(password)
        return self.__password == hashed

    def change_password(self, old_password, new_password):
        """비밀번호 변경"""
        if not self.verify_password(old_password):
            print("✗ 현재 비밀번호가 일치하지 않습니다!")
            return False

        self.__password = self.__hash_password(new_password)
        print("✓ 비밀번호가 변경되었습니다")
        return True

# 사용자 생성
user = User("john", "password123")

# 비밀번호 검증
print(f"비밀번호 검증 (올바른 비밀번호): {user.verify_password('password123')}")
print(f"비밀번호 검증 (잘못된 비밀번호): {user.verify_password('wrong')}")

# 비밀번호 변경
print()
user.change_password("password123", "newpassword456")
print(f"새 비밀번호 검증: {user.verify_password('newpassword456')}")

# 5. 캡슐화의 이점
print("\n[5] 캡슐화의 이점: 내부 구현 변경")
print("-" * 70)

class TemperatureSensor:
    """온도 센서 (내부 구현 숨김)"""

    def __init__(self):
        self.__celsius = 25.0  # 내부적으로 섭씨 저장

    def get_celsius(self):
        """섭씨 온도"""
        return self.__celsius

    def get_fahrenheit(self):
        """화씨 온도 (자동 변환)"""
        return self.__celsius * 9/5 + 32

    def set_celsius(self, value):
        """섭씨 온도 설정"""
        if value < -273.15:
            raise ValueError("절대영도 이하입니다!")
        self.__celsius = value

sensor = TemperatureSensor()

print(f"섭씨: {sensor.get_celsius()}°C")
print(f"화씨: {sensor.get_fahrenheit()}°F")

sensor.set_celsius(30)
print(f"\n온도 변경 후:")
print(f"섭씨: {sensor.get_celsius()}°C")
print(f"화씨: {sensor.get_fahrenheit()}°F")

# 6. 실무 예제: 쇼핑 카트
print("\n[6] 실무 예제: 쇼핑 카트")
print("-" * 70)

class ShoppingCart:
    def __init__(self, owner):
        self.owner = owner
        self.__items = []  # private (외부에서 직접 수정 불가)
        self.__total_price = 0  # private

    def add_item(self, name, price, quantity=1):
        """상품 추가 (검증 포함)"""
        if price < 0:
            raise ValueError("가격은 0 이상이어야 합니다!")
        if quantity < 1:
            raise ValueError("수량은 1 이상이어야 합니다!")

        item = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        self.__items.append(item)
        self.__total_price += price * quantity

        print(f"✓ '{name}' {quantity}개 추가 ({price * quantity:,}원)")

    def remove_item(self, name):
        """상품 제거"""
        for item in self.__items:
            if item["name"] == name:
                self.__total_price -= item["price"] * item["quantity"]
                self.__items.remove(item)
                print(f"✓ '{name}' 제거됨")
                return True

        print(f"✗ '{name}'을(를) 찾을 수 없습니다")
        return False

    def get_total_price(self):
        """총 금액 조회 (Getter)"""
        return self.__total_price

    def get_item_count(self):
        """상품 개수"""
        return len(self.__items)

    def clear(self):
        """장바구니 비우기"""
        self.__items = []
        self.__total_price = 0
        print("✓ 장바구니가 비워졌습니다")

    def show_cart(self):
        """장바구니 내용"""
        print(f"\n{'='*60}")
        print(f"{self.owner}님의 장바구니")
        print(f"{'='*60}")

        if not self.__items:
            print("장바구니가 비어 있습니다")
            return

        print(f"{'상품명':<20} {'단가':<15} {'수량':<10} {'소계':<15}")
        print("-" * 60)

        for item in self.__items:
            subtotal = item["price"] * item["quantity"]
            print(f"{item['name']:<20} {item['price']:>10,}원  "
                  f"{item['quantity']:>5}개  {subtotal:>10,}원")

        print("-" * 60)
        print(f"{'총 금액':<20} {'':<15} {'':<10} {self.__total_price:>10,}원")

# 쇼핑 카트 사용
cart = ShoppingCart("김철수")

cart.add_item("노트북", 1200000)
cart.add_item("마우스", 30000, 2)
cart.add_item("키보드", 89000)

cart.show_cart()

print()
cart.remove_item("마우스")

cart.show_cart()

print(f"\n총 금액: {cart.get_total_price():,}원")
print(f"상품 개수: {cart.get_item_count()}개")

# 7. Getter/Setter 패턴
print("\n[7] Getter/Setter 패턴")
print("-" * 70)

class Rectangle:
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.set_width(width)
        self.set_height(height)

    def get_width(self):
        """너비 조회"""
        return self.__width

    def set_width(self, value):
        """너비 설정 (검증)"""
        if value <= 0:
            raise ValueError("너비는 양수여야 합니다!")
        self.__width = value

    def get_height(self):
        """높이 조회"""
        return self.__height

    def set_height(self, value):
        """높이 설정 (검증)"""
        if value <= 0:
            raise ValueError("높이는 양수여야 합니다!")
        self.__height = value

    def get_area(self):
        """넓이"""
        return self.__width * self.__height

    def get_perimeter(self):
        """둘레"""
        return 2 * (self.__width + self.__height)

rect = Rectangle(10, 20)

print(f"너비: {rect.get_width()}")
print(f"높이: {rect.get_height()}")
print(f"넓이: {rect.get_area()}")
print(f"둘레: {rect.get_perimeter()}")

# 크기 변경
rect.set_width(15)
rect.set_height(25)

print(f"\n크기 변경 후:")
print(f"너비: {rect.get_width()}")
print(f"높이: {rect.get_height()}")
print(f"넓이: {rect.get_area()}")

# 잘못된 값 설정
try:
    rect.set_width(-10)
except ValueError as e:
    print(f"\n✗ 오류: {e}")

print("\n" + "=" * 70)
print("핵심 정리".center(70))
print("=" * 70)

print("""
✅ 캡슐화의 목적:
  1. 데이터 보호 (잘못된 값 설정 방지)
  2. 내부 구현 숨김 (구현 변경해도 외부 영향 없음)
  3. 유지보수성 향상

✅ Python 접근 제어:
  - public: variable (어디서든 접근 가능)
  - protected: _variable (관례상 내부용)
  - private: __variable (Name Mangling)

✅ Getter/Setter 패턴:
  - get_xxx(): 값 조회
  - set_xxx(): 값 설정 + 검증
  - __init__에서도 Setter 사용해서 검증!

⚠️  주의:
  - Python은 진정한 private 아님 (Name Mangling으로 접근 가능)
  - 관례를 따르는 것이 중요!
""")

print("\n💡 Tip: 다음 세션에서 @property로 더 우아하게 구현합니다!")
