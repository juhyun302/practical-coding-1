# Favorite Music Spring API

Spring Boot와 JPA로 구현한 즐겨찾기 REST API입니다. H2 인메모리 데이터베이스를 사용하며 iTunes Search API 프록시도 제공합니다.

```bash
./mvnw spring-boot:run
```

서버는 기본적으로 `http://localhost:3000`에서 실행됩니다.

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/musicSearch?term={artist}` | 앨범 검색 |
| GET | `/likes` | 즐겨찾기 목록 |
| POST | `/likes` | 즐겨찾기 저장 |
| DELETE | `/likes/{id}` | 즐겨찾기 삭제 |
