class ProductStock:

    def __init__(
            self,
            amount: int,
    ):
        self.amount = amount

    def reduce(self) -> "ProductStock":
        return ProductStock(self.amount - 1)
