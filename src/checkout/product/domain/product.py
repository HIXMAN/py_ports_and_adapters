from checkout.product.domain.product_id import ProductId
from checkout.product.domain.product_price import ProductPrice
from checkout.product.domain.product_stock import ProductStock


class Product:

    def __init__(
            self,
            uuid: ProductId,
            price: ProductPrice,
            stock: ProductStock
    ):
        self.uuid = uuid
        self.price = price
        self.stock = stock

    def reduce_stock(self) -> None:
        self.stock = self.stock.reduce()
