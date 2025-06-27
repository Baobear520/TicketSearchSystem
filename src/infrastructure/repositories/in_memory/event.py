from typing import List

from src.domain.models.entities import Event, SearchRequest, Venue, Ticket
from src.infrastructure.repositories.base import BaseRepository


class InMemoryVenueRepository(BaseRepository):
    def __init__(self, venues: List[Venue]):
        self._venues = venues

    def find_by_request(self, request: SearchRequest)-> List[Venue]:
        pass


class InMemoryEventRepository(BaseRepository):
    def __init__(self, events: List[Event]):
        self._events = events

    def find_by_request(self, request: SearchRequest)-> List[Event]:
        return [
            event for event in self._events if request.date_to > event.date > request.date_from \
                and len(event.tickets) > request.quantity
                ]


class InMemoryTicketRepository(BaseRepository):
    def __init__(self, tickets: List[Ticket]):
        self._tickets = tickets

    def find_by_request(self, request: SearchRequest)-> List[Ticket]:
        return [
            ticket for ticket in self._tickets \
            if ticket.type in request.ticket_type
                and ticket.category in request.ticket_category
                and request.price_to >= ticket.price >= request.price_from
        ]






