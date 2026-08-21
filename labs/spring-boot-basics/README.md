# Spring Boot Basics Lab

Spring Boot에서 REST Controller, JPA Entity와 Repository를 구성하고 MySQL/H2 데이터베이스를 연결한 실습입니다.

## Main Topics

- Spring Boot REST API
- Spring Data JPA와 JDBC
- MySQL 및 H2 설정
- Entity, Repository, Controller 계층
- JUnit 기반 repository 테스트

## Run

MySQL을 사용하는 경우 환경변수를 설정합니다.

```bash
export DB_URL="jdbc:mysql://localhost:3306/shop?useSSL=false&serverTimezone=Asia/Seoul"
export DB_USERNAME="root"
export DB_PASSWORD="your-password"
./mvnw spring-boot:run
```

Windows PowerShell에서는 `export` 대신 `$env:DB_PASSWORD = "..."` 형식을 사용할 수 있습니다.
