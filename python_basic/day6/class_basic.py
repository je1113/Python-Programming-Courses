"""
파일명: class_basic.py
목적: 클래스 기초 실습
"""

print("=" * 70)
print("클래스 기초 실습".center(70))
print("=" * 70)

# 1. 기본 클래스 정의
print("\n[1] 기본 클래스 정의")
print("-" * 70)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"안녕하세요, {self.name}입니다. {self.age}세입니다.")

# 객체 생성
person1 = Person("김철수", 28)
person2 = Person("이영희", 32)

# 메서드 호출
person1.introduce()
person2.introduce()

# 속성 접근
print(f"\n{person1.name}의 나이: {person1.age}세")

# 2. 은행 계좌 클래스
print("\n[2] 은행 계좌 클래스")
print("-" * 70)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []  # 거래 내역

    def deposit(self, amount):
        """입금"""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"입금: +{amount:,}원")
            print(f"{amount:,}원 입금 완료. 잔액: {self.balance:,}원")
        else:
            print("입금액은 0보다 커야 합니다!")

    def withdraw(self, amount):
        """출금"""
        if amount > self.balance:
            print(f"잔액 부족! (잔액: {self.balance:,}원)")
        elif amount <= 0:
            print("출금액은 0보다 커야 합니다!")
        else:
            self.balance -= amount
            self.transactions.append(f"출금: -{amount:,}원")
            print(f"{amount:,}원 출금 완료. 잔액: {self.balance:,}원")

    def get_balance(self):
        """잔액 조회"""
        return self.balance

    def show_transactions(self):
        """거래 내역 출력"""
        print(f"\n[{self.owner}님의 거래 내역]")
        if not self.transactions:
            print("  거래 내역이 없습니다.")
        else:
            for i, trans in enumerate(self.transactions, 1):
                print(f"  {i}. {trans}")
        print(f"현재 잔액: {self.balance:,}원")

# 계좌 생성 및 테스트
account1 = BankAccount("김철수", 100000)
account2 = BankAccount("이영희", 200000)

print(f"\n{account1.owner}님 계좌:")
account1.deposit(50000)
account1.withdraw(30000)
account1.withdraw(200000)  # 잔액 부족
account1.show_transactions()

print(f"\n{account2.owner}님 계좌:")
account2.deposit(100000)
account2.withdraw(50000)
account2.show_transactions()

# 3. 상품 클래스
print("\n[3] 상품 클래스")
print("-" * 70)

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        """판매"""
        if quantity > self.stock:
            print(f"재고 부족! (재고: {self.stock}개)")
            return False

        self.stock -= quantity
        total = self.price * quantity
        print(f"{self.name} {quantity}개 판매: {total:,}원")
        print(f"남은 재고: {self.stock}개")
        return True

    def restock(self, quantity):
        """재고 입고"""
        self.stock += quantity
        print(f"{self.name} {quantity}개 입고 완료. 현재 재고: {self.stock}개")

    def get_info(self):
        """상품 정보"""
        print(f"\n상품명: {self.name}")
        print(f"가격: {self.price:,}원")
        print(f"재고: {self.stock}개")

# 상품 생성 및 테스트
laptop = Product("노트북", 1200000, 5)
mouse = Product("마우스", 30000, 50)

laptop.get_info()
laptop.sell(2)
laptop.sell(5)  # 재고 부족
laptop.restock(10)

# 4. 직원 클래스
print("\n[4] 직원 클래스")
print("-" * 70)

class Employee:
    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary

    def give_raise(self, amount):
        """연봉 인상"""
        old_salary = self.salary
        self.salary += amount
        print(f"{self.name}님의 연봉이 {amount:,}원 인상되었습니다.")
        print(f"  {old_salary:,}원 → {self.salary:,}원")

    def change_department(self, new_dept):
        """부서 이동"""
        old_dept = self.department
        self.department = new_dept
        print(f"{self.name}님이 {old_dept} → {new_dept}로 이동하였습니다.")

    def display_info(self):
        """정보 출력"""
        print(f"\n사번: {self.employee_id}")
        print(f"이름: {self.name}")
        print(f"부서: {self.department}")
        print(f"연봉: {self.salary:,}만원")

# 직원 생성 및 관리
emp1 = Employee("E001", "김철수", "개발", 3500)
emp2 = Employee("E002", "이영희", "기획", 4200)

emp1.display_info()
emp1.give_raise(500)
emp1.change_department("AI팀")
emp1.display_info()

# 5. 학생 클래스
print("\n[5] 학생 클래스")
print("-" * 70)

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.scores = {}  # 과목별 점수

    def add_score(self, subject, score):
        """성적 추가"""
        self.scores[subject] = score
        print(f"{self.name} - {subject}: {score}점 입력")

    def get_average(self):
        """평균 계산"""
        if not self.scores:
            return 0
        return sum(self.scores.values()) / len(self.scores)

    def get_grade(self):
        """학점 계산"""
        avg = self.get_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def show_report(self):
        """성적표 출력"""
        print(f"\n{'='*40}")
        print(f"{self.name} ({self.student_id}) 성적표")
        print(f"{'='*40}")

        if not self.scores:
            print("입력된 성적이 없습니다.")
            return

        print(f"{'과목':<10} {'점수':>6}")
        print("-" * 20)
        for subject, score in self.scores.items():
            print(f"{subject:<10} {score:>6}점")

        print("-" * 20)
        avg = self.get_average()
        grade = self.get_grade()
        print(f"{'평균':<10} {avg:>6.1f}점")
        print(f"{'학점':<10} {grade:>6}")

# 학생 생성 및 성적 관리
student1 = Student("김철수", "2024001")
student1.add_score("국어", 85)
student1.add_score("영어", 90)
student1.add_score("수학", 88)
student1.show_report()

student2 = Student("이영희", "2024002")
student2.add_score("국어", 92)
student2.add_score("영어", 95)
student2.add_score("수학", 91)
student2.show_report()

# 6. 도서 클래스
print("\n[6] 도서 클래스")
print("-" * 70)

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrower = None

    def borrow(self, borrower_name):
        """대출"""
        if self.is_borrowed:
            print(f"'{self.title}'은(는) 이미 대출 중입니다. (대출자: {self.borrower})")
            return False

        self.is_borrowed = True
        self.borrower = borrower_name
        print(f"'{self.title}'을(를) {borrower_name}님이 대출하였습니다.")
        return True

    def return_book(self):
        """반납"""
        if not self.is_borrowed:
            print(f"'{self.title}'은(는) 대출 중이 아닙니다.")
            return False

        print(f"'{self.title}'을(를) {self.borrower}님이 반납하였습니다.")
        self.is_borrowed = False
        self.borrower = None
        return True

    def get_info(self):
        """도서 정보"""
        status = f"대출 중 ({self.borrower})" if self.is_borrowed else "대출 가능"
        print(f"\n제목: {self.title}")
        print(f"저자: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"상태: {status}")

# 도서 생성 및 대출 관리
book1 = Book("파이썬 프로그래밍", "홍길동", "978-1234567890")
book2 = Book("데이터 과학 입문", "김영희", "978-0987654321")

book1.get_info()
book1.borrow("김철수")
book1.borrow("이영희")  # 이미 대출 중
book1.return_book()
book1.borrow("이영희")  # 반납 후 다시 대출

# 7. 여러 객체 관리
print("\n[7] 여러 객체 관리")
print("-" * 70)

# 여러 계좌 생성
accounts = [
    BankAccount("김철수", 100000),
    BankAccount("이영희", 200000),
    BankAccount("박민수", 150000)
]

print("전체 계좌 현황:")
print(f"{'소유자':<10} {'잔액':>15}")
print("-" * 30)

total_balance = 0
for account in accounts:
    print(f"{account.owner:<10} {account.balance:>12,}원")
    total_balance += account.balance

print("-" * 30)
print(f"{'총 잔액':<10} {total_balance:>12,}원")

# 8. 클래스와 함수의 차이
print("\n[8] 클래스 vs 함수")
print("-" * 70)

# 함수 방식 (상태 유지 어려움)
def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter_func = create_counter()
print(f"함수 카운터: {counter_func()}, {counter_func()}, {counter_func()}")

# 클래스 방식 (상태 유지 쉬움)
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0

counter_obj = Counter()
print(f"클래스 카운터: {counter_obj.increment()}, {counter_obj.increment()}, {counter_obj.increment()}")
counter_obj.reset()
print(f"리셋 후: {counter_obj.increment()}")

# 9. 종합 예제: 쇼핑 카트
print("\n[9] 종합 예제: 쇼핑 카트")
print("-" * 70)

class ShoppingCart:
    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def add_item(self, product_name, price, quantity=1):
        """상품 추가"""
        item = {
            "product": product_name,
            "price": price,
            "quantity": quantity
        }
        self.items.append(item)
        print(f"'{product_name}' {quantity}개 추가됨")

    def remove_item(self, product_name):
        """상품 제거"""
        for item in self.items:
            if item["product"] == product_name:
                self.items.remove(item)
                print(f"'{product_name}' 제거됨")
                return True
        print(f"'{product_name}'을(를) 찾을 수 없습니다.")
        return False

    def get_total(self):
        """총 금액 계산"""
        total = sum(item["price"] * item["quantity"] for item in self.items)
        return total

    def show_cart(self):
        """장바구니 내용 출력"""
        print(f"\n{'='*50}")
        print(f"{self.owner}님의 장바구니")
        print(f"{'='*50}")

        if not self.items:
            print("장바구니가 비어 있습니다.")
            return

        print(f"{'상품명':<15} {'단가':>12} {'수량':>6} {'소계':>12}")
        print("-" * 50)

        for item in self.items:
            subtotal = item["price"] * item["quantity"]
            print(f"{item['product']:<15} {item['price']:>10,}원 "
                  f"{item['quantity']:>6}개 {subtotal:>10,}원")

        print("-" * 50)
        print(f"{'총 금액':<15} {'':<12} {'':<6} {self.get_total():>10,}원")

# 쇼핑 카트 사용
cart = ShoppingCart("김철수")
cart.add_item("노트북", 1200000)
cart.add_item("마우스", 30000, 2)
cart.add_item("키보드", 89000)
cart.show_cart()

cart.remove_item("마우스")
cart.show_cart()

print("\n" + "=" * 70)
print("클래스 기초 실습 완료".center(70))
print("=" * 70)

print("\n💡 Tip: 클래스는 관련 데이터와 기능을 하나로 묶습니다!")
print("💡 Tip: __init__은 생성자, self는 객체 자신을 가리킵니다!")
