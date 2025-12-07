"""
파일명: session3_inheritance_basic.py
목적: 상속 기초 실습
"""

import math

print("=" * 70)
print("상속 기초".center(70))
print("=" * 70)

# 1. 기본 상속
print("\n[1] 기본 상속")
print("-" * 70)

# 부모 클래스 (Parent, Base, Super)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def info(self):
        print(f"{self.name}: {self.speak()}")

# 자식 클래스 (Child, Derived, Sub)
class Dog(Animal):
    def speak(self):
        return "멍멍!"

class Cat(Animal):
    def speak(self):
        return "야옹!"

# 사용
dog = Dog("바둑이")
cat = Cat("나비")

dog.info()  # 부모의 info(), 자식의 speak()
cat.info()

# 2. 상속 확인
print("\n[2] 상속 관계 확인")
print("-" * 70)

print(f"Dog는 Animal의 자식? {issubclass(Dog, Animal)}")
print(f"dog는 Dog의 인스턴스? {isinstance(dog, Dog)}")
print(f"dog는 Animal의 인스턴스? {isinstance(dog, Animal)}")  # True!

# 3. 실습: 도형 클래스
print("\n[3] 실습: 도형 클래스 계층")
print("-" * 70)

class Shape:
    """도형 기본 클래스"""

    def __init__(self, color):
        self.color = color

    def get_info(self):
        return f"색상: {self.color}"

class Rectangle(Shape):
    """직사각형"""

    def __init__(self, color, width, height):
        super().__init__(color)  # 부모 초기화
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def get_info(self):
        return f"사각형 | {super().get_info()} | 넓이: {self.area()}"

class Circle(Shape):
    """원"""

    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def get_info(self):
        return f"원 | {super().get_info()} | 넓이: {self.area():.2f}"

class Triangle(Shape):
    """삼각형"""

    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2

    def get_info(self):
        return f"삼각형 | {super().get_info()} | 넓이: {self.area()}"

# 도형 생성
shapes = [
    Rectangle("빨강", 10, 20),
    Circle("파랑", 7),
    Triangle("초록", 10, 15)
]

for shape in shapes:
    print(shape.get_info())

# 4. 직원 클래스 상속
print("\n[4] 직원 클래스 상속")
print("-" * 70)

class Employee:
    """기본 직원 클래스"""

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def get_info(self):
        return f"{self.name} ({self.employee_id}): {self.salary:,}만원"

    def work(self):
        return f"{self.name}이(가) 일하고 있습니다"

class Developer(Employee):
    """개발자"""

    def __init__(self, name, employee_id, salary, languages):
        super().__init__(name, employee_id, salary)
        self.languages = languages

    def get_info(self):
        base_info = super().get_info()
        langs = ", ".join(self.languages)
        return f"{base_info} | 언어: {langs}"

    def work(self):
        return f"{self.name}이(가) 코딩하고 있습니다"

    def code_review(self):
        return f"{self.name}이(가) 코드 리뷰하고 있습니다"

class Manager(Employee):
    """관리자"""

    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} | 팀원: {self.team_size}명"

    def work(self):
        return f"{self.name}이(가) 팀을 관리하고 있습니다"

    def hold_meeting(self):
        return f"{self.name}이(가) 회의를 진행하고 있습니다"

# 직원 생성
dev = Developer("김철수", "D001", 4000, ["Python", "JavaScript"])
manager = Manager("이영희", "M001", 6000, 5)

print(dev.get_info())
print(dev.work())
print(dev.code_review())

print()

print(manager.get_info())
print(manager.work())
print(manager.hold_meeting())

# 5. 다형성 (Polymorphism)
print("\n[5] 다형성")
print("-" * 70)

def display_employee_info(employee):
    """다형성 활용: Employee 타입이면 모두 처리 가능"""
    print(f"- {employee.get_info()}")
    print(f"  → {employee.work()}")

# 모든 직원 타입에 동일하게 적용 가능!
employees = [
    Employee("박민수", "E001", 3000),
    Developer("정지훈", "D002", 4500, ["Java", "Spring"]),
    Manager("최민지", "M002", 6500, 8)
]

print("전체 직원 정보:")
for emp in employees:
    display_employee_info(emp)
    print()

# 6. 계좌 클래스 상속
print("\n[6] 계좌 클래스 상속")
print("-" * 70)

class Account:
    """기본 계좌"""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """입금"""
        self.balance += amount
        print(f"[{self.owner}] {amount:,}원 입금. 잔액: {self.balance:,}원")

    def withdraw(self, amount):
        """출금"""
        if amount > self.balance:
            print(f"[{self.owner}] 잔액 부족!")
            return False
        self.balance -= amount
        print(f"[{self.owner}] {amount:,}원 출금. 잔액: {self.balance:,}원")
        return True

    def get_info(self):
        return f"{self.owner}: {self.balance:,}원"

class SavingsAccount(Account):
    """저축 계좌 (이자 적용)"""

    def __init__(self, owner, balance=0, interest_rate=0.03):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        """이자 적용"""
        interest = int(self.balance * self.interest_rate)
        self.balance += interest
        print(f"[{self.owner}] 이자 {interest:,}원 적용. 잔액: {self.balance:,}원")

class CheckingAccount(Account):
    """당좌 계좌 (마이너스 한도)"""

    def __init__(self, owner, balance=0, overdraft_limit=100000):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """출금 (마이너스 한도 고려)"""
        if amount > self.balance + self.overdraft_limit:
            print(f"[{self.owner}] 한도 초과! (한도: {self.overdraft_limit:,}원)")
            return False

        self.balance -= amount
        print(f"[{self.owner}] {amount:,}원 출금. 잔액: {self.balance:,}원")
        return True

# 계좌 생성 및 테스트
print("저축 계좌:")
savings = SavingsAccount("김철수", 1000000, 0.05)
savings.deposit(500000)
savings.apply_interest()  # 5% 이자

print("\n당좌 계좌:")
checking = CheckingAccount("이영희", 100000, 200000)
checking.withdraw(150000)  # 잔액 초과하지만 한도 내
checking.withdraw(200000)  # 한도 초과

# 7. 상속과 코드 재사용
print("\n[7] 상속과 코드 재사용")
print("-" * 70)

class Vehicle:
    """탈것 기본 클래스"""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, distance):
        """주행"""
        self.mileage += distance
        print(f"{self.brand} {self.model} {distance}km 주행. "
              f"총 주행거리: {self.mileage}km")

    def get_info(self):
        return f"{self.year}년 {self.brand} {self.model} ({self.mileage}km)"

class Car(Vehicle):
    """자동차"""

    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type

    def get_info(self):
        return f"{super().get_info()} | 연료: {self.fuel_type}"

class Truck(Vehicle):
    """트럭"""

    def __init__(self, brand, model, year, load_capacity):
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity

    def get_info(self):
        return f"{super().get_info()} | 적재량: {self.load_capacity}톤"

# 차량 생성
car = Car("현대", "소나타", 2023, "가솔린")
truck = Truck("기아", "봉고", 2022, 1.5)

car.drive(100)
truck.drive(50)

print()
print(car.get_info())
print(truck.get_info())

# 8. 상속 체인
print("\n[8] 상속 체인 (다단계 상속)")
print("-" * 70)

class LivingThing:
    """생명체"""

    def __init__(self, name):
        self.name = name

    def breathe(self):
        return f"{self.name}이(가) 숨쉽니다"

class Animal(LivingThing):
    """동물"""

    def move(self):
        return f"{self.name}이(가) 움직입니다"

class Mammal(Animal):
    """포유류"""

    def feed_milk(self):
        return f"{self.name}이(가) 젖을 먹입니다"

class Dog(Mammal):
    """개"""

    def bark(self):
        return f"{self.name}: 멍멍!"

# 다단계 상속
dog = Dog("바둑이")

print(dog.breathe())    # LivingThing의 메서드
print(dog.move())       # Animal의 메서드
print(dog.feed_milk())  # Mammal의 메서드
print(dog.bark())       # Dog의 메서드

# 상속 체인 확인
print(f"\n상속 체인: {Dog.__mro__}")

# 9. 부모 클래스 메서드 확장
print("\n[9] 부모 메서드 확장")
print("-" * 70)

class Logger:
    """기본 로거"""

    def log(self, message):
        print(f"[LOG] {message}")

class FileLogger(Logger):
    """파일 로거 (콘솔 + 파일)"""

    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        # 부모 메서드 호출 (콘솔 출력)
        super().log(message)

        # 추가 기능 (파일 저장)
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"{message}\n")
        print(f"  → {self.filename}에 저장됨")

# 파일 로거 사용
file_logger = FileLogger("app.log")
file_logger.log("애플리케이션 시작")
file_logger.log("데이터 로드 완료")

print("\n" + "=" * 70)
print("핵심 정리".center(70))
print("=" * 70)

print("""
✅ 상속의 장점:
  1. 코드 재사용 (공통 기능을 부모에 한 번만 작성)
  2. 확장성 (기존 코드 수정 없이 새 기능 추가)
  3. 다형성 (같은 인터페이스로 다른 동작)

✅ super() 사용:
  - super().__init__(): 부모 클래스 초기화
  - super().method(): 부모 메서드 호출
  - 항상 자식 생성자에서 부모 생성자 먼저 호출!

✅ 다형성:
  - 부모 타입으로 자식 객체를 다룰 수 있음
  - 함수는 부모 타입만 알아도 모든 자식 처리 가능

⚠️  주의:
  - 과도한 상속은 복잡성 증가 (깊이 3단계 이하 권장)
  - "is-a" 관계일 때만 상속 사용
    (예: Dog is a Animal ✅, Car is a Engine ✗)
""")

print("\n💡 Tip: 다음 세션에서 메서드 오버라이딩을 더 깊게 다룹니다!")
