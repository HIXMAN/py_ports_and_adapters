from enum import Enum


class ShoppingCartStatus(Enum):
    EMPTY = "Empty"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
