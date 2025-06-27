from uuid import UUID
from dataclasses import dataclass
from datetime import datetime
from typing import List, Set


from src.domain.enums import TicketType, TicketCategory


@dataclass
class Ticket:
    id: str
    type: TicketType
    price: float
    category: TicketCategory


@dataclass
class Event:
    id: str
    name: str
    date: datetime
    ticket_categories: Set[TicketCategory]
    tickets: List[Ticket] = None

@dataclass
class Venue:
    id: str
    name: str
    location: str
    existing_ticket_types: Set[TicketType]
    max_capacity: int
    events: List[Event] = None


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
    ticket_type: Set[TicketType]
    ticket_category: Set[TicketCategory]
    quantity: int