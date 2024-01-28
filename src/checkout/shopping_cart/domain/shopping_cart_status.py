from enum import Enum


class ShoppingCartStatus(Enum):
    CREATED = "Created"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
