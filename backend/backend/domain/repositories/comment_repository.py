from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from backend.domain.entities.comment import Comment


class CommentRepository(ABC):

    @abstractmethod
    def create(self, comment: Comment) -> None: ...

    @abstractmethod
    def get_all(self) -> List[Comment]: ...

    @abstractmethod
    def delete(self, id: int) -> None: ...

    @abstractmethod
    def like(self, comment_id: int, user_id: UUID) -> None: ...

    @abstractmethod
    def unlike(self, comment_id: int, user_id: UUID) -> None: ...

    @abstractmethod
    def update_text(self, comment_id: int, text: str) -> None: ...
