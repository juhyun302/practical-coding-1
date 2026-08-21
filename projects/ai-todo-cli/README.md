# AI-assisted Todo CLI

할 일을 JSON 파일에 저장하는 Python 콘솔 애플리케이션입니다. 기능 구현뿐 아니라 테스트 시나리오 작성, 예외 처리, AI 기반 코드 리뷰와 리팩터링 과정을 함께 실습했습니다.

## Features

- 할 일 추가·조회·완료·삭제
- 상·중·하 우선순위와 정렬
- JSON 자동 저장 및 재실행 시 복구
- 잘못된 입력과 파일 오류 처리
- pytest 기반 정상·실패·경계값 테스트

## Run

```bash
python main.py
```

## Test

```bash
python -m pip install -r requirements-dev.txt
python -m pytest
```

`review.py`와 `refactoring.py`를 실행하려면 별도로 `OPENAI_API_KEY` 환경변수가 필요하며, 실제 키는 저장소에 포함하지 않습니다.
