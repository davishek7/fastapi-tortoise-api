from enum import Enum


class OrderStatus(str, Enum):
    DRAFT = "Draft"
    CONFIRMED = "Confirmed"
    SHIPPED = "Shipped"
