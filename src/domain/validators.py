from typing import List


class UniqueValidator:
    @staticmethod
    def is_unique(obj, repository: List):
        if obj.id in repository:
            raise ValueError(f"{obj} with the same id already exists.")
        return True