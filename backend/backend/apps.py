from typing import Any

from django.apps import AppConfig


class BackendConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "backend"

    def ready(self) -> None:
        from backend.application.use_cases.get_comments import GetComments
        from backend.domain.repositories.comment_repository import CommentRepository
        from backend.domain.repositories.user_repository import UserRepository
        from backend.infrastructure.persistence.postgres.comment_postgres_repository import (
            CommentPostgresRepository,
        )
        from backend.application.use_cases.create_comment import CreateComment
        from backend.infrastructure.persistence.postgres.user_postgres_repository import (
            UserPostgresRepository,
        )
        from backend.application.use_cases.delete_comment import DeleteComment
        from backend.application.use_cases.like_comment import LikeComment
        from backend.application.use_cases.unlike_comment import UnlikeComment
        from backend.application.use_cases.update_comment import UpdateComment

        import inject

        def configure_injection(binder: Any) -> None:
            comment_repository_instance = CommentPostgresRepository()
            user_repository_instance = UserPostgresRepository()
            binder.bind(CommentRepository, comment_repository_instance)
            binder.bind(UserRepository, user_repository_instance)
            binder.bind(
                CreateComment,
                CreateComment(comment_repository_instance, user_repository_instance),
            )
            binder.bind(GetComments, GetComments(comment_repository_instance))
            binder.bind(DeleteComment, DeleteComment(comment_repository_instance))
            binder.bind(
                LikeComment,
                LikeComment(comment_repository_instance),
            )
            binder.bind(
                UnlikeComment,
                UnlikeComment(comment_repository_instance),
            )
            binder.bind(
                UpdateComment,
                UpdateComment(comment_repository_instance),
            )

        inject.configure(configure_injection)
