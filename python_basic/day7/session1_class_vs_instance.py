"""
파일명: session1_class_vs_instance.py
목적: 클래스 변수 vs 인스턴스 변수 실습
"""

print("=" * 70)
print("클래스 변수 vs 인스턴스 변수".center(70))
print("=" * 70)

# 1. 기본 개념
print("\n[1] 기본 개념")
print("-" * 70)

class Employee:
    # 클래스 변수 (모든 객체가 공유)
    company_name = "ABC 기업"
    employee_count = 0

    def __init__(self, name, salary):
        # 인스턴스 변수 (각 객체마다 독립적)
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_info(self):
        print(f"{self.name} - {self.company_name} - {self.salary:,}만원")

# 직원 생성
emp1 = Employee("김철수", 3500)
emp2 = Employee("이영희", 4200)
emp3 = Employee("박민수", 3800)

print(f"회사명: {Employee.company_name}")
print(f"총 직원 수: {Employee.employee_count}명")
print()
emp1.display_info()
emp2.display_info()
emp3.display_info()

# 2. 클래스 변수 수정
print("\n[2] 클래스 변수 수정")
print("-" * 70)

# 클래스 변수 변경 → 모든 객체에 영향
Employee.company_name = "XYZ 기업"

print("회사명 변경 후:")
emp1.display_info()
emp2.display_info()

# 3. 인스턴스 변수 수정
print("\n[3] 인스턴스 변수 수정")
print("-" * 70)

# 인스턴스 변수 변경 → 해당 객체만 영향
emp1.salary = 4000

print("김철수 급여 인상 후:")
print(f"emp1: {emp1.salary:,}만원")
print(f"emp2: {emp2.salary:,}만원")  # 변경 안됨

# 4. 주의사항: self로 클래스 변수 수정하면?
print("\n[4] 주의사항: self로 클래스 변수 접근")
print("-" * 70)

# ❌ 잘못된 예: self로 클래스 변수 수정
emp1.company_name = "emp1의 회사"  # 인스턴스 변수 생성!

print(f"emp1.company_name: {emp1.company_name}")  # emp1의 회사
print(f"emp2.company_name: {emp2.company_name}")  # XYZ 기업 (변경 안됨)
print(f"Employee.company_name: {Employee.company_name}")  # XYZ 기업

# 5. 실습: 은행 계좌 관리
print("\n[5] 실습: 은행 계좌 관리")
print("-" * 70)

class BankAccount:
    # 클래스 변수
    bank_name = "Python Bank"
    interest_rate = 0.03  # 3%
    total_accounts = 0

    def __init__(self, account_number, owner, balance=0):
        # 인스턴스 변수
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        """입금"""
        self.balance += amount
        print(f"[{self.owner}] {amount:,}원 입금. 잔액: {self.balance:,}원")

    def withdraw(self, amount):
        """출금"""
        if amount > self.balance:
            print(f"[{self.owner}] 잔액 부족! (잔액: {self.balance:,}원)")
        else:
            self.balance -= amount
            print(f"[{self.owner}] {amount:,}원 출금. 잔액: {self.balance:,}원")

    def apply_interest(self):
        """이자 적용"""
        interest = int(self.balance * BankAccount.interest_rate)
        self.balance += interest
        print(f"[{self.owner}] 이자 {interest:,}원 적용. 잔액: {self.balance:,}원")

    @classmethod
    def change_interest_rate(cls, new_rate):
        """이자율 변경 (클래스 메서드)"""
        cls.interest_rate = new_rate
        print(f"✓ 이자율 변경: {new_rate * 100}%")

    def display_info(self):
        """계좌 정보"""
        print(f"[{self.bank_name}] {self.owner} ({self.account_number}): {self.balance:,}원")

# 계좌 생성
print(f"\n{'='*60}")
print(f"{BankAccount.bank_name} 계좌 생성")
print(f"{'='*60}")

acc1 = BankAccount("001-001", "김철수", 1000000)
acc2 = BankAccount("001-002", "이영희", 2000000)
acc3 = BankAccount("001-003", "박민수", 1500000)

print(f"총 계좌 수: {BankAccount.total_accounts}개")
print()

# 입출금
acc1.deposit(500000)
acc1.withdraw(200000)
acc2.deposit(300000)

print()

# 이자 적용 (3%)
print(f"현재 이자율: {BankAccount.interest_rate * 100}%")
acc1.apply_interest()
acc2.apply_interest()
acc3.apply_interest()

print()

# 이자율 변경
BankAccount.change_interest_rate(0.05)  # 5%로 변경

print("\n이자 재적용:")
acc1.apply_interest()
acc2.apply_interest()
acc3.apply_interest()

# 6. 전체 계좌 현황
print(f"\n{'='*60}")
print("전체 계좌 현황")
print(f"{'='*60}")

accounts = [acc1, acc2, acc3]

for acc in accounts:
    acc.display_info()

print(f"\n총 계좌 수: {BankAccount.total_accounts}개")
total_balance = sum(acc.balance for acc in accounts)
print(f"전체 잔액: {total_balance:,}원")

# 7. 클래스 변수의 활용 사례
print("\n[7] 클래스 변수 활용 사례")
print("-" * 70)

class Product:
    # 클래스 변수: 세금률 (모든 상품 공통)
    tax_rate = 0.1  # 10%
    product_count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.product_count += 1

    def get_price_with_tax(self):
        """세금 포함 가격"""
        return int(self.price * (1 + Product.tax_rate))

    def display(self):
        print(f"{self.name}: {self.price:,}원 → "
              f"{self.get_price_with_tax():,}원 (세금 포함)")

# 상품 생성
products = [
    Product("노트북", 1200000),
    Product("마우스", 30000),
    Product("키보드", 89000)
]

print(f"세금률: {Product.tax_rate * 100}%\n")

for p in products:
    p.display()

# 세금률 변경
print(f"\n세금률을 15%로 변경\n")
Product.tax_rate = 0.15

for p in products:
    p.display()

print(f"\n총 상품 수: {Product.product_count}개")

# 8. 클래스 변수 vs 인스턴스 변수 비교표
print("\n[8] 비교 정리")
print("-" * 70)

class Example:
    class_var = "클래스 변수"  # 클래스 변수

    def __init__(self, value):
        self.instance_var = value  # 인스턴스 변수

ex1 = Example("객체1")
ex2 = Example("객체2")

print(f"{'구분':<20} {'ex1':<20} {'ex2':<20}")
print("-" * 60)
print(f"{'인스턴스 변수':<20} {ex1.instance_var:<20} {ex2.instance_var:<20}")
print(f"{'클래스 변수':<20} {ex1.class_var:<20} {ex2.class_var:<20}")

# 클래스 변수 변경
Example.class_var = "변경된 클래스 변수"

print("\n클래스 변수 변경 후:")
print(f"{'구분':<20} {'ex1':<20} {'ex2':<20}")
print("-" * 60)
print(f"{'인스턴스 변수':<20} {ex1.instance_var:<20} {ex2.instance_var:<20}")
print(f"{'클래스 변수':<20} {ex1.class_var:<20} {ex2.class_var:<20}")

print("\n" + "=" * 70)
print("핵심 정리".center(70))
print("=" * 70)

print("""
✅ 클래스 변수:
  - 클래스 블록에 정의
  - 모든 객체가 공유
  - ClassName.variable로 접근 권장
  - 사용 사례: 설정값, 카운터, 공통 데이터

✅ 인스턴스 변수:
  - __init__에서 self.variable로 정의
  - 각 객체마다 독립적
  - self.variable로 접근
  - 사용 사례: 객체별 고유 데이터

⚠️  주의:
  - self.class_var = value → 인스턴스 변수 생성!
  - ClassName.class_var = value → 클래스 변수 수정
""")

print("\n💡 Tip: 클래스 변수 수정은 항상 클래스명으로!")
