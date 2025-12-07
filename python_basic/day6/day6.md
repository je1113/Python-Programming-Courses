# Day 6: 모듈과 파일 처리 - 실무 데이터 다루기

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

```python
# 수작업으로 하면 몇 시간 걸리는 작업을 몇 초로!

# ❌ 수작업
# 1. 엑셀 파일 100개를 하나씩 열기
# 2. 특정 데이터 복사
# 3. 새 파일에 붙여넣기
# 4. 계산 수식 입력
# 5. 저장
# → 반복... (몇 시간 소요)

# ✅ Python 자동화 (몇 초!)
import pandas as pd

files = ["data1.xlsx", "data2.xlsx", "data3.xlsx"]
combined_data = []

for file in files:
    df = pd.read_excel(file)
    combined_data.append(df)

result = pd.concat(combined_data)
result.to_excel("merged.xlsx")
```

**실무 활용 통계:**
- Python 개발자의 **85%**가 파일 처리 사용
- 업무 자동화 시나리오의 **90%**가 Excel/CSV 관련
- 데이터 분석가가 가장 많이 사용하는 기능 **1위**: 파일 읽기/쓰기

### 2. 모듈 - 거인의 어깨 위에 서기

**왜 모듈을 사용하는가?**
- 이미 검증된 코드 재사용
- 개발 시간 단축 (처음부터 만들 필요 없음)
- 표준화된 방식으로 문제 해결

**Python의 강력함:**
```python
# 단 3줄로 웹 크롤링
import requests
response = requests.get("https://example.com")
print(response.text)

# 단 4줄로 데이터 분석
import pandas as pd
df = pd.read_excel("sales.xlsx")
print(df.describe())  # 통계 요약 자동 생성!
```

### 3. 클래스 - 실세계를 코드로

**클래스가 필요한 이유:**
```python
# ❌ 함수만 사용 (데이터와 동작이 분리됨)
account_balance = 100000
account_owner = "김철수"

def deposit(amount):
    global account_balance
    account_balance += amount

def withdraw(amount):
    global account_balance
    account_balance -= amount

# ✅ 클래스 사용 (데이터와 동작을 하나로)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

# 여러 계좌 관리 가능!
account1 = BankAccount("김철수", 100000)
account2 = BankAccount("이영희", 200000)

account1.deposit(50000)  # 김철수 계좌에만 영향
```

---

## 세션 1: 모듈 import (25분)
**중요도:** ★★★★★

### 📚 이론 (10분)

#### 1.1 모듈이란?

📌 **모듈 (Module)**

**다른 Python 파일에서 작성한 코드를 가져와서 사용**하는 것입니다.

**왜 필요한가?**
- 코드 재사용 (DRY: Don't Repeat Yourself)
- 코드 구조화 및 관리
- 팀 협업 용이

#### 1.2 import 방법

```python
# 1. 전체 모듈 임포트
import math

result = math.sqrt(16)  # 4.0
print(math.pi)  # 3.141592...

# 2. 특정 함수만 임포트
from math import sqrt, pi

result = sqrt(16)  # math. 없이 사용 가능
print(pi)

# 3. 별칭(alias) 사용
import math as m

result = m.sqrt(16)

# 4. 모든 것 임포트 (권장하지 않음!)
from math import *  # ⚠️ 이름 충돌 가능성

# 5. 여러 모듈 임포트
import math, random, datetime
```

#### 1.3 자주 사용하는 import 패턴

```python
# 데이터 분석
import pandas as pd
import numpy as np

# 시각화
import matplotlib.pyplot as plt

# 웹 개발
from flask import Flask, request, render_template

# 날짜/시간
from datetime import datetime, timedelta

# 파일 처리
import os
import json
import csv
```

#### 1.4 내가 만든 모듈 사용하기

**calculator.py 파일:**
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

PI = 3.14159
```

**main.py 파일:**
```python
import calculator

result = calculator.add(10, 5)
print(result)  # 15

print(calculator.PI)  # 3.14159
```

#### 1.5 모듈 경로

```python
# Python이 모듈을 찾는 위치
import sys
print(sys.path)  # 모듈 검색 경로 목록

# 현재 디렉토리의 모듈
import my_module  # ./my_module.py

# 하위 폴더의 모듈
from utils import helper  # ./utils/helper.py
```

#### 1.6 Java와 비교

```java
// Java - import
import java.util.ArrayList;
import java.util.HashMap;
import java.time.LocalDateTime;

ArrayList<String> list = new ArrayList<>();
HashMap<String, Integer> map = new HashMap<>();
```

```python
# Python - import (더 간결)
from collections import defaultdict
from datetime import datetime

data = defaultdict(list)
now = datetime.now()
```

💡 **Tip:** Python의 `import`는 Java의 `import`와 유사하지만, **실제로 코드를 실행**합니다.

### 🔨 실습 (10분)

[실습 파일: module_import.py](./module_import.py)

**과제:** 표준 라이브러리 모듈 활용하기

다양한 표준 라이브러리 모듈을 import하여 활용하는 프로그램을 작성하세요.

**요구사항:**
1. math 모듈로 수학 계산
2. random 모듈로 난수 생성
3. datetime 모듈로 날짜/시간 처리
4. os 모듈로 파일/디렉토리 정보
5. sys 모듈로 시스템 정보

### 💬 해설 (5분)

**핵심 포인트:**
1. `import 모듈명` - 전체 임포트
2. `from 모듈 import 항목` - 특정 항목만
3. `as` - 별칭 사용
4. 모듈명.함수명() 형식으로 사용

**자주 하는 실수:**
```python
# ❌ 임포트 후 모듈명 생략
import math
print(sqrt(16))  # NameError!

# ✅ 모듈명 포함
import math
print(math.sqrt(16))

# 또는
from math import sqrt
print(sqrt(16))
```

**실무 팁:**
- 파일 상단에 모든 import 모아서 작성
- 표준 라이브러리 → 외부 패키지 → 내 모듈 순서
- 별칭은 관례 따르기 (pandas → pd, numpy → np)

---

## 세션 2: 표준 라이브러리 (25분)
**중요도:** ★★★★★

### 📚 이론 (10분)

#### 2.1 random 모듈

```python
import random

# 난수 생성
print(random.random())  # 0.0 ~ 1.0 사이 실수

# 정수 난수
print(random.randint(1, 10))  # 1 ~ 10 사이 정수

# 리스트에서 랜덤 선택
colors = ["red", "blue", "green"]
print(random.choice(colors))

# 여러 개 선택
print(random.sample(colors, 2))

# 리스트 섞기
random.shuffle(colors)
print(colors)
```

**실무 활용:**
```python
# 비밀번호 생성
import random
import string

chars = string.ascii_letters + string.digits
password = ''.join(random.choice(chars) for _ in range(12))
print(password)  # "aB3kL9mP2xQ1"

# 테스트 데이터 생성
test_scores = [random.randint(60, 100) for _ in range(30)]
```

#### 2.2 datetime 모듈

```python
from datetime import datetime, timedelta, date, time

# 현재 날짜/시간
now = datetime.now()
print(now)  # 2024-01-15 14:30:45.123456

# 날짜만
today = date.today()
print(today)  # 2024-01-15

# 시간만
current_time = time(14, 30, 45)
print(current_time)  # 14:30:45

# 날짜/시간 생성
dt = datetime(2024, 1, 15, 14, 30)

# 포맷팅
formatted = now.strftime("%Y년 %m월 %d일 %H:%M:%S")
print(formatted)  # "2024년 01월 15일 14:30:45"

# 파싱
date_str = "2024-01-15"
parsed = datetime.strptime(date_str, "%Y-%m-%d")

# 날짜 연산
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
three_hours_later = now + timedelta(hours=3)
```

**실무 활용:**
```python
# D-Day 계산
from datetime import datetime, date

target = date(2024, 12, 31)
today = date.today()
d_day = (target - today).days
print(f"D-{d_day}")

# 근무 시간 계산
start = datetime(2024, 1, 15, 9, 0)
end = datetime(2024, 1, 15, 18, 0)
work_hours = (end - start).seconds / 3600
print(f"{work_hours}시간")
```

#### 2.3 math 모듈

```python
import math

# 기본 함수
print(math.sqrt(16))      # 4.0 (제곱근)
print(math.pow(2, 3))     # 8.0 (거듭제곱)
print(math.ceil(3.14))    # 4 (올림)
print(math.floor(3.14))   # 3 (내림)

# 상수
print(math.pi)            # 3.141592...
print(math.e)             # 2.718281...

# 삼각함수
print(math.sin(math.pi/2))  # 1.0
print(math.cos(0))          # 1.0

# 로그
print(math.log(10))       # 자연로그
print(math.log10(100))    # 2.0 (상용로그)
```

#### 2.4 os 모듈

```python
import os

# 현재 작업 디렉토리
print(os.getcwd())

# 디렉토리 변경
os.chdir("/path/to/directory")

# 디렉토리 내용 확인
print(os.listdir("."))

# 경로 존재 확인
print(os.path.exists("file.txt"))

# 경로 결합
path = os.path.join("folder", "subfolder", "file.txt")

# 파일/디렉토리 구분
print(os.path.isfile("test.txt"))
print(os.path.isdir("folder"))

# 디렉토리 생성
os.makedirs("new_folder", exist_ok=True)

# 파일 삭제
os.remove("file.txt")

# 환경 변수
print(os.environ.get("PATH"))
```

#### 2.5 sys 모듈

```python
import sys

# Python 버전
print(sys.version)

# 플랫폼 정보
print(sys.platform)  # 'win32', 'linux', 'darwin' (macOS)

# 명령행 인자
print(sys.argv)  # ['script.py', 'arg1', 'arg2']

# 프로그램 종료
sys.exit(0)

# 모듈 경로
print(sys.path)
```

### 🔨 실습 (10분)

[실습 파일: stdlib_practice.py](./stdlib_practice.py)

**과제:** 표준 라이브러리 활용 프로그램

**요구사항:**
1. 로또 번호 생성기 (random)
2. 디데이 계산기 (datetime)
3. 원의 넓이/둘레 계산 (math)
4. 파일 목록 조회 (os)
5. 시스템 정보 출력 (sys)

### 💬 해설 (5분)

**핵심 포인트:**
1. `random` - 난수, 샘플링, 셔플
2. `datetime` - 날짜/시간 생성, 연산, 포맷팅
3. `math` - 수학 함수, 상수
4. `os` - 파일/디렉토리 관리
5. `sys` - 시스템 정보

**자주 하는 실수:**
```python
# ❌ datetime 객체와 문자열 혼동
from datetime import datetime

now = datetime.now()
print(now + "1")  # TypeError!

# ✅ timedelta 사용
from datetime import timedelta
tomorrow = now + timedelta(days=1)
```

**실무 팁:**
- `random.seed()` - 재현 가능한 난수
- `datetime.strftime()` - 날짜 → 문자열
- `datetime.strptime()` - 문자열 → 날짜
- `os.path.join()` - OS 독립적인 경로

---

## 세션 3: 외부 패키지 설치 (pip) (25분)
**중요도:** ★★★★☆

### 📚 이론 (10분)

#### 3.1 pip란?

📌 **pip (Package Installer for Python)**

Python 외부 패키지를 **설치/관리**하는 도구입니다.

**PyPI (Python Package Index):**
- 전 세계 개발자가 공유하는 패키지 저장소
- 50만개 이상의 패키지
- https://pypi.org

#### 3.2 pip 기본 명령어

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

# 패키지 정보 확인
pip show pandas

# requirements.txt로 한번에 설치
pip install -r requirements.txt
```

#### 3.3 가상 환경 (Virtual Environment)

**왜 필요한가?**
- 프로젝트마다 독립된 패키지 관리
- 버전 충돌 방지
- 배포 시 필요한 패키지만 명시

```bash
# 가상 환경 생성
python -m venv myenv

# 활성화
# Windows
myenv\Scripts\activate

# macOS/Linux
source myenv/bin/activate

# 비활성화
deactivate
```

#### 3.4 requirements.txt

```bash
# 현재 환경의 패키지 목록 저장
pip freeze > requirements.txt

# requirements.txt 내용 예시
pandas==2.0.0
numpy==1.24.0
requests==2.31.0
matplotlib==3.7.0
```

```bash
# 다른 환경에서 동일하게 설치
pip install -r requirements.txt
```

#### 3.5 자주 사용하는 패키지

**데이터 처리:**
```python
# pandas - 데이터 분석
import pandas as pd

# numpy - 수치 연산
import numpy as np

# openpyxl - Excel 읽기/쓰기
import openpyxl
```

**웹 관련:**
```python
# requests - HTTP 요청
import requests

# beautifulsoup4 - HTML 파싱
from bs4 import BeautifulSoup

# flask - 웹 프레임워크
from flask import Flask
```

**유틸리티:**
```python
# python-dotenv - 환경 변수 관리
from dotenv import load_dotenv

# pillow - 이미지 처리
from PIL import Image

# tqdm - 진행 표시줄
from tqdm import tqdm
```

#### 3.6 실습 예제

```python
# requests 설치 후 사용
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # 200
print(response.json())  # JSON 데이터

# pandas 사용
import pandas as pd

data = {
    "name": ["김철수", "이영희"],
    "age": [25, 30]
}
df = pd.DataFrame(data)
print(df)
```

### 🔨 실습 (10분)

[실습 파일: pip_packages.py](./pip_packages.py)

**과제:** 외부 패키지 활용

**사전 준비:**
```bash
pip install requests pandas
```

**요구사항:**
1. requests로 웹 API 호출
2. pandas로 데이터프레임 생성
3. 데이터 필터링 및 집계
4. 결과 출력

### 💬 해설 (5분)

**핵심 포인트:**
1. `pip install` - 패키지 설치
2. `pip list` - 설치된 패키지 확인
3. `requirements.txt` - 패키지 목록 관리
4. 가상 환경 - 프로젝트별 독립 환경

**자주 하는 실수:**
```bash
# ❌ 가상 환경 활성화 안 함
pip install pandas  # 전역에 설치됨!

# ✅ 가상 환경에서 설치
python -m venv venv
venv\Scripts\activate  # Windows
pip install pandas
```

**실무 팁:**
- 프로젝트 시작 시 항상 가상 환경 생성
- requirements.txt로 패키지 관리
- `.gitignore`에 `venv/` 추가

---

## 세션 4: 텍스트 파일 읽기/쓰기 (25분)
**중요도:** ★★★★★

### 📚 이론 (10분)

#### 4.1 파일 열기

```python
# 읽기 모드
file = open("data.txt", "r", encoding="utf-8")
content = file.read()
file.close()

# ✅ with문 사용 (권장!)
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
# 자동으로 닫힘
```

**파일 모드:**
- `"r"` - 읽기 (기본값)
- `"w"` - 쓰기 (덮어쓰기)
- `"a"` - 추가 (이어쓰기)
- `"r+"` - 읽기/쓰기

⚠️ **중요:** Windows에서는 `encoding="utf-8"` 필수!

#### 4.2 파일 읽기

```python
# 전체 읽기
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 한 줄씩 읽기
with open("data.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    print(line)

# 모든 줄을 리스트로
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())  # 줄바꿈 제거

# for문으로 한 줄씩 (메모리 효율적)
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

#### 4.3 파일 쓰기

```python
# 새로 쓰기 (덮어쓰기)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.write("Python is awesome!")

# 여러 줄 쓰기
lines = ["첫 번째 줄\n", "두 번째 줄\n", "세 번째 줄\n"]
with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

# 추가 모드
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("새 로그 추가\n")
```

#### 4.4 실무 활용

**로그 파일 분석:**
```python
# 에러 로그만 추출
with open("app.log", "r", encoding="utf-8") as f:
    error_lines = [line for line in f if "ERROR" in line]

with open("errors.txt", "w", encoding="utf-8") as f:
    f.writelines(error_lines)
```

**설정 파일 읽기:**
```python
config = {}
with open("config.txt", "r", encoding="utf-8") as f:
    for line in f:
        if "=" in line:
            key, value = line.strip().split("=")
            config[key] = value

print(config)
```

#### 4.5 파일 존재 확인

```python
import os

if os.path.exists("data.txt"):
    with open("data.txt", "r", encoding="utf-8") as f:
        content = f.read()
else:
    print("파일이 없습니다!")
```

#### 4.6 Java와 비교

```java
// Java - 파일 읽기 (복잡)
BufferedReader reader = new BufferedReader(
    new FileReader("data.txt")
);
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

### 🔨 실습 (10분)

[실습 파일: text_file.py](./text_file.py)

**과제:** 로그 파일 분석기

**요구사항:**
1. 로그 파일 생성 (여러 줄의 로그 데이터)
2. 로그 파일 읽기
3. 에러 로그만 필터링
4. 통계 계산 (전체, 에러, 경고 개수)
5. 결과를 새 파일에 저장

### 💬 해설 (5분)

**핵심 포인트:**
1. `with open()` - 자동 파일 닫기
2. `encoding="utf-8"` - 한글 깨짐 방지
3. `strip()` - 줄바꿈 제거
4. 모드: `r` (읽기), `w` (쓰기), `a` (추가)

**자주 하는 실수:**
```python
# ❌ 파일 안 닫음
f = open("data.txt", "r")
content = f.read()
# f.close() 빠뜨림!

# ❌ encoding 미지정 (Windows에서 문제)
with open("data.txt", "r") as f:  # 한글 깨짐!
    content = f.read()

# ✅ with + encoding
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

**실무 팁:**
- 큰 파일은 `for line in f`로 한 줄씩 처리
- 경로는 `os.path.join()` 사용
- 파일 존재 여부 확인 습관화

---

## 세션 5: CSV 파일 처리 (25분)
**중요도:** ★★★★★

### 📚 이론 (10분)

#### 5.1 CSV란?

📌 **CSV (Comma-Separated Values)**

엑셀보다 **가볍고 호환성이 좋은** 표 형식 데이터 파일입니다.

**CSV 예시:**
```
이름,나이,부서
김철수,28,개발
이영희,32,기획
박민수,25,마케팅
```

**왜 CSV를 사용하는가?**
- 모든 프로그램에서 지원
- 텍스트 파일이라 가볍고 빠름
- Git으로 변경 추적 가능
- 데이터베이스 import/export에 표준

#### 5.2 csv 모듈로 읽기

```python
import csv

# CSV 읽기
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)  # 리스트로 반환
        # ['김철수', '28', '개발']

# 헤더 건너뛰기
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # 첫 줄(헤더) 건너뛰기

    for row in reader:
        print(row)

# DictReader - 딕셔너리로 읽기 (편리!)
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)
        # {'이름': '김철수', '나이': '28', '부서': '개발'}
        print(row['이름'], row['나이'])
```

#### 5.3 csv 모듈로 쓰기

```python
import csv

# CSV 쓰기
data = [
    ["이름", "나이", "부서"],
    ["김철수", 28, "개발"],
    ["이영희", 32, "기획"]
]

with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    for row in data:
        writer.writerow(row)

    # 또는 한번에
    # writer.writerows(data)

# DictWriter - 딕셔너리로 쓰기
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

⚠️ **중요:** Windows에서 `newline=""` 필수! (빈 줄 방지)

#### 5.4 pandas로 CSV 처리 (더 강력!)

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

# CSV 쓰기
df.to_csv("output.csv", index=False, encoding="utf-8-sig")
```

💡 **Tip:** `encoding="utf-8-sig"`를 사용하면 Excel에서 한글이 깨지지 않습니다!

#### 5.5 실무 활용

**엑셀 대신 CSV:**
```python
import pandas as pd

# 여러 CSV 합치기
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

### 🔨 실습 (10분)

[실습 파일: csv_file.py](./csv_file.py)

**과제:** 직원 데이터 관리

**요구사항:**
1. 직원 데이터를 CSV로 저장
2. CSV 파일 읽기
3. 부서별 평균 연봉 계산
4. 특정 부서 직원만 필터링
5. 결과를 새 CSV 파일로 저장

### 💬 해설 (5분)

**핵심 포인트:**
1. `csv.reader()` - 리스트로 읽기
2. `csv.DictReader()` - 딕셔너리로 읽기 (편리)
3. `newline=""` - 빈 줄 방지
4. `pandas` - 더 강력한 CSV 처리

**자주 하는 실수:**
```python
# ❌ newline 미지정 (Windows에서 빈 줄 생김)
with open("data.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)

# ✅ newline="" 추가
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
```

**실무 팁:**
- 간단한 처리: `csv` 모듈
- 복잡한 분석: `pandas`
- Excel 호환: `encoding="utf-8-sig"`

---

## 세션 6: JSON 파일 처리 (25분)
**중요도:** ★★★★★

### 📚 이론 (10분)

#### 6.1 JSON이란?

📌 **JSON (JavaScript Object Notation)**

**웹 API와 데이터 교환의 표준** 포맷입니다.

**JSON 예시:**
```json
{
  "name": "김철수",
  "age": 28,
  "skills": ["Python", "JavaScript"],
  "address": {
    "city": "서울",
    "district": "강남구"
  }
}
```

**왜 JSON을 사용하는가?**
- 웹 API의 표준 응답 형식
- 사람이 읽기 쉬움
- Python 딕셔너리와 구조가 같음
- 모든 프로그래밍 언어에서 지원

#### 6.2 JSON 읽기/쓰기

```python
import json

# Python → JSON (직렬화, Serialization)
data = {
    "name": "김철수",
    "age": 28,
    "skills": ["Python", "JavaScript"]
}

json_string = json.dumps(data, ensure_ascii=False, indent=2)
print(json_string)

# JSON → Python (역직렬화, Deserialization)
json_string = '{"name": "김철수", "age": 28}'
data = json.loads(json_string)
print(data["name"])  # "김철수"
```

#### 6.3 JSON 파일 처리

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

**매개변수 설명:**
- `ensure_ascii=False` - 한글 그대로 저장
- `indent=2` - 들여쓰기로 보기 좋게

#### 6.4 API 응답 처리

```python
import requests
import json

# API 호출
response = requests.get("https://api.github.com/users/python")

# JSON 파싱
data = response.json()  # 자동으로 json.loads() 수행

print(data["name"])
print(data["public_repos"])

# 파일로 저장
with open("github_user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

#### 6.5 설정 파일

**config.json:**
```json
{
  "database": {
    "host": "localhost",
    "port": 5432,
    "username": "admin"
  },
  "logging": {
    "level": "INFO",
    "file": "app.log"
  }
}
```

**사용:**
```python
import json

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

db_host = config["database"]["host"]
log_level = config["logging"]["level"]
```

#### 6.6 JSON vs CSV

| 항목 | JSON | CSV |
|------|------|-----|
| 구조 | 계층적 (중첩 가능) | 평면적 (표) |
| 용도 | API, 설정 파일 | 데이터 교환 |
| 가독성 | 높음 | 보통 |
| Excel | 지원 안 함 | 바로 열림 |

### 🔨 실습 (10분)

[실습 파일: json_file.py](./json_file.py)

**과제:** 제품 정보 관리

**요구사항:**
1. 제품 데이터를 JSON으로 저장
2. JSON 파일 읽기
3. 가격대별 제품 필터링
4. 통계 계산
5. 결과를 JSON으로 저장

### 💬 해설 (5분)

**핵심 포인트:**
1. `json.dumps()` - Python → JSON 문자열
2. `json.loads()` - JSON 문자열 → Python
3. `json.dump()` - Python → JSON 파일
4. `json.load()` - JSON 파일 → Python

**자주 하는 실수:**
```python
# ❌ 한글이 \uXXXX로 저장됨
json.dumps(data)  # {"name": "\uae40\ucca0\uc218"}

# ✅ ensure_ascii=False
json.dumps(data, ensure_ascii=False)  # {"name": "김철수"}
```

**실무 팁:**
- API 응답은 항상 JSON
- 설정 파일로 JSON 활용
- `indent=2`로 보기 좋게

---

## 세션 7: Excel 파일 읽기/쓰기 (25분)
**중요도:** ★★★★★

### 📚 이론 (10분)

#### 7.1 왜 Excel 처리가 중요한가?

**업무 자동화의 핵심!**
- 대부분의 회사가 Excel 사용
- 수작업 → 자동화로 시간 절약
- 데이터 분석 및 리포트 생성

#### 7.2 pandas로 Excel 읽기

```python
import pandas as pd

# Excel 읽기
df = pd.read_excel("sales.xlsx")
print(df)

# 특정 시트 읽기
df = pd.read_excel("sales.xlsx", sheet_name="2024년")

# 여러 시트 읽기
dfs = pd.read_excel("sales.xlsx", sheet_name=None)  # 모든 시트
for sheet_name, df in dfs.items():
    print(f"{sheet_name}: {len(df)}행")

# 헤더 지정
df = pd.read_excel("data.xlsx", header=2)  # 3번째 행을 헤더로

# 특정 열만 읽기
df = pd.read_excel("data.xlsx", usecols=["이름", "나이"])
```

#### 7.3 pandas로 Excel 쓰기

```python
import pandas as pd

# 데이터프레임 생성
data = {
    "이름": ["김철수", "이영희", "박민수"],
    "나이": [28, 32, 25],
    "부서": ["개발", "기획", "마케팅"]
}
df = pd.DataFrame(data)

# Excel로 저장
df.to_excel("output.xlsx", index=False)

# 여러 시트로 저장
with pd.ExcelWriter("multi_sheet.xlsx") as writer:
    df1.to_excel(writer, sheet_name="직원", index=False)
    df2.to_excel(writer, sheet_name="부서", index=False)
```

#### 7.4 openpyxl로 세밀한 제어

```python
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill

# 새 워크북 생성
wb = Workbook()
ws = wb.active
ws.title = "직원명단"

# 데이터 쓰기
ws["A1"] = "이름"
ws["B1"] = "나이"
ws["C1"] = "부서"

# 스타일 적용
header_font = Font(bold=True, color="FFFFFF")
header_fill = PatternFill(start_color="0066CC", fill_type="solid")

for cell in ws[1]:
    cell.font = header_font
    cell.fill = header_fill

# 행 추가
ws.append(["김철수", 28, "개발"])
ws.append(["이영희", 32, "기획"])

# 저장
wb.save("employees.xlsx")

# 기존 파일 읽기
wb = load_workbook("employees.xlsx")
ws = wb.active

# 셀 값 읽기
print(ws["A1"].value)

# 범위 읽기
for row in ws.iter_rows(min_row=2, values_only=True):
    print(row)
```

#### 7.5 실무 활용

**여러 Excel 파일 합치기:**
```python
import pandas as pd
import glob

# 모든 Excel 파일 찾기
files = glob.glob("sales_*.xlsx")

# 합치기
dfs = [pd.read_excel(f) for f in files]
combined = pd.concat(dfs, ignore_index=True)

# 저장
combined.to_excel("combined_sales.xlsx", index=False)
```

**엑셀 템플릿 활용:**
```python
from openpyxl import load_workbook

# 템플릿 열기
wb = load_workbook("template.xlsx")
ws = wb.active

# 데이터 채우기
employees = [("김철수", 28), ("이영희", 32)]

for i, (name, age) in enumerate(employees, start=2):
    ws[f"A{i}"] = name
    ws[f"B{i}"] = age

# 다른 이름으로 저장
wb.save("filled_report.xlsx")
```

### 🔨 실습 (10분)

[실습 파일: excel_file.py](./excel_file.py)

**과제:** 판매 데이터 분석

**사전 준비:**
```bash
pip install pandas openpyxl
```

**요구사항:**
1. 샘플 판매 데이터 생성
2. Excel 파일로 저장
3. 데이터 읽어서 분석 (월별 매출, 제품별 판매량)
4. 결과를 새 시트에 저장
5. 셀 스타일 적용 (헤더 강조)

### 💬 해설 (5분)

**핵심 포인트:**
1. `pd.read_excel()` - 읽기
2. `df.to_excel()` - 쓰기
3. `ExcelWriter` - 여러 시트
4. `openpyxl` - 세밀한 제어

**자주 하는 실수:**
```python
# ❌ openpyxl 미설치
df.to_excel("data.xlsx")  # 에러!

# ✅ openpyxl 설치 필요
# pip install openpyxl
```

**실무 팁:**
- 간단한 작업: `pandas`
- 서식/스타일: `openpyxl`
- `index=False` - 인덱스 열 제거

---

## 세션 8: 클래스 기초 (25분)
**중요도:** ★★★★★

### 📚 이론 (10분)

#### 8.1 클래스란?

📌 **클래스 (Class)**

**데이터와 기능을 하나로 묶은 설계도**입니다.

**왜 필요한가?**
```python
# ❌ 함수만 사용 (불편함)
account1_balance = 100000
account2_balance = 200000

def deposit(account_num, amount):
    global account1_balance, account2_balance
    if account_num == 1:
        account1_balance += amount
    elif account_num == 2:
        account2_balance += amount

# ✅ 클래스 사용 (체계적)
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

account1 = BankAccount(100000)
account2 = BankAccount(200000)

account1.deposit(50000)  # 간단!
```

#### 8.2 클래스 정의

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

#### 8.3 self란?

**`self`는 객체 자기 자신을 가리킵니다.**

```python
class Counter:
    def __init__(self):
        self.count = 0  # 이 객체의 count

    def increment(self):
        self.count += 1  # 이 객체의 count 증가

counter1 = Counter()
counter2 = Counter()

counter1.increment()
counter1.increment()

print(counter1.count)  # 2
print(counter2.count)  # 0 (별개의 객체)
```

#### 8.4 실무 예제

**직원 클래스:**
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
print(emp1.get_info())
```

**상품 클래스:**
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
product.sell(2)
product.restock(10)
```

#### 8.5 Java와 비교

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

### 🔨 실습 (10분)

[실습 파일: class_basic.py](./class_basic.py)

**과제:** 은행 계좌 클래스

**요구사항:**
1. BankAccount 클래스 정의
2. 속성: 소유자, 잔액
3. 메서드: 입금, 출금, 잔액 조회
4. 여러 계좌 생성 및 테스트
5. 거래 내역 출력

### 💬 해설 (5분)

**핵심 포인트:**
1. `class` - 클래스 정의
2. `__init__()` - 생성자 (초기화)
3. `self` - 객체 자신
4. 메서드 - 클래스 내부 함수

**자주 하는 실수:**
```python
# ❌ self 빠뜨림
class Person:
    def __init__(name, age):  # 에러!
        name = name

# ✅ self 필수
class Person:
    def __init__(self, name, age):
        self.name = name
```

**실무 팁:**
- 클래스명은 UpperCamelCase
- 속성은 `__init__`에서 초기화
- 관련 데이터와 기능을 하나로 묶기

---

## 세션 9: 클래스 메서드와 속성 (25분)
**중요도:** ★★★★☆

### 📚 이론 (10분)

#### 9.1 인스턴스 변수 vs 클래스 변수

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

#### 9.2 클래스 메서드와 정적 메서드

```python
class Math:
    PI = 3.14159

    @classmethod
    def circle_area(cls, radius):
        """클래스 메서드 - cls 사용"""
        return cls.PI * radius ** 2

    @staticmethod
    def add(a, b):
        """정적 메서드 - 유틸리티 함수"""
        return a + b

# 클래스로 직접 호출
print(Math.circle_area(5))  # 78.53975
print(Math.add(3, 5))  # 8
```

#### 9.3 프로퍼티 (Property)

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
        """Setter - 검증 추가 가능"""
        if value < -273.15:
            raise ValueError("절대영도보다 낮을 수 없습니다!")
        self._celsius = value

    @property
    def fahrenheit(self):
        """섭씨 → 화씨 자동 계산"""
        return self._celsius * 9/5 + 32

# 사용
temp = Temperature(25)
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0

temp.celsius = 30  # setter 호출
# temp.celsius = -300  # ValueError!
```

#### 9.4 특수 메서드 (Magic Methods)

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        """print()할 때 출력되는 문자열"""
        return f"{self.name}: {self.price:,}원"

    def __repr__(self):
        """개발자용 표현"""
        return f"Product('{self.name}', {self.price})"

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

#### 9.5 상속 (간단히)

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name}: 멍멍!"

class Cat(Animal):
    def speak(self):
        return f"{self.name}: 야옹!"

dog = Dog("바둑이")
cat = Cat("나비")

print(dog.speak())  # "바둑이: 멍멍!"
print(cat.speak())  # "나비: 야옹!"
```

### 🔨 실습 (10분)

[실습 파일: class_advanced.py](./class_advanced.py)

**과제:** 도서 관리 시스템

**요구사항:**
1. Book 클래스 (제목, 저자, 가격)
2. Library 클래스 (도서 목록 관리)
3. 클래스 변수로 전체 도서 수 추적
4. 특수 메서드 구현 (__str__, __lt__)
5. 도서 추가, 검색, 정렬 기능

### 💬 해설 (5분)

**핵심 포인트:**
1. 인스턴스 변수 vs 클래스 변수
2. `@classmethod`, `@staticmethod`
3. `@property` - Getter/Setter
4. 특수 메서드 - `__str__`, `__lt__` 등

**자주 하는 실수:**
```python
# ❌ 클래스 변수를 인스턴스 변수처럼
class Counter:
    count = 0

    def increment(self):
        self.count += 1  # 새 인스턴스 변수 생성!

# ✅ 클래스 변수 수정
class Counter:
    count = 0

    def increment(self):
        Counter.count += 1  # 클래스 변수 수정
```

**실무 팁:**
- Private 속성: `_변수명` (관례)
- Property로 검증 로직 추가
- `__str__`로 읽기 좋은 출력

---

## 🎯 Day 6 마무리

### 학습 내용 요약

1. **모듈 import** ★★★★★
   - import, from...import, as
   - 표준 라이브러리 활용

2. **표준 라이브러리** ★★★★★
   - random, datetime, math, os, sys

3. **외부 패키지 (pip)** ★★★★☆
   - pip install, requirements.txt
   - 가상 환경

4. **텍스트 파일** ★★★★★
   - open(), read(), write()
   - with문, encoding

5. **CSV 파일** ★★★★★
   - csv 모듈, pandas
   - DictReader, DictWriter

6. **JSON 파일** ★★★★★
   - json.dump(), json.load()
   - API 응답 처리

7. **Excel 파일** ★★★★★
   - pandas, openpyxl
   - 읽기/쓰기, 여러 시트

8. **클래스 기초** ★★★★★
   - class, __init__, self
   - 속성, 메서드

9. **클래스 고급** ★★★★☆
   - 클래스 변수, property
   - 특수 메서드, 상속

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

**수고하셨습니다! 🎉**

오늘 배운 파일 처리와 클래스는 실무에서 가장 많이 사용하는 기능입니다.
특히 Excel 자동화는 업무 효율을 크게 향상시킬 수 있으니,
실습 파일을 반복해서 연습하세요!
