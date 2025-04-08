from typing import List, Type
from uuid import UUID

from django.db import IntegrityError

from backend.domain.entities.comment import Comment
from backend.domain.exceptions import (
    CommentAlreadyLiked,
    CommentNotFound,
    CommentNotLiked,
)
from backend.domain.repositories.comment_repository import CommentRepository
from backend.infrastructure.persistence.models import CommentModel, LikeModel


class CommentPostgresRepository(CommentRepository):
    def model_class(self) -> Type[CommentModel]:
        return CommentModel

    def create(self, comment: Comment) -> None:
        CommentModel.save(CommentModel.to_model(comment))

    def get_all(self) -> List[Comment]:
        return [
            comment.to_entity()
            for comment in CommentModel.objects.all().order_by("-created_at")
        ]

    def delete(self, id: int) -> None:
        count, _ = CommentModel.objects.filter(id=id).delete()

        if count == 0:
            raise CommentNotFound(str(id))

    def like(self, comment_id: int, user_id: UUID) -> None:
        try:
            LikeModel.objects.create(comment_id=comment_id, user_id=user_id)
        except IntegrityError:
            raise CommentAlreadyLiked(str(comment_id))

    def unlike(self, comment_id: int, user_id: UUID) -> None:
        count, _ = LikeModel.objects.filter(
            comment_id=comment_id, user_id=user_id
        ).delete()

        if count == 0:
            raise CommentNotLiked(str(comment_id))

    def update_text(self, comment_id: int, text: str) -> None:
        try:
            comment_model = CommentModel.objects.get(id=comment_id)
            comment_model.text = text
            comment_model.save()
        except CommentModel.DoesNotExist:
            raise CommentNotFound(str(comment_id))
