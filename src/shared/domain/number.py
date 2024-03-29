
class Number:
    def __init__(self, value: int) -> None:
        self._value = value

    def __str__(self) -> str:
        return str(self._value)

    def __eq__(self, other: "Number") -> bool:
        return other.value() == self.value()

    def value(self) -> int:
        return self._value
