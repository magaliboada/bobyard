from django.contrib import admin
from django.urls import path
from django.http import JsonResponse, HttpRequest

from backend.infrastructure.api.comment_view import CommentsView
from backend.infrastructure.api.like_view import LikeView


def health_check(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"status": ":)"})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check, name='health_check'),
    path('comments', CommentsView.as_view(), name='comments'),
    path('comments/<int:comment_id>', CommentsView.as_view(), name='comment_detail'),
    path('comments/<int:comment_id>/like', LikeView.as_view(), name='like_comment'),
] 