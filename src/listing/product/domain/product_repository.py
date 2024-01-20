from typing import Optional

from listing.product.domain.product import Product
from listing.product.domain.product_id import ProductId


class ProductRepository:
    def find_by_id(self, product_id: ProductId) -> Optional[Product]:
        pass

    def save(self, product: Product) -> None:
        pass
