from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import PostViewSet  # ModelViewSet 가져오기

router = SimpleRouter()  # 라우터 객체 생성 -> 기본 라우터

router.register(
    r"posts", PostViewSet
)  # 라우터 객체에 ModelViewSet 등록, posts/(붙이기나름, blog도 가능)로 시작하는 URL은 모두 ModelViewSet에서 처리(매핑은 라우터가함)

urlpatterns = [
    path("", include(router.urls)),  # 라우터를 통한 장고의 urlpatterns 등록
]
