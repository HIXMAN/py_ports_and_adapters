from sqlalchemy import Column, Integer, String

from checkout.shopping_cart.infrastructure.sqlalchemy.base import Base


class ShoppingCart(Base):
    __tablename__ = 'shopping_cart'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
