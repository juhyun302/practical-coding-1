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
    """todos.json 파일에서 할 일 목록을 로드하는 함수"""
    global todos
    try:
        with open(TODO_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            todos = [item for item in data if isinstance(item, dict) and "task" in item and "progress" in item]
            for todo in todos:
                if "priority" not in todo:
                    todo["priority"] = "중"
            save_todos()
            print(f"✓ {len(todos)}개의 할 일을 로드했습니다.")
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        todos.clear()
        print("⚠ 파일을 읽는 중 오류가 발생했습니다. 새로 시작합니다.")


def save_todos():
    """현재 할 일 목록을 todos.json 파일로 저장하는 함수"""
    try:
        with open(TODO_FILE, 'w', encoding='utf-8') as f:
            json.dump(todos, f, ensure_ascii=False, indent=2)
    except IOError:
        print("⚠ 파일 저장 중 오류가 발생했습니다.")


def print_menu():
    """메뉴를 출력하는 함수"""
    print("\n==== 할 일 관리 프로그램 ====")
    print("1. 할 일 추가")
    print("2. 할 일 목록 보기")
    print("3. 할 일 완료 처리")
    print("4. 할 일 삭제")
    print("5. 종료")
    print("=" * 28)


def add_todo():
    """할 일을 추가하는 함수"""
    title = input("추가할 할 일을 입력하세요: ")
    if title.strip() == "":
        print("⚠ 할 일은 비어있을 수 없습니다.")
        return

    while True:
        print("우선도를 선택하세요: (1) 상  (2) 중  (3) 하")
        priority_choice = input("선택 (1-3): ")
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

    todo = {
        "task": title,
        "progress": "미완료",
        "priority": priority
    }
    todos.append(todo)
    save_todos()
    print(f"✓ '{title}' 이(가) 추가되었습니다. (우선도: {priority})")


def show_todos():
    """할 일 목록을 조회하는 함수"""
    if not todos:
        print("할 일이 없습니다.")
        return

    sorted_todos = sorted(todos, key=lambda x: PRIORITY_WEIGHT.get(x.get("priority", "중"), 1))

    print("\n=== 할 일 목록 ===")
    for i, todo in enumerate(sorted_todos):
        status = "✓" if todo["progress"] == "완료" else "○"
        priority = todo.get("priority", "중")
        print(f"{i + 1}. [{status}] {todo['task']} [{priority}]")


def get_todo_number():
    """사용자로부터 할 일 번호를 입력받고 검증하는 함수"""
    while True:
        try:
            number = int(input("번호를 입력하세요: "))
            if number < 1 or number > len(todos):
                print("⚠ 존재하지 않는 번호입니다.")
            else:
                return number - 1
        except ValueError:
            print("⚠ 숫자를 입력하세요.")


def complete_todo():
    """할 일을 완료 처리하는 함수"""
    show_todos()
    index = get_todo_number()
    if index != -1:
        todos[index]["progress"] = "완료"
        save_todos()
        print(f"✓ '{todos[index]['task']}'이(가) 완료되었습니다.")


def delete_todo():
    """할 일을 삭제하는 함수"""
    show_todos()
    index = get_todo_number()
    if index != -1:
        deleted_title = todos[index]["task"]
        todos.pop(index)
        save_todos()
        print(f"✓ '{deleted_title}'이(가) 삭제되었습니다.")


def main():
    """프로그램의 메인 루프"""
    load_todos()

    while True:
        print_menu()
        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            add_todo()
        elif choice == "2":
            show_todos()
        elif choice == "3":
            complete_todo()
        elif choice == "4":
            delete_todo()
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("⚠ 1~5 사이의 번호를 입력하세요.")

# 프로그램 시작점
if __name__ == "__main__":
    main()
