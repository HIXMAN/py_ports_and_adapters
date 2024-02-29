
class Id:
    def __init__(self, value: int) -> None:
        self._value = value

    def value(self) -> int:
        return self._value

    def __eq__(self, other: "Id") -> bool:
        return self._value == other.value()
