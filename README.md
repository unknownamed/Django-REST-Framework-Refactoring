# Django Blog REST API · ViewSet & Router

**APIView로 만든 블로그 API를 ModelViewSet과 Router로 리팩터링한 프로젝트입니다.**

`GenericAPIView + Mixins`를 거쳐 공통 CRUD 코드를 줄이고, `@action`으로 제목 변경 기능을 추가했습니다.

`Python` · `Django 6.0.4` · `Django REST Framework` · `SQLite` · `Insomnia`

[리팩터링 과정 전체](docs/learning-notes.md) · [이전 APIView 구현](https://github.com/unknownamed/Simplifying-code-with-Django-REST-Framework)

## 커스텀 기능 미리보기

<img src="images/image%206.png" alt="PATCH 요청으로 글 제목을 A로 바꾸고 JSON 응답을 확인한 화면" width="760">

> `/posts/1/title_change_A/` 요청 후 제목이 `A`로 바뀐 기존 실행 화면입니다.

## 무엇을 바꿨나요?

| 단계 | 처리 방식 | 학습 내용 |
| --- | --- | --- |
| APIView | HTTP 메서드별 직접 구현 | 조회·검증·오류 응답의 반복 확인 |
| GenericAPIView + Mixins | 공통 조회·직렬화와 CRUD 믹스인 사용 | 필요한 동작 조합 |
| ModelViewSet + SimpleRouter | CRUD 액션과 경로 연결 | 반복 코드 정리, 커스텀 액션 확장 |

현재 [PostViewSet](blog/views.py)은 `perform_create()`에서 요청 사용자를 작성자로 저장합니다.

## API

기본 URL: `http://127.0.0.1:8000/api/blog` (루트 `/posts/` 경로도 연결되어 있습니다.)

| 메서드 | 경로 | 내용 |
| --- | --- | --- |
| GET / POST | `/posts/` | 목록 조회 / 글 생성 |
| GET | `/posts/<pk>/` | 글 상세 |
| PUT / PATCH | `/posts/<pk>/` | 글 수정 |
| DELETE | `/posts/<pk>/` | 글 삭제 |
| PATCH | `/posts/<pk>/title_change_A/` | 제목을 `A`로 변경 |

응답 필드: `id`, `title`, `text`, `created_date`. 비로그인 사용자는 읽기만 가능하며, 인증 사용자는 쓰기 요청을 보낼 수 있습니다. 작성자만 수정·삭제할 수 있도록 제한하는 객체 권한은 별도 구현되어 있지 않습니다.

## 로컬 실행

Python 3.12 이상을 사용합니다. 저장소에 의존성 고정 파일이 없으므로 아래는 현재 코드의 Django 버전에 맞춘 설치 예시입니다.

```bash
python -m venv .venv
```

Windows PowerShell은 `.\.venv\Scripts\Activate.ps1`, macOS/Linux는 `source .venv/bin/activate`로 가상환경을 활성화한 뒤 실행합니다.

```bash
python -m pip install "Django==6.0.4" djangorestframework
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 127.0.0.1:8000
```

관리자 화면 `http://127.0.0.1:8000/admin/`에서 사용자를 만들거나 게시글을 준비합니다. 브라우저 API 화면에서는 `/api-auth/login/`으로 로그인하고, API 클라이언트에서는 인증 정보를 설정합니다.

## 요청 예시

조회:

```bash
curl http://127.0.0.1:8000/api/blog/posts/
```

인증된 클라이언트에서 `POST /api/blog/posts/`로 보내는 본문:

```json
{
  "title": "ViewSet으로 작성한 글",
  "text": "공통 CRUD와 커스텀 액션을 학습합니다."
}
```

## 코드와 기록

- [PostViewSet](blog/views.py): CRUD 설정, 작성자 저장, 커스텀 액션
- [SimpleRouter](blog/urls.py): ViewSet 경로 등록
- [PostSerializer](blog/serializers.py): 요청·응답 필드
- [리팩터링 코드와 7개 요청 화면](docs/learning-notes.md)
