from abc import abstractmethod, ABC
from typing import Any

from src.domain.models.entities import Venue, Event, Ticket
from src.domain.services.services import EventValidationService, TicketValidationService


class IAddItem(ABC):
    @classmethod
    def add(cls, *args: Any, **kwargs: Any)-> None:
        raise NotImplementedError

class AddEventService(IAddItem):
    @classmethod
    def add(
            cls,
            venue: Venue,
            event: Event,
            validator=EventValidationService
    ) -> None:
        try:
            validator().is_valid(venue, event)
            if venue.events:
                venue.events.append(event)
            venue.events = [event]
            print(f"Event {event} has been added to the venue {venue} successfully!")
        except ValueError as e:
            print(e)


class AddTicketService(IAddItem):
    @classmethod
    def add(
            cls,
            venue: Venue,
            event: Event,
            ticket: Ticket,
            validator=TicketValidationService
    ) -> None:
        try:
            validator().is_valid(venue, event, ticket)
            if event.tickets:
                event.tickets.append(ticket)
            event.tickets = [ticket]
            print(f"Ticket {ticket} has been added to the event {event} successfully!")
        except ValueError as e:
            print(e)
