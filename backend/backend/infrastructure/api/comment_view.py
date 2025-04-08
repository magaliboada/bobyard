import inject
import json
from django.http import HttpRequest, JsonResponse, HttpResponseBase
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from uuid import UUID

from backend.application.use_cases.create_comment import CreateComment
from backend.application.use_cases.delete_comment import DeleteComment
from backend.application.use_cases.get_comments import GetComments
from backend.application.use_cases.like_comment import LikeComment
from backend.application.use_cases.unlike_comment import UnlikeComment
from backend.application.use_cases.update_comment import UpdateComment
from backend.domain.exceptions import BaseException
from backend.infrastructure.persistence.models import CommentModel, UserModel


@method_decorator(csrf_exempt, name="dispatch")
class CommentsView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        comments = inject.instance(GetComments).execute()
        return JsonResponse([comment.to_dict() for comment in comments], safe=False)

    def post(self, request: HttpRequest) -> JsonResponse:
        data = json.loads(request.body)
        try:
            user_id = UUID(data["user_id"])
            text = data["text"]
            image_url = data.get("image_url", None)
        except KeyError:
            raise BaseException(400, "Invalid request body")

        comment = inject.instance(CreateComment).execute(
            text=text, user_id=user_id, image_url=image_url
        )
        return JsonResponse(comment.to_dict(), status=201)

    def delete(self, request: HttpRequest, comment_id: int) -> JsonResponse:
        inject.instance(DeleteComment).execute(comment_id)
        return JsonResponse({}, status=204)

    def patch(self, request: HttpRequest, comment_id: int) -> JsonResponse:
        data = json.loads(request.body)
        try:
            text = data["text"]
        except KeyError:
            raise BaseException(400, "Invalid request body")

        inject.instance(UpdateComment).execute(comment_id, text)
        return JsonResponse({}, status=200)
