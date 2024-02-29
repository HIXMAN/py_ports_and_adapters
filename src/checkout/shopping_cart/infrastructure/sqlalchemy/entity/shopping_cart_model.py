from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship

from checkout.shopping_cart.infrastructure.sqlalchemy.entity.base import Base
from checkout.shopping_cart.infrastructure.sqlalchemy.entity.shopping_cart_line_model import ShoppingCartLineModel


class ShoppingCartModel(Base):
    __tablename__ = 'shopping_cart'

    id = Column(Integer, primary_key=True)
    status = Column(String(50), nullable=False)
    total_price = Column(Float, nullable=True)
    lines = relationship(
        'ShoppingCartLineModel',
        order_by=ShoppingCartLineModel.id,
        back_populates="shopping_cart",
        cascade="all"
    )

