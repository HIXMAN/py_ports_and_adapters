
class Number:
    def __init__(self, value: int) -> None:
        self._value = value

    def __str__(self):
        return str(self._value)

    def value(self) -> int:
        return self._value
