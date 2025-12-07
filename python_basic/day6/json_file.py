"""
파일명: json_file.py
목적: JSON 파일 처리 실습
"""

import json
import os

print("=" * 70)
print("JSON 파일 처리 실습".center(70))
print("=" * 70)

# 1. JSON 파일 생성
print("\n[1] JSON 파일 생성")
print("-" * 70)

employee_data = {
    "company": "ABC 기업",
    "employees": [
        {
            "id": "E001",
            "name": "김철수",
            "age": 28,
            "department": "개발",
            "skills": ["Python", "JavaScript", "SQL"],
            "salary": 3500
        },
        {
            "id": "E002",
            "name": "이영희",
            "age": 32,
            "department": "기획",
            "skills": ["기획", "마케팅", "PM"],
            "salary": 4200
        },
        {
            "id": "E003",
            "name": "박민수",
            "age": 25,
            "department": "개발",
            "skills": ["Java", "Spring", "Docker"],
            "salary": 3200
        }
    ]
}

# JSON 파일로 저장
with open("employees.json", "w", encoding="utf-8") as f:
    json.dump(employee_data, f, ensure_ascii=False, indent=2)

print("✓ employees.json 생성 완료")

# 2. JSON 파일 읽기
print("\n[2] JSON 파일 읽기")
print("-" * 70)

with open("employees.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"회사: {data['company']}")
print(f"직원 수: {len(data['employees'])}명\n")

print(f"{'ID':<6} {'이름':<10} {'부서':<10} {'기술':<30}")
print("-" * 60)

for emp in data['employees']:
    skills = ", ".join(emp['skills'])
    print(f"{emp['id']:<6} {emp['name']:<10} {emp['department']:<10} {skills:<30}")

# 3. JSON 문자열 처리
print("\n[3] JSON 문자열 변환")
print("-" * 70)

# Python 딕셔너리 → JSON 문자열
person = {
    "name": "홍길동",
    "age": 30,
    "city": "서울"
}

json_string = json.dumps(person, ensure_ascii=False, indent=2)
print("Python → JSON:")
print(json_string)

# JSON 문자열 → Python 딕셔너리
parsed = json.loads(json_string)
print(f"\nJSON → Python:")
print(f"타입: {type(parsed)}")
print(f"이름: {parsed['name']}")

# 4. 제품 데이터 처리
print("\n[4] 제품 데이터 관리")
print("-" * 70)

products = {
    "products": [
        {
            "id": "P001",
            "name": "노트북",
            "price": 1200000,
            "stock": 5,
            "category": "전자기기",
            "specs": {
                "cpu": "Intel i7",
                "ram": "16GB",
                "ssd": "512GB"
            }
        },
        {
            "id": "P002",
            "name": "마우스",
            "price": 30000,
            "stock": 50,
            "category": "주변기기",
            "specs": {
                "type": "무선",
                "dpi": "1600"
            }
        },
        {
            "id": "P003",
            "name": "키보드",
            "price": 89000,
            "stock": 30,
            "category": "주변기기",
            "specs": {
                "type": "기계식",
                "switch": "청축"
            }
        }
    ]
}

# 저장
with open("products.json", "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print("✓ products.json 생성 완료")

# 제품 정보 출력
print(f"\n{'제품명':<10} {'가격':<15} {'재고':<10} {'카테고리':<12}")
print("-" * 50)

for product in products['products']:
    print(f"{product['name']:<10} {product['price']:>10,}원  "
          f"{product['stock']:>5}개  {product['category']:<12}")

# 5. 설정 파일
print("\n[5] 애플리케이션 설정 파일")
print("-" * 70)

config = {
    "app_name": "My Application",
    "version": "1.0.0",
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb",
        "user": "admin"
    },
    "logging": {
        "level": "INFO",
        "file": "app.log",
        "max_size": 10485760
    },
    "features": {
        "email_notifications": True,
        "dark_mode": False,
        "auto_save": True
    }
}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

# 설정 읽기
with open("config.json", "r", encoding="utf-8") as f:
    loaded_config = json.load(f)

print(f"애플리케이션: {loaded_config['app_name']} v{loaded_config['version']}")
print(f"\n데이터베이스 설정:")
print(f"  호스트: {loaded_config['database']['host']}")
print(f"  포트: {loaded_config['database']['port']}")
print(f"  DB명: {loaded_config['database']['name']}")

print(f"\n활성화된 기능:")
for feature, enabled in loaded_config['features'].items():
    status = "✓" if enabled else "✗"
    print(f"  {status} {feature}")

# 6. 데이터 필터링 및 수정
print("\n[6] 데이터 필터링 및 수정")
print("-" * 70)

# 재고 부족 제품 찾기
with open("products.json", "r", encoding="utf-8") as f:
    products_data = json.load(f)

print("재고 부족 제품 (20개 미만):")
for product in products_data['products']:
    if product['stock'] < 20:
        print(f"  - {product['name']}: {product['stock']}개")

# 가격 10% 인상
for product in products_data['products']:
    product['price'] = int(product['price'] * 1.1)

# 수정된 데이터 저장
with open("products_updated.json", "w", encoding="utf-8") as f:
    json.dump(products_data, f, ensure_ascii=False, indent=2)

print("\n✓ 가격 10% 인상 완료 (products_updated.json)")

# 7. API 응답 시뮬레이션
print("\n[7] API 응답 데이터")
print("-" * 70)

api_response = {
    "status": "success",
    "code": 200,
    "data": {
        "user": {
            "id": 12345,
            "username": "user123",
            "email": "user@example.com",
            "created_at": "2024-01-15T10:00:00Z"
        },
        "posts": [
            {
                "id": 1,
                "title": "첫 번째 게시글",
                "content": "안녕하세요!",
                "likes": 10
            },
            {
                "id": 2,
                "title": "두 번째 게시글",
                "content": "Python 좋아요!",
                "likes": 25
            }
        ]
    },
    "metadata": {
        "total_posts": 2,
        "page": 1,
        "per_page": 10
    }
}

with open("api_response.json", "w", encoding="utf-8") as f:
    json.dump(api_response, f, ensure_ascii=False, indent=2)

# API 응답 처리
print(f"상태: {api_response['status']}")
print(f"사용자: {api_response['data']['user']['username']}")
print(f"\n게시글 ({api_response['metadata']['total_posts']}개):")

for post in api_response['data']['posts']:
    print(f"  [{post['id']}] {post['title']} (좋아요 {post['likes']}개)")

# 8. 여러 JSON 파일 병합
print("\n[8] JSON 파일 병합")
print("-" * 70)

# 부서별 데이터 생성
dept_dev = {
    "department": "개발",
    "employees": [
        {"name": "김철수", "level": "중급"},
        {"name": "박민수", "level": "초급"}
    ]
}

dept_plan = {
    "department": "기획",
    "employees": [
        {"name": "이영희", "level": "고급"}
    ]
}

with open("dept_dev.json", "w", encoding="utf-8") as f:
    json.dump(dept_dev, f, ensure_ascii=False, indent=2)

with open("dept_plan.json", "w", encoding="utf-8") as f:
    json.dump(dept_plan, f, ensure_ascii=False, indent=2)

# 병합
all_departments = {"departments": []}

for filename in ["dept_dev.json", "dept_plan.json"]:
    with open(filename, "r", encoding="utf-8") as f:
        dept_data = json.load(f)
        all_departments["departments"].append(dept_data)

with open("all_departments.json", "w", encoding="utf-8") as f:
    json.dump(all_departments, f, ensure_ascii=False, indent=2)

print("✓ 부서 데이터 병합 완료")

# 9. JSON 유효성 검사
print("\n[9] JSON 유효성 검사")
print("-" * 70)

# 잘못된 JSON
invalid_json = '{"name": "test", "age": 30,}'  # 마지막 콤마 오류

try:
    data = json.loads(invalid_json)
    print("✓ 유효한 JSON")
except json.JSONDecodeError as e:
    print(f"✗ JSON 오류: {e}")

# 올바른 JSON
valid_json = '{"name": "test", "age": 30}'

try:
    data = json.loads(valid_json)
    print("✓ 유효한 JSON")
except json.JSONDecodeError as e:
    print(f"✗ JSON 오류: {e}")

# 10. Pretty Print
print("\n[10] JSON Pretty Print")
print("-" * 70)

# 복잡한 중첩 데이터
complex_data = {
    "user": {"name": "김철수", "age": 28, "address": {"city": "서울", "district": "강남구"}},
    "orders": [{"id": 1, "items": [{"name": "상품A", "price": 1000}]}]
}

# 압축 형식
compact = json.dumps(complex_data, ensure_ascii=False)
print("압축 형식:")
print(compact[:50] + "...")

# 보기 좋은 형식
pretty = json.dumps(complex_data, ensure_ascii=False, indent=2)
print("\n보기 좋은 형식:")
print(pretty)

# 11. 생성된 파일 목록
print("\n[11] 생성된 JSON 파일")
print("-" * 70)

json_files = [f for f in os.listdir(".") if f.endswith('.json')]

print(f"{'파일명':<30} {'크기':<15}")
print("-" * 45)

for filename in json_files:
    size = os.path.getsize(filename)
    print(f"{filename:<30} {size:>10} bytes")

    # 파일 내용 미리보기
    with open(filename, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            keys = list(data.keys()) if isinstance(data, dict) else []
            if keys:
                print(f"  → 키: {', '.join(keys[:3])}")
        except:
            pass

print("\n" + "=" * 70)
print("JSON 파일 처리 완료".center(70))
print("=" * 70)

print("\n💡 Tip: JSON은 웹 API와 데이터 교환의 표준 형식입니다!")
print("💡 Tip: ensure_ascii=False로 한글을 그대로 저장하세요!")
