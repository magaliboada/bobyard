from datetime import datetime
import uuid
from typing import cast

from django.db import models

from backend.domain.entities.comment import Comment, User


class UserModel(models.Model):
    class Meta:
        db_table = "user"

    id = cast(
        uuid.UUID,
        models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False),
    )
    name = cast(str, models.CharField(max_length=50, unique=True))
    created_at = cast(datetime, models.DateTimeField(auto_now_add=True))
    updated_at = cast(datetime, models.DateTimeField(auto_now=True))

    @staticmethod
    def to_entity(user: "UserModel") -> User:
        return User(id=user.id, name=user.name)

    @staticmethod
    def to_model(user: User) -> "UserModel":
        return UserModel(id=user.id, name=user.name)


class LikeModel(models.Model):
    class Meta:
        db_table = "like"
        unique_together = ("user", "comment")

    id = cast(
        uuid.UUID,
        models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False),
    )
    user = cast(
        UserModel,
        models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="likes"),
    )
    comment = cast(
        "CommentModel",
        models.ForeignKey(
            "CommentModel", on_delete=models.CASCADE, related_name="likes"
        ),
    )


class CommentModel(models.Model):
    class Meta:
        db_table = "comment"

    id = cast(int, models.AutoField(primary_key=True))
    text = cast(str, models.CharField(max_length=1000, unique=False))
    user = cast(UserModel, models.ForeignKey(UserModel, on_delete=models.CASCADE))
    image_url = cast(str, models.CharField(max_length=255, unique=False, null=True))
    created_at = cast(datetime, models.DateTimeField(auto_now_add=True))
    updated_at = cast(datetime, models.DateTimeField(auto_now=True))
    likes: models.QuerySet[LikeModel]

    @staticmethod
    def to_model(comment: Comment) -> "CommentModel":
        user_model = UserModel.objects.get(name=comment.user.name)
        comment_model = CommentModel(
            id=comment.id,
            text=comment.text,
            user=user_model,
            created_at=comment.created_at,
            image_url=comment.image_url,
        )
        comment_model.save()

        return comment_model

    def to_entity(self) -> Comment:
        return Comment(
            id=self.id,
            text=self.text,
            user=User(id=self.user.id, name=self.user.name),
            created_at=self.created_at,
            image_url=self.image_url,
            likes_count=self.likes.count(),
        )
