from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
import sys
import os
import json

load_dotenv()  # .env 파일에서 환경 변수 로드
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    print("ERROR: OPENAI_API_KEY가 설정되어 있지 않습니다. .env 파일을 확인하세요.")
    sys.exit(1)
client = OpenAI(api_key=API_KEY)

# main.py 파일에서 코드 읽어오기
target_file = Path("main.py")
try:
    code = target_file.read_text(encoding="utf-8")
except Exception as e:
    print(f"ERROR: main.py 파일을 읽는 중 오류 발생: {e}")
    sys.exit(1)
# 코드 읽기
code = target_file.read_text(encoding="utf-8")

# 리뷰를 위한 프롬프트 생성
prompt = f"""
너는 Python 코드 리뷰어야.
아래 코드를 리뷰해줘.

리뷰 기준 :
1. 상세 리뷰 + 개선안 (권장)
2. 버그 가능성
3. 가독성
4. 함수 분리
5. 예외 처리
6. 보안 문제
7. 개선하면 좋은 코드 예시
8. 기타 의견

리뷰 결과는 아래 형식으로 정리해줘
출력 형식 :
| 위치 | 문제 유형 | 심각도 | 개선 제안 | 이유 |
마지막에는 “우선 반영할 3가지”를 별도로 정리해줘.

중요 :
- 바로 전체 코드를 고치지 마
- 먼저 개선 항목만 제안해줘
- 초급자가 이해할 수 있는 수준으로 설명해줘
- 기존 todos.json 파일 출력형식은 유지하면서, 코드 개선 방향을 제안해줘


```python
{code}
```
"""

response = client.responses.create(
model="gpt-4o-mini",
input=prompt
)

print(response.output_text)
