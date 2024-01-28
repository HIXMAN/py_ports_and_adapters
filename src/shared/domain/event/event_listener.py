from shared.domain.event.event import Event


class EventListener:

    def is_subscribed(self, event: Event) -> bool:
        raise NotImplementedError

    def execute(self, event: Event) -> None:
        raise NotImplementedError
