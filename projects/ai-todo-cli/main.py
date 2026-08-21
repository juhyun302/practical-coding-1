# 할 일 관리 프로그램
# 할 일을 추가, 조회, 완료, 삭제할 수 있는 콘솔 기반 프로그램
# 데이터는 todos.json 파일에 자동 저장된다.
# 우선도(상/중/하)에 따라 할 일을 정렬해서 표시한다.

import json

# 전역 변수: 할 일 목록 저장
todos = []

# JSON 파일 경로
TODO_FILE = "todos.json"

# 우선도 가중치 (정렬에 사용)
PRIORITY_WEIGHT = {"상": 0, "중": 1, "하": 2}


def load_todos():
    """
    todos.json 파일에서 할 일 목록을 로드하는 함수
    - 파일이 없거나 읽기 실패 시 빈 리스트 반환
    - 기존 데이터(priority 필드 없음)에 기본값 "중" 추가
    """
    global todos
    try:
        with open(TODO_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # 문자열 형태의 잘못된 데이터 필터링 (객체만 유지)
            loaded = [item for item in data if isinstance(item, dict) and "task" in item and "progress" in item]

            # 기존 데이터에 priority 필드가 없으면 기본값 "중" 추가
            for todo in loaded:
                if "priority" not in todo:
                    todo["priority"] = "중"

            todos.clear()
            todos.extend(loaded)
            # 변경된 데이터 저장
            save_todos()
            print(f"✓ {len(todos)}개의 할 일을 로드했습니다.")
    except FileNotFoundError:
        todos.clear()
        print("✓ 새로운 할 일 목록으로 시작합니다.")
    except (json.JSONDecodeError, ValueError):
        todos.clear()
        print("⚠ 파일을 읽는 중 오류가 발생했습니다. 새로 시작합니다.")


def save_todos():
    """
    현재 할 일 목록을 todos.json 파일로 저장하는 함수
    - 파일 쓰기 실패 시 오류 메시지 출력
    """
    try:
        with open(TODO_FILE, 'w', encoding='utf-8') as f:
            json.dump(todos, f, ensure_ascii=False, indent=2)
    except IOError:
        print("⚠ 파일 저장 중 오류가 발생했습니다.")


def show_menu():
    """메뉴를 출력하는 함수"""
    print("\n==== 할 일 관리 프로그램 ====")
    print("1. 할 일 추가")
    print("2. 할 일 목록 보기")
    print("3. 할 일 완료 처리")
    print("4. 할 일 삭제")
    print("5. 종료")
    print("=" * 28)


def add_todo(title):
    """
    할 일을 추가하는 함수
    - title: 추가할 할 일의 제목
    - 사용자로부터 우선도(상/중/하)를 선택받음
    """
    # 우선도 선택 프롬프트
    while True:
        print("우선도를 선택하세요: (1) 상  (2) 중  (3) 하")
        priority_choice = input("선택 (1-3): ")

        # 우선도 선택 검증
        if priority_choice == "1":
            priority = "상"
            break
        elif priority_choice == "2":
            priority = "중"
            break
        elif priority_choice == "3":
            priority = "하"
            break
        else:
            print("⚠ 1, 2, 3 중 하나를 선택하세요.")

    # 할 일 객체 생성
    todo = {
        "task": title,
        "progress": "미완료",
        "priority": priority
    }
    todos.append(todo)
    save_todos()
    print(f"✓ '{title}' 이(가) 추가되었습니다. (우선도: {priority})")


def view_todos():
    """
    할 일 목록을 조회하는 함수
    - 우선도(상 → 중 → 하)로 정렬하여 표시
    - 같은 우선도 내에서는 추가된 순서 유지
    """
    if len(todos) == 0:
        print("할 일이 없습니다.")
        return

    # 우선도로 정렬 (stable sort 사용)
    sorted_todos = sorted(todos, key=lambda x: PRIORITY_WEIGHT.get(x.get("priority", "중"), 1))

    print("\n=== 할 일 목록 ===")
    for i, todo in enumerate(sorted_todos):
        status = "✓" if todo["progress"] == "완료" else "○"
        priority = todo.get("priority", "중")
        print(f"{i + 1}. [{status}] {todo['task']} [{priority}]")


def get_sorted_todos():
    """
    정렬된 할 일 목록을 반환하는 함수
    - 우선도(상 → 중 → 하)로 정렬
    """
    return sorted(todos, key=lambda x: PRIORITY_WEIGHT.get(x.get("priority", "중"), 1))


def get_original_index(sorted_index):
    """
    정렬된 목록의 인덱스를 원래 todos 리스트의 인덱스로 변환
    """
    sorted_todos = get_sorted_todos()
    if sorted_index < 0 or sorted_index >= len(sorted_todos):
        return -1

    # 정렬된 리스트의 원소를 원래 리스트에서 찾기
    target_todo = sorted_todos[sorted_index]
    for i, todo in enumerate(todos):
        if todo is target_todo:
            return i
    return -1


def complete_todo(sorted_index):
    """
    할 일을 완료 처리하는 함수
    - sorted_index: 정렬된 목록에서의 할 일 번호
    """
    if sorted_index < 0 or sorted_index >= len(todos):
        print("⚠ 잘못된 번호입니다.")
        return

    # 정렬된 인덱스를 원래 인덱스로 변환
    original_index = get_original_index(sorted_index)
    if original_index < 0:
        print("⚠ 잘못된 번호입니다.")
        return

    todos[original_index]["progress"] = "완료"
    save_todos()
    print(f"✓ '{todos[original_index]['task']}'이(가) 완료되었습니다.")


def delete_todo(sorted_index):
    """
    할 일을 삭제하는 함수
    - sorted_index: 정렬된 목록에서의 할 일 번호
    """
    if sorted_index < 0 or sorted_index >= len(todos):
        print("⚠ 잘못된 번호입니다.")
        return

    # 정렬된 인덱스를 원래 인덱스로 변환
    original_index = get_original_index(sorted_index)
    if original_index < 0:
        print("⚠ 잘못된 번호입니다.")
        return

    deleted_title = todos[original_index]["task"]
    todos.pop(original_index)
    save_todos()
    print(f"✓ '{deleted_title}'이(가) 삭제되었습니다.")


def main():
    """프로그램의 메인 루프"""
    load_todos()

    while True:
        show_menu()
        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            # 할 일 추가
            title = input("추가할 할 일을 입력하세요: ")
            if title.strip() == "":
                print("⚠ 할 일은 비어있을 수 없습니다.")
            else:
                add_todo(title)

        elif choice == "2":
            # 할 일 목록 조회
            view_todos()

        elif choice == "3":
            # 할 일 완료 처리
            view_todos()
            try:
                number = int(input("완료할 할 일의 번호를 입력하세요: "))
                complete_todo(number - 1)
            except ValueError:
                print("⚠ 숫자를 입력하세요.")

        elif choice == "4":
            # 할 일 삭제
            view_todos()
            try:
                number = int(input("삭제할 할 일의 번호를 입력하세요: "))
                delete_todo(number - 1)
            except ValueError:
                print("⚠ 숫자를 입력하세요.")

        elif choice == "5":
            # 프로그램 종료
            print("프로그램을 종료합니다.")
            break

        else:
            # 잘못된 메뉴 선택
            print("⚠ 1~5 사이의 번호를 입력하세요.")


# 프로그램 시작점
if __name__ == "__main__":
    main()
