from datetime import datetime
from typing import Optional

from backend.domain.entities.user import User


class Comment:
    def __init__(self, text: str, user: User, created_at: Optional[datetime] = None, image_url: Optional[str] = None, id: Optional[int] = None, likes_count: int = 0):
        self.id = id
        self.text = text
        self.user = user
        self.created_at = created_at
        self.image_url = image_url
        self.likes_count = likes_count

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "text": self.text,
            "user": self.user.to_dict(),
            "created_at": self.created_at,
            "image_url": self.image_url,
            "likes_count": self.likes_count
        }
    