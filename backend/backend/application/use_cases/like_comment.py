from uuid import UUID
from backend.domain.repositories.comment_repository import CommentRepository
from backend.domain.repositories.user_repository import UserRepository
from backend.infrastructure.persistence.models import LikeModel, UserModel, CommentModel
from backend.domain.exceptions import BaseException, CommentAlreadyLiked


class LikeComment:
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository

    def execute(self, user_id: UUID, comment_id: int) -> None:
        self.comment_repository.like(comment_id, user_id)
