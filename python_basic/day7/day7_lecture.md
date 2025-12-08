# Day 7: 클래스 심화 - 객체지향 프로그래밍

## 📋 강의 개요

**학습 목표:**
- 인스턴스 변수와 클래스 변수의 차이 이해
- 캡슐화를 통한 정보 은닉 구현
- 상속으로 코드 재사용성 향상
- 메서드 오버라이딩과 super() 활용
- 특수 메서드로 Python다운 클래스 작성
- 프로퍼티로 안전한 속성 관리

**소요 시간:** 4시간 (240분)

**세션 구성:** 9개 세션 × 25분 (이론 10분 + 실습 10분 + 해설 5분)

---

## 💡 Day 7을 배워야 하는 이유

### 1. 객체지향 프로그래밍의 핵심

**OOP가 중요한 이유:**
- 코드 재사용성 향상
- 유지보수 용이성
- 대규모 프로젝트 구조화

### 2. 실무 프로젝트 필수 스킬

**실무 활용:**
- Django, Flask 웹 프레임워크
- 데이터 분석 라이브러리
- 게임 개발, GUI 프로그래밍

### 3. Python다운 코드 작성

**특수 메서드와 프로퍼티:**
- 직관적이고 깔끔한 코드
- Python의 내장 기능 활용
- 더 읽기 쉬운 코드

---

## 세션 1: 인스턴스 vs 클래스 변수 (25분)
**중요도:** ★★★★★

### 📖 이론 (10분)

#### 1.1 변수의 종류

**인스턴스 변수**와 **클래스 변수**는 객체지향 프로그래밍의 핵심 개념입니다.

**예시 1: 기본 구분**
```python
class Employee:
    # 클래스 변수 (모든 인스턴스가 공유)
    company_name = "ABC 기업"
    employee_count = 0

    def __init__(self, name, salary):
        # 인스턴스 변수 (각 객체마다 고유)
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

emp1 = Employee("김철수", 3000000)
emp2 = Employee("이영희", 3500000)

print(Employee.company_name)  # "ABC 기업" (공유)
print(Employee.employee_count)  # 2 (모든 객체가 증가)
print(emp1.name)  # "김철수" (개별)
print(emp2.name)  # "이영희" (개별)
```

**예시 2: 차이점 비교**
```python
class BankAccount:
    # 클래스 변수: 은행명, 이자율 (모든 계좌 공통)
    bank_name = "Python Bank"
    interest_rate = 0.03

    def __init__(self, owner, balance):
        # 인스턴스 변수: 각 계좌마다 다름
        self.owner = owner
        self.balance = balance

    def apply_interest(self):
        # 클래스 변수 사용
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest

account1 = BankAccount("김철수", 1000000)
account2 = BankAccount("이영희", 2000000)

# 이자율 변경시 모든 계좌에 영향
BankAccount.interest_rate = 0.05
account1.apply_interest()  # 5% 적용
account2.apply_interest()  # 5% 적용
```

**예시 3: 실무 활용 - 데이터베이스 연결**
```python
class DatabaseConnection:
    # 클래스 변수: 연결 설정 (모든 연결에 공통)
    max_connections = 10
    active_connections = 0
    server = "localhost"

    def __init__(self, database_name):
        # 인스턴스 변수: 각 연결마다 다름
        self.database_name = database_name
        self.connection_id = DatabaseConnection.active_connections
        DatabaseConnection.active_connections += 1

    def get_info(self):
        return f"DB: {self.database_name} (연결 {self.connection_id}/{DatabaseConnection.max_connections})"

conn1 = DatabaseConnection("users_db")
conn2 = DatabaseConnection("products_db")
print(conn1.get_info())
print(conn2.get_info())
print(f"총 연결 수: {DatabaseConnection.active_connections}")
```

#### 1.2 Java와 비교

| 구분 | Python | Java |
|------|--------|------|
| 클래스 변수 | 클래스 블록에 정의 | `static` 키워드 |
| 인스턴스 변수 | `__init__`에서 `self.변수` | 클래스 블록에 정의 |
| 접근 | `클래스명.변수` / `self.변수` | `클래스명.변수` / `this.변수` |

### 💻 실습 (10분)

**[실습 파일: session1_class_vs_instance_practice.py](./session1_class_vs_instance_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session1_class_vs_instance_solution.py](./session1_class_vs_instance_solution.py)**

**핵심 포인트:**
1. 클래스 변수는 `클래스명.변수명`으로 접근
2. `total_accounts`처럼 카운터는 클래스 변수
3. 각 계좌의 잔액은 독립적이므로 인스턴스 변수
4. `self.클래스변수`로 읽기는 가능하지만 쓰기는 인스턴스 변수 생성

---

## 세션 2: 캡슐화와 정보 은닉 (25분)
**중요도:** ★★★★★

### 📖 이론 (10분)

#### 2.1 캡슐화 (Encapsulation)

**캡슐화**는 데이터와 메서드를 하나로 묶고, 외부 접근을 제한하는 것입니다.

**예시 1: 접근 제어자**
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public (어디서든 접근)
        self._account_number = "123-456"  # protected (내부 구현)
        self.__balance = balance    # private (외부 접근 어려움)

    def get_balance(self):  # Getter
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("입금액은 0보다 커야 합니다")

account = BankAccount("김철수", 100000)
print(account.owner)  # 접근 가능
print(account.get_balance())  # Getter로 접근
# print(account.__balance)  # AttributeError! (접근 불가)
```

**예시 2: Name Mangling**
```python
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = self.__hash_password(password)

    def __hash_password(self, password):
        """비밀번호 해싱 (private 메서드)"""
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        """비밀번호 검증"""
        return self.__password == self.__hash_password(password)

user = User("john", "secret123")
print(user.username)  # "john" (접근 가능)
print(user.verify_password("secret123"))  # True
# user.__password  # AttributeError!
# 실제로는 _User__password로 저장됨 (비추천)
```

**예시 3: 검증 로직이 있는 Setter**
```python
class Employee:
    MIN_SALARY = 1000000  # 최소 급여 (클래스 변수)

    def __init__(self, name, salary):
        self.name = name
        self.__salary = 0
        self.set_salary(salary)  # 검증 로직 사용

    def get_salary(self):
        """급여 조회"""
        return self.__salary

    def set_salary(self, amount):
        """급여 설정 (검증 포함)"""
        if amount < Employee.MIN_SALARY:
            raise ValueError(f"급여는 {Employee.MIN_SALARY:,}원 이상이어야 합니다")
        self.__salary = amount

    def give_raise(self, percentage):
        """급여 인상"""
        if not 0 <= percentage <= 100:
            raise ValueError("인상률은 0~100% 사이여야 합니다")
        increase = self.__salary * (percentage / 100)
        self.__salary += increase
        print(f"{self.name}님 급여 {percentage}% 인상: {self.__salary:,}원")

emp = Employee("김철수", 3000000)
emp.give_raise(10)
# emp.set_salary(500000)  # ValueError!
```

#### 2.2 Java와 비교

```java
// Java
class BankAccount {
    private int balance;  // private

    public int getBalance() {
        return balance;
    }

    public void deposit(int amount) {
        this.balance += amount;
    }
}
```

```python
# Python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private (__)

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
```

### 💻 실습 (10분)

**[실습 파일: session2_encapsulation_practice.py](./session2_encapsulation_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session2_encapsulation_solution.py](./session2_encapsulation_solution.py)**

**핵심 포인트:**
1. `__` (double underscore) - private 변수
2. `_` (single underscore) - protected (관례)
3. Getter/Setter로 외부 접근 제어
4. 검증 로직을 Setter에 포함

---

## 세션 3: 상속 기초 (25분)
**중요도:** ★★★★★

### 📖 이론 (10분)

#### 3.1 상속 (Inheritance)

**상속**은 기존 클래스의 기능을 물려받아 새로운 클래스를 만드는 것입니다.

**예시 1: 기본 상속**
```python
# 부모 클래스 (슈퍼 클래스)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

# 자식 클래스 (서브 클래스)
class Dog(Animal):
    def speak(self):
        return "멍멍!"

class Cat(Animal):
    def speak(self):
        return "야옹!"

dog = Dog("바둑이")
cat = Cat("나비")
print(dog.speak())  # "멍멍!"
print(cat.speak())  # "야옹!"
print(dog.name)     # "바둑이" (부모 속성 상속)
```

**예시 2: 실무 활용 - 직원 클래스**
```python
# 기본 직원 클래스
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def get_info(self):
        return f"{self.name} ({self.employee_id}): {self.salary:,}원"

# 개발자 클래스 (추가 속성: 프로그래밍 언어)
class Developer(Employee):
    def __init__(self, name, employee_id, salary, languages):
        super().__init__(name, employee_id, salary)
        self.languages = languages

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} | 언어: {', '.join(self.languages)}"

# 관리자 클래스 (추가 속성: 관리 팀원 수)
class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} | 팀원: {self.team_size}명"

dev = Developer("김철수", "D001", 4000000, ["Python", "JavaScript"])
mgr = Manager("이영희", "M001", 5000000, 10)
print(dev.get_info())
print(mgr.get_info())
```

**예시 3: 도형 클래스 계층**
```python
import math

class Shape:
    def __init__(self, color):
        self.color = color

    def get_info(self):
        return f"색상: {self.color}"

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def get_info(self):
        return f"사각형 | {super().get_info()} | 넓이: {self.area()}"

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def get_info(self):
        return f"원 | {super().get_info()} | 넓이: {self.area():.2f}"

rect = Rectangle("빨강", 10, 5)
circle = Circle("파랑", 7)
print(rect.get_info())
print(circle.get_info())
```

#### 3.2 Java와 비교

```java
// Java
class Dog extends Animal {
    @Override
    public String speak() {
        return "멍멍!";
    }
}
```

```python
# Python - 더 간결
class Dog(Animal):
    def speak(self):
        return "멍멍!"
```

### 💻 실습 (10분)

**[실습 파일: session3_inheritance_basic_practice.py](./session3_inheritance_basic_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session3_inheritance_basic_solution.py](./session3_inheritance_basic_solution.py)**

**핵심 포인트:**
1. `super().__init__()`로 부모 클래스 초기화
2. 각 자식 클래스에서 고유 메서드 구현
3. `get_info()`에서 부모 메서드 재사용
4. `isinstance(obj, ClassName)` - 타입 확인

---

## 세션 4: 메서드 오버라이딩 (25분)
**중요도:** ★★★★★

### 📖 이론 (10분)

#### 4.1 메서드 오버라이딩

**메서드 오버라이딩**은 부모 클래스의 메서드를 자식 클래스에서 재정의하는 것입니다.

**예시 1: 보너스 계산 다형성**
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.1  # 기본 10%

class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.2  # 관리자는 20%

class Intern(Employee):
    def calculate_bonus(self):
        return self.salary * 0.05  # 인턴은 5%

# 다형성: 같은 메서드 이름으로 다른 동작
employees = [
    Employee("직원A", 3000000),
    Manager("관리자B", 5000000),
    Intern("인턴C", 1500000)
]

for emp in employees:
    bonus = emp.calculate_bonus()
    print(f"{emp.name}: 보너스 {bonus:,}원")
```

**예시 2: 결제 시스템**
```python
class PaymentMethod:
    def process_payment(self, amount):
        raise NotImplementedError("하위 클래스에서 구현해야 합니다")

class CreditCard(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def process_payment(self, amount):
        print(f"신용카드({self.card_number})로 {amount:,}원 결제")
        # 신용카드 결제 로직
        return True

class BankTransfer(PaymentMethod):
    def __init__(self, account_number):
        self.account_number = account_number

    def process_payment(self, amount):
        print(f"계좌이체({self.account_number})로 {amount:,}원 결제")
        # 계좌이체 로직
        return True

class KakaoPay(PaymentMethod):
    def process_payment(self, amount):
        print(f"카카오페이로 {amount:,}원 결제")
        return True

# 다형성 활용
def checkout(payment_method, amount):
    payment_method.process_payment(amount)

checkout(CreditCard("1234-5678"), 50000)
checkout(BankTransfer("110-123-456789"), 100000)
checkout(KakaoPay(), 75000)
```

**예시 3: 급여 계산 시스템**
```python
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def calculate_pay(self):
        raise NotImplementedError("하위 클래스에서 구현")

class HourlyEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

class SalariedEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary

class CommissionEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, sales_amount, commission_rate):
        super().__init__(name, employee_id)
        self.base_salary = base_salary
        self.sales_amount = sales_amount
        self.commission_rate = commission_rate

    def calculate_pay(self):
        commission = self.sales_amount * self.commission_rate
        return self.base_salary + commission

employees = [
    HourlyEmployee("시급직A", "H001", 15000, 160),
    SalariedEmployee("월급직B", "S001", 3000000),
    CommissionEmployee("영업직C", "C001", 2000000, 10000000, 0.03)
]

for emp in employees:
    pay = emp.calculate_pay()
    print(f"{emp.name}: {pay:,}원")
```

### 💻 실습 (10분)

**[실습 파일: session4_method_overriding_practice.py](./session4_method_overriding_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session4_method_overriding_solution.py](./session4_method_overriding_solution.py)**

**핵심 포인트:**
1. 부모 클래스에서 `NotImplementedError` 발생
2. 각 자식 클래스에서 고유한 로직 구현
3. 다형성: 하나의 인터페이스로 여러 구현

---

## 세션 5: super() 함수 (25분)
**중요도:** ★★★★★

### 📖 이론 (10분)

#### 5.1 super() 활용

`super()`는 부모 클래스의 메서드를 호출할 때 사용합니다.

**예시 1: 기본 사용**
```python
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"안녕하세요, {self.name}입니다"

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # 부모 초기화
        self.age = age

    def greet(self):
        parent_greeting = super().greet()  # 부모 메서드 호출
        return f"{parent_greeting}. {self.age}세입니다"

child = Child("김철수", 25)
print(child.greet())
# "안녕하세요, 김철수입니다. 25세입니다"
```

**예시 2: 계좌 클래스 상속**
```python
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount:,}원 입금. 잔액: {self.balance:,}원")

    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액 부족!")
            return False
        self.balance -= amount
        print(f"{amount:,}원 출금. 잔액: {self.balance:,}원")
        return True

class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.03):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        super().deposit(interest)  # 부모의 deposit 사용
        print(f"이자 {interest:,}원 적용")

    def withdraw(self, amount):
        fee = 1000
        total = amount + fee
        if super().withdraw(total):  # 부모 메서드 호출
            print(f"수수료 {fee:,}원 차감")
            return True
        return False

account = SavingsAccount("김철수", 1000000)
account.apply_interest()
account.withdraw(500000)
```

**예시 3: Logger 확장**
```python
class Logger:
    def log(self, message):
        print(f"[LOG] {message}")

class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        # 부모 메서드 먼저 호출 (콘솔 출력)
        super().log(message)

        # 추가 동작 (파일 저장)
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"{message}\n")

class TimestampLogger(Logger):
    def log(self, message):
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 부모 메서드에 타임스탬프 추가해서 호출
        super().log(f"[{timestamp}] {message}")

file_logger = FileLogger("app.log")
file_logger.log("애플리케이션 시작")

time_logger = TimestampLogger()
time_logger.log("사용자 로그인")
```

### 💻 실습 (10분)

**[실습 파일: session5_super_function_practice.py](./session5_super_function_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session5_super_function_solution.py](./session5_super_function_solution.py)**

**핵심 포인트:**
1. `super().__init__()` - 부모 초기화 먼저
2. 부모 메서드 호출 후 추가 로직 수행
3. `super().method()`의 반환값 활용

---

## 세션 6: 다중 상속 (25분)
**중요도:** ★★★★☆

### 📖 이론 (10분)

#### 6.1 다중 상속

**다중 상속**은 여러 부모 클래스로부터 상속받는 것입니다.

**예시 1: 기본 다중 상속**
```python
class Flyable:
    def fly(self):
        return "날 수 있습니다"

class Swimmable:
    def swim(self):
        return "수영할 수 있습니다"

class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name

duck = Duck("도날드")
print(duck.fly())   # "날 수 있습니다" (Flyable)
print(duck.swim())  # "수영할 수 있습니다" (Swimmable)
```

**예시 2: Mixin 패턴**
```python
# Mixin 클래스들
class JSONSerializableMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__, ensure_ascii=False)

class LoggableMixin:
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

class TimestampMixin:
    def __init__(self, *args, **kwargs):
        from datetime import datetime
        super().__init__(*args, **kwargs)
        self.created_at = datetime.now()

# Mixin 조합
class User(JSONSerializableMixin, LoggableMixin, TimestampMixin):
    def __init__(self, username, email):
        super().__init__()
        self.username = username
        self.email = email

user = User("john", "john@example.com")
print(user.to_json())
user.log("사용자 생성됨")
print(f"생성 시각: {user.created_at}")
```

**예시 3: 스마트 기기**
```python
class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def call(self, number):
        print(f"{self.phone_number} -> {number} 전화 걸기")

class Camera:
    def __init__(self, resolution):
        self.resolution = resolution

    def take_photo(self):
        print(f"{self.resolution}로 사진 촬영")

class MusicPlayer:
    def __init__(self):
        self.playlist = []

    def play_music(self, song):
        print(f"♪ {song} 재생 중")

class SmartPhone(Phone, Camera, MusicPlayer):
    def __init__(self, phone_number, resolution, brand):
        Phone.__init__(self, phone_number)
        Camera.__init__(self, resolution)
        MusicPlayer.__init__(self)
        self.brand = brand

    def get_info(self):
        return f"{self.brand} 스마트폰 ({self.phone_number})"

phone = SmartPhone("010-1234-5678", "12MP", "Samsung")
phone.call("010-9876-5432")
phone.take_photo()
phone.play_music("Dynamite")
print(phone.get_info())
```

#### 6.2 MRO (Method Resolution Order)

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

print(D().method())  # "B" (MRO: D -> B -> C -> A)
print(D.__mro__)     # MRO 확인
```

### 💻 실습 (10분)

**[실습 파일: session6_multiple_inheritance_practice.py](./session6_multiple_inheritance_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session6_multiple_inheritance_solution.py](./session6_multiple_inheritance_solution.py)**

**핵심 포인트:**
1. 다중 상속시 각 부모 클래스 명시적 초기화
2. Mixin 패턴으로 기능 조합
3. MRO로 메서드 호출 순서 결정

---

## 세션 7: 특수 메서드 (25분)
**중요도:** ★★★★★

### 📖 이론 (10분)

#### 7.1 특수 메서드 (Magic Methods)

**특수 메서드**는 `__method__` 형태로 Python의 내장 기능과 연동됩니다.

**예시 1: 기본 특수 메서드**
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        """print() 할 때"""
        return f"{self.name}: {self.price:,}원"

    def __repr__(self):
        """repr() 할 때 (디버깅용)"""
        return f"Product('{self.name}', {self.price})"

    def __lt__(self, other):
        """< 연산자"""
        return self.price < other.price

    def __eq__(self, other):
        """== 연산자"""
        return self.price == other.price

p1 = Product("노트북", 1200000)
p2 = Product("마우스", 30000)

print(p1)  # "노트북: 1,200,000원" (__str__)
print(repr(p1))  # Product('노트북', 1200000) (__repr__)
print(p1 < p2)  # False (__lt__)
print(p1 == p2)  # False (__eq__)
```

**예시 2: 연산자 오버로딩**
```python
import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        """+ 연산자"""
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """- 연산자"""
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """* 연산자 (스칼라 곱)"""
        return Vector2D(self.x * scalar, self.y * scalar)

    def __len__(self):
        """len() 함수"""
        return int(math.sqrt(self.x**2 + self.y**2))

v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print(v1 + v2)  # Vector(4, 6)
print(v1 - v2)  # Vector(2, 2)
print(v1 * 2)   # Vector(6, 8)
print(len(v1))  # 5
```

**예시 3: 컨테이너 특수 메서드**
```python
class ShoppingCart:
    def __init__(self):
        self.items = []

    def __len__(self):
        """len(cart) -> 상품 개수"""
        return len(self.items)

    def __getitem__(self, index):
        """cart[0] -> 첫 번째 상품"""
        return self.items[index]

    def __setitem__(self, index, value):
        """cart[0] = '상품' -> 상품 설정"""
        self.items[index] = value

    def __contains__(self, item):
        """item in cart -> 포함 여부"""
        return item in self.items

    def __iter__(self):
        """for item in cart"""
        return iter(self.items)

    def add(self, item):
        self.items.append(item)

cart = ShoppingCart()
cart.add("노트북")
cart.add("마우스")
cart.add("키보드")

print(len(cart))  # 3
print(cart[0])    # "노트북"
print("마우스" in cart)  # True

for item in cart:
    print(item)
```

### 💻 실습 (10분)

**[실습 파일: session7_special_methods_practice.py](./session7_special_methods_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session7_special_methods_solution.py](./session7_special_methods_solution.py)**

**핵심 포인트:**
1. `__str__`과 `__repr__` 구분
2. 연산자 오버로딩으로 직관적인 코드
3. 새 객체 반환 (원본 수정 안함)

---

## 세션 8: 프로퍼티 (@property) (25분)
**중요도:** ★★★★★

### 📖 이론 (10분)

#### 8.1 프로퍼티 (Property)

**프로퍼티**는 메서드를 속성처럼 사용하게 해주는 데코레이터입니다.

**예시 1: 기본 프로퍼티**
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """Getter"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter"""
        if value < -273.15:
            raise ValueError("절대영도 이하입니다!")
        self._celsius = value

    @property
    def fahrenheit(self):
        """자동 계산 (읽기 전용)"""
        return self._celsius * 9/5 + 32

temp = Temperature(25)
print(temp.celsius)      # Getter 호출
temp.celsius = 30        # Setter 호출
print(temp.fahrenheit)   # 86.0 (계산됨)
# temp.fahrenheit = 100  # AttributeError! (setter 없음)
```

**예시 2: 검증 프로퍼티**
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        """가격 조회"""
        return self._price

    @price.setter
    def price(self, value):
        """가격 설정 (검증)"""
        if value < 0:
            raise ValueError("가격은 0 이상이어야 합니다")
        self._price = value

    @property
    def display_price(self):
        """표시 가격 (세금 포함, 읽기 전용)"""
        return int(self._price * 1.1)  # 10% 세금

product = Product("노트북", 1000000)
print(product.price)          # 1000000
print(product.display_price)  # 1100000
product.price = 1200000       # OK
# product.price = -1000       # ValueError!
```

**예시 3: 직사각형 클래스**
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width   # setter 호출됨
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("너비는 양수여야 합니다")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("높이는 양수여야 합니다")
        self._height = value

    @property
    def area(self):
        """넓이 (자동 계산, 읽기 전용)"""
        return self._width * self._height

    @property
    def perimeter(self):
        """둘레 (자동 계산, 읽기 전용)"""
        return 2 * (self._width + self._height)

rect = Rectangle(10, 5)
print(rect.area)       # 50
print(rect.perimeter)  # 30
rect.width = 20        # setter 호출
print(rect.area)       # 100 (자동 업데이트)
```

#### 8.2 Java와 비교

```java
// Java - Getter/Setter 메서드
temp.setCelsius(25);  // 메서드 호출
```

```python
# Python - 속성처럼 사용
temp.celsius = 25  # 프로퍼티 사용
```

### 💻 실습 (10분)

**[실습 파일: session8_property_practice.py](./session8_property_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session8_property_solution.py](./session8_property_solution.py)**

**핵심 포인트:**
1. Setter에서 검증 로직
2. 계산 프로퍼티는 Getter만 (읽기 전용)
3. `__init__`에서 프로퍼티 사용하면 검증 자동

---

## 세션 9: 종합 실습 프로젝트 (25분)
**중요도:** ★★★★★

### 📖 이론 (5분)

#### 9.1 프로젝트: 도서관 관리 시스템

**구현해야 할 클래스:**
1. **Book**: 기본 도서 정보
2. **EBook**: 전자책 (Book 상속)
3. **AudioBook**: 오디오북 (Book 상속)
4. **Library**: 도서 관리

**적용할 OOP 개념:**
- 상속 (Book → EBook, AudioBook)
- 캡슐화 (private 변수)
- 메서드 오버라이딩 (get_info)
- 특수 메서드 (__str__, __repr__)
- 프로퍼티 (@property)

### 💻 실습 (15분)

**[실습 파일: session9_final_project_practice.py](./session9_final_project_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session9_final_project_solution.py](./session9_final_project_solution.py)**

**핵심 구조:**
```python
class Book:
    total_books = 0  # 클래스 변수

    def __init__(self, title, author, isbn, price):
        self.title = title
        self.author = author
        self.__is_borrowed = False
        Book.total_books += 1

    @property
    def is_available(self):
        return not self.__is_borrowed

    def borrow(self):
        if self.__is_borrowed:
            return False
        self.__is_borrowed = True
        return True

class EBook(Book):
    def __init__(self, title, author, isbn, price, file_size):
        super().__init__(title, author, isbn, price)
        self.file_size = file_size

class Library:
    def __init__(self, name):
        self.name = name
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)
```

---

## 🎯 Day 7 마무리

### 학습 내용 요약

| 세션 | 주제 | 중요도 | 핵심 키워드 |
|-----|------|--------|-----------|
| 1 | 인스턴스 vs 클래스 변수 | ★★★★★ | self.변수, 클래스명.변수 |
| 2 | 캡슐화 | ★★★★★ | __, _, Getter/Setter |
| 3 | 상속 기초 | ★★★★★ | class Child(Parent), super() |
| 4 | 메서드 오버라이딩 | ★★★★★ | 다형성, NotImplementedError |
| 5 | super() 함수 | ★★★★★ | 부모 메서드 호출 |
| 6 | 다중 상속 | ★★★★☆ | Mixin, MRO |
| 7 | 특수 메서드 | ★★★★★ | __str__, __add__, __len__ |
| 8 | 프로퍼티 | ★★★★★ | @property, @setter |
| 9 | 종합 프로젝트 | ★★★★★ | OOP 종합 적용 |

### 실무 활용 포인트

**객체지향 프로그래밍이 중요한 이유:**
- 코드 재사용성 향상
- 유지보수 용이
- 대규모 프로젝트 구조화

**다음 단계:**
- Django, Flask 웹 프레임워크
- 데이터 분석 라이브러리 (pandas, numpy)
- 디자인 패턴 학습
- 실전 프로젝트 개발

---

**축하합니다!**

Python 객체지향 프로그래밍의 핵심을 모두 학습하셨습니다!
이제 실무 프로젝트를 만들어보세요!
