from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from backend.domain.entities.user import User


class UserRepository(ABC):

    @abstractmethod
    def get_by_id(self, id: UUID) -> User:
        ...