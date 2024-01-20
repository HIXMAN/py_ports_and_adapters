from typing import Set

from shared.domain.command.command import Command
from shared.domain.command.command_listener import CommandListener


class CommandBus:
    def __init__(self):
        self.listeners: Set[CommandListener] = set()

    def add_listener(self, listener: CommandListener) -> None:
        self.listeners.add(listener)

    def remove_listener(self, listener: CommandListener) -> None:
        self.listeners.remove(listener)

    def publish(self, command: Command) -> None:
        for listener in self.listeners:
            if listener.is_subscribed(command):
                listener.execute(command)

