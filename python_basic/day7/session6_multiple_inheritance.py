"""
파일명: session6_multiple_inheritance.py
목적: 다중 상속 실습
"""

print("=" * 70)
print("다중 상속".center(70))
print("=" * 70)

# 1. 기본 다중 상속
print("\n[1] 기본 다중 상속")
print("-" * 70)

class Flyable:
    def fly(self):
        return f"{self.name}이(가) 날고 있습니다"

class Swimmable:
    def swim(self):
        return f"{self.name}이(가) 수영하고 있습니다"

class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name

# 오리는 날 수도, 수영할 수도 있음
duck = Duck("도날드")
print(duck.fly())
print(duck.swim())

# 2. Mixin 패턴
print("\n[2] Mixin 패턴 (기능 조합)")
print("-" * 70)

class JSONSerializableMixin:
    """JSON 직렬화 기능"""

    def to_json(self):
        import json
        return json.dumps(self.__dict__, ensure_ascii=False)

class LoggableMixin:
    """로깅 기능"""

    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

class SaveableMixin:
    """저장 기능"""

    def save(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.to_json())
        print(f"✓ {filename} 저장 완료")

# Mixin 조합
class User(JSONSerializableMixin, LoggableMixin, SaveableMixin):
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.log(f"사용자 생성: {username}")

# 사용
user = User("john", "john@example.com")
print(f"JSON: {user.to_json()}")
user.save("user.json")

# 3. MRO (Method Resolution Order)
print("\n[3] MRO (메서드 해결 순서)")
print("-" * 70)

class A:
    def method(self):
        print("A.method()")

class B(A):
    def method(self):
        print("B.method()")

class C(A):
    def method(self):
        print("C.method()")

class D(B, C):  # 다중 상속
    pass

# MRO 확인
print(f"D의 MRO: {[cls.__name__ for cls in D.__mro__]}")

# 메서드 호출 (MRO 순서대로)
d = D()
d.method()  # B.method() 호출 (D → B → C → A 순서)

# 4. 실습: 스마트 기기
print("\n[4] 실습: 스마트 기기 클래스")
print("-" * 70)

class Phone:
    """전화 기능"""

    def __init__(self, phone_number):
        self.phone_number = phone_number

    def call(self, number):
        print(f"📞 {self.phone_number} → {number} 전화 걸기")

    def receive_call(self):
        print(f"📞 전화 받기")

class Camera:
    """카메라 기능"""

    def __init__(self, resolution):
        self.resolution = resolution

    def take_photo(self):
        print(f"📷 {self.resolution}로 사진 촬영")

    def record_video(self):
        print(f"🎥 {self.resolution}로 영상 녹화")

class MusicPlayer:
    """음악 재생 기능"""

    def __init__(self):
        self.playlist = []

    def play_music(self, song):
        self.playlist.append(song)
        print(f"♪ {song} 재생 중")

    def pause_music(self):
        print("⏸️  일시 정지")

class GPSNavigator:
    """GPS 내비게이션 기능"""

    def navigate(self, destination):
        print(f"🗺️  {destination}(으)로 길안내")

# 스마트폰 = Phone + Camera + MusicPlayer + GPS
class SmartPhone(Phone, Camera, MusicPlayer, GPSNavigator):
    def __init__(self, phone_number, resolution, brand, model):
        Phone.__init__(self, phone_number)
        Camera.__init__(self, resolution)
        MusicPlayer.__init__(self)
        self.brand = brand
        self.model = model

    def get_info(self):
        return f"{self.brand} {self.model} ({self.phone_number})"

# 스마트폰 사용
phone = SmartPhone("010-1234-5678", "4K", "Samsung", "Galaxy S23")

print(f"기기: {phone.get_info()}\n")

phone.call("010-9876-5432")
phone.take_photo()
phone.play_music("Bad Guy - Billie Eilish")
phone.navigate("강남역")

# 5. Diamond Problem
print("\n[5] Diamond Problem (다이아몬드 문제)")
print("-" * 70)

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal.__init__({name})")

    def speak(self):
        print(f"{self.name}: ...")

class Mammal(Animal):
    def __init__(self, name):
        print(f"Mammal.__init__({name})")
        super().__init__(name)

class Bird(Animal):
    def __init__(self, name):
        print(f"Bird.__init__({name})")
        super().__init__(name)

# Platypus는 Mammal과 Bird의 특성을 모두 가짐
class Platypus(Mammal, Bird):
    def __init__(self, name):
        print(f"Platypus.__init__({name})")
        super().__init__(name)  # MRO에 따라 호출

print(f"MRO: {[cls.__name__ for cls in Platypus.__mro__]}")
print()

platypus = Platypus("Perry")

# 6. 기능별 Mixin
print("\n[6] 기능별 Mixin 조합")
print("-" * 70)

class TimestampMixin:
    """타임스탬프 기능"""

    def get_timestamp(self):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class ValidateMixin:
    """검증 기능"""

    def validate(self):
        """하위 클래스에서 구현"""
        return True

class ComparableMixin:
    """비교 기능"""

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

# Mixin 조합한 클래스
class Product(TimestampMixin, ValidateMixin, ComparableMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.value = price  # ComparableMixin용

    def validate(self):
        if self.price < 0:
            return False
        return True

    def __str__(self):
        timestamp = self.get_timestamp()
        return f"{self.name} ({self.price:,}원) @ {timestamp}"

# 상품 생성
products = [
    Product("노트북", 1200000),
    Product("마우스", 30000),
    Product("키보드", 89000)
]

# 비교 (ComparableMixin)
print("가격 비교:")
print(f"노트북 > 마우스: {products[0] > products[1]}")

# 정렬
sorted_products = sorted(products)
print("\n가격순 정렬:")
for p in sorted_products:
    if p.validate():
        print(f"  {p}")

# 7. 실무 예제: 직원 시스템
print("\n[7] 실무 예제: 다양한 직원 유형")
print("-" * 70)

class FullTimeEmployee:
    """정규직"""

    def __init__(self):
        self.employment_type = "정규직"

    def get_benefits(self):
        return ["건강보험", "퇴직금", "유급휴가"]

class PartTimeEmployee:
    """비정규직"""

    def __init__(self):
        self.employment_type = "비정규직"

    def get_benefits(self):
        return ["건강보험"]

class Developer:
    """개발자"""

    def __init__(self):
        self.job = "개발자"

    def code(self):
        print(f"코딩 중...")

class Manager:
    """관리자"""

    def __init__(self):
        self.job = "관리자"

    def manage_team(self):
        print(f"팀 관리 중...")

# 조합
class FullTimeDeveloper(FullTimeEmployee, Developer):
    """정규직 개발자"""

    def __init__(self, name):
        FullTimeEmployee.__init__(self)
        Developer.__init__(self)
        self.name = name

class PartTimeManager(PartTimeEmployee, Manager):
    """비정규직 관리자"""

    def __init__(self, name):
        PartTimeEmployee.__init__(self)
        Manager.__init__(self)
        self.name = name

# 직원 생성
dev = FullTimeDeveloper("김철수")
mgr = PartTimeManager("이영희")

print(f"{dev.name} ({dev.employment_type} {dev.job})")
print(f"  혜택: {', '.join(dev.get_benefits())}")
dev.code()

print()

print(f"{mgr.name} ({mgr.employment_type} {mgr.job})")
print(f"  혜택: {', '.join(mgr.get_benefits())}")
mgr.manage_team()

# 8. 다중 상속 vs 컴포지션
print("\n[8] 다중 상속 vs 컴포지션")
print("-" * 70)

# 다중 상속 방식
class Printer:
    def print_document(self, doc):
        print(f"🖨️  인쇄: {doc}")

class Scanner:
    def scan_document(self):
        print("📄 스캔 중...")

class MultiFunctionDevice1(Printer, Scanner):
    """다중 상속"""
    pass

# 컴포지션 방식 (권장)
class MultiFunctionDevice2:
    """컴포지션 (has-a 관계)"""

    def __init__(self):
        self.printer = Printer()
        self.scanner = Scanner()

    def print_document(self, doc):
        self.printer.print_document(doc)

    def scan_document(self):
        self.scanner.scan_document()

# 사용 (둘 다 동일하게 동작)
print("다중 상속 방식:")
mfd1 = MultiFunctionDevice1()
mfd1.print_document("report.pdf")
mfd1.scan_document()

print("\n컴포지션 방식:")
mfd2 = MultiFunctionDevice2()
mfd2.print_document("report.pdf")
mfd2.scan_document()

# 9. Mixin 실전 활용
print("\n[9] Mixin 실전 활용: API 응답 클래스")
print("-" * 70)

class DictConvertibleMixin:
    """딕셔너리 변환 Mixin"""

    def to_dict(self):
        return {
            key: value for key, value in self.__dict__.items()
            if not key.startswith('_')
        }

class ValidationMixin:
    """검증 Mixin"""

    def is_valid(self):
        return all(
            value is not None
            for value in self.__dict__.values()
        )

class APIResponse(DictConvertibleMixin, ValidationMixin):
    """API 응답 클래스"""

    def __init__(self, status, message, data=None):
        self.status = status
        self.message = message
        self.data = data

    def to_json(self):
        import json
        return json.dumps(self.to_dict(), ensure_ascii=False)

# API 응답 생성
response = APIResponse(200, "성공", {"user_id": 123, "username": "john"})

print(f"검증: {response.is_valid()}")
print(f"딕셔너리: {response.to_dict()}")
print(f"JSON: {response.to_json()}")

# 10. 다중 상속 주의사항
print("\n[10] 다중 상속 주의사항")
print("-" * 70)

# ❌ 나쁜 예: 복잡한 다중 상속
class A1:
    def method(self):
        print("A1")

class B1:
    def method(self):
        print("B1")

class C1(A1, B1):
    # 어느 method가 호출될지 혼란
    pass

# ✅ 좋은 예: Mixin은 작고 명확한 기능만
class ReadableMixin:
    def read(self):
        return self.content

class WritableMixin:
    def write(self, content):
        self.content = content

class File(ReadableMixin, WritableMixin):
    def __init__(self):
        self.content = ""

file = File()
file.write("Hello, World!")
print(f"파일 내용: {file.read()}")

print("\n" + "=" * 70)
print("핵심 정리".center(70))
print("=" * 70)

print("""
✅ 다중 상속:
  - 여러 부모 클래스로부터 상속
  - class Child(Parent1, Parent2, ...)
  - 기능 조합에 유용

✅ Mixin 패턴:
  - 작고 독립적인 기능을 제공하는 클래스
  - 주로 ~Mixin 이름으로 명명
  - 단일 목적만 수행

✅ MRO (Method Resolution Order):
  - 메서드 호출 순서 결정
  - C3 선형화 알고리즘 사용
  - ClassName.__mro__로 확인

⚠️  주의사항:
  1. Diamond Problem 조심
  2. MRO 이해 필수
  3. 복잡한 다중 상속 피하기 (2-3개 이하)
  4. Mixin은 단일 기능만!

💡 대안:
  - 컴포지션 (has-a 관계)
  - 인터페이스 패턴
  - ABC (Abstract Base Class)
""")

print("\n💡 Tip: 실무에서는 Mixin 패턴을 많이 사용합니다!")
