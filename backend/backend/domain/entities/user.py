from uuid import UUID


class User:
    def __init__(self, id: UUID, name: str):
        self.id = id
        self.name = name

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "name": self.name,
        }
