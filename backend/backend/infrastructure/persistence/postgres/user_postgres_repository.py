from typing import List, Type
from uuid import UUID

from backend.domain.entities.user import User
from backend.domain.exceptions import UserNotFound
from backend.domain.repositories.user_repository import UserRepository
from backend.infrastructure.persistence.models import UserModel


class  UserPostgresRepository(UserRepository):
    def model_class(self) -> Type[UserModel]:
        return UserModel
    
    def get_by_id(self, id: UUID) -> User:
        try:
            return UserModel.to_entity(UserModel.objects.get(id=id))
        except UserModel.DoesNotExist:
            raise UserNotFound(str(id))
