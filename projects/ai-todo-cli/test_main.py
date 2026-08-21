import json
from pathlib import Path

import pytest # type: ignore

import main
from main import add_todo, save_todos


@pytest.fixture(autouse=True)
def reset_todos():
    # 매 테스트 전에 빈 상태로 초기화 (자동 적용)
    main.todos.clear()
    save_todos()


# [ADD-01] 정상: 빈 리스트에서 우선도 상으로 할 일 추가
def test_ADD_01_normal_add(monkeypatch):
    # Arrange
    monkeypatch.setattr("builtins.input", lambda prompt="": "1")
    # Act
    add_todo("공부하기")
    # Assert
    assert len(main.todos) == 1
    assert main.todos[0] == {"task": "공부하기", "progress": "미완료", "priority": "상"}
    assert json.loads(Path(main.TODO_FILE).read_text(encoding="utf-8")) == main.todos


# [ADD-02] 정상: 기존 항목이 있을 때 200자 제목으로 우선도 중 추가
def test_ADD_02_add_200_char_title_with_medium_priority(monkeypatch):
    # Arrange
    main.todos.append({"task": "기존 항목", "progress": "미완료", "priority": "중"})
    save_todos()
    long_title_200 = "가" * 200
    monkeypatch.setattr("builtins.input", lambda prompt="": "2")
    # Act
    add_todo(long_title_200)
    # Assert
    assert len(main.todos) == 2
    assert main.todos[-1] == {"task": long_title_200, "progress": "미완료", "priority": "중"}
    assert json.loads(Path(main.TODO_FILE).read_text(encoding="utf-8")) == main.todos


# [ADD-03] 실패: main() 메뉴에서 빈 문자열 입력 시 거부
def test_ADD_03_reject_empty_title_in_main_menu(monkeypatch, capsys):
    # Arrange
    inputs = iter(["1", "", "5"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))
    # Act
    main.main()
    # Assert
    captured = capsys.readouterr()
    assert "⚠ 할 일은 비어있을 수 없습니다." in captured.out
    main.load_todos()
    assert main.todos == []


# [ADD-04] 실패: main() 메뉴에서 공백 문자열 입력 시 거부
def test_ADD_04_reject_whitespace_title_in_main_menu(monkeypatch, capsys):
    # Arrange
    inputs = iter(["1", "   ", "5"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))
    # Act
    main.main()
    # Assert
    captured = capsys.readouterr()
    assert "⚠ 할 일은 비어있을 수 없습니다." in captured.out
    main.load_todos()
    assert main.todos == []


# [ADD-05] 경계: 1자 제목을 우선도 중으로 추가
def test_ADD_05_add_one_char_title_with_medium_priority(monkeypatch):
    # Arrange
    monkeypatch.setattr("builtins.input", lambda prompt="": "2")
    # Act
    add_todo("가")
    # Assert
    assert len(main.todos) == 1
    assert main.todos[0] == {"task": "가", "progress": "미완료", "priority": "중"}
    assert json.loads(Path(main.TODO_FILE).read_text(encoding="utf-8")) == main.todos


# [ADD-06] 경계: 200자 제목을 우선도 하로 추가
def test_ADD_06_add_200_char_title_with_low_priority(monkeypatch):
    # Arrange
    main.todos.clear()
    save_todos()
    long_title_200 = "가" * 200
    monkeypatch.setattr("builtins.input", lambda prompt="": "3")
    # Act
    add_todo(long_title_200)
    # Assert
    assert len(main.todos) == 1
    assert main.todos[0] == {"task": long_title_200, "progress": "미완료", "priority": "하"}
    assert json.loads(Path(main.TODO_FILE).read_text(encoding="utf-8")) == main.todos


# [ADD-07] 경계: 우선도 입력에서 잘못된 값 후 재입력
def test_ADD_07_reprompt_priority_on_invalid_choice(monkeypatch, capsys):
    # Arrange
    main.todos.clear()
    save_todos()
    inputs = iter(["4", "2"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))
    # Act
    add_todo("운동하기")
    # Assert
    captured = capsys.readouterr()
    assert "⚠ 1, 2, 3 중 하나를 선택하세요." in captured.out
    assert len(main.todos) == 1
    assert main.todos[0]["priority"] == "중"
    assert json.loads(Path(main.TODO_FILE).read_text(encoding="utf-8")) == main.todos


# [ADD-08] 누락 가능 시나리오: priority 필드 없는 기존 항목 로드 후 새 항목 추가
def test_ADD_08_load_missing_priority_and_add_new_todo(monkeypatch):
    # Arrange
    Path(main.TODO_FILE).write_text(
        json.dumps([{"task": "기존", "progress": "미완료"}], ensure_ascii=False),
        encoding="utf-8",
    )
    main.todos.clear()
    main.load_todos()
    monkeypatch.setattr("builtins.input", lambda prompt="": "1")
    # Act
    add_todo("새 할 일")
    # Assert
    assert len(main.todos) == 2
    assert main.todos[0]["priority"] == "중"
    assert main.todos[1] == {"task": "새 할 일", "progress": "미완료", "priority": "상"}
    assert json.loads(Path(main.TODO_FILE).read_text(encoding="utf-8")) == main.todos


# [ADD-09] 누락 가능 시나리오: save_todos() IOError 발생 시 예외 없이 계속 실행
def test_ADD_09_continue_when_save_todos_io_error(monkeypatch, capsys):
    # Arrange
    main.todos.clear()
    save_todos()
    monkeypatch.setattr("builtins.input", lambda prompt="": "1")

    def raise_io_error(*args, **kwargs):
        raise IOError("disk error")

    monkeypatch.setattr("builtins.open", raise_io_error)
    # Act
    add_todo("오류 테스트")
    # Assert
    captured = capsys.readouterr()
    assert "⚠ 파일 저장 중 오류가 발생했습니다." in captured.out
    assert len(main.todos) == 1
    assert main.todos[0] == {"task": "오류 테스트", "progress": "미완료", "priority": "상"}
