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
from backend.domain.exceptions import BaseException
from backend.infrastructure.persistence.models import CommentModel, UserModel


@method_decorator(csrf_exempt, name="dispatch")
class LikeView(View):
    def post(self, request: HttpRequest, comment_id: int) -> JsonResponse:
        data = json.loads(request.body)
        try:
            user_id = UUID(data["user_id"])
        except KeyError:
            raise BaseException(400, "Invalid request body")

        inject.instance(LikeComment).execute(user_id, comment_id)
        return JsonResponse({}, status=201)

    def delete(self, request: HttpRequest, comment_id: int) -> JsonResponse:
        data = json.loads(request.body)
        try:
            user_id = UUID(data["user_id"])
        except KeyError:
            raise BaseException(400, "Invalid request body")

        inject.instance(UnlikeComment).execute(user_id, comment_id)
        return JsonResponse({}, status=204)
