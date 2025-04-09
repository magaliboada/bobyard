import inject
from backend.domain.entities.comment import Comment
from backend.domain.repositories.comment_repository import CommentRepository
from backend.infrastructure.persistence.models import CommentModel
from backend.domain.exceptions import BaseException


class UpdateComment:
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository

    def execute(self, comment_id: int, text: str) -> None:
        print(f"Updating comment {comment_id} with text {text}")
        self.comment_repository.update_text(comment_id, text)
