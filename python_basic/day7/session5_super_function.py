"""
파일명: session5_super_function.py
목적: super() 함수 실습
"""

print("=" * 70)
print("super() 함수".center(70))
print("=" * 70)

# 1. super()의 기본 사용
print("\n[1] super()로 부모 초기화")
print("-" * 70)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person 초기화: {name}, {age}세")

    def introduce(self):
        return f"안녕하세요, {self.name}입니다"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # 부모 초기화
        self.student_id = student_id
        print(f"Student 초기화: 학번 {student_id}")

    def introduce(self):
        parent_intro = super().introduce()  # 부모 메서드 호출
        return f"{parent_intro}. 학번은 {self.student_id}입니다"

# 사용
student = Student("김철수", 20, "2024001")
print(student.introduce())

# 2. super() 없이 vs super() 사용
print("\n[2] super() 없이 vs super() 사용")
print("-" * 70)

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

# ❌ super() 없이 (부모 클래스 직접 호출)
class Dog1(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)  # 직접 호출 (비추천)
        self.breed = breed

    def speak(self):
        return Animal.speak(self) + " 멍멍!"

# ✅ super() 사용 (권장)
class Dog2(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # super 사용 (권장)
        self.breed = breed

    def speak(self):
        return super().speak() + " 멍멍!"

dog1 = Dog1("바둑이", "진돗개")
dog2 = Dog2("초코", "푸들")

print(f"Dog1: {dog1.name} - {dog1.speak()}")
print(f"Dog2: {dog2.name} - {dog2.speak()}")

# 3. 실습: 계좌 클래스
print("\n[3] 실습: 계좌 클래스 상속")
print("-" * 70)

class Account:
    """기본 계좌"""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []  # 거래 내역
        print(f"✓ 계좌 개설: {owner}")

    def deposit(self, amount):
        """입금"""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"입금: +{amount:,}원")
            print(f"[{self.owner}] {amount:,}원 입금. 잔액: {self.balance:,}원")
        else:
            print("입금액은 0보다 커야 합니다!")

    def withdraw(self, amount):
        """출금"""
        if amount > self.balance:
            print(f"[{self.owner}] 잔액 부족!")
            return False

        self.balance -= amount
        self.transactions.append(f"출금: -{amount:,}원")
        print(f"[{self.owner}] {amount:,}원 출금. 잔액: {self.balance:,}원")
        return True

    def get_balance(self):
        return self.balance

class SavingsAccount(Account):
    """저축 계좌 (이자 + 출금 수수료)"""

    def __init__(self, owner, balance=0, interest_rate=0.03):
        super().__init__(owner, balance)  # 부모 초기화
        self.interest_rate = interest_rate
        print(f"  이자율: {interest_rate * 100}%")

    def apply_interest(self):
        """이자 적용"""
        interest = int(self.balance * self.interest_rate)
        super().deposit(interest)  # 부모의 deposit 사용
        print(f"  이자 {interest:,}원 적용")

    def withdraw(self, amount):
        """출금 (수수료 차감)"""
        fee = 1000
        total = amount + fee

        # 부모의 withdraw 호출
        if super().withdraw(total):
            print(f"  출금 수수료: {fee:,}원")
            return True
        return False

class CheckingAccount(Account):
    """당좌 계좌 (마이너스 한도)"""

    def __init__(self, owner, balance=0, overdraft_limit=100000):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit
        print(f"  마이너스 한도: {overdraft_limit:,}원")

    def withdraw(self, amount):
        """출금 (마이너스 한도 고려)"""
        # 한도 체크
        if amount > self.balance + self.overdraft_limit:
            print(f"[{self.owner}] 한도 초과! (한도: {self.overdraft_limit:,}원)")
            return False

        # 부모 메서드 호출하지 않고 직접 구현
        # (부모는 잔액만 체크하므로)
        self.balance -= amount
        self.transactions.append(f"출금: -{amount:,}원")
        print(f"[{self.owner}] {amount:,}원 출금. 잔액: {self.balance:,}원")

        if self.balance < 0:
            print(f"  마이너스 사용: {-self.balance:,}원")

        return True

# 계좌 생성 및 테스트
print("\n저축 계좌 테스트:")
savings = SavingsAccount("김철수", 1000000, 0.05)
print()
savings.deposit(500000)
savings.apply_interest()
savings.withdraw(200000)

print("\n당좌 계좌 테스트:")
checking = CheckingAccount("이영희", 100000, 200000)
print()
checking.withdraw(150000)  # 잔액 초과하지만 한도 내
checking.withdraw(200000)  # 한도 초과

# 4. super()로 부모 메서드 확장
print("\n[4] super()로 부모 메서드 확장")
print("-" * 70)

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} 시동 켜기")

    def stop(self):
        print(f"{self.brand} {self.model} 시동 끄기")

class ElectricCar(Vehicle):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
        self.battery_level = 100

    def start(self):
        # 부모 메서드 호출
        super().start()

        # 추가 기능
        print(f"  배터리 잔량: {self.battery_level}%")
        if self.battery_level < 20:
            print("  ⚠️  배터리가 부족합니다!")

    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        print(f"충전 완료. 배터리: {self.battery_level}%")

# 전기차 사용
car = ElectricCar("Tesla", "Model 3", 75)
car.start()
car.charge(50)

# 5. 다중 상속과 super()
print("\n[5] 다중 상속과 super() (MRO)")
print("-" * 70)

class A:
    def method(self):
        print("A.method()")

class B(A):
    def method(self):
        print("B.method()")
        super().method()

class C(A):
    def method(self):
        print("C.method()")
        super().method()

class D(B, C):
    def method(self):
        print("D.method()")
        super().method()

# MRO (Method Resolution Order) 확인
print(f"MRO: {[cls.__name__ for cls in D.__mro__]}")
print()

# 메서드 호출
d = D()
d.method()

# 6. super()를 통한 협력적 메서드
print("\n[6] 협력적 메서드 (Cooperative Methods)")
print("-" * 70)

class LoggerMixin:
    def log(self, message):
        print(f"[LOG] {message}")
        # 다음 클래스의 log 호출 (있으면)
        if hasattr(super(), 'log'):
            super().log(message)

class FileSaverMixin:
    def log(self, message):
        with open("messages.log", "a", encoding="utf-8") as f:
            f.write(f"{message}\n")
        print(f"  → 파일 저장")
        # 다음 클래스의 log 호출 (있으면)
        if hasattr(super(), 'log'):
            super().log(message)

class Application(LoggerMixin, FileSaverMixin):
    def log(self, message):
        print("Application.log():")
        super().log(message)

app = Application()
app.log("애플리케이션 시작")

# 7. 초기화 체인
print("\n[7] 초기화 체인")
print("-" * 70)

class Level1:
    def __init__(self):
        print("Level1 초기화")
        self.level1_data = "Level1"

class Level2(Level1):
    def __init__(self):
        print("Level2 초기화")
        super().__init__()  # Level1 초기화
        self.level2_data = "Level2"

class Level3(Level2):
    def __init__(self):
        print("Level3 초기화")
        super().__init__()  # Level2 초기화 (연쇄적으로 Level1도)
        self.level3_data = "Level3"

print("객체 생성:")
obj = Level3()

print(f"\n데이터 확인:")
print(f"level1_data: {obj.level1_data}")
print(f"level2_data: {obj.level2_data}")
print(f"level3_data: {obj.level3_data}")

# 8. 실무 예제: 직원 관리
print("\n[8] 실무 예제: 직원 관리 시스템")
print("-" * 70)

class Employee:
    """기본 직원 클래스"""

    employee_count = 0

    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        Employee.employee_count += 1
        print(f"✓ 직원 등록: {name} ({department})")

    def get_info(self):
        return f"{self.name} ({self.employee_id}) - {self.department}"

    def work(self):
        print(f"{self.name}이(가) 일하고 있습니다")

class Developer(Employee):
    """개발자"""

    def __init__(self, name, employee_id, department, languages):
        super().__init__(name, employee_id, department)
        self.languages = languages
        print(f"  프로그래밍 언어: {', '.join(languages)}")

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} | {', '.join(self.languages)}"

    def work(self):
        super().work()  # 부모 메서드 호출
        print(f"  → 코딩 중: {self.languages[0]}")

class TeamLeader(Developer):
    """팀 리더"""

    def __init__(self, name, employee_id, department, languages, team_size):
        super().__init__(name, employee_id, department, languages)
        self.team_size = team_size
        print(f"  팀원 수: {team_size}명")

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} | 팀원 {self.team_size}명"

    def work(self):
        super().work()  # Developer.work() 호출 (연쇄적으로 Employee.work()도)
        print(f"  → 팀 관리 중 ({self.team_size}명)")

# 직원 생성
print()
emp = Employee("박민수", "E001", "기획")
print()
dev = Developer("김철수", "D001", "개발", ["Python", "JavaScript"])
print()
leader = TeamLeader("이영희", "TL001", "개발", ["Python", "Java", "Go"], 5)

print(f"\n총 직원 수: {Employee.employee_count}명")

print("\n직원 정보:")
print(f"- {emp.get_info()}")
print(f"- {dev.get_info()}")
print(f"- {leader.get_info()}")

print("\n업무 현황:")
emp.work()
print()
dev.work()
print()
leader.work()

# 9. super() 사용 시 주의사항
print("\n[9] super() 사용 시 주의사항")
print("-" * 70)

class Parent:
    def __init__(self, value):
        self.value = value

# ❌ super() 호출 안함 (부모 초기화 안됨!)
class BadChild(Parent):
    def __init__(self, value, extra):
        # super().__init__(value)  # 빠뜨림!
        self.extra = extra

# ✅ super() 제대로 호출
class GoodChild(Parent):
    def __init__(self, value, extra):
        super().__init__(value)  # 부모 초기화
        self.extra = extra

# 테스트
try:
    bad = BadChild(10, 20)
    print(f"BadChild.value: {bad.value}")  # AttributeError!
except AttributeError as e:
    print(f"✗ BadChild 오류: {e}")

good = GoodChild(10, 20)
print(f"✓ GoodChild.value: {good.value}")
print(f"✓ GoodChild.extra: {good.extra}")

print("\n" + "=" * 70)
print("핵심 정리".center(70))
print("=" * 70)

print("""
✅ super()의 역할:
  1. 부모 클래스 초기화 (super().__init__())
  2. 부모 메서드 호출 (super().method())
  3. 다중 상속에서 MRO 따라 호출

✅ super() 사용 패턴:
  # 부모 초기화
  def __init__(self, ...):
      super().__init__(...)
      # 자식 초기화

  # 부모 메서드 확장
  def method(self):
      super().method()  # 부모 메서드
      # 추가 기능

✅ 장점:
  - 클래스 이름 하드코딩 불필요
  - 다중 상속에서 유연함
  - 코드 변경 시 유지보수 쉬움

⚠️  주의:
  - 자식 __init__에서 super().__init__() 호출 필수!
  - 부모 메서드 시그니처 확인 (매개변수 개수)
  - MRO 이해 (다중 상속 시)
""")

print("\n💡 Tip: super()는 부모를 직접 호출하는 것보다 안전하고 유연합니다!")
