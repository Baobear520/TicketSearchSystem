from typing import List

from src.domain.models.entities import Ticket, SearchRequest
from src.infrastructure.repositories.in_memory.event import InMemoryEventRepository



class TicketSearchService:
    def __init__(self, event_repo: InMemoryEventRepository):
        self._event_repo = event_repo

    def find_tickets(self, request: SearchRequest)-> List[Ticket]:
        matching_events = self._event_repo.find_by_request(request)

        return [
            ticket for event in matching_events for ticket in event.tickets \
            if ticket.category in request.ticket_category \
            and ticket.type in request.ticket_type \
            and request.price_from < ticket.price < request.price_to
        ][:request.quantity]