from typing import List

from src.domain.models.entities import Event, SearchRequest
from src.infrastructure.repositories.base import BaseRepository


class InMemoryEventRepository(BaseRepository):
    def __init__(self, events):
        self._events = events

    def find_by_request(self, request: SearchRequest)-> List[Event]:
        return [
            event for event in self._events if request.date_to > event.date > request.date_from \
                and len(event.tickets) > request.quantity
                ]