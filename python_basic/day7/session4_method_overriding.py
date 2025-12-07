"""
파일명: session4_method_overriding.py
목적: 메서드 오버라이딩 실습
"""

print("=" * 70)
print("메서드 오버라이딩".center(70))
print("=" * 70)

# 1. 기본 오버라이딩
print("\n[1] 기본 메서드 오버라이딩")
print("-" * 70)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        """기본 보너스: 10%"""
        return self.salary * 0.1

class Manager(Employee):
    def calculate_bonus(self):
        """관리자 보너스: 20%"""
        return self.salary * 0.2

class Intern(Employee):
    def calculate_bonus(self):
        """인턴 보너스: 5%"""
        return self.salary * 0.05

# 사용
employees = [
    Employee("사원A", 3000),
    Manager("관리자B", 5000),
    Intern("인턴C", 2000)
]

for emp in employees:
    bonus = emp.calculate_bonus()
    total = emp.salary + bonus
    print(f"{emp.__class__.__name__:<10} {emp.name}: "
          f"급여 {emp.salary:,}만원 + 보너스 {bonus:,}만원 = {total:,}만원")

# 2. 실습: 급여 계산 시스템
print("\n[2] 실습: 다양한 급여 계산 방식")
print("-" * 70)

class EmployeeBase:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def calculate_pay(self):
        """하위 클래스에서 구현 필요"""
        raise NotImplementedError("하위 클래스에서 구현해야 합니다!")

    def display_pay(self):
        pay = self.calculate_pay()
        print(f"{self.name} ({self.__class__.__name__}): {pay:,}원")

class HourlyEmployee(EmployeeBase):
    """시간급 직원"""

    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

class SalariedEmployee(EmployeeBase):
    """월급 직원"""

    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary

class CommissionEmployee(EmployeeBase):
    """수수료 직원 (기본급 + 판매 수수료)"""

    def __init__(self, name, employee_id, base_salary, sales_amount, commission_rate):
        super().__init__(name, employee_id)
        self.base_salary = base_salary
        self.sales_amount = sales_amount
        self.commission_rate = commission_rate

    def calculate_pay(self):
        commission = self.sales_amount * self.commission_rate
        return self.base_salary + commission

# 직원 생성
print("급여 계산:")
emp1 = HourlyEmployee("김철수", "H001", 15000, 160)  # 시급 15000원, 160시간
emp2 = SalariedEmployee("이영희", "S001", 4000000)   # 월급 400만원
emp3 = CommissionEmployee("박민수", "C001", 2000000, 10000000, 0.05)  # 기본급 + 5% 수수료

emp1.display_pay()
emp2.display_pay()
emp3.display_pay()

# 3. 부모 메서드 활용 오버라이딩
print("\n[3] 부모 메서드를 활용한 오버라이딩")
print("-" * 70)

class Shape:
    def __init__(self, color):
        self.color = color

    def describe(self):
        return f"색상: {self.color}"

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def describe(self):
        # 부모 메서드 호출 + 추가 정보
        base = super().describe()
        return f"사각형 | {base} | {self.width}x{self.height}"

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def describe(self):
        base = super().describe()
        return f"원 | {base} | 반지름 {self.radius}"

# 사용
shapes = [
    Rectangle("빨강", 10, 20),
    Circle("파랑", 15)
]

for shape in shapes:
    print(shape.describe())

# 4. 결제 시스템
print("\n[4] 결제 시스템 (다형성 활용)")
print("-" * 70)

class PaymentMethod:
    """결제 수단 기본 클래스"""

    def process_payment(self, amount):
        raise NotImplementedError("하위 클래스에서 구현")

    def get_fee(self, amount):
        """수수료 (기본 0%)"""
        return 0

class CreditCard(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def process_payment(self, amount):
        fee = self.get_fee(amount)
        total = amount + fee
        print(f"💳 신용카드({self.card_number[-4:]}) 결제: {amount:,}원")
        if fee > 0:
            print(f"   수수료: {fee:,}원")
        print(f"   총액: {total:,}원")
        return True

    def get_fee(self, amount):
        return int(amount * 0.03)  # 3% 수수료

class BankTransfer(PaymentMethod):
    def __init__(self, bank_name, account_number):
        self.bank_name = bank_name
        self.account_number = account_number

    def process_payment(self, amount):
        fee = self.get_fee(amount)
        total = amount + fee
        print(f"🏦 계좌이체({self.bank_name}) 결제: {amount:,}원")
        if fee > 0:
            print(f"   수수료: {fee:,}원")
        print(f"   총액: {total:,}원")
        return True

    def get_fee(self, amount):
        return 1000  # 고정 1000원

class Cash(PaymentMethod):
    def process_payment(self, amount):
        print(f"💵 현금 결제: {amount:,}원")
        print(f"   수수료: 없음")
        return True

    # get_fee는 부모의 기본 구현 사용 (0원)

# 결제 처리 함수 (다형성)
def checkout(payment_method, amount):
    """결제 처리 (어떤 결제 수단이든 동일하게 처리)"""
    print(f"\n{'='*50}")
    payment_method.process_payment(amount)
    print(f"{'='*50}")

# 다양한 결제 수단으로 결제
checkout(CreditCard("1234-5678-9012-3456"), 100000)
checkout(BankTransfer("국민은행", "123-456-789"), 100000)
checkout(Cash(), 100000)

# 5. 게임 캐릭터 시스템
print("\n[5] 게임 캐릭터 시스템")
print("-" * 70)

class Character:
    """캐릭터 기본 클래스"""

    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.power = power

    def attack(self):
        """기본 공격"""
        return self.power

    def special_attack(self):
        """특수 공격 (자식 클래스에서 오버라이드)"""
        return self.attack()

    def take_damage(self, damage):
        """피해 받기"""
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} HP: {self.hp}/{self.max_hp}")

    def is_alive(self):
        return self.hp > 0

class Warrior(Character):
    """전사 (강력한 물리 공격)"""

    def special_attack(self):
        """강타 (2배 데미지)"""
        return self.power * 2

    def attack(self):
        print(f"⚔️  {self.name}의 검 공격!")
        return super().attack()

class Mage(Character):
    """마법사 (마법 공격)"""

    def __init__(self, name, hp, power, mana):
        super().__init__(name, hp, power)
        self.mana = mana
        self.max_mana = mana

    def special_attack(self):
        """파이어볼 (3배 데미지, 마나 소모)"""
        if self.mana >= 30:
            self.mana -= 30
            return self.power * 3
        else:
            print(f"{self.name}: 마나 부족!")
            return self.attack()

    def attack(self):
        print(f"🔮 {self.name}의 마법 공격!")
        return super().attack()

class Archer(Character):
    """궁수 (원거리 공격)"""

    def special_attack(self):
        """연속 사격 (1.5배 데미지 × 2회)"""
        return self.power * 1.5 * 2

    def attack(self):
        print(f"🏹 {self.name}의 화살 공격!")
        return super().attack()

# 전투 시뮬레이션
print("전투 시작!")
print()

warrior = Warrior("전사", 150, 30)
mage = Mage("마법사", 100, 25, 100)
archer = Archer("궁수", 120, 20)

# 일반 공격
damage1 = warrior.attack()
print(f"데미지: {damage1}")

print()

damage2 = mage.attack()
print(f"데미지: {damage2}")

print()

# 특수 공격
print("특수 공격!")
print(f"⚔️  전사 강타: {warrior.special_attack()} 데미지")
print(f"🔮 마법사 파이어볼: {mage.special_attack()} 데미지 (마나: {mage.mana}/{mage.max_mana})")
print(f"🏹 궁수 연속 사격: {archer.special_attack()} 데미지")

# 6. 파일 처리 시스템
print("\n[6] 파일 처리 시스템")
print("-" * 70)

class FileProcessor:
    """파일 처리 기본 클래스"""

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        """읽기 (하위 클래스에서 구현)"""
        raise NotImplementedError()

    def write(self, data):
        """쓰기 (하위 클래스에서 구현)"""
        raise NotImplementedError()

class TextFileProcessor(FileProcessor):
    """텍스트 파일 처리"""

    def read(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return ""

    def write(self, data):
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(data)
        print(f"✓ {self.filename} 저장 완료 (텍스트)")

class JsonFileProcessor(FileProcessor):
    """JSON 파일 처리"""

    def read(self):
        import json
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def write(self, data):
        import json
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✓ {self.filename} 저장 완료 (JSON)")

# 파일 처리 함수 (다형성)
def save_data(processor, data):
    """파일 저장 (어떤 프로세서든 동일하게 처리)"""
    processor.write(data)

# 사용
text_processor = TextFileProcessor("data.txt")
json_processor = JsonFileProcessor("data.json")

save_data(text_processor, "Hello, World!")
save_data(json_processor, {"name": "김철수", "age": 28})

# 7. 로깅 시스템
print("\n[7] 로깅 레벨 시스템")
print("-" * 70)

class Logger:
    """로거 기본 클래스"""

    def log(self, message):
        print(f"[LOG] {message}")

class DebugLogger(Logger):
    """디버그 로거 (상세한 정보 포함)"""

    def log(self, message):
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[DEBUG] [{timestamp}] {message}")

class ErrorLogger(Logger):
    """에러 로거 (에러만 기록)"""

    def log(self, message):
        super().log(f"❌ ERROR: {message}")

        # 파일에도 저장
        with open("error.log", "a", encoding="utf-8") as f:
            import datetime
            timestamp = datetime.datetime.now()
            f.write(f"[{timestamp}] {message}\n")

# 로거 사용
loggers = [
    Logger(),
    DebugLogger(),
    ErrorLogger()
]

for logger in loggers:
    logger.log("애플리케이션 시작")
    print()

print("\n" + "=" * 70)
print("핵심 정리".center(70))
print("=" * 70)

print("""
✅ 메서드 오버라이딩:
  - 부모 메서드를 자식에서 재정의
  - 같은 이름, 다른 구현
  - 다형성의 핵심!

✅ NotImplementedError:
  - 부모에서 raise NotImplementedError
  - 자식 클래스에서 반드시 구현하도록 강제
  - 추상 메서드 패턴

✅ 다형성 활용:
  - 부모 타입으로 모든 자식 처리 가능
  - 함수는 부모 타입만 알아도 됨
  - 확장성이 뛰어남 (새 자식 추가 쉬움)

⚠️  주의:
  - 오버라이딩 시 부모 메서드 시그니처 유지
  - super().method()로 부모 기능 재사용 가능
""")

print("\n💡 Tip: 다음 세션에서 super()를 더 깊게 다룹니다!")
