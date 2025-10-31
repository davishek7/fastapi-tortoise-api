from .settings import settings

# Tortoise ORM Configuration
TORTOISE_ORM = {
    "connections": {"default": settings.DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.customer.models", "app.order.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
