import pytest # type: ignore
import main
from pathlib import Path


@pytest.fixture(autouse=True)
def reset_todos():
    # 모든 테스트 시작 전/후에 todos.json을 비우고 메모리도 초기화
    main.todos.clear()
    Path(main.TODO_FILE).unlink(missing_ok=True)
    yield
    main.todos.clear()
    Path(main.TODO_FILE).unlink(missing_ok=True)


@pytest.fixture
def sample_todos():
    return [
        {"id": 1, "text": "우유", "done": False},
        {"id": 2, "text": "빵", "done": True},
    ]
