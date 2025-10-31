from tortoise import fields, models
import uuid
from .enum import OrderStatus


# Order Related Tortoise ORM Models
class Order(models.Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    customer = fields.ForeignKeyField(
        "models.Customer", related_name="orders", on_delete=fields.CASCADE
    )
    date = fields.DatetimeField(auto_now_add=True)
    status = fields.CharEnumField(OrderStatus, default=OrderStatus.DRAFT)


class OrderItem(models.Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    order = fields.ForeignKeyField(
        "models.Order", related_name="order_items", on_delete=fields.CASCADE
    )
    product_name = fields.CharField(max_length=255)
    quantity = fields.SmallIntField()
    price = fields.FloatField()
