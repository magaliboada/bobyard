from typing import List


from backend.domain.entities.comment import Comment
from backend.domain.repositories.comment_repository import CommentRepository

class GetComments:
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository

    def execute(self) -> List[Comment]:
        return self.comment_repository.get_all()