# ViewSet 실행 GIF

Python 3.12, Django 6.0.4, Django REST Framework 3.18.1로 저장소의 Django 코드를 실행했습니다. GIF는 실제 HTTP 요청·응답·상태 코드를 1280×720 프레임에 배치한 기록입니다.

## 실행 환경

캡처에는 원본 코드의 별도 복사본과 새 SQLite DB를 사용했습니다. 원본 소스와 저장소의 기존 DB는 변경하지 않았습니다. 로컬 데모 사용자로 Basic 인증을 적용했으며 인증 정보는 GIF에 포함하지 않았습니다.

```bash
python -m pip install "Django==6.0.4" "djangorestframework==3.18.1"
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 127.0.0.1:18082
```

## 확인한 요청

| 순서 | 요청 | 실제 응답 |
| --- | --- | --- |
| 1 | GET `/api/blog/posts/` | 200, 빈 배열 |
| 2 | POST `/api/blog/posts/` | 201, 새 글과 ID |
| 3 | GET `/api/blog/posts/{id}/` | 200, 글 상세 |
| 4 | PATCH `/api/blog/posts/{id}/` | 200, 제목 `Updated title` |
| 5 | PATCH `/api/blog/posts/{id}/title_change_A/` | 200, 제목 `A` |
| 6 | DELETE `/api/blog/posts/{id}/` | 204, 본문 없음 |
| 7 | GET `/api/blog/posts/` | 200, 빈 배열 |

생성에는 `{"title": "ViewSet Demo", "text": "Created through the API"}`, 수정에는 `{"title": "Updated title"}`을 전송했습니다. 커스텀 액션 요청에는 본문이 필요하지 않습니다.
