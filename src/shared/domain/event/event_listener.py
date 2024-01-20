from shared.domain.event.event import Event


class EventListener:

    def is_subscribed(self, event: Event) -> bool:
        pass

    def execute(self, event: Event) -> None:
        pass
