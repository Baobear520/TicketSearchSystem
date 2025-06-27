from abc import ABC, abstractmethod
from typing import List

from src.domain.models.entities import SearchRequest


class BaseRepository(ABC):
    @abstractmethod
    def find_by_request(self, request: SearchRequest)-> List:
        pass
