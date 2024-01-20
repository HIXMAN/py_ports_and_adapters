from typing import Set

from shared.domain.event.event import Event
from shared.domain.event.event_listener import EventListener


class EventBus:
    def __init__(self):
        self.listeners: Set[EventListener] = set()

    def add_listener(self, listener: EventListener) -> None:
        self.listeners.add(listener)

    def remove_listener(self, listener: EventListener) -> None:
        self.listeners.remove(listener)

    def publish(self, event: Event) -> None:
        for listener in self.listeners:
            if listener.is_subscribed(event):
                listener.execute(event)

