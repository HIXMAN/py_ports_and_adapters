from sqlalchemy import Column, String, Integer, Uuid
from sqlalchemy.orm import relationship

from checkout.shopping_cart.infrastructure.sqlalchemy.entity.base import Base
from checkout.shopping_cart.infrastructure.sqlalchemy.entity.shopping_cart_line import ShoppingCartLine

print('imported shopping_cart')


class ShoppingCart(Base):
    __tablename__ = 'shopping_cart'

    id = Column(Integer, primary_key=True)
    status = Column(String(50), nullable=False)
    lines = relationship('ShoppingCartLine', order_by=ShoppingCartLine.id, back_populates="shopping_cart")

