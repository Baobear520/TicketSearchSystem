from abc import ABC, abstractmethod


class BaseRepository(ABC):
    @abstractmethod
    def find_by_request(self, request: SearchRequest):
        pass