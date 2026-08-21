# Favorite Music

앨범을 검색하고 좋아하는 항목을 저장하는 풀스택 학습 프로젝트입니다. 하나의 Flutter 클라이언트와 동일한 도메인을 구현한 Spring Boot·Node.js 백엔드를 함께 비교할 수 있습니다.

## Architecture

```text
Flutter client
  |-- iTunes Search API: 앨범 검색
  `-- Favorite API: 즐겨찾기 조회·추가·삭제
        |-- Spring Boot + JPA + H2
        `-- Node.js + Express + Firebase
```

## Components

- [`flutter-client`](flutter-client): Flutter, Provider, HTTP
- [`spring-api`](spring-api): Spring Boot, REST, JPA, H2, Docker
- [`node-firebase-api`](node-firebase-api): Express, Firebase Admin, Firestore

Flutter 클라이언트는 기본적으로 `http://localhost:3000`을 사용합니다. 다른 API 주소는 다음처럼 전달할 수 있습니다.

```bash
flutter run --dart-define=API_BASE_URL=https://your-api.example.com
```
