from typing import Optional

from checkout.product.domain.product import Product
from checkout.product.domain.product_id import ProductId
from checkout.product.domain.product_repository import ProductRepository


class AlchemyProductRepository(ProductRepository):

    def __init__(self, connection: Session):
        self._connection: Session = connection

    def find_by_id(self, product_id: ProductId) -> Optional[Product]:
        shopping_cart = (
            self._connection.query(Product)
            .filter_by(id=product_id)
            .first()
        )
        return shopping_cart

    def save(self, product: Product) -> None:
        self._connection.add(product)
