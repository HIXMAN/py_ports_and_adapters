from shared.domain.command.command import Command


class CommandListener:

    def is_subscribed(self, command: Command) -> bool:
        raise NotImplementedError

    def execute(self, command: Command) -> None:
        raise NotImplementedError
