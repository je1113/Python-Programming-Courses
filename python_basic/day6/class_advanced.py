"""
파일명: class_advanced.py
목적: 클래스 메서드와 속성 (고급) 실습
"""

print("=" * 70)
print("클래스 고급 기능 실습".center(70))
print("=" * 70)

# 1. 클래스 변수 vs 인스턴스 변수
print("\n[1] 클래스 변수 vs 인스턴스 변수")
print("-" * 70)

class Employee:
    # 클래스 변수 (모든 객체가 공유)
    company = "ABC 기업"
    employee_count = 0

    def __init__(self, name, salary):
        # 인스턴스 변수 (각 객체마다 별도)
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

emp1 = Employee("김철수", 3500)
emp2 = Employee("이영희", 4200)

print(f"회사명: {Employee.company}")
print(f"총 직원 수: {Employee.employee_count}명")
print(f"\n{emp1.name}: {emp1.salary}만원")
print(f"{emp2.name}: {emp2.salary}만원")

# 2. 클래스 메서드
print("\n[2] 클래스 메서드 (@classmethod)")
print("-" * 70)

class BankAccount:
    interest_rate = 0.03  # 클래스 변수

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @classmethod
    def set_interest_rate(cls, rate):
        """이자율 변경 (모든 계좌에 적용)"""
        cls.interest_rate = rate
        print(f"이자율이 {rate*100}%로 변경되었습니다.")

    @classmethod
    def create_zero_balance_account(cls, owner):
        """잔액 0인 계좌 생성 (팩토리 메서드)"""
        return cls(owner, 0)

    def apply_interest(self):
        """이자 적용"""
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"{self.owner}: 이자 {interest:,.0f}원 적용 → 잔액 {self.balance:,.0f}원")

# 클래스 메서드 사용
BankAccount.set_interest_rate(0.05)

acc1 = BankAccount("김철수", 1000000)
acc2 = BankAccount.create_zero_balance_account("이영희")
acc2.balance = 2000000

acc1.apply_interest()
acc2.apply_interest()

# 3. 정적 메서드
print("\n[3] 정적 메서드 (@staticmethod)")
print("-" * 70)

class MathUtils:
    @staticmethod
    def add(a, b):
        """덧셈"""
        return a + b

    @staticmethod
    def multiply(a, b):
        """곱셈"""
        return a * b

    @staticmethod
    def is_even(n):
        """짝수 판별"""
        return n % 2 == 0

# 정적 메서드는 객체 생성 없이 호출 가능
print(f"10 + 5 = {MathUtils.add(10, 5)}")
print(f"10 × 5 = {MathUtils.multiply(10, 5)}")
print(f"10은 짝수? {MathUtils.is_even(10)}")

# 4. 프로퍼티 (Property)
print("\n[4] 프로퍼티 (@property)")
print("-" * 70)

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """섭씨 온도 (Getter)"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """섭씨 온도 설정 (Setter)"""
        if value < -273.15:
            raise ValueError("절대영도보다 낮을 수 없습니다!")
        self._celsius = value

    @property
    def fahrenheit(self):
        """화씨 온도 (자동 계산)"""
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """화씨 온도로 설정"""
        self._celsius = (value - 32) * 5/9

temp = Temperature(25)
print(f"섭씨: {temp.celsius}°C")
print(f"화씨: {temp.fahrenheit}°F")

temp.celsius = 30
print(f"\n섭씨 30도로 변경:")
print(f"섭씨: {temp.celsius}°C")
print(f"화씨: {temp.fahrenheit}°F")

temp.fahrenheit = 86
print(f"\n화씨 86도로 변경:")
print(f"섭씨: {temp.celsius}°C")
print(f"화씨: {temp.fahrenheit}°F")

# 5. 특수 메서드 (__str__, __repr__)
print("\n[5] 특수 메서드")
print("-" * 70)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        """사용자용 문자열 (print할 때)"""
        return f"{self.name}: {self.price:,}원"

    def __repr__(self):
        """개발자용 표현 (디버깅용)"""
        return f"Product('{self.name}', {self.price})"

    def __lt__(self, other):
        """< 연산자 (가격 비교)"""
        return self.price < other.price

    def __eq__(self, other):
        """== 연산자"""
        return self.price == other.price

    def __add__(self, other):
        """+ 연산자 (가격 합산)"""
        return self.price + other.price

p1 = Product("노트북", 1200000)
p2 = Product("마우스", 30000)

print(f"print(p1): {p1}")  # __str__
print(f"repr(p1): {repr(p1)}")  # __repr__
print(f"\np1 < p2: {p1 < p2}")  # __lt__
print(f"p1 == p2: {p1 == p2}")  # __eq__
print(f"p1 + p2: {p1 + p2:,}원")  # __add__

# 정렬
products = [
    Product("노트북", 1200000),
    Product("마우스", 30000),
    Product("키보드", 89000)
]

sorted_products = sorted(products)
print("\n가격순 정렬:")
for p in sorted_products:
    print(f"  {p}")

# 6. 상속 (Inheritance)
print("\n[6] 상속")
print("-" * 70)

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        """동물 소리 (기본)"""
        return "..."

    def info(self):
        """정보 출력"""
        print(f"{self.name}: {self.speak()}")

class Dog(Animal):
    def speak(self):
        """강아지 소리"""
        return "멍멍!"

class Cat(Animal):
    def speak(self):
        """고양이 소리"""
        return "야옹!"

# 상속 사용
dog = Dog("바둑이")
cat = Cat("나비")

dog.info()  # 부모의 info(), 자식의 speak()
cat.info()

# 7. 실무 예제: 도서 관리 시스템
print("\n[7] 도서 관리 시스템 (종합)")
print("-" * 70)

class Book:
    total_books = 0  # 클래스 변수

    def __init__(self, title, author, isbn, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        Book.total_books += 1

    @classmethod
    def get_total_books(cls):
        """전체 도서 수 조회"""
        return cls.total_books

    def __str__(self):
        return f"'{self.title}' - {self.author} ({self.price:,}원)"

    def __lt__(self, other):
        """가격 비교"""
        return self.price < other.price

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        """도서 추가"""
        self.books.append(book)
        print(f"'{book.title}' 추가 완료")

    def search_by_author(self, author):
        """저자로 검색"""
        results = [book for book in self.books if author in book.author]
        return results

    def sort_by_price(self):
        """가격순 정렬"""
        return sorted(self.books)

    def show_all(self):
        """전체 도서 목록"""
        print(f"\n{'='*50}")
        print(f"{self.name} 도서 목록 ({len(self.books)}권)")
        print(f"{'='*50}")

        if not self.books:
            print("도서가 없습니다.")
            return

        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")

# 도서관 사용
library = Library("시립 도서관")

# 도서 추가
library.add_book(Book("파이썬 프로그래밍", "홍길동", "978-1234567890", 30000))
library.add_book(Book("데이터 과학", "김영희", "978-0987654321", 35000))
library.add_book(Book("알고리즘 입문", "이철수", "978-1111111111", 25000))
library.add_book(Book("파이썬 심화", "홍길동", "978-2222222222", 40000))

library.show_all()

# 저자 검색
print("\n'홍길동' 저자의 책:")
results = library.search_by_author("홍길동")
for book in results:
    print(f"  - {book}")

# 가격순 정렬
print("\n가격순 정렬:")
sorted_books = library.sort_by_price()
for book in sorted_books:
    print(f"  - {book}")

print(f"\n총 도서 수: {Book.get_total_books()}권")

# 8. 계좌 클래스 (프로퍼티 활용)
print("\n[8] 계좌 클래스 (프로퍼티)")
print("-" * 70)

class SavingsAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  # private 변수 (관례)

    @property
    def balance(self):
        """잔액 조회 (Getter)"""
        return self._balance

    @balance.setter
    def balance(self, value):
        """잔액 설정 (Setter) - 검증 포함"""
        if value < 0:
            raise ValueError("잔액은 0 이상이어야 합니다!")
        self._balance = value

    def deposit(self, amount):
        """입금"""
        if amount <= 0:
            print("입금액은 0보다 커야 합니다!")
            return

        self.balance += amount  # setter 호출
        print(f"{amount:,}원 입금 완료. 잔액: {self.balance:,}원")

    def withdraw(self, amount):
        """출금"""
        if amount > self.balance:
            print("잔액이 부족합니다!")
            return

        self.balance -= amount  # setter 호출
        print(f"{amount:,}원 출금 완료. 잔액: {self.balance:,}원")

account = SavingsAccount("김철수", 100000)
print(f"초기 잔액: {account.balance:,}원")

account.deposit(50000)
account.withdraw(30000)

# 9. 특수 메서드 종합
print("\n[9] 특수 메서드 종합")
print("-" * 70)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        """벡터 덧셈"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """벡터 뺄셈"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """스칼라 곱"""
        return Vector(self.x * scalar, self.y * scalar)

    def __len__(self):
        """크기"""
        return int((self.x**2 + self.y**2)**0.5)

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")
print(f"크기: {len(v1)}")

# 10. 종합 예제: 쇼핑몰
print("\n[10] 종합 예제: 쇼핑몰")
print("-" * 70)

class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} ({self.price:,}원, 재고: {self.stock}개)"

class ShoppingMall:
    discount_rate = 0.1  # 클래스 변수 (10% 할인)

    def __init__(self, name):
        self.name = name
        self.items = []

    @classmethod
    def set_discount_rate(cls, rate):
        """할인율 설정"""
        cls.discount_rate = rate
        print(f"할인율 {rate*100}%로 변경")

    def add_item(self, item):
        """상품 추가"""
        self.items.append(item)

    def search(self, keyword):
        """상품 검색"""
        results = [item for item in self.items if keyword in item.name]
        return results

    def apply_discount(self, item):
        """할인 적용"""
        discount = item.price * self.discount_rate
        final_price = item.price - discount
        return final_price

    def show_items(self):
        """상품 목록"""
        print(f"\n{'='*60}")
        print(f"{self.name} 상품 목록")
        print(f"{'='*60}")

        for i, item in enumerate(self.items, 1):
            discount_price = self.apply_discount(item)
            print(f"{i}. {item.name}")
            print(f"   정가: {item.price:,}원 → "
                  f"할인가: {discount_price:,.0f}원 "
                  f"(재고: {item.stock}개)")

# 쇼핑몰 운영
mall = ShoppingMall("Python Mall")

mall.add_item(Item("노트북", 1200000, 5))
mall.add_item(Item("무선 마우스", 30000, 50))
mall.add_item(Item("기계식 키보드", 89000, 30))
mall.add_item(Item("무선 헤드셋", 120000, 20))

mall.show_items()

# 할인율 변경
ShoppingMall.set_discount_rate(0.2)
mall.show_items()

# 상품 검색
print("\n'무선' 검색 결과:")
results = mall.search("무선")
for item in results:
    print(f"  - {item}")

print("\n" + "=" * 70)
print("클래스 고급 기능 실습 완료".center(70))
print("=" * 70)

print("\n💡 Tip: 클래스 변수는 모든 객체가 공유합니다!")
print("💡 Tip: @property로 Getter/Setter를 구현하세요!")
print("💡 Tip: 특수 메서드로 연산자를 재정의할 수 있습니다!")
