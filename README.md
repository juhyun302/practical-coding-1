# Practical Coding 1: Learning Journey

실전코딩1 수업에서 Git 협업부터 프론트엔드, 백엔드, 데이터 저장, 테스트와 AI 기반 코드 리뷰까지 단계적으로 학습한 내용을 한 저장소에 정리했습니다.

## Skills at a Glance

| 영역 | 학습 내용 | 결과물 |
| --- | --- | --- |
| 협업 | Git, branch, merge, fork, merge request | `labs/git-collaboration` |
| Java 빌드 | Maven, JUnit, 프로젝트 구조 | `labs/java-maven` |
| 백엔드 기초 | Spring Boot, REST API, JPA, MySQL/H2 | `labs/spring-boot-basics` |
| 모바일 UI | Flutter, Provider, navigation, responsive layout | `labs/flutter-*` |
| 풀스택 | Flutter + Spring Boot/Node.js + Firebase + 외부 API | `projects/favorite-music` |
| 콘텐츠 처리 | Markdown parsing, Thymeleaf rendering | `projects/spring-markdown-viewer` |
| 품질 관리 | Python, JSON persistence, pytest, AI code review | `projects/ai-todo-cli` |

## Featured Projects

### Favorite Music

iTunes Search API로 앨범을 검색하고 즐겨찾기를 저장하는 애플리케이션입니다. Flutter 클라이언트와 두 가지 백엔드 구현을 함께 두어 같은 요구사항을 서로 다른 기술로 해결한 과정을 보여줍니다.

- Flutter와 Provider를 이용한 상태 관리
- 비동기 HTTP 통신과 외부 API 연동
- Spring Boot, JPA, H2 기반 REST API
- Node.js, Express, Firebase Admin 기반 REST API
- 즐겨찾기 조회·추가·삭제 기능

[프로젝트 보기](projects/favorite-music)

### Spring Markdown Viewer

classpath의 Markdown 문서를 읽어 CommonMark로 HTML을 생성하고 Thymeleaf 화면에 렌더링하는 Spring Boot 실습입니다.

[프로젝트 보기](projects/spring-markdown-viewer)

### AI-assisted Todo CLI

JSON 파일에 데이터를 저장하는 콘솔 Todo 애플리케이션입니다. 우선순위 정렬, 입력 검증, 예외 처리와 pytest 시나리오를 포함하며 AI를 활용한 리뷰·리팩터링 흐름도 기록했습니다.

[프로젝트 보기](projects/ai-todo-cli)

## Repository Structure

```text
.
|-- docs/                       # 원본 과제와 통합 구조 매핑
|-- labs/                       # 개념별 소규모 실습
|   |-- git-collaboration/
|   |-- java-maven/
|   |-- spring-boot-basics/
|   |-- flutter-namer/
|   `-- flutter-navigation/
`-- projects/                   # 기능 단위 대표 프로젝트
    |-- favorite-music/
    |-- spring-markdown-viewer/
    `-- ai-todo-cli/
```

## Notes

- 수업 과정에서 만든 저장소를 기술 주제와 결과물 중심으로 재구성했습니다.
- 실행에 필요한 비밀 키와 로컬 비밀번호는 저장소에 포함하지 않습니다.
- 일부 예제는 학습 당시의 구현을 보존하며, 개선 가능한 부분은 각 폴더 README에 기록했습니다.
