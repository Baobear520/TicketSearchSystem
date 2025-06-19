from uuid import UUID
from dataclasses import dataclass
from datetime import datetime
from typing import List, Set, Optional

from main import UniqueValidator
from src.domain.models.enums import TicketType, TicketCategory


@dataclass
class Ticket:
    id: str
    type: TicketType
    price: float
    category: TicketCategory

@dataclass
class Venue:
    id: UUID
    name: str
    location: str
    existing_ticket_types: Set[TicketType]
    max_capacity: int


class Event:
    def __init__(
            self,
            id: str,
            name: str,
            venue: Venue,
            date: datetime,
            ticket_categories: Set[TicketCategory]
    ):
        self.id = id
        self.name = name
        self.venue = venue
        self.date = date
        self.tickets = []
        self.ticket_categories = ticket_categories

    def add_ticket(self, ticket: Ticket):
        try:
            if UniqueValidator.is_unique(ticket, self.tickets):
                if ticket.type in self.venue.existing_ticket_types and ticket.category in self.ticket_categories:
                    self.tickets.append(ticket)
            else:
                raise ValueError("Current event doesn't support tickets of this type.")
        except ValueError as e:
            print(e)


@dataclass
class User:
    id: str
    username: str
    bookings: List[Ticket] = None


@dataclass
class SearchRequest:
    date_from: datetime
    date_to: datetime
    price_from: float
    price_to: float
    ticket_type: Optional[Set[TicketType]]
    ticket_category: Optional[Set[TicketCategory]]
    quantity: int