
class DecimalNumber:
    def __init__(self, value: float) -> None:
        self._value = value

    def __str__(self) -> str:
        return str(self._value)

    def __eq__(self, other: "DecimalNumber") -> bool:
        return other.value() == self.value()

    def value(self) -> float:
        return self._value
