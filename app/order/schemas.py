from pydantic import BaseModel, Field
from .models import Order, OrderItem
from .enum import OrderStatus as OrderStatusEnum
from typing import List


# Schema Definitions for Order
class OrderItemIn(BaseModel):
    product_name: str
    quantity: int
    price: float


class OrderItemOut(OrderItemIn):
    id: str
    order_id: str


class OrderIn(BaseModel):
    customer_id: str
    status: OrderStatusEnum = Field(default=OrderStatusEnum.DRAFT)
    order_items: List[OrderItemIn]

    class Config:
        use_enum_values = True


class OrderOut(BaseModel):
    id: str
    customer_id: str
    date: str
    status: str
    order_items: List[OrderItemOut]
