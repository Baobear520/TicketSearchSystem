
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
    id="3nn3n",
    name="Wembley Stadium",
    location_lat=33.11,
    location_long=11.44,
    existing_ticket_types={TicketType.dance_floor,TicketType.zone_a,TicketType.zone_b,TicketType.zone_c}
)
event1 = Event(
    id="31dsd",
    name="David Guetta show",
    venue=venue1,
    date=datetime(2025,1,1,18,00),
    ticket_categories={TicketCategory.standard,TicketCategory.VIP, TicketCategory.early_bird}
)
event2 = Event(
    id="3322mmm",
    name="Football game",
    venue=venue1,
    date=datetime(2025,1,2,20,00),
    ticket_categories={TicketCategory.standard,TicketCategory.VIP}
)

events_repo = InMemoryEventRepository([event1, event2])
event1.add_ticket(ticket1)
event1.add_ticket(ticket2)
event2.add_ticket(ticket2)
search_service = TicketSearchService(events_repo)

res = search_service.find_tickets(
    request=SearchRequest(
        date_from=datetime(2025,1,1,0,0),
        date_to=datetime(2025,1,2,19,59),
        price_from=0,
        price_to=12000,
        quantity=5
    )
)


class UniqueValidator:
    pass