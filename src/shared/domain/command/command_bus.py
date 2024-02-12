from typing import Set

from injector import inject
from sqlalchemy.orm import Session

from shared.domain.command.command import Command
from shared.domain.command.command_listener import CommandListener


class CommandBus:

    @inject
    def __init__(self, session: Session) -> None:
        self._session = session
        self.listeners: Set[CommandListener] = set()

    def add_listener(self, listener: CommandListener) -> None:
        self.listeners.add(listener)

    def remove_listener(self, listener: CommandListener) -> None:
        self.listeners.remove(listener)

    def publish(self, command: Command) -> None:
        for listener in self.listeners:
            if listener.is_subscribed(command):
                listener.execute(command)
        self._session.commit()
