"""
파일명: session7_special_methods.py
목적: 특수 메서드 실습
"""

import math

print("=" * 70)
print("특수 메서드 (Magic Methods)".center(70))
print("=" * 70)

# 1. __str__ vs __repr__
print("\n[1] __str__ vs __repr__")
print("-" * 70)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        """사용자 친화적 문자열 (print용)"""
        return f"{self.name}: {self.price:,}원"

    def __repr__(self):
        """개발자용 표현 (디버깅용)"""
        return f"Product('{self.name}', {self.price})"

product = Product("노트북", 1200000)

print(f"str(product): {str(product)}")      # __str__ 호출
print(f"repr(product): {repr(product)}")    # __repr__ 호출
print(f"print(product): {product}")         # __str__ 호출

# 2. 비교 연산자 (__lt__, __eq__, __le__, __gt__, __ge__, __ne__)
print("\n[2] 비교 연산자")
print("-" * 70)

class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __lt__(self, other):
        """< 연산자"""
        return self.price < other.price

    def __le__(self, other):
        """<= 연산자"""
        return self.price <= other.price

    def __gt__(self, other):
        """> 연산자"""
        return self.price > other.price

    def __ge__(self, other):
        """>= 연산자"""
        return self.price >= other.price

    def __eq__(self, other):
        """== 연산자"""
        return self.price == other.price

    def __ne__(self, other):
        """!= 연산자"""
        return self.price != other.price

    def __str__(self):
        return f"{self.title} ({self.price:,}원)"

book1 = Book("파이썬 입문", 25000)
book2 = Book("자바 완벽 가이드", 35000)

print(f"{book1}")
print(f"{book2}")
print()

print(f"book1 < book2: {book1 < book2}")
print(f"book1 > book2: {book1 > book2}")
print(f"book1 == book2: {book1 == book2}")
print(f"book1 != book2: {book1 != book2}")

# 정렬
books = [
    Book("Python 심화", 30000),
    Book("JavaScript 기초", 20000),
    Book("알고리즘", 40000)
]

sorted_books = sorted(books)

print("\n가격순 정렬:")
for book in sorted_books:
    print(f"  {book}")

# 3. 산술 연산자 (__add__, __sub__, __mul__, __div__)
print("\n[3] 산술 연산자")
print("-" * 70)

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """+ 연산자 (벡터 덧셈)"""
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """- 연산자 (벡터 뺄셈)"""
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """* 연산자 (스칼라 곱)"""
        return Vector2D(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        """/ 연산자 (스칼라 나눗셈)"""
        return Vector2D(self.x / scalar, self.y / scalar)

    def __len__(self):
        """len() 함수 (벡터 크기)"""
        return int(math.sqrt(self.x**2 + self.y**2))

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")
print(f"v1 / 2 = {v1 / 2}")
print(f"len(v1) = {len(v1)}")

# 4. 컨테이너 메서드 (__len__, __getitem__, __setitem__, __contains__)
print("\n[4] 컨테이너 메서드")
print("-" * 70)

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def __len__(self):
        """len(playlist)"""
        return len(self.songs)

    def __getitem__(self, index):
        """playlist[index]"""
        return self.songs[index]

    def __setitem__(self, index, value):
        """playlist[index] = value"""
        self.songs[index] = value

    def __contains__(self, item):
        """item in playlist"""
        return item in self.songs

    def __iter__(self):
        """for song in playlist"""
        return iter(self.songs)

    def add_song(self, song):
        self.songs.append(song)

    def __str__(self):
        return f"{self.name} ({len(self)} songs)"

# 플레이리스트 사용
playlist = Playlist("내가 좋아하는 음악")
playlist.add_song("Bad Guy - Billie Eilish")
playlist.add_song("Blinding Lights - The Weeknd")
playlist.add_song("Shape of You - Ed Sheeran")

print(f"{playlist}")
print(f"len(playlist): {len(playlist)}")
print(f"playlist[0]: {playlist[0]}")
print(f"'Bad Guy' in playlist: {'Bad Guy - Billie Eilish' in playlist}")

print("\n전체 곡:")
for i, song in enumerate(playlist, 1):
    print(f"  {i}. {song}")

# 5. 실습: Money 클래스
print("\n[5] 실습: Money 클래스")
print("-" * 70)

class Money:
    def __init__(self, amount, currency="KRW"):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        """돈 더하기"""
        if self.currency != other.currency:
            raise ValueError("통화가 다릅니다!")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        """돈 빼기"""
        if self.currency != other.currency:
            raise ValueError("통화가 다릅니다!")
        return Money(self.amount - other.amount, self.currency)

    def __mul__(self, multiplier):
        """돈 곱하기"""
        return Money(self.amount * multiplier, self.currency)

    def __lt__(self, other):
        """< 비교"""
        if self.currency != other.currency:
            raise ValueError("통화가 다릅니다!")
        return self.amount < other.amount

    def __eq__(self, other):
        """== 비교"""
        return self.amount == other.amount and self.currency == other.currency

    def __str__(self):
        return f"{self.amount:,}{self.currency}"

    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"

# Money 클래스 사용
price1 = Money(50000)
price2 = Money(30000)
price3 = Money(20000)

print(f"가격1: {price1}")
print(f"가격2: {price2}")
print(f"가격3: {price3}")

print(f"\n가격1 + 가격2 = {price1 + price2}")
print(f"가격1 - 가격2 = {price1 - price2}")
print(f"가격2 * 3 = {price2 * 3}")

print(f"\n가격1 > 가격2: {price1 > price2}")
print(f"가격2 == 가격3: {price2 == price3}")

# 6. __call__ (호출 가능한 객체)
print("\n[6] __call__ (호출 가능한 객체)")
print("-" * 70)

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        """객체를 함수처럼 호출"""
        return x * self.factor

# 객체를 함수처럼 사용
double = Multiplier(2)
triple = Multiplier(3)

print(f"double(5) = {double(5)}")
print(f"triple(5) = {triple(5)}")

# 7. __enter__와 __exit__ (컨텍스트 매니저)
print("\n[7] __enter__와 __exit__ (with문)")
print("-" * 70)

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """with 블록 진입 시"""
        print(f"파일 열기: {self.filename}")
        self.file = open(self.filename, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """with 블록 종료 시"""
        if self.file:
            self.file.close()
            print(f"파일 닫기: {self.filename}")

# with문 사용
with FileManager("test.txt", "w") as f:
    f.write("Hello, World!")

# 8. 실전 예제: BankAccount 클래스
print("\n[8] 실전 예제: BankAccount 클래스")
print("-" * 70)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def __str__(self):
        """사용자 친화적 출력"""
        return f"{self.owner}님의 계좌 (잔액: {self.balance:,}원)"

    def __repr__(self):
        """개발자용 출력"""
        return f"BankAccount('{self.owner}', {self.balance})"

    def __len__(self):
        """거래 건수"""
        return len(self.transactions)

    def __getitem__(self, index):
        """거래 내역 조회"""
        return self.transactions[index]

    def __add__(self, amount):
        """계좌 + 금액 (입금)"""
        new_account = BankAccount(self.owner, self.balance + amount)
        new_account.transactions = self.transactions.copy()
        new_account.transactions.append(f"입금: +{amount:,}원")
        return new_account

    def __sub__(self, amount):
        """계좌 - 금액 (출금)"""
        if amount > self.balance:
            raise ValueError("잔액 부족!")
        new_account = BankAccount(self.owner, self.balance - amount)
        new_account.transactions = self.transactions.copy()
        new_account.transactions.append(f"출금: -{amount:,}원")
        return new_account

    def __lt__(self, other):
        """잔액 비교"""
        return self.balance < other.balance

    def __eq__(self, other):
        """잔액 같음"""
        return self.balance == other.balance

# 계좌 생성
acc1 = BankAccount("김철수", 100000)
acc2 = BankAccount("이영희", 200000)

print(acc1)
print(acc2)

# 입출금
acc1 = acc1 + 50000  # 입금
acc1 = acc1 - 30000  # 출금

print(f"\n거래 후: {acc1}")
print(f"거래 건수: {len(acc1)}")
print("거래 내역:")
for i, transaction in enumerate(acc1, 1):
    print(f"  {i}. {transaction}")

# 비교
print(f"\nacc1 < acc2: {acc1 < acc2}")

# 9. 특수 메서드 종합
print("\n[9] 특수 메서드 종합: Point 클래스")
print("-" * 70)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 문자열 표현
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    # 산술 연산
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # 비교 연산 (원점으로부터의 거리)
    def __lt__(self, other):
        return self.distance() < other.distance()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # 기타
    def __len__(self):
        """원점으로부터의 거리"""
        return int(math.sqrt(self.x**2 + self.y**2))

    def __bool__(self):
        """원점이 아니면 True"""
        return self.x != 0 or self.y != 0

    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)

# Point 사용
p1 = Point(3, 4)
p2 = Point(1, 2)

print(f"p1 = {p1}")
print(f"p2 = {p2}")
print(f"p1 + p2 = {p1 + p2}")
print(f"p1 - p2 = {p1 - p2}")
print(f"len(p1) = {len(p1)}")
print(f"p1 > p2: {p1 > p2}")
print(f"bool(p1): {bool(p1)}")
print(f"bool(Point(0, 0)): {bool(Point(0, 0))}")

# 10. 주요 특수 메서드 정리
print("\n[10] 주요 특수 메서드 정리")
print("-" * 70)

special_methods = {
    "문자열 표현": [
        ("__str__", "str(), print()"),
        ("__repr__", "repr(), 디버깅"),
    ],
    "비교 연산": [
        ("__lt__", "< 연산자"),
        ("__le__", "<= 연산자"),
        ("__gt__", "> 연산자"),
        ("__ge__", ">= 연산자"),
        ("__eq__", "== 연산자"),
        ("__ne__", "!= 연산자"),
    ],
    "산술 연산": [
        ("__add__", "+ 연산자"),
        ("__sub__", "- 연산자"),
        ("__mul__", "* 연산자"),
        ("__truediv__", "/ 연산자"),
    ],
    "컨테이너": [
        ("__len__", "len()"),
        ("__getitem__", "obj[key]"),
        ("__setitem__", "obj[key] = value"),
        ("__contains__", "item in obj"),
        ("__iter__", "for item in obj"),
    ],
    "기타": [
        ("__call__", "obj()"),
        ("__enter__, __exit__", "with obj:"),
    ]
}

for category, methods in special_methods.items():
    print(f"\n{category}:")
    for method, description in methods:
        print(f"  {method:<20} → {description}")

print("\n" + "=" * 70)
print("핵심 정리".center(70))
print("=" * 70)

print("""
✅ 특수 메서드 (Magic Methods):
  - __method__ 형태
  - Python 내장 기능과 연동
  - 연산자 오버로딩 구현

✅ 필수 특수 메서드:
  - __init__: 초기화
  - __str__: 사용자용 문자열
  - __repr__: 개발자용 표현

✅ 유용한 특수 메서드:
  - 비교: __lt__, __eq__
  - 산술: __add__, __sub__
  - 컨테이너: __len__, __getitem__

💡 장점:
  - Python다운 클래스 작성
  - 내장 함수와 자연스럽게 통합
  - 코드 가독성 향상
""")

print("\n💡 Tip: 다음 세션에서 @property로 더 우아한 속성 관리를 배웁니다!")
