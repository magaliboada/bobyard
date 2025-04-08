from typing import Optional


class BaseException(Exception):
    def __init__(
        self,
        status_code: int,
        message: str,
    ) -> None:
        self.status_code = status_code
        self.message = message
        super().__init__(message)


class UserNotFound(BaseException):
    def __init__(self, user_id: str) -> None:
        super().__init__(404, f"User with id {user_id} not found")

class CommentNotFound(BaseException):
    def __init__(self, comment_id: str) -> None:
        super().__init__(404, f"Comment with id {comment_id} not found")

class CommentAlreadyLiked(BaseException):
    def __init__(self, comment_id: str) -> None:
        super().__init__(400, f"Comment with id {comment_id} already liked")

class CommentNotLiked(BaseException):
    def __init__(self, comment_id: str) -> None:
        super().__init__(400, f"Comment with id {comment_id} not liked")
