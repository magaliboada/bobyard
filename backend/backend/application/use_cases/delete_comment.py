from typing import List
from uuid import UUID


from backend.domain.entities.comment import Comment
from backend.domain.repositories.comment_repository import CommentRepository

class DeleteComment:
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository

    def execute(self, id: int) -> None:
        self.comment_repository.delete(id=id)