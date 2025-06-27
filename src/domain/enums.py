from enum import Enum


class TicketCategory(str, Enum):
    VIP = "vip"
    standard = "standard"
    early_bird = "early_bird"


class TicketType(str, Enum):
    uncategorized = "uncategorized"
    dance_floor = "dance floor"
    balcony = "balcony"
    zone_a = "Zone A"
    zone_b = "Zone B"
    zone_c = "Zone C"