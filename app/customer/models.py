from tortoise import fields, models
import uuid

# Customer Related Tortoise ORM Models

class Customer(models.Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, unique=True)
