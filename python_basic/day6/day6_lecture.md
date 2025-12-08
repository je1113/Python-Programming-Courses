# Day 6: 모듈과 파일 처리

## 📋 강의 개요

**학습 목표:**
- 모듈을 활용한 코드 재사용
- 다양한 파일 형식 처리 (텍스트, CSV, JSON, Excel)
- 클래스를 통한 객체 지향 프로그래밍 기초
- 실무 데이터 자동화

**소요 시간:** 4시간 (240분)

**세션 구성:** 9개 세션 × 25분 (이론 10분 + 실습 10분 + 해설 5분)

---

## 💡 Day 6을 배워야 하는 이유

### 1. 파일 처리 - 업무 자동화의 핵심

**실무에서 파일 처리가 중요한 이유:**
- Python 개발자의 **85%**가 파일 처리 사용
- 업무 자동화 시나리오의 **90%**가 Excel/CSV 관련
- 수작업 몇 시간 → Python 몇 초로 단축

### 2. 모듈 - 거인의 어깨 위에 서기

**Python의 강력함:**
- 이미 검증된 코드 재사용
- 개발 시간 단축 (처음부터 만들 필요 없음)
- 50만개 이상의 패키지 활용 가능

### 3. 클래스 - 실세계를 코드로

**클래스가 필요한 이유:**
- 데이터와 동작을 하나로 묶음
- 여러 객체 관리 용이
- 코드 재사용성 및 유지보수성 향상

---

## 세션 1: 모듈 import (25분)
**중요도:** ★★★★★

### 📖 이론 (10분)

#### 1.1 모듈이란?

📌 **모듈 (Module)**: 다른 Python 파일에서 작성한 코드를 가져와서 사용하는 것

**왜 필요한가?**
- 코드 재사용 (DRY: Don't Repeat Yourself)
- 코드 구조화 및 관리
- 팀 협업 용이

#### 1.2 모듈 활용 예시

**예시 1: 기본 import**
```python
# 전체 모듈 임포트
import math

result = math.sqrt(16)  # 4.0
print(math.pi)  # 3.141592...

# 특정 함수만 임포트
from math import sqrt, pi
result = sqrt(16)  # math. 없이 사용
print(pi)
```

**예시 2: 별칭 사용 (실무 패턴)**
```python
# 데이터 분석
import pandas as pd
import numpy as np

# 시각화
import matplotlib.pyplot as plt

# 웹 개발
from flask import Flask, request

# 날짜/시간
from datetime import datetime, timedelta
```

**예시 3: 내가 만든 모듈**
```python
# calculator.py 파일
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

PI = 3.14159

# main.py 파일에서 사용
import calculator

result = calculator.add(10, 5)  # 15
print(calculator.PI)  # 3.14159
```

#### 1.3 Java와 비교

```java
// Java - import
import java.util.ArrayList;
import java.time.LocalDateTime;

ArrayList<String> list = new ArrayList<>();
```

```python
# Python - 더 간결
from collections import defaultdict
from datetime import datetime

data = defaultdict(list)
now = datetime.now()
```

### 💻 실습 (10분)

**[실습 파일: session1_module_import_practice.py](./session1_module_import_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session1_module_import_solution.py](./session1_module_import_solution.py)**

**핵심 포인트:**
1. `import 모듈명` - 전체 임포트
2. `from 모듈 import 항목` - 특정 항목만
3. `as` - 별칭 사용
4. 파일 상단에 모든 import 모아서 작성

---

## 세션 2: 표준 라이브러리 (25분)
**중요도:** ★★★★★

### 📖 이론 (10분)

#### 2.1 표준 라이브러리 활용

Python 설치 시 기본 제공되는 강력한 모듈들을 활용하여 다양한 작업을 수행할 수 있습니다.

**예시 1: random - 난수 생성**
```python
import random

# 난수 생성
print(random.randint(1, 10))  # 1~10 사이 정수

# 리스트에서 랜덤 선택
colors = ["red", "blue", "green"]
print(random.choice(colors))

# 비밀번호 생성
import string
chars = string.ascii_letters + string.digits
password = ''.join(random.choice(chars) for _ in range(12))
print(password)  # "aB3kL9mP2xQ1"
```

**예시 2: datetime - 날짜/시간 처리**
```python
from datetime import datetime, timedelta, date

# 현재 날짜/시간
now = datetime.now()
print(now)  # 2024-01-15 14:30:45

# 날짜 연산
tomorrow = date.today() + timedelta(days=1)
next_week = date.today() + timedelta(weeks=1)

# D-Day 계산
target = date(2024, 12, 31)
d_day = (target - date.today()).days
print(f"D-{d_day}")

# 포맷팅
formatted = now.strftime("%Y년 %m월 %d일 %H:%M:%S")
print(formatted)  # "2024년 01월 15일 14:30:45"
```

**예시 3: os, math - 파일/수학 처리**
```python
import os
import math

# 파일/디렉토리 관리
print(os.getcwd())  # 현재 작업 디렉토리
print(os.listdir("."))  # 디렉토리 내용
path = os.path.join("folder", "file.txt")  # 경로 결합

# 수학 계산
print(math.sqrt(16))      # 4.0 (제곱근)
print(math.ceil(3.14))    # 4 (올림)
print(math.floor(3.14))   # 3 (내림)
print(math.pi)            # 3.141592...
```

### 💻 실습 (10분)

**[실습 파일: session2_stdlib_practice.py](./session2_stdlib_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session2_stdlib_solution.py](./session2_stdlib_solution.py)**

**핵심 포인트:**
1. `random` - 난수, 샘플링, 셔플
2. `datetime` - 날짜/시간 생성, 연산, 포맷팅
3. `math` - 수학 함수, 상수
4. `os` - 파일/디렉토리 관리

---

## 세션 3: 외부 패키지 (pip) (25분)
**중요도:** ★★★★☆

### 📖 이론 (10분)

#### 3.1 pip로 패키지 관리

📌 **pip**: Python 외부 패키지를 설치/관리하는 도구
- PyPI (Python Package Index): 50만개 이상의 패키지

**예시 1: pip 기본 명령어**
```bash
# 패키지 설치
pip install requests

# 특정 버전 설치
pip install pandas==2.0.0

# 최신 버전으로 업그레이드
pip install --upgrade numpy

# 패키지 제거
pip uninstall matplotlib

# 설치된 패키지 목록
pip list

# requirements.txt로 한번에 설치
pip install -r requirements.txt
```

**예시 2: 가상 환경 사용**
```bash
# 가상 환경 생성
python -m venv myenv

# 활성화 (Windows)
myenv\Scripts\activate

# 활성화 (macOS/Linux)
source myenv/bin/activate

# 비활성화
deactivate

# 현재 환경의 패키지 목록 저장
pip freeze > requirements.txt
```

**예시 3: 외부 패키지 활용**
```python
# requests로 웹 API 호출
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # 200
print(response.json())

# pandas로 데이터 처리
import pandas as pd

data = {
    "name": ["김철수", "이영희"],
    "age": [25, 30]
}
df = pd.DataFrame(data)
print(df)
```

### 💻 실습 (10분)

**[실습 파일: session3_pip_packages_practice.py](./session3_pip_packages_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session3_pip_packages_solution.py](./session3_pip_packages_solution.py)**

**핵심 포인트:**
1. `pip install` - 패키지 설치
2. `requirements.txt` - 패키지 목록 관리
3. 가상 환경 - 프로젝트별 독립 환경
4. 프로젝트 시작 시 항상 가상 환경 생성

---

## 세션 4: 텍스트 파일 처리 (25분)
**중요도:** ★★★★★

### 📖 이론 (10분)

#### 4.1 파일 읽기/쓰기

**예시 1: 파일 읽기 (여러 방법)**
```python
# ✅ with문 사용 (권장!)
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()  # 전체 읽기
    print(content)

# 한 줄씩 읽기 (메모리 효율적)
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())  # 줄바꿈 제거

# 모든 줄을 리스트로
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
```

**예시 2: 파일 쓰기**
```python
# 새로 쓰기 (덮어쓰기)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.write("Python is awesome!")

# 여러 줄 쓰기
lines = ["첫 번째 줄\n", "두 번째 줄\n", "세 번째 줄\n"]
with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

# 추가 모드 (이어쓰기)
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("새 로그 추가\n")
```

**예시 3: 실무 활용 - 로그 파일 분석**
```python
import os

# 파일 존재 확인
if os.path.exists("app.log"):
    # 에러 로그만 추출
    with open("app.log", "r", encoding="utf-8") as f:
        error_lines = [line for line in f if "ERROR" in line]

    # 결과 저장
    with open("errors.txt", "w", encoding="utf-8") as f:
        f.writelines(error_lines)
else:
    print("파일이 없습니다!")
```

#### 4.2 Java와 비교

```java
// Java - 파일 읽기 (복잡)
BufferedReader reader = new BufferedReader(new FileReader("data.txt"));
String line;
while ((line = reader.readLine()) != null) {
    System.out.println(line);
}
reader.close();
```

```python
# Python - 훨씬 간결!
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

### 💻 실습 (10분)

**[실습 파일: session4_text_file_practice.py](./session4_text_file_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session4_text_file_solution.py](./session4_text_file_solution.py)**

**핵심 포인트:**
1. `with open()` - 자동 파일 닫기
2. `encoding="utf-8"` - 한글 깨짐 방지 (Windows 필수)
3. `strip()` - 줄바꿈 제거
4. 모드: `r` (읽기), `w` (쓰기), `a` (추가)

---

## 세션 5: CSV 파일 처리 (25분)
**중요도:** ★★★★★

### 📖 이론 (10분)

#### 5.1 CSV 파일 다루기

📌 **CSV (Comma-Separated Values)**: 엑셀보다 가볍고 호환성이 좋은 표 형식 데이터

**예시 1: csv 모듈로 읽기/쓰기**
```python
import csv

# CSV 읽기 (딕셔너리로)
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        # {'이름': '김철수', '나이': '28', '부서': '개발'}
        print(row['이름'], row['나이'])

# CSV 쓰기
employees = [
    {"이름": "김철수", "나이": 28, "부서": "개발"},
    {"이름": "이영희", "나이": 32, "부서": "기획"}
]

with open("output.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["이름", "나이", "부서"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()  # 헤더 쓰기
    writer.writerows(employees)
```

**예시 2: pandas로 CSV 처리 (더 강력!)**
```python
import pandas as pd

# CSV 읽기 (pandas 사용 - 권장!)
df = pd.read_csv("data.csv", encoding="utf-8")
print(df)

# 특정 열만 선택
print(df["이름"])

# 조건 필터링
dev_team = df[df["부서"] == "개발"]
print(dev_team)

# 통계
print(df["나이"].mean())  # 평균
print(df["부서"].value_counts())  # 부서별 개수

# CSV 쓰기 (Excel 호환)
df.to_csv("output.csv", index=False, encoding="utf-8-sig")
```

**예시 3: 실무 활용 - 여러 CSV 합치기**
```python
import pandas as pd

# 여러 CSV 파일 합치기
files = ["sales_jan.csv", "sales_feb.csv", "sales_mar.csv"]
dfs = [pd.read_csv(f) for f in files]
combined = pd.concat(dfs)
combined.to_csv("sales_q1.csv", index=False, encoding="utf-8-sig")

# 데이터 정제
df = pd.read_csv("dirty_data.csv")
df = df.dropna()  # 빈 값 제거
df = df.drop_duplicates()  # 중복 제거
df.to_csv("clean_data.csv", index=False, encoding="utf-8-sig")
```

### 💻 실습 (10분)

**[실습 파일: session5_csv_file_practice.py](./session5_csv_file_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session5_csv_file_solution.py](./session5_csv_file_solution.py)**

**핵심 포인트:**
1. `csv.DictReader()` - 딕셔너리로 읽기 (편리)
2. `newline=""` - 빈 줄 방지 (Windows)
3. `pandas` - 더 강력한 CSV 처리
4. `encoding="utf-8-sig"` - Excel 호환

---

## 세션 6: JSON 파일 처리 (25분)
**중요도:** ★★★★★

### 📖 이론 (10분)

#### 6.1 JSON 파일 다루기

📌 **JSON**: 웹 API와 데이터 교환의 표준 포맷
- Python 딕셔너리와 구조가 같음
- 모든 프로그래밍 언어에서 지원

**예시 1: JSON 기본 사용**
```python
import json

# Python → JSON (직렬화)
data = {
    "name": "김철수",
    "age": 28,
    "skills": ["Python", "JavaScript"]
}

json_string = json.dumps(data, ensure_ascii=False, indent=2)
print(json_string)

# JSON → Python (역직렬화)
json_string = '{"name": "김철수", "age": 28}'
data = json.loads(json_string)
print(data["name"])  # "김철수"
```

**예시 2: JSON 파일 처리**
```python
import json

# JSON 파일 쓰기
data = {
    "employees": [
        {"name": "김철수", "age": 28, "department": "개발"},
        {"name": "이영희", "age": 32, "department": "기획"}
    ]
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# JSON 파일 읽기
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data["employees"][0]["name"])
```

**예시 3: API 응답 처리 및 설정 파일**
```python
import requests
import json

# API 호출 및 JSON 파싱
response = requests.get("https://api.github.com/users/python")
data = response.json()  # 자동으로 json.loads() 수행
print(data["name"])

# 파일로 저장
with open("github_user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 설정 파일 읽기
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
    db_host = config["database"]["host"]
    log_level = config["logging"]["level"]
```

### 💻 실습 (10분)

**[실습 파일: session6_json_file_practice.py](./session6_json_file_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session6_json_file_solution.py](./session6_json_file_solution.py)**

**핵심 포인트:**
1. `json.dumps()` - Python → JSON 문자열
2. `json.loads()` - JSON 문자열 → Python
3. `json.dump()` - Python → JSON 파일
4. `json.load()` - JSON 파일 → Python
5. `ensure_ascii=False` - 한글 그대로 저장

---

## 세션 7: Excel 파일 처리 (25분)
**중요도:** ★★★★★

### 📖 이론 (10분)

#### 7.1 Excel 자동화

**업무 자동화의 핵심!**
- 대부분의 회사가 Excel 사용
- 수작업 → 자동화로 시간 절약
- 데이터 분석 및 리포트 생성

**예시 1: pandas로 Excel 읽기/쓰기**
```python
import pandas as pd

# Excel 읽기
df = pd.read_excel("sales.xlsx")
print(df)

# 특정 시트 읽기
df = pd.read_excel("sales.xlsx", sheet_name="2024년")

# 여러 시트 읽기
dfs = pd.read_excel("sales.xlsx", sheet_name=None)
for sheet_name, df in dfs.items():
    print(f"{sheet_name}: {len(df)}행")

# Excel로 저장
data = {
    "이름": ["김철수", "이영희", "박민수"],
    "나이": [28, 32, 25],
    "부서": ["개발", "기획", "마케팅"]
}
df = pd.DataFrame(data)
df.to_excel("output.xlsx", index=False)
```

**예시 2: 여러 시트로 저장**
```python
import pandas as pd

# 여러 시트로 저장
df1 = pd.DataFrame({"이름": ["김철수", "이영희"], "부서": ["개발", "기획"]})
df2 = pd.DataFrame({"부서": ["개발", "기획"], "인원": [10, 5]})

with pd.ExcelWriter("multi_sheet.xlsx") as writer:
    df1.to_excel(writer, sheet_name="직원", index=False)
    df2.to_excel(writer, sheet_name="부서", index=False)
```

**예시 3: openpyxl로 세밀한 제어 (스타일 적용)**
```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

# 새 워크북 생성
wb = Workbook()
ws = wb.active
ws.title = "직원명단"

# 헤더 작성
ws["A1"] = "이름"
ws["B1"] = "나이"
ws["C1"] = "부서"

# 스타일 적용
header_font = Font(bold=True, color="FFFFFF")
header_fill = PatternFill(start_color="0066CC", fill_type="solid")

for cell in ws[1]:
    cell.font = header_font
    cell.fill = header_fill

# 데이터 추가
ws.append(["김철수", 28, "개발"])
ws.append(["이영희", 32, "기획"])

# 저장
wb.save("employees.xlsx")
```

### 💻 실습 (10분)

**[실습 파일: session7_excel_file_practice.py](./session7_excel_file_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session7_excel_file_solution.py](./session7_excel_file_solution.py)**

**핵심 포인트:**
1. `pd.read_excel()` - 읽기
2. `df.to_excel()` - 쓰기
3. `ExcelWriter` - 여러 시트
4. `openpyxl` - 세밀한 제어 (스타일)
5. `index=False` - 인덱스 열 제거

---

## 세션 8: 클래스 기초 (25분)
**중요도:** ★★★★★

### 📖 이론 (10분)

#### 8.1 클래스로 체계적인 코드 작성

📌 **클래스**: 데이터와 기능을 하나로 묶은 설계도

**예시 1: 클래스 기본 구조**
```python
class Person:
    # 생성자 (초기화 메서드)
    def __init__(self, name, age):
        self.name = name  # 속성
        self.age = age

    # 메서드
    def introduce(self):
        print(f"안녕하세요, {self.name}입니다. {self.age}세입니다.")

# 객체 생성
person1 = Person("김철수", 28)
person2 = Person("이영희", 32)

# 메서드 호출
person1.introduce()  # "안녕하세요, 김철수입니다. 28세입니다."

# 속성 접근
print(person1.name)  # "김철수"
print(person1.age)   # 28
```

**예시 2: 실무 예제 - 직원 클래스**
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name}의 연봉이 {amount:,}원 인상되었습니다.")

    def get_info(self):
        return f"{self.name}: {self.salary:,}원"

# 사용
emp1 = Employee("김철수", 3500000)
emp1.give_raise(500000)
print(emp1.get_info())  # "김철수: 4,000,000원"
```

**예시 3: 상품 클래스 (재고 관리)**
```python
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        if quantity > self.stock:
            print("재고 부족!")
            return False

        self.stock -= quantity
        total = self.price * quantity
        print(f"{self.name} {quantity}개 판매: {total:,}원")
        return True

    def restock(self, quantity):
        self.stock += quantity
        print(f"{self.name} {quantity}개 입고 완료")

# 사용
product = Product("노트북", 1200000, 5)
product.sell(2)  # "노트북 2개 판매: 2,400,000원"
product.restock(10)  # "노트북 10개 입고 완료"
```

#### 8.2 Java와 비교

```java
// Java
public class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void introduce() {
        System.out.println("안녕하세요, " + name + "입니다.");
    }
}

Person person = new Person("김철수", 28);
```

```python
# Python - 더 간결
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"안녕하세요, {self.name}입니다.")

person = Person("김철수", 28)
```

### 💻 실습 (10분)

**[실습 파일: session8_class_basic_practice.py](./session8_class_basic_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session8_class_basic_solution.py](./session8_class_basic_solution.py)**

**핵심 포인트:**
1. `class` - 클래스 정의
2. `__init__()` - 생성자 (초기화)
3. `self` - 객체 자신
4. 메서드 - 클래스 내부 함수
5. 클래스명은 UpperCamelCase

---

## 세션 9: 클래스 고급 (25분)
**중요도:** ★★★★☆

### 📖 이론 (10분)

#### 9.1 클래스 고급 기능

**예시 1: 클래스 변수 vs 인스턴스 변수**
```python
class Employee:
    # 클래스 변수 (모든 객체가 공유)
    company = "ABC 회사"
    employee_count = 0

    def __init__(self, name):
        # 인스턴스 변수 (각 객체마다 별도)
        self.name = name
        Employee.employee_count += 1

emp1 = Employee("김철수")
emp2 = Employee("이영희")

print(Employee.company)  # "ABC 회사"
print(Employee.employee_count)  # 2

print(emp1.name)  # "김철수" (개별)
print(emp2.name)  # "이영희" (개별)
```

**예시 2: 특수 메서드 (Magic Methods)**
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        """print()할 때 출력되는 문자열"""
        return f"{self.name}: {self.price:,}원"

    def __lt__(self, other):
        """< 연산자"""
        return self.price < other.price

    def __add__(self, other):
        """+ 연산자"""
        return self.price + other.price

p1 = Product("노트북", 1200000)
p2 = Product("마우스", 30000)

print(p1)  # "노트북: 1,200,000원" (__str__)
print(p1 < p2)  # False (__lt__)
print(p1 + p2)  # 1230000 (__add__)
```

**예시 3: Property와 상속**
```python
# Property - Getter/Setter
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("절대영도보다 낮을 수 없습니다!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

temp = Temperature(25)
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0

# 상속
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name}: 멍멍!"

dog = Dog("바둑이")
print(dog.speak())  # "바둑이: 멍멍!"
```

### 💻 실습 (10분)

**[실습 파일: session9_class_advanced_practice.py](./session9_class_advanced_practice.py)**

### ✅ 해설 (5분)

**[해설 파일: session9_class_advanced_solution.py](./session9_class_advanced_solution.py)**

**핵심 포인트:**
1. 인스턴스 변수 vs 클래스 변수
2. `@property` - Getter/Setter
3. 특수 메서드 - `__str__`, `__lt__` 등
4. 상속 - 코드 재사용

---

## 🎯 Day 6 마무리

### 학습 내용 요약

| 세션 | 주제 | 중요도 | 핵심 키워드 |
|-----|------|--------|-----------|
| 1 | 모듈 import | ★★★★★ | import, from...import, as |
| 2 | 표준 라이브러리 | ★★★★★ | random, datetime, math, os |
| 3 | 외부 패키지 (pip) | ★★★★☆ | pip install, 가상환경 |
| 4 | 텍스트 파일 | ★★★★★ | open(), with, encoding |
| 5 | CSV 파일 | ★★★★★ | csv, pandas, DictReader |
| 6 | JSON 파일 | ★★★★★ | json.dump(), json.load() |
| 7 | Excel 파일 | ★★★★★ | pandas, openpyxl |
| 8 | 클래스 기초 | ★★★★★ | class, __init__, self |
| 9 | 클래스 고급 | ★★★★☆ | property, 특수 메서드, 상속 |

### 실무 활용 포인트

**파일 처리가 중요한 이유:**
- 업무 자동화의 90%가 파일 처리
- Excel 자동화로 수십 시간 절약
- 데이터 분석의 시작점

**클래스를 사용하는 경우:**
- 관련 데이터와 기능을 묶을 때
- 같은 구조의 객체 여러 개 필요할 때
- 코드 재사용성 향상

### 다음 단계

- 데이터베이스 연동 (SQLite, MySQL)
- 웹 크롤링 (requests, BeautifulSoup)
- 웹 개발 (Flask, Django)
- 데이터 분석 (Pandas 심화)
- 자동화 스크립트 작성

### 추가 학습 자료

**공식 문서:**
- Python 표준 라이브러리: https://docs.python.org/ko/3/library/
- Pandas: https://pandas.pydata.org
- openpyxl: https://openpyxl.readthedocs.io

**실습 프로젝트:**
1. 엑셀 자동 리포트 생성기
2. CSV 데이터 분석 대시보드
3. 파일 백업 자동화
4. 도서 관리 시스템

---

**수고하셨습니다!**

오늘 배운 파일 처리와 클래스는 실무에서 가장 많이 사용하는 기능입니다.
특히 Excel 자동화는 업무 효율을 크게 향상시킬 수 있으니, 실습 파일을 반복해서 연습하세요!
