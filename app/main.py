from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from .configs.db import TORTOISE_ORM
from .customer.routes import router as customer_router
from .order.routes import router as order_router


app = FastAPI()

# register Tortoise ORM with FastAPI
register_tortoise(
    app=app, config=TORTOISE_ORM, generate_schemas=False, add_exception_handlers=True
)

URL_PREFIX = "/api"

# Include routers for different modules
app.include_router(
    customer_router, prefix=f"{URL_PREFIX}/customers", tags=["Customers"]
)
app.include_router(order_router, prefix=f"{URL_PREFIX}/orders", tags=["Orders"])
