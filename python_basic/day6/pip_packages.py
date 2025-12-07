"""
파일명: pip_packages.py
목적: 외부 패키지 활용

사전 준비:
pip install requests pandas
"""

print("=" * 70)
print("외부 패키지 활용 프로그램".center(70))
print("=" * 70)

# 1. requests 패키지 - 웹 API 호출
print("\n[1] requests - 웹 API 호출")
print("-" * 70)

try:
    import requests

    # GitHub API 호출
    print("GitHub API 호출 중...")
    response = requests.get("https://api.github.com/users/python")

    if response.status_code == 200:
        data = response.json()
        print(f"\n계정명: {data['login']}")
        print(f"이름: {data.get('name', 'N/A')}")
        print(f"공개 저장소: {data['public_repos']}개")
        print(f"팔로워: {data['followers']}명")
        print(f"생성일: {data['created_at']}")
    else:
        print(f"오류: {response.status_code}")

except ImportError:
    print("⚠️  requests 패키지가 설치되지 않았습니다.")
    print("   설치 방법: pip install requests")

# 2. pandas 패키지 - 데이터 분석
print("\n[2] pandas - 데이터 분석")
print("-" * 70)

try:
    import pandas as pd

    # 데이터프레임 생성
    data = {
        "이름": ["김철수", "이영희", "박민수", "정지훈", "최민지"],
        "나이": [28, 32, 25, 30, 27],
        "부서": ["개발", "기획", "개발", "마케팅", "기획"],
        "연봉": [3500, 4200, 3200, 3800, 4000]
    }

    df = pd.DataFrame(data)

    print("직원 데이터프레임:")
    print(df)

    # 기본 통계
    print("\n연봉 통계:")
    print(f"  평균: {df['연봉'].mean():,.0f}만원")
    print(f"  최대: {df['연봉'].max():,}만원")
    print(f"  최소: {df['연봉'].min():,}만원")

    # 부서별 평균 연봉
    print("\n부서별 평균 연봉:")
    dept_avg = df.groupby('부서')['연봉'].mean()
    for dept, avg in dept_avg.items():
        print(f"  {dept}: {avg:,.0f}만원")

    # 필터링
    print("\n연봉 3500만원 이상 직원:")
    high_salary = df[df['연봉'] >= 3500]
    for _, row in high_salary.iterrows():
        print(f"  - {row['이름']}: {row['연봉']:,}만원")

except ImportError:
    print("⚠️  pandas 패키지가 설치되지 않았습니다.")
    print("   설치 방법: pip install pandas")

# 3. 종합 예제: API + pandas
print("\n[3] 종합 예제: API 데이터를 pandas로 분석")
print("-" * 70)

try:
    import requests
    import pandas as pd

    # 가상의 제품 데이터 생성 (실제로는 API에서 가져옴)
    products_data = {
        "제품명": ["노트북", "마우스", "키보드", "모니터", "헤드셋"],
        "가격": [1200000, 30000, 89000, 350000, 120000],
        "재고": [5, 50, 30, 10, 25],
        "카테고리": ["컴퓨터", "주변기기", "주변기기", "컴퓨터", "주변기기"]
    }

    df = pd.DataFrame(products_data)

    print("제품 목록:")
    print(df.to_string(index=False))

    # 총 재고 가치
    df['총가치'] = df['가격'] * df['재고']

    print("\n재고 분석:")
    print(f"  총 제품 수: {len(df)}개")
    print(f"  총 재고 수량: {df['재고'].sum()}개")
    print(f"  총 재고 가치: {df['총가치'].sum():,}원")

    # 카테고리별 통계
    print("\n카테고리별 통계:")
    category_stats = df.groupby('카테고리').agg({
        '가격': 'mean',
        '재고': 'sum',
        '총가치': 'sum'
    })

    for category, stats in category_stats.iterrows():
        print(f"\n{category}:")
        print(f"  평균 가격: {stats['가격']:,.0f}원")
        print(f"  총 재고: {stats['재고']}개")
        print(f"  재고 가치: {stats['총가치']:,}원")

except ImportError as e:
    print(f"⚠️  필요한 패키지가 설치되지 않았습니다: {e}")

# 4. 패키지 정보 확인
print("\n[4] 설치된 패키지 정보")
print("-" * 70)

packages = []

try:
    import requests
    packages.append(("requests", requests.__version__))
except ImportError:
    packages.append(("requests", "미설치"))

try:
    import pandas
    packages.append(("pandas", pandas.__version__))
except ImportError:
    packages.append(("pandas", "미설치"))

try:
    import numpy
    packages.append(("numpy", numpy.__version__))
except ImportError:
    packages.append(("numpy", "미설치"))

try:
    import openpyxl
    packages.append(("openpyxl", openpyxl.__version__))
except ImportError:
    packages.append(("openpyxl", "미설치"))

print(f"{'패키지':<15} {'버전':<15} {'상태':<10}")
print("-" * 40)

for package, version in packages:
    status = "✓ 설치됨" if version != "미설치" else "✗ 미설치"
    print(f"{package:<15} {version:<15} {status:<10}")

# 5. 실습 안내
print("\n[5] 패키지 설치 안내")
print("-" * 70)

print("""
필요한 패키지 설치 방법:

1. requests (웹 API 호출)
   pip install requests

2. pandas (데이터 분석)
   pip install pandas

3. openpyxl (Excel 처리)
   pip install openpyxl

4. 한 번에 설치:
   pip install requests pandas openpyxl

5. requirements.txt로 관리:
   # requirements.txt 파일 생성
   requests==2.31.0
   pandas==2.0.0
   openpyxl==3.1.0

   # 설치
   pip install -r requirements.txt
""")

print("\n" + "=" * 70)
print("외부 패키지 실습 완료".center(70))
print("=" * 70)
