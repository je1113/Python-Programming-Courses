"""
파일명: module_import.py
목적: 모듈 import 실습
"""

print("=" * 70)
print("Python 모듈 import 실습".center(70))
print("=" * 70)

# 1. math 모듈
print("\n[1] math 모듈 - 수학 계산")
print("-" * 70)

import math

numbers = [16, 25, 100, 144]

print(f"{'숫자':<10} {'제곱근':<10} {'올림':<10} {'내림':<10}")
print("-" * 40)

for num in numbers:
    sqrt_val = math.sqrt(num)
    ceil_val = math.ceil(num / 3)
    floor_val = math.floor(num / 3)
    print(f"{num:<10} {sqrt_val:<10.2f} {ceil_val:<10} {floor_val:<10}")

print(f"\nπ (파이): {math.pi:.10f}")
print(f"e (자연상수): {math.e:.10f}")

# 원의 넓이와 둘레
radius = 5
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"\n반지름 {radius}인 원:")
print(f"  넓이: {area:.2f}")
print(f"  둘레: {circumference:.2f}")

# 2. random 모듈
print("\n[2] random 모듈 - 난수 생성")
print("-" * 70)

import random

# 난수 생성
print(f"0~1 사이 실수: {random.random():.4f}")
print(f"1~100 사이 정수: {random.randint(1, 100)}")
print(f"1~10 사이 정수 (5개): {[random.randint(1, 10) for _ in range(5)]}")

# 리스트에서 선택
fruits = ["사과", "바나나", "오렌지", "포도", "딸기"]
print(f"\n과일 목록: {fruits}")
print(f"랜덤 선택: {random.choice(fruits)}")
print(f"2개 샘플링: {random.sample(fruits, 2)}")

# 리스트 섞기
numbers = [1, 2, 3, 4, 5]
print(f"\n원본: {numbers}")
random.shuffle(numbers)
print(f"섞은 후: {numbers}")

# 3. datetime 모듈
print("\n[3] datetime 모듈 - 날짜/시간")
print("-" * 70)

from datetime import datetime, date, time, timedelta

# 현재 날짜/시간
now = datetime.now()
today = date.today()

print(f"현재 날짜/시간: {now}")
print(f"오늘 날짜: {today}")

# 포맷팅
formatted = now.strftime("%Y년 %m월 %d일 %H:%M:%S")
print(f"포맷팅: {formatted}")

# 날짜 연산
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
yesterday = today - timedelta(days=1)

print(f"\n어제: {yesterday}")
print(f"오늘: {today}")
print(f"내일: {tomorrow}")
print(f"다음 주: {next_week}")

# D-Day 계산
target_date = date(2024, 12, 31)
d_day = (target_date - today).days
print(f"\n2024년 12월 31일까지 D-{d_day}")

# 4. os 모듈
print("\n[4] os 모듈 - 파일/디렉토리")
print("-" * 70)

import os

# 현재 작업 디렉토리
cwd = os.getcwd()
print(f"현재 디렉토리: {cwd}")

# 디렉토리 내용
print(f"\n현재 디렉토리 파일 목록:")
files = os.listdir(".")
for i, file in enumerate(files[:10], 1):  # 처음 10개만
    print(f"  {i}. {file}")

if len(files) > 10:
    print(f"  ... (총 {len(files)}개)")

# 경로 관련
print(f"\n경로 정보:")
sample_path = os.path.join("folder", "subfolder", "file.txt")
print(f"  경로 결합: {sample_path}")
print(f"  Python 실행 파일 존재: {os.path.exists('python')}")

# 환경 변수
print(f"\n시스템 환경:")
print(f"  사용자명: {os.environ.get('USERNAME', os.environ.get('USER', '알 수 없음'))}")
print(f"  홈 디렉토리: {os.environ.get('HOME', os.environ.get('USERPROFILE', '알 수 없음'))}")

# 5. sys 모듈
print("\n[5] sys 모듈 - 시스템 정보")
print("-" * 70)

import sys

print(f"Python 버전: {sys.version}")
print(f"플랫폼: {sys.platform}")
print(f"실행 파일: {sys.executable}")

print(f"\n모듈 검색 경로 (처음 3개):")
for i, path in enumerate(sys.path[:3], 1):
    print(f"  {i}. {path}")

# 6. from import 사용
print("\n[6] from import - 특정 함수만 임포트")
print("-" * 70)

from math import sqrt, pi, pow
from random import randint, choice

# math. 없이 직접 사용
print(f"sqrt(144) = {sqrt(144)}")
print(f"pi = {pi:.5f}")
print(f"pow(2, 10) = {pow(2, 10)}")

# random. 없이 직접 사용
print(f"\n1~100 랜덤: {randint(1, 100)}")
colors = ["빨강", "파랑", "노랑", "초록"]
print(f"색상 선택: {choice(colors)}")

# 7. 별칭(alias) 사용
print("\n[7] import as - 별칭 사용")
print("-" * 70)

import math as m
import random as r

print(f"m.sqrt(81) = {m.sqrt(81)}")
print(f"r.randint(1, 10) = {r.randint(1, 10)}")

# 실무에서 자주 사용하는 별칭
try:
    import pandas as pd
    import numpy as np
    print("\npandas → pd, numpy → np (데이터 분석 표준)")
except ImportError:
    print("\npandas, numpy는 pip install로 설치 필요")

# 8. 종합 예제: 로또 번호 생성기
print("\n[8] 종합 예제: 로또 번호 생성기")
print("-" * 70)

from random import sample
from datetime import datetime

print(f"생성 일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

for i in range(5):
    lotto = sorted(sample(range(1, 46), 6))
    bonus = sample([n for n in range(1, 46) if n not in lotto], 1)[0]
    print(f"  [{i+1}] {lotto} + Bonus: {bonus}")

# 9. 모듈 정보 확인
print("\n[9] 모듈 정보")
print("-" * 70)

print(f"math 모듈 위치: {math.__file__}")
print(f"random 모듈 이름: {random.__name__}")

# math 모듈의 주요 함수들
print("\nmath 모듈의 주요 함수:")
math_functions = [name for name in dir(math) if not name.startswith('_')]
for i, func in enumerate(math_functions[:10], 1):
    print(f"  {i}. {func}")
print(f"  ... (총 {len(math_functions)}개)")

print("\n" + "=" * 70)
print("모듈 import 실습 완료".center(70))
print("=" * 70)
