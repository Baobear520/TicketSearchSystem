

from src.domain.models.entities import Venue, Event, Ticket


class EventValidationService:
    @staticmethod
    def _venue_has_capacity(venue: Venue, event: Event):
        if venue.max_capacity > len(event.tickets):
            return True
        raise ValueError("Current event exceeds max capacity of the venue.")


    @staticmethod
    def _venue_has_ticket_types(venue: Venue, event: Event):
        if len(event.tickets) == [t for t in event.tickets if t.type in venue.existing_ticket_types]:
            return True
        raise ValueError("This event contains ticket types that the venue doesn't support.")


    def is_valid(self, venue: Venue, event: Event):
        if not event.tickets:
            return True
        return self._venue_has_ticket_types(venue, event) and self._venue_has_capacity(venue, event)



class TicketValidationService:
        @staticmethod
        def _venue_has_ticket_type(venue: Venue, ticket: Ticket):
            if ticket.type in venue.existing_ticket_types:
                return True
            raise ValueError("Venue assigned to this event doesn't support chosen ticket type.")

        @staticmethod
        def _event_has_ticket_category(event: Event, ticket: Ticket):
            if ticket.category in event.ticket_categories:
                return True
            raise ValueError("Current event doesn't support chosen ticket category.")

        def is_valid(self, venue: Venue, event: Event, ticket: Ticket):
            return self._venue_has_ticket_type(venue,ticket) and self._event_has_ticket_category(event, ticket)


