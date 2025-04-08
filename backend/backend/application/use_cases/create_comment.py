from typing import List
import uuid
from uuid import UUID
from backend.domain.entities.comment import Comment
from backend.domain.repositories.comment_repository import CommentRepository
from backend.domain.repositories.user_repository import UserRepository

class CreateComment:
    def __init__(self, comment_repository: CommentRepository, user_repository: UserRepository):
        self.comment_repository = comment_repository
        self.user_repository = user_repository

    def execute(self, text: str, user_id: UUID, image_url: str) -> Comment:
        user = self.user_repository.get_by_id(user_id)
        
        comment = Comment(text=text, user=user, image_url=image_url)
        self.comment_repository.create(comment)

        return comment