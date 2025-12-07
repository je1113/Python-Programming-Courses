# 7일차: 클래스 심화 - 객체지향 프로그래밍 마스터

## 📚 학습 목표
- 인스턴스 변수와 클래스 변수의 차이 이해
- 캡슐화를 통한 정보 은닉 구현
- 상속으로 코드 재사용성 향상
- 메서드 오버라이딩과 super() 활용
- 특수 메서드로 Python다운 클래스 작성
- 프로퍼티로 안전한 속성 관리

---

## 🎯 오늘의 주요 내용

### ⏰ 일정 (총 4시간, 240분)
| 세션 | 주제 | 시간 | 실습 파일 |
|------|------|------|-----------|
| 1 | 인스턴스 vs 클래스 변수 | 25분 | [session1_class_vs_instance.py](session1_class_vs_instance.py) |
| 2 | 캡슐화와 정보 은닉 | 25분 | [session2_encapsulation.py](session2_encapsulation.py) |
| 3 | 상속 기초 | 25분 | [session3_inheritance_basic.py](session3_inheritance_basic.py) |
| 4 | 메서드 오버라이딩 | 25분 | [session4_method_overriding.py](session4_method_overriding.py) |
| 5 | super() 함수 | 25분 | [session5_super_function.py](session5_super_function.py) |
| 6 | 다중 상속 | 25분 | [session6_multiple_inheritance.py](session6_multiple_inheritance.py) |
| 7 | 특수 메서드 | 30분 | [session7_special_methods.py](session7_special_methods.py) |
| 8 | 프로퍼티 (@property) | 25분 | [session8_property.py](session8_property.py) |
| 9 | 종합 실습 프로젝트 | 35분 | [session9_final_project.py](session9_final_project.py) |

---

## 📖 Session 1: 인스턴스 vs 클래스 변수 (25분)

### 이론 (10분)

#### 개념 ★★★★★
**인스턴스 변수**와 **클래스 변수**는 객체지향 프로그래밍의 핵심 개념입니다.

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
```

**차이점:**
| 구분 | 인스턴스 변수 | 클래스 변수 |
|------|--------------|-------------|
| 정의 위치 | `__init__` 내부 | 클래스 블록 최상단 |
| 접근 방식 | `self.변수명` | `클래스명.변수명` |
| 공유 여부 | 각 객체마다 독립적 | 모든 객체가 공유 |
| 사용 사례 | 개인 정보 (이름, 나이) | 공통 설정 (회사명, 카운터) |

---

#### Java와 비교
```java
// Java
class Employee {
    // 클래스 변수 (static)
    static String companyName = "ABC 기업";
    static int employeeCount = 0;

    // 인스턴스 변수
    private String name;
    private int salary;
}
```

```python
# Python
class Employee:
    # 클래스 변수
    company_name = "ABC 기업"
    employee_count = 0

    def __init__(self, name, salary):
        # 인스턴스 변수
        self.name = name
        self.salary = salary
```

**Python의 특징:**
- Java의 `static` 키워드 없이 클래스 블록에 정의하면 클래스 변수
- `self.`를 붙이면 인스턴스 변수

---

#### 실무 활용 사례
```python
class DatabaseConnection:
    # 클래스 변수: 연결 풀 크기 (모든 연결에 공통)
    max_connections = 10
    active_connections = 0

    def __init__(self, host, port):
        # 인스턴스 변수: 각 연결마다 다름
        self.host = host
        self.port = port
        DatabaseConnection.active_connections += 1
```

**언제 사용하나?**
- **클래스 변수**: 설정값, 카운터, 공유 리소스
- **인스턴스 변수**: 객체별 고유 데이터

---

### 실습 (10분)
**문제:** 은행 계좌 관리 시스템을 만들어보세요.

**요구사항:**
1. `BankAccount` 클래스 생성
2. 클래스 변수: `bank_name` (은행명), `interest_rate` (이자율), `total_accounts` (총 계좌 수)
3. 인스턴스 변수: `account_number` (계좌번호), `owner` (예금주), `balance` (잔액)
4. 메서드: `deposit()`, `withdraw()`, `apply_interest()` (이자 적용)

**실습 파일:** [session1_class_vs_instance.py](session1_class_vs_instance.py)

---

### 해설 (5분)

#### 모범 답안
```python
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
        self.balance += amount
        print(f"{amount:,}원 입금 완료. 잔액: {self.balance:,}원")

    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액 부족!")
        else:
            self.balance -= amount
            print(f"{amount:,}원 출금 완료. 잔액: {self.balance:,}원")

    def apply_interest(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"이자 {interest:,}원 적용. 잔액: {self.balance:,}원")
```

#### 주요 포인트
✅ 클래스 변수는 `클래스명.변수명`으로 접근
✅ `total_accounts`처럼 객체 생성시마다 증가하는 카운터는 클래스 변수
✅ 각 계좌의 잔액은 독립적이므로 인스턴스 변수

#### 자주 하는 실수
```python
# ❌ 잘못된 예
def __init__(self, name):
    self.name = name
    self.employee_count += 1  # 인스턴스 변수로 인식됨!

# ✅ 올바른 예
def __init__(self, name):
    self.name = name
    Employee.employee_count += 1  # 클래스 변수 접근
```

#### 💡 Tip
- 클래스 변수 수정시 항상 `클래스명.변수명` 사용
- `self.클래스변수`로 읽기는 가능하지만 쓰기는 인스턴스 변수 생성!

---

## 📖 Session 2: 캡슐화와 정보 은닉 (25분)

### 이론 (10분)

#### 개념 ★★★★★
**캡슐화(Encapsulation)**는 데이터와 메서드를 하나로 묶고, 외부 접근을 제한하는 것입니다.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private 변수 (__)

    def get_balance(self):  # Getter
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("입금액은 0보다 커야 합니다")
```

**Python의 접근 제어자:**
| 표기 | 의미 | 설명 |
|------|------|------|
| `name` | public | 어디서든 접근 가능 |
| `_name` | protected | 내부 구현 (관례상 외부에서 사용 자제) |
| `__name` | private | Name Mangling (외부 접근 어려움) |

---

#### Java와 비교
```java
// Java
class BankAccount {
    private int balance;  // private

    public int getBalance() {  // Getter
        return balance;
    }

    public void deposit(int amount) {
        if (amount > 0) {
            this.balance += amount;
        }
    }
}
```

```python
# Python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private (__)

    def get_balance(self):  # Getter
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
```

**Python의 특징:**
- Java의 `private`, `public` 키워드 대신 `__` 접두사 사용
- 완전한 private은 아니지만 Name Mangling으로 접근 어렵게 만듦

---

#### 실무 활용 사례
```python
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = self.__hash_password(password)  # 비밀번호 숨김

    def __hash_password(self, password):
        """비밀번호 해싱 (private 메서드)"""
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        """비밀번호 검증"""
        return self.__password == self.__hash_password(password)
```

**왜 캡슐화가 중요한가?**
1. **데이터 보호**: 잘못된 값 설정 방지
2. **내부 구현 숨김**: 외부에서 구현 세부사항 몰라도 됨
3. **유지보수성**: 내부 구조 변경해도 외부 코드 영향 없음

---

### 실습 (10분)
**문제:** 직원 급여 관리 클래스를 만들어보세요.

**요구사항:**
1. `Employee` 클래스 생성
2. `__salary` (급여)는 private으로 보호
3. `get_salary()`: 급여 조회 (Getter)
4. `set_salary(amount)`: 급여 설정 (최소 급여 검증)
5. `give_raise(percentage)`: 급여 인상 (0~100% 범위 검증)

**실습 파일:** [session2_encapsulation.py](session2_encapsulation.py)

---

### 해설 (5분)

#### 모범 답안
```python
class Employee:
    MIN_SALARY = 1000  # 최소 급여 (클래스 변수)

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
```

#### 주요 포인트
✅ `__init__`에서도 `set_salary()` 사용해서 검증 로직 재사용
✅ Getter/Setter로 외부 접근 제어
✅ 잘못된 값 설정시 예외 발생

#### 자주 하는 실수
```python
# ❌ 검증 없이 직접 설정
def __init__(self, salary):
    self.__salary = salary  # 음수도 설정됨!

# ✅ Setter를 통한 검증
def __init__(self, salary):
    self.set_salary(salary)  # 검증 로직 통과
```

#### 💡 Tip
- Name Mangling: `__balance`는 실제로 `_ClassName__balance`로 저장됨
- 정말 급하면 `obj._ClassName__private_var`로 접근 가능 (비추천!)

---

## 📖 Session 3: 상속 기초 (25분)

### 이론 (10분)

#### 개념 ★★★★★
**상속(Inheritance)**은 기존 클래스의 기능을 물려받아 새로운 클래스를 만드는 것입니다.

```python
# 부모 클래스 (상위 클래스, 슈퍼 클래스)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

# 자식 클래스 (하위 클래스, 서브 클래스)
class Dog(Animal):
    def speak(self):
        return "멍멍!"

class Cat(Animal):
    def speak(self):
        return "야옹!"
```

**상속의 장점:**
1. **코드 재사용**: 공통 기능을 부모 클래스에 한 번만 작성
2. **확장성**: 기존 코드 수정 없이 새 기능 추가
3. **다형성**: 같은 인터페이스로 다른 동작 구현

---

#### Java와 비교
```java
// Java
class Animal {
    protected String name;

    public Animal(String name) {
        this.name = name;
    }

    public String speak() {
        return "...";
    }
}

class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }

    @Override
    public String speak() {
        return "멍멍!";
    }
}
```

```python
# Python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "멍멍!"
```

**Python의 특징:**
- `extends` 키워드 대신 `class Dog(Animal):` 형태
- `@Override` 없이 그냥 메서드 재정의

---

#### 실무 활용 사례
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
```

---

### 실습 (10분)
**문제:** 도형 클래스 계층 구조를 만들어보세요.

**요구사항:**
1. `Shape` 부모 클래스: `color` 속성, `get_info()` 메서드
2. `Rectangle` 클래스: `width`, `height` 추가, `area()` 메서드
3. `Circle` 클래스: `radius` 추가, `area()` 메서드
4. 각 도형의 넓이를 계산하고 정보 출력

**실습 파일:** [session3_inheritance_basic.py](session3_inheritance_basic.py)

---

### 해설 (5분)

#### 모범 답안
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
```

#### 주요 포인트
✅ `super().__init__()`로 부모 클래스 초기화
✅ 각 자식 클래스에서 `area()` 구현
✅ `get_info()`에서 부모 메서드 재사용

#### 💡 Tip
- `isinstance(obj, ClassName)`: 객체가 특정 클래스의 인스턴스인지 확인
- `issubclass(SubClass, ParentClass)`: 상속 관계 확인

---

## 📖 Session 4: 메서드 오버라이딩 (25분)

### 이론 (10분)

#### 개념 ★★★★★
**메서드 오버라이딩(Method Overriding)**은 부모 클래스의 메서드를 자식 클래스에서 재정의하는 것입니다.

```python
class Employee:
    def calculate_bonus(self):
        return self.salary * 0.1  # 기본 10%

class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.2  # 관리자는 20%

class Intern(Employee):
    def calculate_bonus(self):
        return self.salary * 0.05  # 인턴은 5%
```

**오버라이딩 규칙:**
1. 메서드 이름이 동일해야 함
2. 매개변수 구조가 호환되어야 함 (Python은 유연함)
3. 자식 클래스에서 더 구체적인 구현 제공

---

#### 실무 활용 사례
```python
class PaymentMethod:
    def process_payment(self, amount):
        raise NotImplementedError("하위 클래스에서 구현해야 합니다")

class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        print(f"신용카드로 {amount:,}원 결제")
        # 신용카드 결제 로직
        return True

class BankTransfer(PaymentMethod):
    def process_payment(self, amount):
        print(f"계좌이체로 {amount:,}원 결제")
        # 계좌이체 로직
        return True

# 다형성 활용
def checkout(payment_method, amount):
    payment_method.process_payment(amount)  # 어떤 결제 수단이든 동일하게 호출

checkout(CreditCard(), 50000)
checkout(BankTransfer(), 100000)
```

---

### 실습 (10분)
**문제:** 직원 급여 계산 시스템을 만들어보세요.

**요구사항:**
1. `Employee` 부모 클래스: `calculate_pay()` 메서드 (기본 급여)
2. `HourlyEmployee`: 시급 * 근무시간
3. `SalariedEmployee`: 월급 고정
4. `CommissionEmployee`: 기본급 + 판매 수수료
5. 각 직원 타입별로 급여 계산 및 출력

**실습 파일:** [session4_method_overriding.py](session4_method_overriding.py)

---

### 해설 (5분)

#### 모범 답안
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
```

#### 주요 포인트
✅ 부모 클래스에서 `NotImplementedError` 발생시켜 추상 메서드 표현
✅ 각 자식 클래스에서 고유한 계산 로직 구현
✅ 다형성: `calculate_pay()` 하나로 모든 직원 처리 가능

---

## 📖 Session 5: super() 함수 (25분)

### 이론 (10분)

#### 개념 ★★★★★
`super()`는 부모 클래스의 메서드를 호출할 때 사용합니다.

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
```

**super()의 용도:**
1. 부모 클래스의 `__init__()` 호출
2. 오버라이딩한 메서드에서 부모 메서드 재사용
3. 다중 상속에서 MRO(Method Resolution Order) 따라 호출

---

#### Java와 비교
```java
// Java
class Child extends Parent {
    public Child(String name, int age) {
        super(name);  // 부모 생성자
        this.age = age;
    }

    public void greet() {
        super.greet();  // 부모 메서드
    }
}
```

```python
# Python
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # 부모 생성자
        self.age = age

    def greet(self):
        super().greet()  # 부모 메서드
```

**Python의 특징:**
- Java와 거의 동일하게 `super()` 사용
- Python 2에서는 `super(ClassName, self)` 형태였지만 Python 3부터 간소화

---

#### 실무 활용 사례
```python
class Logger:
    def log(self, message):
        print(f"[LOG] {message}")

class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        super().log(message)  # 콘솔에 출력
        with open(self.filename, "a") as f:  # 파일에도 저장
            f.write(f"{message}\n")
```

---

### 실습 (10분)
**문제:** 계좌 클래스 상속 구조를 만들어보세요.

**요구사항:**
1. `Account` 부모 클래스: 예금/출금 기능
2. `SavingsAccount`: 이자 적용 기능 추가, 출금시 수수료
3. `CheckingAccount`: 한도 체크 기능 추가
4. `super()`를 사용해서 부모 기능 재사용

**실습 파일:** [session5_super_function.py](session5_super_function.py)

---

### 해설 (5분)

#### 모범 답안
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

class CheckingAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=100000):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print(f"한도 초과! (한도: {self.overdraft_limit:,}원)")
            return False
        return super().withdraw(amount)
```

#### 주요 포인트
✅ `super().__init__()`로 부모 초기화 먼저 수행
✅ 부모 메서드 호출 후 추가 로직 수행
✅ `super().withdraw()`의 반환값 활용

---

## 📖 Session 6: 다중 상속 (25분)

### 이론 (10분)

#### 개념 ★★★★
**다중 상속(Multiple Inheritance)**은 여러 부모 클래스로부터 상속받는 것입니다.

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
print(duck.fly())   # Flyable의 메서드
print(duck.swim())  # Swimmable의 메서드
```

**MRO (Method Resolution Order):**
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

---

#### Java와 비교
```java
// Java는 다중 상속 불가능! (인터페이스로 대체)
interface Flyable {
    void fly();
}

interface Swimmable {
    void swim();
}

class Duck implements Flyable, Swimmable {
    public void fly() { }
    public void swim() { }
}
```

```python
# Python은 다중 상속 가능
class Duck(Flyable, Swimmable):
    pass
```

**Python의 특징:**
- 다중 상속 지원 (Diamond Problem 주의!)
- MRO로 메서드 호출 순서 결정 (C3 linearization)

---

#### 실무 활용 사례
```python
# Mixin 패턴
class JSONSerializableMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class LoggableMixin:
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

class User(JSONSerializableMixin, LoggableMixin):
    def __init__(self, username, email):
        self.username = username
        self.email = email

user = User("john", "john@example.com")
print(user.to_json())  # {"username": "john", "email": "john@example.com"}
user.log("사용자 생성됨")  # [User] 사용자 생성됨
```

---

### 실습 (10분)
**문제:** 스마트 기기 클래스를 만들어보세요.

**요구사항:**
1. `Phone`: 전화 기능
2. `Camera`: 사진 촬영 기능
3. `MusicPlayer`: 음악 재생 기능
4. `SmartPhone`: Phone, Camera, MusicPlayer 모두 상속

**실습 파일:** [session6_multiple_inheritance.py](session6_multiple_inheritance.py)

---

### 해설 (5분)

#### 모범 답안
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
```

#### 주요 포인트
✅ 다중 상속시 각 부모 클래스 명시적 초기화
✅ Mixin 패턴으로 기능 조합
⚠️ Diamond Problem 주의 (공통 부모 있을 때 충돌)

---

## 📖 Session 7: 특수 메서드 (30분)

### 이론 (10분)

#### 개념 ★★★★★
**특수 메서드(Special Methods)**는 `__method__` 형태로 Python의 내장 기능과 연동됩니다.

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

    def __add__(self, other):
        """+ 연산자"""
        return self.price + other.price
```

**주요 특수 메서드:**
| 메서드 | 용도 | 예시 |
|--------|------|------|
| `__init__` | 초기화 | `obj = MyClass()` |
| `__str__` | 문자열 표현 | `print(obj)` |
| `__repr__` | 공식 표현 | `repr(obj)` |
| `__len__` | 길이 | `len(obj)` |
| `__getitem__` | 인덱싱 | `obj[key]` |
| `__add__` | 덧셈 | `obj1 + obj2` |
| `__lt__` | 작다 | `obj1 < obj2` |
| `__eq__` | 같다 | `obj1 == obj2` |

---

#### 실무 활용 사례
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

    def __contains__(self, item):
        """item in cart -> 포함 여부"""
        return item in self.items

    def __iter__(self):
        """for item in cart"""
        return iter(self.items)

cart = ShoppingCart()
cart.items = ["노트북", "마우스", "키보드"]

print(len(cart))  # 3
print(cart[0])    # 노트북
print("마우스" in cart)  # True
for item in cart:
    print(item)
```

---

### 실습 (15분)
**문제:** 벡터 클래스를 만들어보세요.

**요구사항:**
1. `Vector2D` 클래스 (x, y 좌표)
2. `__str__`: 벡터 출력
3. `__add__`: 벡터 덧셈
4. `__sub__`: 벡터 뺄셈
5. `__mul__`: 스칼라 곱
6. `__len__`: 벡터 크기

**실습 파일:** [session7_special_methods.py](session7_special_methods.py)

---

### 해설 (5분)

#### 모범 답안
```python
import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __len__(self):
        return int(math.sqrt(self.x**2 + self.y**2))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

#### 주요 포인트
✅ 특수 메서드로 연산자 오버로딩
✅ `__str__`과 `__repr__` 구분
✅ 새 객체 반환 (원본 수정 안함)

---

## 📖 Session 8: 프로퍼티 (@property) (25분)

### 이론 (10분)

#### 개념 ★★★★★
**프로퍼티(Property)**는 메서드를 속성처럼 사용하게 해주는 데코레이터입니다.

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
        """자동 계산"""
        return self._celsius * 9/5 + 32

temp = Temperature(25)
print(temp.celsius)      # Getter 호출
temp.celsius = 30        # Setter 호출
print(temp.fahrenheit)   # 계산 프로퍼티
```

**장점:**
1. Getter/Setter를 속성처럼 사용
2. 검증 로직 추가 가능
3. 계산된 속성 구현
4. 리팩토링 쉬움 (필드 → 프로퍼티 변환)

---

#### Java와 비교
```java
// Java
class Temperature {
    private double celsius;

    public double getCelsius() {
        return celsius;
    }

    public void setCelsius(double value) {
        if (value < -273.15) {
            throw new IllegalArgumentException();
        }
        this.celsius = value;
    }
}

Temperature temp = new Temperature();
temp.setCelsius(25);  // 메서드 호출
```

```python
# Python
class Temperature:
    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError()
        self._celsius = value

temp = Temperature()
temp.celsius = 25  # 속성처럼 사용!
```

---

#### 실무 활용 사례
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
        """표시 가격 (세금 포함)"""
        return self._price * 1.1  # 10% 세금
```

---

### 실습 (10분)
**문제:** 직사각형 클래스를 만들어보세요.

**요구사항:**
1. `Rectangle` 클래스
2. `width`, `height` 프로퍼티 (양수만 허용)
3. `area` 프로퍼티 (읽기 전용, 자동 계산)
4. `perimeter` 프로퍼티 (읽기 전용, 자동 계산)

**실습 파일:** [session8_property.py](session8_property.py)

---

### 해설 (5분)

#### 모범 답안
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
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
        """넓이 (읽기 전용)"""
        return self._width * self._height

    @property
    def perimeter(self):
        """둘레 (읽기 전용)"""
        return 2 * (self._width + self._height)
```

#### 주요 포인트
✅ Setter에서 검증 로직
✅ 계산 프로퍼티는 Setter 없이 Getter만
✅ `__init__`에서 프로퍼티 사용하면 검증 자동

---

## 📖 Session 9: 종합 실습 프로젝트 (35분)

### 프로젝트: 도서관 관리 시스템 (★★★★★)

#### 요구사항
1. **Book 클래스**: 기본 도서 정보
2. **EBook 클래스**: 전자책 (Book 상속, 파일 크기 추가)
3. **AudioBook 클래스**: 오디오북 (Book 상속, 재생 시간 추가)
4. **Library 클래스**: 도서 관리
   - 도서 추가/삭제
   - 검색 (제목, 저자)
   - 대출/반납
   - 통계 (총 도서 수, 대출 중인 도서)

#### 구현해야 할 기능
- 상속 (Book → EBook, AudioBook)
- 캡슐화 (private 변수)
- 메서드 오버라이딩 (get_info)
- 특수 메서드 (__str__, __repr__)
- 프로퍼티 (@property)

**실습 파일:** [session9_final_project.py](session9_final_project.py)

---

### 모범 답안 구조
```python
class Book:
    """기본 도서 클래스"""
    total_books = 0  # 클래스 변수

    def __init__(self, title, author, isbn, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._price = price
        self.__is_borrowed = False
        Book.total_books += 1

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("가격은 0 이상")
        self._price = value

    def borrow(self):
        if self.__is_borrowed:
            return False
        self.__is_borrowed = True
        return True

    def return_book(self):
        self.__is_borrowed = False

    @property
    def is_available(self):
        return not self.__is_borrowed

    def get_info(self):
        status = "대출 가능" if self.is_available else "대출 중"
        return f"{self.title} - {self.author} ({status})"

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

class EBook(Book):
    """전자책"""
    def __init__(self, title, author, isbn, price, file_size):
        super().__init__(title, author, isbn, price)
        self.file_size = file_size

    def get_info(self):
        base_info = super().get_info()
        return f"[전자책] {base_info} | {self.file_size}MB"

class AudioBook(Book):
    """오디오북"""
    def __init__(self, title, author, isbn, price, duration):
        super().__init__(title, author, isbn, price)
        self.duration = duration

    def get_info(self):
        base_info = super().get_info()
        return f"[오디오북] {base_info} | {self.duration}분"

class Library:
    """도서관 관리"""
    def __init__(self, name):
        self.name = name
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)
        print(f"✓ '{book.title}' 추가 완료")

    def search_by_title(self, keyword):
        return [book for book in self.__books if keyword in book.title]

    def search_by_author(self, author):
        return [book for book in self.__books if author in book.author]

    @property
    def total_books(self):
        return len(self.__books)

    @property
    def available_books(self):
        return [book for book in self.__books if book.is_available]

    def show_all(self):
        print(f"\n{'='*60}")
        print(f"{self.name} 도서 목록 ({self.total_books}권)")
        print(f"{'='*60}")
        for i, book in enumerate(self.__books, 1):
            print(f"{i}. {book.get_info()}")
```

---

## 💡 핵심 정리

### 오늘 배운 내용
```
✅ 인스턴스 vs 클래스 변수
  → 객체별 데이터 vs 공유 데이터

✅ 캡슐화
  → __ (private), _ (protected)로 정보 은닉

✅ 상속
  → 코드 재사용, 확장성

✅ 메서드 오버라이딩
  → 부모 메서드를 자식에서 재정의

✅ super()
  → 부모 클래스 메서드 호출

✅ 다중 상속
  → 여러 부모로부터 상속 (MRO 주의)

✅ 특수 메서드
  → __str__, __add__ 등으로 Python다운 클래스

✅ 프로퍼티
  → @property로 Getter/Setter를 속성처럼
```

---

### 객체지향 설계 원칙 (SOLID)

#### 1. SRP (Single Responsibility Principle)
**단일 책임 원칙**: 클래스는 하나의 책임만
```python
# ❌ 나쁜 예
class Employee:
    def calculate_salary(self): pass
    def save_to_database(self): pass  # DB는 별도 클래스로!

# ✅ 좋은 예
class Employee:
    def calculate_salary(self): pass

class EmployeeRepository:
    def save(self, employee): pass
```

#### 2. OCP (Open-Closed Principle)
**개방-폐쇄 원칙**: 확장에는 열려있고, 수정에는 닫혀있어야
```python
# 상속으로 기능 확장 (기존 코드 수정 안함)
class PaymentMethod:
    def process(self): pass

class CreditCard(PaymentMethod):
    def process(self): pass

class BankTransfer(PaymentMethod):
    def process(self): pass
```

#### 3. LSP (Liskov Substitution Principle)
**리스코프 치환 원칙**: 자식 클래스는 부모 클래스를 대체 가능
```python
def process_payment(payment_method: PaymentMethod):
    payment_method.process()  # 어떤 자식 클래스든 OK
```

---

### 다음 학습 방향

#### 고급 OOP
- 추상 클래스 (`abc` 모듈)
- 데이터 클래스 (`dataclasses`)
- 디스크립터 (Descriptor)

#### 디자인 패턴
- 생성 패턴: 싱글톤, 팩토리, 빌더
- 구조 패턴: 어댑터, 데코레이터, 프록시
- 행위 패턴: 옵저버, 전략, 템플릿 메서드

---

## 📎 실습 파일 목록
1. [session1_class_vs_instance.py](session1_class_vs_instance.py) - 클래스/인스턴스 변수
2. [session2_encapsulation.py](session2_encapsulation.py) - 캡슐화와 정보 은닉
3. [session3_inheritance_basic.py](session3_inheritance_basic.py) - 상속 기초
4. [session4_method_overriding.py](session4_method_overriding.py) - 메서드 오버라이딩
5. [session5_super_function.py](session5_super_function.py) - super() 함수
6. [session6_multiple_inheritance.py](session6_multiple_inheritance.py) - 다중 상속
7. [session7_special_methods.py](session7_special_methods.py) - 특수 메서드
8. [session8_property.py](session8_property.py) - 프로퍼티
9. [session9_final_project.py](session9_final_project.py) - 종합 프로젝트

---

**축하합니다!** 🎉

7일간의 Python 기초 과정을 완료하셨습니다!

이제 여러분은:
- ✅ Python 기본 문법 마스터
- ✅ 객체지향 프로그래밍 이해
- ✅ 실무 프로젝트 구현 가능

**다음 단계:**
1. 실전 프로젝트 만들기
2. Django/Flask 웹 프레임워크
3. 데이터 분석 (Pandas, NumPy)
4. 자동화 스크립트

**Happy Coding!** 🐍✨
