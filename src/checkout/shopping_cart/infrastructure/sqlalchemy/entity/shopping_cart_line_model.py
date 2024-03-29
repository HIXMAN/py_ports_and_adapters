from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from checkout.shopping_cart.infrastructure.sqlalchemy.entity.base import Base


class ShoppingCartLineModel(Base):
    __tablename__ = 'shopping_cart_line'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    cart_id = Column(Integer, ForeignKey('shopping_cart.id'), nullable=False)
    shopping_cart = relationship('ShoppingCartModel', back_populates="lines", cascade="save-update")
