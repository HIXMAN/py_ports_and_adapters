from shared.domain.event.event import Event
from shared.domain.event.event_listener import EventListener


class RabbitMQEventListener(EventListener):

    def is_subscribed(self, event: Event) -> bool:
        return True

    def execute(self, event: Event) -> None:
        pass
