from rest_framework import viewsets  # ModelViewSet에 모두 정의되어있음, 상속만 받자
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import action  # 데코레이터 action을 사용하기 위해
from rest_framework.response import Response  # 반환을 직접 넣어줘야함


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by(
        "-published_date"
    )  # 정렬만 기존 list의 정렬을 유지하기위해 "-published_date" 유지
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=["PATCH"])
    def title_change_A(
        self, request, pk=None
    ):  # 혹시 pk값 없을 경우, 프로그램의 오류 발생을 막기위함
        destination_post = self.get_object()
        destination_post.title = "A"
        destination_post.save()
        serializer = self.get_serializer(
            destination_post
        )  # 클래스의 직렬화 방법을 따름, 직렬화 해서 넘겨주기
        return Response(
            serializer.data
        )  # title만 A로 만들고 나머지는 그대로 넘겨줌, 바뀌었다는 정보를 Json으로 알려줌
