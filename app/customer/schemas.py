from tortoise.contrib.pydantic import pydantic_model_creator
from .models import Customer


# Schema Definitions for Customer
CustomerIn = pydantic_model_creator(Customer, name="CustomerIn", exclude_readonly=True)
CustomerOut = pydantic_model_creator(Customer, name="CustomerOut")