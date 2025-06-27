from datetime import datetime
from src.application.use_cases.populate import AddEventService, AddTicketService
from src.application.use_cases.search_tickets import TicketSearchService
from src.domain.enums import TicketType, TicketCategory
from src.domain.models.entities import Ticket, Venue, Event, SearchRequest
from src.infrastructure.repositories.in_memory.event import InMemoryEventRepository


def main():
    ticket1 = Ticket(
        id="1dssdd",
        type=TicketType.dance_floor,
        price=8500,
        category=TicketCategory.standard
    )
    ticket2 = Ticket(
        id="1dssd",
        type=TicketType.zone_b,
        price=3434,
        category=TicketCategory.standard
    )
    ticket3 = Ticket(
        id="34242fsdfs",
        type=TicketType.zone_a,
        price=11000,
        category=TicketCategory.VIP
    )

    venue1 = Venue(
        id='313sssss',
        name="Wembley Stadium",
        location='London',
        existing_ticket_types={TicketType.dance_floor, TicketType.zone_a, TicketType.zone_b, TicketType.zone_c},
        max_capacity=80000

    )
    event1 = Event(
        id="31dsd",
        name="David Guetta show",
        date=datetime(2025, 1, 1, 18, 00),
        ticket_categories={TicketCategory.standard, TicketCategory.VIP, TicketCategory.early_bird}
    )
    event2 = Event(
        id="3322mmm",
        name="Football game",
        date=datetime(2025, 1, 2, 20, 00),
        ticket_categories={TicketCategory.standard, TicketCategory.VIP}
    )

    def find_tickets(search_service):
        return search_service.find_tickets(
            request=SearchRequest(
                date_from=datetime(2025, 1, 1, 0, 0),
                date_to=datetime(2025, 1, 2, 19, 59),
                price_from=0,
                price_to=12000,
                ticket_type={TicketType.zone_a},
                ticket_category={TicketCategory.VIP},
                quantity=1
            )
        )
    events = [event1, event2]

    tickets = [ticket1, ticket2, ticket3]

    events_repo = InMemoryEventRepository(events)
    search_service = TicketSearchService(events_repo)

    # for e in events:
    #     AddEventService.add(venue=venue1, event=e)
    #     for t in tickets:
    #         AddTicketService.add(venue=venue1, event=e, ticket=t)
    for event in events:
        print(event.tickets)
    print(find_tickets(search_service))


if __name__ == "__main__":
    main()
