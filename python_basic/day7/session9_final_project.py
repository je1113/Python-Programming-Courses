"""
파일명: session9_final_project.py
목적: 종합 프로젝트 - 도서관 관리 시스템

프로젝트 목표:
- 클래스 심화 내용 종합 활용
- 상속, 캡슐화, 다형성 구현
- 특수 메서드, 프로퍼티 활용
- 실무 수준의 프로그램 작성
"""

print("=" * 70)
print("종합 프로젝트: 도서관 관리 시스템".center(70))
print("=" * 70)

# 1. Book 기본 클래스
print("\n[1] Book 기본 클래스")
print("-" * 70)

class Book:
    """도서 기본 클래스"""

    # 클래스 변수
    total_books = 0

    def __init__(self, title, author, isbn, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._price = price
        self.__is_borrowed = False  # private
        self.__borrower = None
        Book.total_books += 1

    # 프로퍼티: 가격
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("가격은 0 이상이어야 합니다!")
        self._price = value

    # 프로퍼티: 대출 가능 여부
    @property
    def is_available(self):
        return not self.__is_borrowed

    # 프로퍼티: 대출자
    @property
    def borrower(self):
        return self.__borrower

    # 대출
    def borrow(self, borrower_name):
        """도서 대출"""
        if self.__is_borrowed:
            return False

        self.__is_borrowed = True
        self.__borrower = borrower_name
        return True

    # 반납
    def return_book(self):
        """도서 반납"""
        if not self.__is_borrowed:
            return False

        self.__is_borrowed = False
        self.__borrower = None
        return True

    # 정보 출력
    def get_info(self):
        """도서 정보"""
        status = "대출 가능" if self.is_available else f"대출 중 ({self.__borrower})"
        return f"{self.title} - {self.author} ({status})"

    # 특수 메서드
    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}', {self._price})"

    def __lt__(self, other):
        """가격 비교"""
        return self._price < other._price

    def __eq__(self, other):
        """ISBN 비교"""
        return self.isbn == other.isbn

# 기본 도서 테스트
print("기본 도서 생성:")
book1 = Book("파이썬 프로그래밍", "홍길동", "978-1234567890", 30000)
book2 = Book("자바 완벽 가이드", "김영희", "978-0987654321", 35000)

print(f"1. {book1.get_info()}")
print(f"2. {book2.get_info()}")

# 대출
print("\n대출 테스트:")
if book1.borrow("김철수"):
    print(f"✓ '{book1.title}' 대출 성공")
else:
    print(f"✗ '{book1.title}' 대출 실패")

print(f"1. {book1.get_info()}")

# 2. EBook, AudioBook 클래스 (상속)
print("\n[2] EBook, AudioBook 클래스")
print("-" * 70)

class EBook(Book):
    """전자책"""

    def __init__(self, title, author, isbn, price, file_size, format):
        super().__init__(title, author, isbn, price)
        self.file_size = file_size  # MB
        self.format = format  # PDF, EPUB 등

    def get_info(self):
        base_info = super().get_info()
        return f"[전자책] {base_info} | {self.file_size}MB ({self.format})"

    def download(self):
        """다운로드"""
        if not self.is_available:
            return f"✗ '{self.title}'은(는) 대출 중입니다"
        return f"✓ '{self.title}' 다운로드 완료 ({self.file_size}MB)"

    def __str__(self):
        return f"[E-Book] {self.title} by {self.author}"

class AudioBook(Book):
    """오디오북"""

    def __init__(self, title, author, isbn, price, duration, narrator):
        super().__init__(title, author, isbn, price)
        self.duration = duration  # 분
        self.narrator = narrator  # 내레이터

    def get_info(self):
        base_info = super().get_info()
        return f"[오디오북] {base_info} | {self.duration}분 (낭독: {self.narrator})"

    def play(self):
        """재생"""
        if not self.is_available:
            return f"✗ '{self.title}'은(는) 대출 중입니다"
        return f"♪ '{self.title}' 재생 중 (낭독: {self.narrator})"

    def __str__(self):
        return f"[Audio] {self.title} by {self.author}"

# 다양한 도서 생성
print("다양한 도서 타입:")
ebook = EBook("클린 코드", "로버트 마틴", "978-1111111111", 25000, 5.2, "PDF")
audiobook = AudioBook("해리 포터", "J.K. 롤링", "978-2222222222", 20000, 720, "김영희")

print(f"1. {ebook.get_info()}")
print(f"2. {audiobook.get_info()}")

print(f"\n{ebook.download()}")
print(f"{audiobook.play()}")

# 3. Library 클래스
print("\n[3] Library 클래스")
print("-" * 70)

class Library:
    """도서관 관리 클래스"""

    def __init__(self, name):
        self.name = name
        self.__books = []  # private

    # 도서 추가
    def add_book(self, book):
        """도서 추가"""
        # 중복 확인 (ISBN)
        if any(b.isbn == book.isbn for b in self.__books):
            return False

        self.__books.append(book)
        return True

    # 도서 삭제
    def remove_book(self, isbn):
        """도서 삭제"""
        for book in self.__books:
            if book.isbn == isbn:
                self.__books.remove(book)
                return True
        return False

    # 제목으로 검색
    def search_by_title(self, keyword):
        """제목으로 검색"""
        return [book for book in self.__books if keyword.lower() in book.title.lower()]

    # 저자로 검색
    def search_by_author(self, author):
        """저자로 검색"""
        return [book for book in self.__books if author.lower() in book.author.lower()]

    # 대출 가능한 도서
    @property
    def available_books(self):
        """대출 가능한 도서 목록"""
        return [book for book in self.__books if book.is_available]

    # 대출 중인 도서
    @property
    def borrowed_books(self):
        """대출 중인 도서 목록"""
        return [book for book in self.__books if not book.is_available]

    # 총 도서 수
    @property
    def total_books(self):
        """총 도서 수"""
        return len(self.__books)

    # 도서 대출
    def borrow_book(self, isbn, borrower_name):
        """도서 대출"""
        for book in self.__books:
            if book.isbn == isbn:
                if book.borrow(borrower_name):
                    print(f"✓ '{book.title}' 대출 완료 (대출자: {borrower_name})")
                    return True
                else:
                    print(f"✗ '{book.title}'은(는) 이미 대출 중입니다")
                    return False

        print(f"✗ ISBN {isbn}에 해당하는 도서를 찾을 수 없습니다")
        return False

    # 도서 반납
    def return_book(self, isbn):
        """도서 반납"""
        for book in self.__books:
            if book.isbn == isbn:
                if book.return_book():
                    print(f"✓ '{book.title}' 반납 완료")
                    return True
                else:
                    print(f"✗ '{book.title}'은(는) 대출 중이 아닙니다")
                    return False

        print(f"✗ ISBN {isbn}에 해당하는 도서를 찾을 수 없습니다")
        return False

    # 전체 도서 목록
    def show_all_books(self):
        """전체 도서 목록"""
        print(f"\n{'='*70}")
        print(f"{self.name} 도서 목록 ({self.total_books}권)".center(70))
        print(f"{'='*70}")

        if not self.__books:
            print("도서가 없습니다.")
            return

        for i, book in enumerate(self.__books, 1):
            print(f"{i}. {book.get_info()}")

    # 통계
    def show_statistics(self):
        """도서관 통계"""
        print(f"\n{'='*70}")
        print(f"{self.name} 통계".center(70))
        print(f"{'='*70}")

        print(f"총 도서 수: {self.total_books}권")
        print(f"대출 가능: {len(self.available_books)}권")
        print(f"대출 중: {len(self.borrowed_books)}권")

        # 도서 타입별 통계
        regular_count = sum(1 for b in self.__books if type(b) == Book)
        ebook_count = sum(1 for b in self.__books if isinstance(b, EBook))
        audiobook_count = sum(1 for b in self.__books if isinstance(b, AudioBook))

        print(f"\n도서 타입별:")
        print(f"  일반 도서: {regular_count}권")
        print(f"  전자책: {ebook_count}권")
        print(f"  오디오북: {audiobook_count}권")

    # 특수 메서드
    def __len__(self):
        """len(library)"""
        return self.total_books

    def __getitem__(self, index):
        """library[index]"""
        return self.__books[index]

    def __iter__(self):
        """for book in library"""
        return iter(self.__books)

    def __contains__(self, isbn):
        """isbn in library"""
        return any(book.isbn == isbn for book in self.__books)

# 도서관 생성 및 운영
print("도서관 생성:")
library = Library("Python 시립 도서관")

# 4. 도서 추가
print("\n[4] 도서 추가")
print("-" * 70)

# 다양한 도서 추가
books_to_add = [
    Book("파이썬 프로그래밍", "홍길동", "978-1111111111", 30000),
    Book("자바 완벽 가이드", "김영희", "978-2222222222", 35000),
    EBook("클린 코드", "로버트 마틴", "978-3333333333", 25000, 5.2, "PDF"),
    EBook("리팩토링", "마틴 파울러", "978-4444444444", 28000, 6.1, "EPUB"),
    AudioBook("해리 포터", "J.K. 롤링", "978-5555555555", 20000, 720, "김영희"),
    AudioBook("반지의 제왕", "톨킨", "978-6666666666", 25000, 960, "박민수"),
    Book("알고리즘 입문", "이철수", "978-7777777777", 32000),
]

for book in books_to_add:
    if library.add_book(book):
        print(f"✓ '{book.title}' 추가 완료")
    else:
        print(f"✗ '{book.title}' 추가 실패 (중복)")

# 5. 도서 목록 및 검색
print("\n[5] 도서 목록 및 검색")
print("-" * 70)

library.show_all_books()

# 제목으로 검색
print("\n제목 검색 ('파이썬'):")
results = library.search_by_title("파이썬")
for book in results:
    print(f"  - {book.get_info()}")

# 저자로 검색
print("\n저자 검색 ('김영희'):")
results = library.search_by_author("김영희")
for book in results:
    print(f"  - {book.get_info()}")

# 6. 대출 및 반납
print("\n[6] 대출 및 반납")
print("-" * 70)

# 대출
print("대출:")
library.borrow_book("978-1111111111", "김철수")
library.borrow_book("978-3333333333", "이영희")
library.borrow_book("978-5555555555", "박민수")

# 중복 대출 시도
print("\n중복 대출 시도:")
library.borrow_book("978-1111111111", "정지훈")

# 반납
print("\n반납:")
library.return_book("978-1111111111")

# 현재 상태
print()
library.show_all_books()

# 7. 통계
print("\n[7] 통계")
print("-" * 70)

library.show_statistics()

# 8. 고급 기능 테스트
print("\n[8] 고급 기능 테스트")
print("-" * 70)

# len() 사용
print(f"len(library): {len(library)}권")

# in 연산자
isbn_to_check = "978-1111111111"
print(f"'{isbn_to_check}' in library: {isbn_to_check in library}")

# 인덱싱
print(f"library[0]: {library[0]}")

# 반복
print("\n대출 가능한 도서:")
for book in library.available_books:
    print(f"  - {book}")

# 정렬 (가격순)
print("\n가격순 정렬:")
sorted_books = sorted(library, key=lambda b: b.price)
for book in sorted_books[:5]:
    print(f"  - {book} ({book.price:,}원)")

# 9. Member 클래스 (추가 기능)
print("\n[9] Member 클래스 (회원 관리)")
print("-" * 70)

class Member:
    """도서관 회원"""

    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.__borrowed_books = []  # private

    @property
    def borrowed_books(self):
        """대출 도서 목록"""
        return self.__borrowed_books.copy()

    @property
    def borrowed_count(self):
        """대출 도서 수"""
        return len(self.__borrowed_books)

    def borrow(self, book):
        """도서 대출"""
        if book in self.__borrowed_books:
            return False

        if book.borrow(self.name):
            self.__borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        """도서 반납"""
        if book not in self.__borrowed_books:
            return False

        if book.return_book():
            self.__borrowed_books.remove(book)
            return True
        return False

    def __str__(self):
        return f"{self.name} ({self.member_id}) - {self.borrowed_count}권 대출 중"

    def __repr__(self):
        return f"Member('{self.member_id}', '{self.name}', '{self.email}')"

# 회원 생성 및 대출
member1 = Member("M001", "김철수", "kim@example.com")
member2 = Member("M002", "이영희", "lee@example.com")

print("회원 정보:")
print(f"1. {member1}")
print(f"2. {member2}")

# 10. 최종 정리
print("\n[10] 최종 정리")
print("-" * 70)

print("""
✅ 이 프로젝트에서 사용한 OOP 개념:

1. 클래스와 객체
   - Book, EBook, AudioBook, Library, Member 클래스

2. 상속
   - Book → EBook, AudioBook

3. 캡슐화
   - private 변수 (__books, __is_borrowed)
   - Getter/Setter를 통한 접근 제어

4. 다형성
   - get_info() 메서드 오버라이딩
   - 다양한 Book 타입을 동일하게 처리

5. 프로퍼티
   - @property (is_available, total_books 등)
   - 계산된 속성

6. 특수 메서드
   - __str__, __repr__: 문자열 표현
   - __lt__, __eq__: 비교
   - __len__, __getitem__, __iter__, __contains__: 컨테이너

7. 클래스 변수
   - Book.total_books

8. 메서드 오버라이딩
   - get_info() 각 클래스에서 확장

9. super() 사용
   - 부모 클래스 초기화 및 메서드 호출
""")

print("\n" + "=" * 70)
print("축하합니다! 도서관 관리 시스템 구현 완료!".center(70))
print("=" * 70)

print("""
💡 다음 단계:
1. 데이터베이스 연동 (SQLite, MySQL)
2. GUI 추가 (Tkinter, PyQt)
3. 웹 API 구축 (Flask, FastAPI)
4. 테스트 코드 작성 (unittest, pytest)
5. 로깅 및 예외 처리 강화

🎓 학습한 내용:
- 객체지향 설계 원칙 (SOLID)
- 상속 vs 컴포지션
- 인터페이스 설계
- 캡슐화와 정보 은닉
- 다형성 활용

Happy Coding! 🐍✨
""")

# 최종 도서관 상태
print("최종 도서관 상태:")
library.show_all_books()
print()
library.show_statistics()
