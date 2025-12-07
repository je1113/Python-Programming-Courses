"""
파일명: session8_property.py
목적: 프로퍼티 (@property) 실습
"""

print("=" * 70)
print("프로퍼티 (@property)".center(70))
print("=" * 70)

# 1. Getter/Setter 없이 vs @property
print("\n[1] Getter/Setter 없이 vs @property")
print("-" * 70)

# ❌ 검증 없이 (문제 발생 가능)
class Employee1:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary  # 음수도 설정 가능!

emp1 = Employee1("김철수", -1000)  # 잘못된 값!
print(f"급여: {emp1.salary}만원")  # -1000만원?!

# ✅ @property 사용 (검증 포함)
class Employee2:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary  # setter 호출

    @property
    def salary(self):
        """급여 조회 (Getter)"""
        return self._salary

    @salary.setter
    def salary(self, value):
        """급여 설정 (Setter + 검증)"""
        if value < 0:
            raise ValueError("급여는 0 이상이어야 합니다!")
        self._salary = value

emp2 = Employee2("이영희", 3500)
print(f"급여: {emp2.salary}만원")

# 잘못된 값 설정 시도
try:
    emp2.salary = -1000
except ValueError as e:
    print(f"✗ 오류: {e}")

# 2. 읽기 전용 프로퍼티
print("\n[2] 읽기 전용 프로퍼티")
print("-" * 70)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        """지름 (읽기 전용)"""
        return self.radius * 2

    @property
    def area(self):
        """넓이 (읽기 전용)"""
        import math
        return math.pi * self.radius ** 2

    @property
    def circumference(self):
        """둘레 (읽기 전용)"""
        import math
        return 2 * math.pi * self.radius

circle = Circle(10)

print(f"반지름: {circle.radius}")
print(f"지름: {circle.diameter}")
print(f"넓이: {circle.area:.2f}")
print(f"둘레: {circle.circumference:.2f}")

# 읽기 전용이므로 설정 불가
try:
    circle.diameter = 20
except AttributeError as e:
    print(f"\n✗ 오류: can't set attribute")

# 3. 실습: Rectangle 클래스
print("\n[3] 실습: Rectangle 클래스")
print("-" * 70)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        """너비 조회"""
        return self._width

    @width.setter
    def width(self, value):
        """너비 설정 (검증)"""
        if value <= 0:
            raise ValueError("너비는 양수여야 합니다!")
        self._width = value

    @property
    def height(self):
        """높이 조회"""
        return self._height

    @height.setter
    def height(self, value):
        """높이 설정 (검증)"""
        if value <= 0:
            raise ValueError("높이는 양수여야 합니다!")
        self._height = value

    @property
    def area(self):
        """넓이 (읽기 전용, 자동 계산)"""
        return self._width * self._height

    @property
    def perimeter(self):
        """둘레 (읽기 전용, 자동 계산)"""
        return 2 * (self._width + self._height)

# 사각형 생성
rect = Rectangle(10, 20)

print(f"너비: {rect.width}")
print(f"높이: {rect.height}")
print(f"넓이: {rect.area}")
print(f"둘레: {rect.perimeter}")

# 크기 변경
rect.width = 15
rect.height = 25

print(f"\n크기 변경 후:")
print(f"너비: {rect.width}")
print(f"높이: {rect.height}")
print(f"넓이: {rect.area}")
print(f"둘레: {rect.perimeter}")

# 잘못된 값 설정
try:
    rect.width = -10
except ValueError as e:
    print(f"\n✗ 오류: {e}")

# 4. 프로퍼티로 데이터 검증
print("\n[4] 프로퍼티로 데이터 검증")
print("-" * 70)

class User:
    def __init__(self, email, age):
        self.email = email
        self.age = age

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        """이메일 검증"""
        if "@" not in value:
            raise ValueError("올바른 이메일 형식이 아닙니다!")
        self._email = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        """나이 검증"""
        if not 0 <= value <= 150:
            raise ValueError("나이는 0~150 사이여야 합니다!")
        self._age = value

    @property
    def is_adult(self):
        """성인 여부 (읽기 전용)"""
        return self._age >= 19

# 사용자 생성
user = User("john@example.com", 25)

print(f"이메일: {user.email}")
print(f"나이: {user.age}세")
print(f"성인 여부: {user.is_adult}")

# 검증 테스트
print()
try:
    user.email = "invalid-email"
except ValueError as e:
    print(f"✗ 이메일 오류: {e}")

try:
    user.age = 200
except ValueError as e:
    print(f"✗ 나이 오류: {e}")

# 5. 온도 변환 클래스
print("\n[5] 온도 변환 클래스")
print("-" * 70)

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        """섭씨 온도"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """섭씨 온도 설정 (검증)"""
        if value < -273.15:
            raise ValueError("절대영도(-273.15°C) 이하입니다!")
        self._celsius = value

    @property
    def fahrenheit(self):
        """화씨 온도 (자동 변환)"""
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """화씨 온도로 설정"""
        self.celsius = (value - 32) * 5/9

    @property
    def kelvin(self):
        """켈빈 온도 (자동 변환)"""
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value):
        """켈빈 온도로 설정"""
        self.celsius = value - 273.15

# 온도 변환
temp = Temperature(25)

print(f"섭씨: {temp.celsius}°C")
print(f"화씨: {temp.fahrenheit}°F")
print(f"켈빈: {temp.kelvin}K")

# 화씨로 설정
temp.fahrenheit = 86

print(f"\n화씨 86°F로 설정:")
print(f"섭씨: {temp.celsius}°C")
print(f"화씨: {temp.fahrenheit}°F")
print(f"켈빈: {temp.kelvin}K")

# 6. 계좌 클래스
print("\n[6] 계좌 클래스")
print("-" * 70)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
        self._transactions = []

    @property
    def balance(self):
        """잔액 조회"""
        return self._balance

    @property
    def transactions(self):
        """거래 내역 (읽기 전용)"""
        return self._transactions.copy()  # 복사본 반환

    def deposit(self, amount):
        """입금"""
        if amount <= 0:
            raise ValueError("입금액은 0보다 커야 합니다!")

        self._balance += amount
        self._transactions.append(f"입금: +{amount:,}원")
        print(f"{amount:,}원 입금. 잔액: {self._balance:,}원")

    def withdraw(self, amount):
        """출금"""
        if amount > self._balance:
            raise ValueError("잔액이 부족합니다!")
        if amount <= 0:
            raise ValueError("출금액은 0보다 커야 합니다!")

        self._balance -= amount
        self._transactions.append(f"출금: -{amount:,}원")
        print(f"{amount:,}원 출금. 잔액: {self._balance:,}원")

# 계좌 사용
account = BankAccount("김철수", 100000)

print(f"초기 잔액: {account.balance:,}원")

account.deposit(50000)
account.withdraw(30000)

print(f"\n현재 잔액: {account.balance:,}원")
print("\n거래 내역:")
for i, trans in enumerate(account.transactions, 1):
    print(f"  {i}. {trans}")

# 잔액 직접 수정 불가
try:
    account.balance = 1000000  # AttributeError!
except AttributeError:
    print("\n✗ 잔액 직접 수정 불가!")

# 7. Lazy Property (지연 평가)
print("\n[7] Lazy Property (지연 평가)")
print("-" * 70)

class DataProcessor:
    def __init__(self, data):
        self.data = data
        self._processed_data = None

    @property
    def processed_data(self):
        """처리된 데이터 (처음 접근시에만 계산)"""
        if self._processed_data is None:
            print("데이터 처리 중... (시간이 걸림)")
            # 무거운 연산 시뮬레이션
            self._processed_data = [x ** 2 for x in self.data]

        return self._processed_data

# 데이터 프로세서
processor = DataProcessor([1, 2, 3, 4, 5])

print("데이터 처리기 생성 완료")
print()

# 첫 번째 접근 (실제 계산)
print("첫 번째 접근:")
print(processor.processed_data)

# 두 번째 접근 (캐시 사용)
print("\n두 번째 접근:")
print(processor.processed_data)

# 8. 실무 예제: Product 클래스
print("\n[8] 실무 예제: Product 클래스")
print("-" * 70)

class Product:
    TAX_RATE = 0.1  # 세금 10%

    def __init__(self, name, price, discount_rate=0):
        self.name = name
        self.price = price
        self.discount_rate = discount_rate

    @property
    def price(self):
        """가격"""
        return self._price

    @price.setter
    def price(self, value):
        """가격 설정 (검증)"""
        if value < 0:
            raise ValueError("가격은 0 이상이어야 합니다!")
        self._price = value

    @property
    def discount_rate(self):
        """할인율"""
        return self._discount_rate

    @discount_rate.setter
    def discount_rate(self, value):
        """할인율 설정 (검증)"""
        if not 0 <= value <= 1:
            raise ValueError("할인율은 0~1 사이여야 합니다!")
        self._discount_rate = value

    @property
    def discount_amount(self):
        """할인 금액 (읽기 전용)"""
        return int(self._price * self._discount_rate)

    @property
    def sale_price(self):
        """판매 가격 (읽기 전용)"""
        return self._price - self.discount_amount

    @property
    def tax_amount(self):
        """세금 (읽기 전용)"""
        return int(self.sale_price * Product.TAX_RATE)

    @property
    def final_price(self):
        """최종 가격 (판매가 + 세금)"""
        return self.sale_price + self.tax_amount

    def __str__(self):
        return (f"{self.name}\n"
                f"  정가: {self._price:,}원\n"
                f"  할인: -{self.discount_amount:,}원 ({self._discount_rate*100}%)\n"
                f"  판매가: {self.sale_price:,}원\n"
                f"  세금: +{self.tax_amount:,}원\n"
                f"  최종가: {self.final_price:,}원")

# 상품 생성
product = Product("노트북", 1200000, 0.15)  # 15% 할인
print(product)

# 가격 변경
print("\n가격 20% 인하:")
product.price = 960000
print(product)

# 9. 프로퍼티 vs 일반 메서드
print("\n[9] 프로퍼티 vs 일반 메서드")
print("-" * 70)

class Example:
    def __init__(self, value):
        self._value = value

    # 프로퍼티 (속성처럼 사용)
    @property
    def value_property(self):
        return self._value

    # 일반 메서드 (함수처럼 호출)
    def get_value_method(self):
        return self._value

ex = Example(100)

# 프로퍼티: 속성처럼 접근
print(f"프로퍼티: {ex.value_property}")  # 괄호 없음

# 메서드: 함수처럼 호출
print(f"메서드: {ex.get_value_method()}")  # 괄호 필요

print("""
💡 프로퍼티를 사용할 때:
  - 단순 계산 (복잡한 로직 X)
  - 속성처럼 자연스럽게 접근
  - 부수 효과 없음

💡 메서드를 사용할 때:
  - 복잡한 연산
  - 매개변수 필요
  - 부수 효과 있음 (파일 저장 등)
""")

# 10. @property.deleter
print("\n[10] @property.deleter")
print("-" * 70)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("나이는 0 이상이어야 합니다!")
        self._age = value

    @age.deleter
    def age(self):
        """나이 삭제"""
        print("나이 정보 삭제")
        del self._age

person = Person("김철수", 25)
print(f"이름: {person.name}, 나이: {person.age}")

# 프로퍼티 삭제
del person.age

try:
    print(person.age)
except AttributeError:
    print("나이 정보가 삭제되었습니다")

print("\n" + "=" * 70)
print("핵심 정리".center(70))
print("=" * 70)

print("""
✅ @property의 장점:
  1. 속성처럼 사용 (obj.attr)
  2. 검증 로직 추가 가능
  3. 계산된 속성 구현
  4. 리팩토링 쉬움

✅ 패턴:
  # Getter
  @property
  def attr(self):
      return self._attr

  # Setter
  @attr.setter
  def attr(self, value):
      # 검증
      self._attr = value

  # Deleter
  @attr.deleter
  def attr(self):
      del self._attr

✅ 사용 시기:
  - 데이터 검증 필요할 때
  - 계산된 속성 (읽기 전용)
  - 속성 접근 제어

⚠️  주의:
  - 복잡한 연산은 메서드로
  - private 변수(_attr) 사용
  - __init__에서도 Setter 사용
""")

print("\n💡 Tip: @property는 Python다운 Getter/Setter 패턴입니다!")
