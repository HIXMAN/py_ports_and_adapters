from shared.domain.command.command import Command


class CommandListener:

    def is_subscribed(self, command: Command) -> bool:
        pass

    def execute(self, command: Command) -> None:
        pass
